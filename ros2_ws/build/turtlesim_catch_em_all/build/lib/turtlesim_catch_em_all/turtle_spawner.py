#!/usr/bin/env python3

########################################################################
# Spawns turtle at random location [x, y] and publishes the new        #
# coordinates on new_target topic.                                     #
########################################################################

import rclpy
from rclpy.node import Node
import random as rnd
from my_robot_interfaces.msg import TargetList
from turtlesim.srv import Spawn
from functools import partial
 
 
class TurtleSpawnerNode(Node):
    def __init__(self):
        super().__init__("turtle_spawner")
        self.target_publisher_ = self.create_publisher(TargetList,'new_target',10)
        self.target_publish_timer_ = self.create_timer(1.0,self.target_spawn)

    def target_spawn(self): #Send request to service
        x = rnd.uniform(1.0,10.0)
        y = rnd.uniform(1.0,10.0)
        client = self.create_client(Spawn, "spawn") 
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service to start.")

        request = Spawn.Request()
        request.x = x
        request.y = y

        future = client.call_async(request)
        future.add_done_callback(partial(self.spawn_callback, x=x, y=y))
    
    def spawn_callback(self, future, x, y):
        try:
            response = future.result()
            self.get_logger().info("New turtle launched with name "+response.name)
            msg = TargetList()
            msg.name = response.name
            msg.target_x = x
            msg.target_y = y
            self.target_publisher_.publish(msg)
        except Exception as e:
            self.get_logger().error("Service Failed %r" % (e,))
        
 
 
def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawnerNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()