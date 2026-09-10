#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class NumberPublisherNode(Node):

    def __init__(self):
        super().__init__("number_publisher")

        # Declare parameters
        self.declare_parameter("number", 2)
        self.declare_parameter("publish_period", 1.0)

        # Read parameters
        self.number_ = self.get_parameter("number").value
        self.publish_period_ = self.get_parameter(
            "publish_period"
        ).value

        # Publisher
        self.publisher_ = self.create_publisher(
            Int64,
            "Num",
            10
        )

        # Timer
        self.timer_ = self.create_timer(
            self.publish_period_,
            self.publish_number
        )

        # Parameter update callback
        self.add_post_set_parameters_callback(
            self.parameters_callback
        )

        self.get_logger().info(
            f"Number: {self.number_}, "
            f"Period: {self.publish_period_}"
        )

    def publish_number(self):

        msg = Int64()
        msg.data = self.number_

        self.publisher_.publish(msg)

        self.get_logger().info(
            f"Publishing: {self.number_}"
        )

    def parameters_callback(self, params):

        for param in params:

            if param.name == "number":
                self.number_ = param.value

            elif param.name == "publish_period":
                self.get_logger().info(
                    f"Publish period changed to {param.value}"
                )


def main(args=None):

    rclpy.init(args=args)

    node = NumberPublisherNode()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()