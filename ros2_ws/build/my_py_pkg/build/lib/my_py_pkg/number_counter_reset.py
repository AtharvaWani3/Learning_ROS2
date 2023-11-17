#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool
 
 
class NumberCounterResetNode(Node):
    def __init__(self):
        super().__init__("node_name")
        self.subscriber_ = self.create_subscription(
            Int64,"/number_count", self.call_reset_count, 10
            )
        self.get_logger().info("Number_reset is active.")
        

    def call_reset_count(self, msg):
        if msg.data >= 300:
            client = self.create_client(SetBool,"reset_counter")
            while not client.wait_for_service(1.0):
                self.get_logger().warn("Waiting for service...")
            
            request = SetBool.Request()
            request.data = True

            future = client.call_async(request)
    
 
 
def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterResetNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()