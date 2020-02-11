#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math


twist = Twist()
flag = 0
start = 0
now = 0

pub_int = rospy.Publisher('cmd_vel',Twist,queue_size = 1)
rospy.init_node("Listen_node")

def kk_cb(msg):
    global flag
    global start
    global now
    global twist
    if flag == 0:
        start = msg.pose.pose.position.x  
        twist.linear.x = 0.05
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        pub_int.publish(twist)
        flag = 1
    # else :
    #     pub_int.publish(twist)
    now = msg.pose.pose.position.x  
    print(start)
    print(now)
    if abs(now) >abs(start) +0.2:
    # if math.sqrt((now*now)-(start*start)) > 0.2:
        print('stop')
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        pub_int.publish(twist)
        rospy.signal_shutdown('eiei')

rospy.Subscriber("odom",Odometry,kk_cb)

rospy.spin()