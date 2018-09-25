#!/usr/bin/env python

# E28 - Mobile Robotics
# Matt Zucker, Fall 2018
# Sharing data to callbacks in ROS, example 1: global variables

import rospy
from std_msgs.msg import String

foo = None

def callback(data):
    rospy.loginfo('foo is:' + str(foo))

def listener():

    global foo
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    foo = 'here is a message'

    rospy.spin()

if __name__ == '__main__':
    listener()
