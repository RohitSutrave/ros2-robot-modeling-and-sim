import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

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
        self.get_logger().info("Turtle Controller Closed-Loop Node started.")

    def pose_callback(self, pose: Pose):
        cmd = Twist()
        
        # Adjust speeds based on current X position
        if pose.x < 5.5:
            cmd.linear.x = 3.0
            cmd.angular.z = 2.5
        else:
            cmd.linear.x = 2.0
            cmd.angular.z = 2.0

        # Publish command immediately inside subscriber callback
        self.cmd_vel_pub_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()