#!/usr/bin/env python3

import rospy 
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

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

#practice about service
def callback_reset_counter(req):
    if req.data == 1:
        global counter
        counter = 0
        rospy.loginfo("Counter has benn reset!!")
        return True, "counter has been successfully reset"
    else:
        return False, "counter has not been reset"


if __name__ == '__main__':
    rospy.init_node("number_count")
    sub = rospy.Subscriber('/number', Int64, callback_add_ints)
    pub = rospy.Publisher('/number_count', Int64, queue_size= 10)
    #rospy.spin()

    #practice about service
    reset_service = rospy.Service('/reset_counter',SetBool, callback_reset_counter)

    rospy.spin()