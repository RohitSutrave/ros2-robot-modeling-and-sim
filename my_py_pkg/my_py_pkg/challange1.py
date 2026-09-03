import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen


class TurtleControllerNode(Node):
    
    def __init__(self):
        super().__init__("turtle_controller")
        
        # Publisher for turtle movement commands
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        
        # Subscriber for turtle position updates
        self.pose_sub_ = self.create_subscription(
            Pose, 
            "/turtle1/pose", 
            self.pose_callback, 
            10
        )

        self.pen_client_ = self.create_client(
            SetPen,
            "/turtle1/set_pen"
        )
        self.previous_side = None
        self.get_logger().info("Turtle Controller Closed-Loop Node started.")

    def pose_callback(self, pose: Pose):
        cmd = Twist()
        
        # Adjust speeds based on current X position
        if pose.x < 5.5:
            cmd.linear.x = 3.0
            cmd.angular.z = 2.5
            current_side = "left"
        else:
            cmd.linear.x = 2.0
            cmd.angular.z = 2.0
            current_side = "right"

        # Publish command immediately inside subscriber callback
        self.cmd_vel_pub_.publish(cmd)

        if current_side != self.previous_side:

            if current_side == "left":
                self.change_pen(0, 255, 0)
            else:
                self.change_pen(255, 0, 0)

            self.previous_side = current_side



    def change_pen(self, r, g, b):

        while not self.pen_client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for set_pen service...")

        request = SetPen.Request()

        request.r = r
        request.g = g
        request.b = b
        request.width = 3
        request.off = 0

        self.pen_client_.call_async(request)



def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()