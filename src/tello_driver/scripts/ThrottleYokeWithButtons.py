#!/usr/bin/env python

# Haobo Yuan
# Jan 17, 2023
# File Version 4
# Desp: a script to subscribe data from simulators(Namespace/joy): throttle&yoke and publish takeoff/velocity/land commands to UAV

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from sensor_msgs.msg import Joy


def callback1(data):
	print('##################')

	twist.linear.z = data.axes[0]
	print('vertical speed: %.2f'%(twist.linear.z)) # positive-50~100-upward

	twist.linear.y = data.axes[1]
	print('forward speed: %.2f'%(twist.linear.y)) # positive-50~100-forward

	pub1.publish(twist)
	
	print('##################')
	

def callback2(data):
    # Use yoke buttons to takeoff/land
	empty1 = Empty()
	empty2 = Empty()

	if data.buttons[3] == 1:
	    pub2.publish(empty1)
        # print('take off')

	if data.buttons[2] == 1:
		pub3.publish(empty2)
		# print('land')
    
    # Use yoke axes to control horizontal locomation
	print('##################')

	twist.linear.x = data.axes[0]
	print('horizontal speed: %.2f'%(twist.linear.x)) # positive-50~100-right
	pub1.publish(twist)
	
	print('##################')


# Intializes everything
def start():
	# publishing to "tello/cmd_vel" to control velocity
	global pub1
	pub1 = rospy.Publisher('tello/cmd_vel', Twist)

    # publishing to "tello/takeoff" to start
	global pub2
	pub2 = rospy.Publisher('tello/takeoff', Empty)

    # publishing to "tello/land" to end
	global pub3
	pub3 = rospy.Publisher('tello/land', Empty)

    # instantiation
	global twist
	twist = Twist()


	# subscribed to throttle
	rospy.Subscriber("/throttle/joy", Joy, callback1)

	# subscribed to yoke
	rospy.Subscriber("/yoke/joy", Joy, callback2)

	# starts the node
	rospy.init_node('Simulator2UAV')
	rospy.spin()


if __name__ == '__main__':
	start()
