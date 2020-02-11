#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
from tf.transformations import euler_from_quaternion

twist = Twist()
nowX = 0
nowY = 0
theta = 0
goalX = 0.4
goalY = -0.25

pub_int = rospy.Publisher('cmd_vel',Twist,queue_size = 1)
rospy.init_node("Listen_node")

def kk_cb(msg):
    global nowX
    global nowY
    global theta
    global twist

    global goalX
    global goalY
    
    nowX = msg.pose.pose.position.x
    nowY = msg.pose.pose.position.y

    distance = math.sqrt( math.pow(nowX-goalX,2) + math.pow(nowY-goalY,2))
    print(distance)
    if distance >= 0.05: 
        theta = math.atan2((goalY - nowY),(goalX - nowX))
        
        qua = msg.pose.pose.orientation
        quaternion_list = [qua.x,qua.y,qua.z,qua.w]
        temp = euler_from_quaternion(quaternion_list)[2] #get yow
        
        e_theta = (theta-temp)
        omega = e_theta/3
        if omega > 0.15:
            omega = 0.15
        elif omega < -0.15:
            omega = -0.15
        # twist.linear.x = 0.05
        # twist.linear.y = 0.0
        # twist.linear.z = 0.0
        # twist.angular.x = 0.0
        # twist.angular.y = 0.0
        # twist.angular.z = 0.02
        # pub_int.publish(twist)
        if abs(e_theta) < math.pi/6:
            twist.linear.x = 0.05
            twist.angular.z = omega
            pub_int.publish(twist)
        else : 
            twist.linear.x = 0.0
            twist.angular.z = omega
            pub_int.publish(twist)
    else:
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