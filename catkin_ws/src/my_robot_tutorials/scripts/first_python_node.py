#!/usr/bin/env python3

import rospy

if __name__ == '__main__':
    rospy.init_node('first_python_node')
    rospy.loginfo("This node has been started")

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown(): # if the node is not shutdowned, it work again
        rospy.loginfo("Hellow")
        rate.sleep()
