#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64 
from example_interfaces.srv import SetBool
 
class NumberCounterNode(Node): 
    def __init__(self):
        super().__init__("number_counter")
        self.counter = 0
        self.subscriber_ = self.create_subscription(
            Int64, "number", self.callback_number, 10
        )
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        #self.timer_ = self.create_timer(0.5, self.callback_count_publisher) -- Don't really need this
        self.service_ = self.create_service(SetBool,"reset_counter",self.callback_reset_counter)
        self.get_logger().info("number_counter_server is active.")


    def callback_number(self, msg):
        self.counter += msg.data
        #Need to do following steps to fix "Don't really need to do this" remarks
        new_msg = Int64()
        new_msg.data = self.counter
        self.publisher_.publish(new_msg)

    def callback_reset_counter(self, request, response):
        if request.data == True:
            self.counter = 0
            response.success = True
            response.message = "Counter has been Reset."
        else:
            response.success = False
            response.message = "Counter has not been Reset."
        return response
    
    # def callback_count_publisher(self): Dont really need this
    #     msg = Int64()
    #     msg.data = self.counter
    #     self.publisher_.publish(msg)
        

 
 
def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()