#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
import socketio
from std_msgs.msg import String


myUsername = "robot1"

# Initialize ROS node
rospy.init_node('socket_io_to_arduino')

# Create a ROS publisher to send data to Arduino
arduino_pub = rospy.Publisher('arduino_topic', String, queue_size=10)

# Initialize Socket.IO client
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    rospy.loginfo('Connected to Socket.IO server')
    sio.emit('join', myUsername)

@sio.on('perintah')
def perintah(command):
    rospy.loginfo('Received data: %s', command)
    
    # Create a ROSserial message
    ros_data = String()
    ros_data.data = String(command)

    #motor a
    if(command == "akiri"):
        arduino_pub.publish(ros_data)
        print("motor a ke kiri")

    elif(command == "akanan"):
        arduino_pub.publish(ros_data)
        print("motor a ke kanan")

    #motor b
    elif(command == "bkiri"):
        arduino_pub.publish(ros_data)
        print("motor b ke kiri")

    elif(command == "bkanan"):
        arduino_pub.publish(ros_data)
        print("motor b ke kanan")

    #motor c
    elif(command == "ckiri"):
        arduino_pub.publish(ros_data)
        print("motor c ke kiri")

    elif(command == "ckanan"):
        arduino_pub.publish(ros_data)
        print("motor c ke kanan")

    #motor penendang
    elif(command == "umpan"):
        arduino_pub.publish(ros_data)
        print("tendangan umpan")
    
    elif(command == "sesi satu"):
        arduino_pub.publish(ros_data)
        print("mulai sesi 1")

    elif(command == "sesi dua"):
        arduino_pub.publish(ros_data)
        print("mulai sesi 2")
        
    elif(command == "sesi dua beda"):
        arduino_pub.publish(ros_data)
        print("mulai sesi 2")

    elif(command == "minta umpan"):
        arduino_pub.publish(ros_data)
        print("robot 1 meminta umpan")

    elif(command == "sesi tiga"):
        arduino_pub.publish(ros_data)
        print("mulai sesi 3")


    elif(command == "gol"):
        arduino_pub.publish(ros_data)
        print("tendangan gol")

    #motor penggiring
    elif(command == "penggiring hidup"):
        arduino_pub.publish(ros_data)
        print("penggiring dihidupkan")

    elif(command == "penggiring mati"):
        arduino_pub.publish(ros_data)
        print("penggiring dimatikan")
    
    #cas
    elif(command == "cas hidup"):
        arduino_pub.publish(ros_data)
        print("penggiring dihidupkan")

    elif(command == "cas mati"):
        arduino_pub.publish(ros_data)
        print("cas dimatikan")
    #gerakan1
    elif(command == "maju"):
        arduino_pub.publish(ros_data)
        print("robot bergerak maju")

    elif(command == "mundur"):
        arduino_pub.publish(ros_data)
        print("robot bergerak mundur")
    
    #gerakan2
    elif(command == "gerak kiri"):
        arduino_pub.publish(ros_data)
        print("robot bergerak ke kiri")

    elif(command == "gerak kanan"):
        arduino_pub.publish(ros_data)
        print("robot bergerak ke kanan")

    # elif(command == "putar kiri"):
    #     tell("putar kiri")
    #     print("robot bergerak putar kiri")

    # elif(command == "putar kanan"):
    #     tell("putar kanan")
    #     print("robot bergerak putar kanan")
    
    # elif(command == "serong kiri"):
    #     tell("serong kiri")
    #     print("robot bergerak serong kiri")

    # elif(command == "serong kanan"):
    #     tell("serong kanan")
    #     print("robot bergerak serong kanan")
    
    # #berhenti
    # elif(command == "berhenti"):
    #     tell("berhenti")
    #     print("semua motor penggerak dimatikan")

    # #skill
    # elif(command == "ambil posisi"):
    #     tell("ambil posisi")
    #     print("robot mengambil posisi ke tengah lapangan")
    
    # elif(command == "ambil bola"):
    #     tell("ambil bola")
    #     print("robot mengambil bola ke tengah lapangan")
        
    # elif(command == "cari bola"):
    #     tell("cari bola")
    #     print("robot mencari bola")
        
    # elif(command == "cari kawan"):
    #     tell("cari kawan")
    #     print("robot mencari kawan")
        
    # elif(command == "stop program"):
    #     tell("stop program")
    #     print("robot menghentikan program skill")
        
    # elif(command == "servo"):
    #     tell("servo")
    #     print("robot menundukan servo")

@sio.on('data_event')
def on_data(data):
    rospy.loginfo('Received data: %f', data)

    # Create a ROSserial message
    ros_data = String()
    ros_data.data = data

    # Publish the data to Arduino
    arduino_pub.publish(ros_data)

@sio.on('disconnect')
def on_disconnect():
    rospy.loginfo('Disconnected from Socket.IO server')

# Start the Socket.IO client
sio.connect('http://localhost:3000')

# Run the ROS node
rospy.spin()

# Disconnect from the Socket.IO server when ROS node is shutdown
sio.disconnect()