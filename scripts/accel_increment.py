#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
 
 def updateAccel(msg,publisher_accel_increment):
 	odom = Odometry()
    odom.header.stamp = rospy.Time.now()
    odom.header.frame_id = "odom"
    odom.child_frame_id = "vtec_u3/base_link"

    odom.twist.twist.linear = [msg.odom.twist.twist.linear.x + 10, msg.odom.twist.twist.linear.y + 10, msg.odom.twist.twist.linear.z + 10]
    # odom.twist.twist.linear.x = msg.odom.twist.twist.linear.x + 10
    # odom.twist.twist.linear.y = msg.odom.twist.twist.linear.y + 10
    # odom.twist.twist.linear.z = msg.odom.twist.twist.linear.z + 10

    odom.twist.twist.angular = [msg.odom.twist.twist.angular.x + 10, msg.odom.twist.twist.angular.y + 10, msg.odom.twist.twist.angular.z + 10]
    # odom.twist.twist.angular.x = msg.odom.twist.twist.angular.x + 10
    # odom.twist.twist.angular.y = msg.odom.twist.twist.angular.y + 10
    # odom.twist.twist.angular.z = msg.odom.twist.twist.angular.z + 10

    # rospy.loginfo(odom)

    # Cada dos segundos
    rate = rospy.Rate(0.5) 

    while not rospy.is_shutdown():
		publisher_accel_increment.publish(odom)


 def accel_increment():
 	rospy.init_node('accel_increment')
 	publisher_accel_increment = rospy.Publisher('/vtec_u3/accel_increment', Odometry, queue_size= 10)
 	# Nombre de topico para obtener odometria del robot
 	rospy.Subscriber('/gazebo/model_states', Odometry, updateAccel, publisher_accel_increment)
 	rospy.spin()

if __name__ == '__main__':
	accel_increment()
    