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
from geometry_msgs.msg import Twist, Pose
from gazebo_msgs.msg import ModelStates
from sensor_msgs.msg import Imu

class Imu_msg:
  def __init__(self):
    self.imu_msg = Imu()
    rospy.init_node('pub_imu_accel')
    self.pub_imu = rospy.Publisher('/vtec_u3/imu', Imu, queue_size= 1)
    rospy.Subscriber('/uuv_accel', Twist, self.updateAccel)
    # rospy.Subscriber('/uuv_simulation/dynamic_model/pose', Pose, updateAccel, pub_imu)
    rospy.Subscriber('/uuv_simulation/dynamic_model/vel', Twist, self.updateVel)
    rospy.Subscriber('/gazebo/model_states', ModelStates, self.updateAttitude)

  def updateVel(self, msg):
      self.imu_msg.angular_velocity.x = 0
      self.imu_msg.angular_velocity.y = 0
      self.imu_msg.angular_velocity.z = msg.angular.z

  def updateAttitude(self, msg):
      i = msg.name.index('vtec_u3')
      self.imu_msg.orientation.x = msg.pose[i].orientation.y
      self.imu_msg.orientation.y = msg.pose[i].orientation.x
      self.imu_msg.orientation.z = -msg.pose[i].orientation.z
      self.imu_msg.orientation.w = msg.pose[i].orientation.w

  def updateAccel(self, msg):
      self.imu_msg.linear_acceleration.x = msg.linear.x
      self.imu_msg.linear_acceleration.y = msg.linear.y
      self.imu_msg.linear_acceleration.z = msg.linear.z

  def pubMsg(self):
      self.pub_imu.publish(self.imu_msg)

if __name__ == '__main__':
  imu = Imu_msg()
  rate = rospy.Rate(10)
  while(not rospy.is_shutdown()):
    imu.pubMsg()
    rate.sleep()
