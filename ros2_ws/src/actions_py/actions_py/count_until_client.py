#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.action import CountUntil
from rclpy.action import ActionClient
 
 
class CountUntilClientNode(Node):
    def __init__(self):
        super().__init__("count_until_client")
        self.count_until_client_ = ActionClient(self, CountUntil, "count_until")

    def send_goal(self, target_number, period):
        #Wait for action server
        self.count_until_client_.wait_for_server()

        #Create goal
        goal = CountUntil.Goal()
        goal.target_number = target_number
        goal.period = period

        #Send goal
        self.get_logger().info("Sending Goal")
        self.count_until_client_.send_goal_async(goal)

def main(args=None):
    rclpy.init(args=args)
    node = CountUntilClientNode()
    node.send_goal(6, 1.0)
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()