#!/usr/bin/env python

# E28 - Mobile Robotics
# Matt Zucker, Fall 2018
# Sharing data to callbacks in ROS, example 3: inner functions

import rospy
from std_msgs.msg import String


def listener():

    rospy.init_node('listener', anonymous=True)

    def callback(msg):
        rospy.loginfo('foo is:' + str(foo) + ' and data is ' + msg.data)

    rospy.Subscriber("chatter", String, callback)

    foo = 'here is a message'

    rospy.spin()

if __name__ == '__main__':
    listener()
