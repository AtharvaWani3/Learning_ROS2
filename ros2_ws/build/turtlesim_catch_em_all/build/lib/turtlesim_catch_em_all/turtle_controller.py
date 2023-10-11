#!/usr/bin/env python3

########################################################################
# Listens to target [x,y] from turtle_catcher and then controls the    #
# turtle to follow the goal.                                           #
# Sends a message back to turtle_catcher when reaches target.          #
########################################################################
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import numpy as np
from my_robot_interfaces.msg import TargetList
from functools import partial
import random
from turtlesim.srv import Kill
 
 
class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.pose_ = None
        self.target_list_ = [[random.uniform(1.0,10.0),random.uniform(1.0,10.0),'dummy']]
        self.target = []
        self.stuck_counter = 0
        self.pose_subscriber_ = self.create_subscription(Pose,'turtle1/pose',self.turtle_pose_callback,10)
        self.control_publisher_ = self.create_publisher(Twist,'turtle1/cmd_vel',10)
        self.new_target_subscriber_ = self.create_subscription(TargetList, 'new_target', 
                                                               self.populate_target, 10)
        if len(self.target_list_) >= 1:
            self.choose_target()
        
        

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
        # self.get_logger().info(str(self.target_list_))

    def choose_target(self):
        self.stuck_counter = 0
        self.target_list_.sort(key=self.euclidean_dist)
        if len(self.target_list_) < 1:
            self.target = [random.uniform(3.0,8.0),random.uniform(3.0,8.0),'dummy']
        else:
            self.target = self.target_list_[0]
        self.control_loop_timer_ = self.create_timer(0.1, self.turtle_control)
          

    def turtle_control(self):
        if self.pose_ == None:
            return 0
        
        dist_x = self.target[0] - self.pose_.x
        dist_y = self.target[1] - self.pose_.y
        dist = np.sqrt(dist_x * dist_x + dist_y * dist_y)

        msg = Twist()

        if dist > 1.0:
            
            msg.linear.x = 2.5*dist
            goal_theta = np.arctan2(dist_y,dist_x)
            diff = goal_theta - self.pose_.theta
            if diff > np.pi:
                diff -= np.pi
            elif diff < -np.pi:
                diff += np.pi
            msg.angular.z = 7*diff
            self.stuck_counter += 1
            self.get_logger().info(str(self.stuck_counter))
            if self.stuck_counter > 100:
                self.choose_target()
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            while len(self.target_list_) < 1:
                i=0
            kill = self.target_list_.pop(0)
            self.get_logger().info("Killed "+str(kill))
            self.kill_turtle(kill[2])
            self.choose_target()
        self.control_publisher_.publish(msg)
    
    def kill_turtle(self, name):
        client = self.create_client(Kill, "kill")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server...")

        request = Kill.Request()
        request.name = name

        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_call_kill, turtle_name=name))
    
    def callback_call_kill(self, future, turtle_name):
        try:
            future.result()
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()

