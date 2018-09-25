#!/usr/bin/env python

# E28 - Mobile Robotics
# Matt Zucker, Fall 2018
# Sharing data to callbacks in ROS, example 5: class variables

import rospy
from std_msgs.msg import String

class Listener:

    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("chatter", String, self.callback)

        self.foo = 'hello everybody'

    def callback(self, msg):
        rospy.loginfo('foo is:' + str(self.foo) + ' and data is ' + msg.data)

def main():
    
    l = Listener()
    
    #l.foo = 'does this work?' 

    rospy.spin()

if __name__ == '__main__':
    main()
