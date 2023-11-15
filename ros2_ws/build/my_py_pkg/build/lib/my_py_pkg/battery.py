#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial
from my_robot_interfaces.srv import SetLed
 
 
class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery_node")
        self.battery_status = "Full"
        self.battery_last_check = self.get_current_time_sec()
        self.battery_timer = self.create_timer(0.1, self.check_battery_status)
        self.get_logger().info("Battery node is started.")

    def get_current_time_sec(self):
        sec, nsec = self.get_clock().now().seconds_nanoseconds()
        time_now = sec + nsec / 1000000000.0
        return time_now

    def check_battery_status(self):
        time_now = self.get_current_time_sec()
        if self.battery_status == "Full":
            if time_now - self.battery_last_check > 4.0:
                self.battery_status = "Empty"
                self.get_logger().info("Battery is empty!")
                self.battery_last_check = time_now
                self.call_set_led(3,1)

        else:
            if time_now - self.battery_last_check > 6.0:
                self.battery_status = "Full"
                self.get_logger().info("Battery is Full!")
                self.battery_last_check = time_now
                self.call_set_led(3,0)
                

    def call_set_led(self, led_number, state):
        client = self.create_client(SetLed,"set_led")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service to start.")

        request = SetLed.Request()
        request.led_number = led_number
        request.state = state

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_set_led, led_number=led_number, state=state))

    def callback_set_led(self, future, led_number, state):
        try:
            response = future.result()
            if response.success == True:
                self.get_logger().info("Led Panel changed correctly.")
            else:
                self.get_logger().info("Error in using service.")
        except Exception as e:
            self.get_logger().error("Service failed %r" % (e,))
    
 
 
def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()