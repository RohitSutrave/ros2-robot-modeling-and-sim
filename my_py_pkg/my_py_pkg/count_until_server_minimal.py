#!/usr/bin/env python3

import rclpy
import time

from rclpy.node import Node
from rclpy.action import ActionServer, GoalResponse
from rclpy.action.server import ServerGoalHandle

from my_robot_interfaces.action import CountUntil


class CountUntilServerNode(Node):

    def __init__(self):
        super().__init__("count_until_server")

        self.count_until_server_ = ActionServer(
            self,
            CountUntil,
            "count_until",
            goal_callback=self.goal_callback,
            execute_callback=self.execute_callback
        )

        self.get_logger().info("Count Until Action Server started")


    # Called when client sends a goal
    def goal_callback(self, goal_request: CountUntil.Goal):

        self.get_logger().info("Received a goal")

        # Validate goal
        if goal_request.target_number <= 0:
            self.get_logger().warn(
                "Rejecting goal: target number must be positive"
            )
            return GoalResponse.REJECT

        self.get_logger().info(
            f"Accepting goal: Count until {goal_request.target_number}"
        )

        return GoalResponse.ACCEPT


    # Called only after goal is accepted
    def execute_callback(
        self,
        goal_handle: ServerGoalHandle
    ):

        target_number = goal_handle.request.target_number
        delay = goal_handle.request.delay

        self.get_logger().info(
            f"Executing goal: counting until {target_number}"
        )

        # Count from 0 to target
        for i in range(target_number + 1):

            self.get_logger().info(f"Count: {i}")

            time.sleep(delay)

        # Create result
        result = CountUntil.Result()
        result.reached_number = target_number

        # Tell ROS the goal succeeded
        goal_handle.succeed()

        self.get_logger().info("Goal completed")

        return result


def main(args=None):

    rclpy.init(args=args)

    node = CountUntilServerNode()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()