#!/usr/bin/env python

# Haobo Yuan
# Jan 17, 2023
# File Version 2
# Desp: a test script to subscribe data from thruttle(/joy) and publish verticle data for UAV
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
 
def callback(data):
	twist = Twist()

	twist.linear.z = data.axes[0]
	print('vertical speed: %.2f'%(twist.linear.z)) # positive-50~100-upward

    	twist.linear.y = data.axes[1]
    	print('forward speed: %.2f'%(twist.linear.y)) # positive-50~100-forward

	twist.linear.x = data.axes[2]
    	print('horizontal speed: %.2f'%(twist.linear.x)) # positive-50~100-right

	pub.publish(twist)
 
# Intializes everything
def start():
	# publishing to "tello/cmd_vel" to control turtle1
	global pub
	pub = rospy.Publisher('tello/cmd_vel', Twist)

	# subscribed to joystick inputs on topic "joy"
	rospy.Subscriber("joy", Joy, callback)

	# starts the node
	rospy.init_node('Joy2Turtle')
	rospy.spin()
 
if __name__ == '__main__':
	start()
