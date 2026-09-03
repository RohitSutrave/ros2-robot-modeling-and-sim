import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super() .__init__("first_node")
        self.get_logger().info("Hello Ros2")
        self.counter_=0
        self.timer_ = self.create_timer(1.0, self.print_hello)

    def print_hello(self):
        self.get_logger().info("Hello "+str(self.counter_))
        self.counter_+=1



def main():
    rclpy.init()
    node=MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()



