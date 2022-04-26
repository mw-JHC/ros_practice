#!/usr/bin/env python3

import rospy 
from std_msgs.msg import Int64

counter = 0
pub = None

def callback_add_ints(msg):
    global counter
    counter += msg.data
    rospy.loginfo("The answer of addtion : ")
    rospy.loginfo(counter)
    answer = Int64()
    answer.data = counter
    pub.publish(answer)



if __name__ == '__main__':
    rospy.init_node("number_count")
    sub = rospy.Subscriber('/number', Int64, callback_add_ints)
    pub = rospy.Publisher('/number_count', Int64, queue_size= 10)
    rospy.spin()
