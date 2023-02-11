#!/usr/bin/env python

# Haobo Yuan
# Jan 17, 2023
# File Version 3
# Desp: a script to subscribe data from simulator(/joy): thruttle&yoke and pulish velocity commands /tello/cmd_vel to UAV

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
 
def callback1(data):
	print('##################')

	twist.linear.z = data.axes[0]
	print('vertical speed: %.2f'%(twist.linear.z)) # positive-50~100-upward

	twist.linear.y = data.axes[1]
	print('forward speed: %.2f'%(twist.linear.y)) # positive-50~100-forward

	print('##################')
	pub.publish(twist)


def callback2(data):
	print('##################')

	twist.linear.x = data.axes[0]
	print('horizontal speed: %.2f'%(twist.linear.x)) # positive-50~100-right

	print('##################')
	pub.publish(twist)
	

	


# Intializes everything
def start():
	# publishing to "tello/cmd_vel" to control turtle1
	global pub
	pub = rospy.Publisher('tello/cmd_vel', Twist)

	global twist
	twist = Twist()

	# subscribed to thruttle
	rospy.Subscriber("/throttle/joy", Joy, callback1)

	# subscribed to yoke
	rospy.Subscriber("/yoke/joy", Joy, callback2)


	# starts the node
	rospy.init_node('Joy2UAV')
	rospy.spin()
 
if __name__ == '__main__':
	start()
