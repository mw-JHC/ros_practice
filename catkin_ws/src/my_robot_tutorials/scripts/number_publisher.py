#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64
import random

if __name__ == '__main__':
    rospy.init_node("number_publisher")
    pub = rospy.Publisher('/number', Int64, queue_size= 10)
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = Int64()
        msg.data = random.randint(1,10) # send random integer
        pub.publish(msg)
        rate.sleep()
    
    rospy.loginfo("Node was stopped")
