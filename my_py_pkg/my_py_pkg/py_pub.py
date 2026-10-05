import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumPubNode(Node):
    def __init__(self):
        super().__init__("py_num_pub")
        self.get_logger().info("Hello Ros2")

        self.publisher_= self.create_publisher(Int64,"num",10)
        self.counter_=0
        self.timer_ = self.create_timer(1.0, self.pub_num)

    def pub_num(self):
        # 1. Create the message object
        msg = Int64()
        
        # 2. Assign the counter value to the message's data field
        msg.data = self.counter_
        
        # 3. Publish the message to the "Num" topic
        self.publisher_.publish(msg)
        
        # Log the action and increment the counter
        self.get_logger().info("Publishing: " + str(msg.data))
        self.counter_ += 1

def main(args=None):
    # Initialize the ROS 2 communications
    rclpy.init(args=args)
    
    # Create the node
    node = NumPubNode()
    
    try:
        # Keep the node running so it can process the timer callbacks
        rclpy.spin(node)
    except KeyboardInterrupt:
        # Allow graceful exit on Ctrl+C
        pass
    finally:
        # Destroy the node explicitly and shut down ROS 2
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()