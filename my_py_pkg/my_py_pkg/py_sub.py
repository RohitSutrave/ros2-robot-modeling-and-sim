#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__('py_num_sub')
        
        # Initialize internal state
        self.counter_ = 0
        
        # create_subscription(Interface, topic_name, callback, queue_size)
        self.subscriber_ = self.create_subscription(
            Int64, 
            'num', 
            self.callback_number, 
            10
        )
        self.get_logger().info('Number counter has been started.')

    def callback_number(self, msg: Int64):
        # Extract data from the message payload
        self.counter_ = msg.data
        self.get_logger().info(f'Current count: {self.counter_}')

def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()




