#!/usr/bin/env python

# E28 - Mobile Robotics
# Matt Zucker, Fall 2018
# Sharing data to callbacks in ROS, example 4: lambdas (anymous functions)

import rospy
from std_msgs.msg import String

def callback_two_args(msg, foo):
     rospy.loginfo('foo is:' + str(foo) + ' and data is ' + msg.data)

def listener():

    rospy.init_node('listener', anonymous=True)

    callback = lambda msg: callback_two_args(msg, lfoo)

    rospy.Subscriber("chatter", String, callback)

    lfoo = 'here is a message'

    rospy.spin()

if __name__ == '__main__':
    listener()
