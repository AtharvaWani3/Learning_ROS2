#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
 
from my_robot_interfaces.srv import ComputeRectangleArea
from functools import partial

class RectangleAreaClientNode(Node):
    def __init__(self):
        super().__init__("rectangle_area_client_node")
        self.call_rectangle_area(10.0,10.0)
        
    def call_rectangle_area(self, length, width): #Send request to service
        client = self.create_client(ComputeRectangleArea, "rectangle_area") 
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service to start.")

        request = ComputeRectangleArea.Request()
        request.length = length
        request.width = width

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_rectangle_area, length=length, width=width))
    
    def callback_rectangle_area(self, future, length, width):
        try:
            response = future.result()
            self.get_logger().info("Area of rectangle with length "+str(length)+" and width "+str(width)+" = "+str(response.area))
        except Exception as e:
            self.get_logger().error("Service Failed %r" % (e,))

 
def main(args=None):
    rclpy.init(args=args)
    node = RectangleAreaClientNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()