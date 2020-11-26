#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import FluidPressure
from tf.transformations import euler_from_quaternion, quaternion_from_euler

def get_height(msg,publisher_height):
 pressure = msg.fluid_pressure
 height = pressure/(1000*9.81)
 odom = Odometry()
 odom.pose.pose.position.z = height
 odom.pose.pose.position.x = 0
 odom.pose.pose.position.y = 0
 odom.twist.twist.linear.x = 0
 odom.twist.twist.linear.y = 0
 odom.twist.twist.linear.z = 0
 odom.twist.twist.angular.x = 0
 odom.twist.twist.angular.y = 0
 odom.twist.twist.angular.z = 0
 odom.header = msg.header
 rospy.loginfo(odom) 
 publisher_height.publish(odom)
 
def processing():
 rospy.init_node('processing')
 publisher_height = rospy.Publisher('/vtec_u3/odom_height', Odometry, queue_size=10) ######CAMBIAR
 rospy.Subscriber ('/vtec_u3/pressure', FluidPressure, get_height, publisher_height)
 rate = rospy.Rate(20)
 rospy.spin()

if __name__ == '__main__':
 processing()