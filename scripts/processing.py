#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import FluidPressure

def get_height(msg,publisher_height):
    # Pabs = gauge + Patm
    absolute_pressure = 1000 * msg.fluid_pressure
    gauge_pressure = absolute_pressure - 101325
    height = gauge_pressure/(1000*9.81)

    odom = Odometry()
    odom.pose.pose.position.z = -height
    odom.header.frame_id = "odom"
    odom.child_frame_id = "vtec_u3/base_link"
    odom.header.stamp = rospy.Time.now()

    rospy.loginfo(odom)
    publisher_height.publish(odom)

def processing():
    rospy.init_node('processing')
    publisher_height = rospy.Publisher('/vtec_u3/odom_height', Odometry, queue_size=10)
    rospy.Subscriber ('/vtec_u3/pressure', FluidPressure, get_height, publisher_height)
    rospy.spin()

if __name__ == '__main__':
    processing()