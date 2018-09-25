#!/usr/bin/env python

# E28 - Mobile Robotics
# Matt Zucker, Fall 2018
# Sharing data to callbacks in ROS, example 2: using callback_args (hacky, bad)

import rospy
from std_msgs.msg import String

def callback(msg, foo):
    rospy.loginfo('foo is:' + str(foo) + ' and data is' + msg.data)

def listener():

    foo = [None]
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback, callback_args=foo)
    foo[0] = 'here is a message'

    rospy.spin()

if __name__ == '__main__':
    listener()
