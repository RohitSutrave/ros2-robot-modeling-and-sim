import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from my_robot_interfaces.srv import ResetCounter  # Import custom service

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.counter_ = 0
        # Topic Subscriber
        self.number_subscriber_ = self.create_subscription(
            Int64, "Num", self.callback_number, 10
        )
        
        # Service Server
        self.reset_counter_service_ = self.create_service(
            ResetCounter, "reset_counter", self.callback_reset_counter
        ) 
        
        self.get_logger().info("Number Counter Server Node initialized.")

    def callback_number(self, msg: Int64):
        self.counter_ += msg.data
        self.get_logger().info(f"Counter: {self.counter_}")

    def callback_reset_counter(
        self, 
        request: ResetCounter.Request, 
        response: ResetCounter.Response
    ) -> ResetCounter.Response:
        
        # Input Validation: reject negative reset values
        if request.reset_value < 0:
            response.success = False
            response.message = "Failed: Reset value cannot be negative."
            self.get_logger().warn(f"Rejected invalid reset request: {request.reset_value}")
        else:
            self.counter_ = request.reset_value
            response.success = True
            response.message = f"Counter successfully reset to {self.counter_}."
            self.get_logger().info(f"Counter reset to {self.counter_}")

        return response  # Always return the response object

def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()