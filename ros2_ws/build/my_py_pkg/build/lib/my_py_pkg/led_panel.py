#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from my_robot_interfaces.srv import SetLed
from my_robot_interfaces.msg import LedStatus
 
 
class LedPanelNode(Node):
    def __init__(self):
        super().__init__("led_panel_node")
        self.declare_parameter("led_states",[0,0,0])
        self.led_panel_status = self.get_parameter("led_states").value
        self.set_led_service = self.create_service(SetLed, "set_led",self.callback_set_led)
        self.publisher_ = self.create_publisher(LedStatus,"led_status",10)
        self.timer_ = self.create_timer(1.0, self.callback_led_status)
        self.get_logger().info("Led panel node is started.")

    def callback_set_led(self, request ,response):
        led_number = request.led_number - 1
        led_state = request.state
        if led_number > len(self.led_panel_status) or led_number < 0:
            response.success = False
            return response
        
        if led_state not in [0,1]:
            response.success = False
            return response
        
        self.led_panel_status[request.led_number - 1] = request.state
        response.success = True
        return response
    
    def callback_led_status(self):
        msg = LedStatus()
        msg.led_status = self.led_panel_status
        self.publisher_.publish(msg)
    
 
 
def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()