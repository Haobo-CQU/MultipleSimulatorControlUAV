#!/usr/bin/env python

# Haobo Yuan
# Nov 7, 2022
# File Version 1
# Desp: a test script to subscribe data from thruttle(/joy) and publish verticle data for UAV
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
 
def callback(data):
	twist = Twist()

	twist.linear.z = data.axes[0]
	print('vertical speed: %.2f'%(twist.linear.z))
	pub.publish(twist)
 
# Intializes everything
def start():
	# publishing to "cmd_vel" to control turtle1
	global pub
	pub = rospy.Publisher('tello/cmd_vel', Twist)

	# subscribed to joystick inputs on topic "joy"
	rospy.Subscriber("joy", Joy, callback)

	# starts the node
	rospy.init_node('Joy2Turtle')
	rospy.spin()
 
if __name__ == '__main__':
	start()
