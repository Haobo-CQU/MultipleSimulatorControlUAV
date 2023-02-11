# Description
The software programs in this virtual machine are developed by
## Haobo Yuan , Xiangyu Han, Haoting Feng, Hongrui Yi
`yanho AT mail DOT uc DOT edu` and guided by
## Janet Dong, Ou Ma
in 2022-2023 at University of Cincinnati, College of Engineering and Applied Science,  Intelligent Robotics and Autonomous Systems (IRAS) Laboratory
## UC CEAS IRAS Lab
used for their senior design Capstone Project: Control UAV through a simulator

# Introduction
The simulator is composed of three devices: the throttle(1. right hand side), yoke(2. front of user), and rudder(3. front below of user). The whole system is run under Linux Ubuntu 16.04 with ROS1(Robot Operating System) Kinetics in VMWare.


# Usage
The set environment of this VMWare allows user to launch a file `YHB_Final.launch` to start up everything in ROS after firstly connecting to 
- the UAV `Tello...` through WIFI 
- the whole simulator into VMWare through 3 USB cables in the **right** order mentioned above
> roslaunch tello_driver YHB_Final.launch

User can operate the whole system followed these instructions:
1. The red bottom on the yoke flight right hand side allows user to sent `takeoff` command.
2. The first rod(left, black) and second rod (middle, blue) of throttle allows user to sent `z-axis`(vertical) and `x-axis` (forward and backwoard) linear velocity command. 
3. The yoke rotating left and right allows user to sent `y-axis` (horizontal) linear velocity command. 
4. The yoke rotating left and right allows user to sent `z-axis` (yaw) angular velocity command. 
5. The white bottom on the yoke flight right hand side allows user to sent `land` command.

Before taking off and after landing, sending any velocity command is meaningless.

# Software Program Description
## Driver
The UAV named tello is driven by `/home/ros/catkin_ws/src/tello_driver`.

> # tello_driver [![Build Status](http://build.ros.org/job/Ksrc_uX__tello_driver__ubuntu_xenial__source/badge/icon)](http://build.ros.org/job/Ksrc_uX__tello_driver__ubuntu_xenial__source/)
> 
> # 1. Overview
> Communicating with the Tello drone can be done either using official [Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf) or one of the unofficial libraries. The unofficial libraries originated from the reverse-engineering the raw packages broadcasted by the Tello. This ROS package is build on top of the unofficial [TelloPy](https://github.com/hanyazou/TelloPy) library. The [TelloPy](https://github.com/hanyazou/TelloPy) library is used at this moment since it offers more functionalities than the official [Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf) or any other unofficial library. 
> 
> eveloping of the tello_driver ROS package is inspired by [tello_driver](https://github.com/anqixu/tello_driver), which by now diverged considerately from the original work. Furthermore, development of this ROS package pursues not to modify the TelloPy library, but instead apply any modification or addition to the ros_driver package in an encapsulated manner. This prevents breaking functionalities when updating the TelloPy library.
> 
> ## Installation
> 
> ### ROS distribution  
> Binary release from the ROS repository:  
> * Kinetic: ``` $ sudo apt install ros-kinetic-tello-driver```
> 
> ### Build from source
> * ```$ cd <CATKIN_WS/SRC>```
> * ```$ git clone --recursive https://github.com/appie-17/tello_driver.git```
> * ```$ cd ..```
> * ```$ catkin_make```
> * ```$ source devel/setup.bash```
> 
> ## Launch
> 
> * Turn on Tello drone
> * Connect to drone's WiFi access point (```TELLO_XXXXXX)```
> * ```$ roslaunch tello_driver tello_node.launch```
> 
> # 2. Nodes
> 
> ## 2.1 tello_driver_node
> Main node running as interface for the TelloPy library
> 
> ### Subscribed topics
> * ```/tello/cmd_vel``` [geometry_msgs/Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html)
> * ```/tello/emergency``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
> * ```/tello/fast_mode``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
> * ```/tello/flattrim``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
> * ```/tello/flip``` [std_msgs/Uint8](http://docs.ros.org/api/std_msgs/html/msg/UInt8.html)
> * ```/tello/land``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
> * ```/tello/palm_land``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
> * ```/tello/takeoff``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
> * ```/tello/manual_takeoff``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
> * ```/tello/throw_takeoff``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
> 
> ### Published topics
> * ```/tello/camera/camera_info``` [sensor_msgs/CameraInfo](http://docs.ros.org/api/sensor_msgs/html/msg/CameraInfo.html)
> * ```/tello/image_raw``` [sensor_msgs/Image](http://docs.ros.org/api/sensor_msgs/html/msg/Image.html)
> * ```/tello/imag/raw/h264``` [h264_image_transport/H264Packet](https://github.com/tilk/h264_image_transport/blob/master/msg/H264Packet.msg)
> * ```/tello/odom``` [nav_msgs/Odometry](http://docs.ros.org/api/nav_msgs/html/msg/Odometry.html)
> * ```/tello/imu``` [sensor_msgs/Imu](http://docs.ros.org/api/sensor_msgs/html/msg/Imu.html)
> * ```/tello/status``` [tello_driver/TelloStatus](https://github.com/appie-17/tello_driver/blob/development/msg/TelloStatus.msg)

## ThrottleYokeWithButtonsAndRudder.py
We developed a Python program `ThrottleYokeWithButtonsAndRudder.py` to initialize ROS publisher and sub, subscribe data of both axis and button from three devides of the simulator, process the data, and send commands to the UAV

## YHB_Final.launch
We developed a launch file `YHB_Final.launch` to start up everything including
- set param needed to connect UAV through WIFI
- launch tello driver `tello_driver_node`
- launch `ThrottleYokeWithButtonsAndRudder.py`
- launch `joy_node` with three different **namespace** to collect data from the simulator semitanelously
    - `/throttle`
    - `/yoke`
    - `rudder`
- TODO: launch image transportation

# Last Edit
Haobo Yuan
Feb 8, 2023
