#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray
import socketio

# Create a ROS node
rospy.init_node('odometry_subscriber')

# Create a subscriber to listen for odometry data
def odometry_callback(data):
    x = data.data[0]
    y = data.data[1]
    degree = data.data[2]
    socket.emit('odometry', {'x': x, 'y': y, 'degree': degree})

odometry_sub = rospy.Subscriber('odometry', Float32MultiArray, odometry_callback)

# Connect to the socket.io server
socket = socketio.Client()
socket.connect('http://localhost:3000')

rospy.spin()
