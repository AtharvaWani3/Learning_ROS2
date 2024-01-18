#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.action import CountUntil
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle, GoalStatus


class CountUntilClientNode(Node):
    def __init__(self):
        super().__init__("count_until_client")
        self.count_until_client_ = ActionClient(self, CountUntil, "count_until")

    def send_goal(self, target_number, period):
        # Wait for action server
        self.count_until_client_.wait_for_server()

        # Create goal
        goal = CountUntil.Goal()
        goal.target_number = target_number
        goal.period = period

        # Send goal
        self.get_logger().info("Sending Goal")
        self.count_until_client_.send_goal_async(
            goal, feedback_callback=self.goal_feedback_callback
        ).add_done_callback(self.goal_response_callback)

        # Send cancel after 2 seconds
        self.timer_ = self.create_timer(2, self.cancel_goal)

    def cancel_goal(self):  
        self.timer_.cancel()
        self.get_logger().info("Sending cancel request")
        self.goal_handle_.cancel_goal_async()

    def goal_response_callback(self, future):
        # Get response for whether goal is accepted or not
        self.goal_handle_: ClientGoalHandle = future.result()
        if self.goal_handle_.accepted:
            self.get_logger().info("Goal Accepted")
            self.goal_handle_.get_result_async().add_done_callback(
                self.goal_result_callback
            )
        else:
            self.get_logger().warn("Goal Rejected")

    def goal_result_callback(self, future):
        # If the goal was accepted, Get result after the goal is completed whether it was successful, aborted or cancelled
        status = future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info("Success")
        elif status == GoalStatus.STATUS_ABORTED:
            self.get_logger().error("Aborted")
        elif status == GoalStatus.STATUS_CANCELED:
            self.get_logger().warn("Cancelled")
        result = future.result().result
        self.get_logger().info("Result : " + str(result.reached_number))

    def goal_feedback_callback(self, feedback_msg):
        # If the goal was accepted, Get feedback while the goal is being executed. Can be used to stop or modify goal or some other things depending on the feedback
        number = feedback_msg.feedback.current_number
        self.get_logger().info("Feedback : " + str(number))


def main(args=None):
    rclpy.init(args=args)
    node = CountUntilClientNode()
    node.send_goal(6, 1.0)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
