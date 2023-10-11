#!/usr/bin/env python3

########################################################################
# listens to new_target and populates a dict of uncaught targets.      #
# chooses the closest target to the turle and sends the chosen         #
# coordinates to ControlTurtle service. Once it receives success       #
# flag from service it gives the next coordinates and removes the      #
# caught turtle from the list and despawns (kill) it from the screen   #
########################################################################
import rclpy
from rclpy.node import Node

from my_robot_interfaces.srv import ControlTurtle
from my_robot_interfaces.msg import TargetList
from turtlesim.msg import Pose
from turtlesim.srv import Kill
import numpy as np
from functools import partial

class TurtleCatcherNode(Node):
    def __init__(self):
        super().__init__("turtle_catcher")
        self.pose_ = None
        self.new_target_subscriber_ = self.create_subscription(TargetList, 'new_target', 
                                                               self.populate_target, 10)
        self.pose_subscriber_ = self.create_subscription(Pose,'turtle1/pose',
                                                         self.turtle_pose_callback,10)
        self.target_list_ = []
        

    def turtle_pose_callback(self,msg):
        self.pose_ = msg

    def euclidean_dist(self,target):
        if self.pose_ == None:
            return 0
        dx = float(target[0]) - self.pose_.x
        dy = float(target[1]) - self.pose_.y
        distance = np.sqrt(dx ** 2 + dy ** 2)
        return distance
    
    def populate_target(self,msg):
        target = [msg.target_x, msg.target_y, msg.name]
        self.target_list_.append(target)
        self.choose_target()

    def choose_target(self):
        self.get_logger().info("choosing target")
        if self.target_list_ == []:
            return
        
        self.target_list_.sort(key=self.euclidean_dist)
        self.turtle_control_call(self.target_list_[0][0], self.target_list_[0][1], 
                                 self.target_list_[0][2])

    def turtle_control_call(self,target_x, target_y, name):
        client = self.create_client(ControlTurtle, 'turtle_control') 
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service to start.")

        request = ControlTurtle.Request()
        request.target_x = float(target_x)
        request.target_y = float(target_y)

        future = client.call_async(request)
        future.add_done_callback(partial(self.kill_call,name=name))

    def kill_call(self,future,name):
        try:
            response = future.result()
            if response.success == True:
                client = self.create_client(Kill, "kill") 
                while not client.wait_for_service(1.0):
                    self.get_logger().warn("Waiting for service to start.")
                request = Kill.Request()
                request.name = name
                future = client.call_async(request)
                future.add_done_callback(self.choose_target)
                self.get_logger().info("Turtle killed"+name)
                
        except Exception as e:
            self.get_logger().error("Service Failed %r" % (e,))

def main(args=None):
    rclpy.init(args=args)
    node = TurtleCatcherNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()