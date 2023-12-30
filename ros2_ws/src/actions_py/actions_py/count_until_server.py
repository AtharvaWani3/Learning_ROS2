#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.action import CountUntil
from rclpy.action import ActionServer, GoalResponse
from rclpy.action.server import ServerGoalHandle
import time


class CountUntilServerNode(Node):
    def __init__(self):
        super().__init__("count_until_server")
        self.count_until_server_ = ActionServer(
            self,
            CountUntil,
            "count_until",
            goal_callback=self.goal_callback,
            execute_callback=self.execute_callback,
        )
        self.get_logger().info("Action Server has been started.")

    def goal_callback(self, goal_request: CountUntil.Goal):
        self.get_logger().info("Goal Received.")
        #Validate Goal Parameters
        if goal_request.target_number <= 0:
            self.get_logger().info("Goal Rejected")
            return GoalResponse.REJECT 
        
        self.get_logger().info("Goal Rejected")
        return GoalResponse.ACCEPT

    def execute_callback(self, goal_handle: ServerGoalHandle):
        # Get request from goal
        target_number = goal_handle.request.target_number
        period = goal_handle.request.period

        # Execute the action
        self.get_logger().info("Executing goal.")
        counter = 0
        for i in range(target_number):
            counter += 1
            self.get_logger().info(str(counter))
            time.sleep(period)

        # Once done, set final goal state
        goal_handle.succeed()

        # and send result
        result = CountUntil.Result()
        result.reached_number = counter
        return result


def main(args=None):
    rclpy.init(args=args)
    node = CountUntilServerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
