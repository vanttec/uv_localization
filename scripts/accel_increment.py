#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
----------------------------------------------------------
    @file: accel_increment.py
    @date: 9/3/2021
    @author: Yulisa Medina
    @e-mail: a01570056@itesm.mx
    @brief: ROS node to simulate accelerations
    @version: 1.0
    Open source
---------------------------------------------------------
'''

import rospy
from nav_msgs.msg import Odometry
from gazebo_msgs.msg import ModelStates, ModelState
from sensor_msgs import Imu
 
def updateAccel(msg,publisher_accel_increment):
  modelState = ModelState()
  modelState.model_name = msg.name[2]
  modelState.pose = msg.pose[2]

  modelState.twist.linear.x = msg.twist[2].linear.x + 0.1
  modelState.twist.linear.y = msg.twist[2].linear.y
  modelState.twist.linear.z = msg.twist[2].linear.z
  
  modelState.twist.angular.x = msg.twist[2].angular.x
  modelState.twist.angular.y = msg.twist[2].angular.y
  modelState.twist.angular.z = msg.twist[2].angular.z

  rospy.loginfo(modelState)
  publisher_accel_increment.publish(modelState)


def accel_increment():
  rospy.init_node('accel_increment')
  publisher_accel_increment = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size= 10)
  rospy.Subscriber('/gazebo/model_states', ModelStates, updateAccel, publisher_accel_increment)

if __name__ == '__main__':
  accel_increment()
  rospy.spin()
