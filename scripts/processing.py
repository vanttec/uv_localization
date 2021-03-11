#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from gazebo_msgs.msg import LinkStates
from sensor_msgs.msg import FluidPressure

def get_height(msg,publisher_height):
    odom = Odometry()

    # Pabs = gauge + Patm
    absolute_pressure = 1000 * msg.fluid_pressure
    gauge_pressure = absolute_pressure - 101325
    height = gauge_pressure/(1000*9.81)

    odom.header.frame_id = "odom"
    odom.child_frame_id = "vtec_u3/pressure_link"
    odom.header.stamp = rospy.Time.now()

    odom.pose.pose.position.x = 0
    odom.pose.pose.position.y = 0
    odom.pose.pose.position.z = -height
    odom.pose.pose.orientation.x = 0
    odom.pose.pose.orientation.y = 0
    odom.pose.pose.orientation.z = 0
    odom.pose.pose.orientation.w = 0
    odom.pose.covariance = [0.00001] * 36

    odom.twist.twist.linear.x = 0
    odom.twist.twist.linear.y = 0
    odom.twist.twist.linear.z = 0
    odom.twist.twist.angular.x = 0
    odom.twist.twist.angular.y = 0
    odom.twist.twist.angular.z = 0
    odom.twist.covariance = [0.00001] * 36

    rospy.loginfo(odom)
    publisher_height.publish(odom)

def set_height(msg,link_states):
    odom = Odometry()

    index = link_states.name.index("vtec_u3/pressure_link")

    odom.header.frame_id = "odom"
    odom.child_frame_id = "odom"
    odom.header.stamp = rospy.Time.now()

    odom.pose.pose.position.x = 0
    odom.pose.pose.position.y = 0
    odom.pose.pose.position.z = link_states[index].pose.z
    odom.pose.pose.orientation.x = 0
    odom.pose.pose.orientation.y = 0
    odom.pose.pose.orientation.z = 0
    odom.pose.pose.orientation.w = 0
    odom.pose.covariance = [0.00001] * 36

    odom.twist.twist.linear.x = 0
    odom.twist.twist.linear.y = 0
    odom.twist.twist.linear.z = 0
    odom.twist.twist.angular.x = 0
    odom.twist.twist.angular.y = 0
    odom.twist.twist.angular.z = 0
    odom.twist.covariance = [0.00001] * 36

    rospy.loginfo(odom)
    publisher_height.publish(odom)

def processing():
    rospy.init_node('processing')
    publisher_height = rospy.Publisher('/vtec_u3/odom_height', Odometry, queue_size=10)
    publisher_gt = rospy.Publisher('/vtec_u3/odom_gt', Odometry, queue_size=10)
    rospy.Subscriber('/gazebo/LinkStates', LinkStates, set_height, publisher_gt)
    rospy.Subscriber ('/vtec_u3/pressure', FluidPressure, get_height, publisher_height)
    rospy.spin()

if __name__ == '__main__':
    processing()