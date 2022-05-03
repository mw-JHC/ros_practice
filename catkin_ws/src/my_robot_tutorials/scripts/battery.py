#!/usr/bin/env python3

import rospy
from my_robot_msgs.srv import SetLed


def set_led(battery_state):
    rospy.wait_for_service("/set_led")
    try:
        service = rospy.ServiceProxy("/set_led",SetLed)
        state = 0
        if battery_state == "empty":
            state = 1
        resp = service(1, state)
        rospy.loginfo("Set led: " +str(resp))
    except rospy.ServiceException as e:
        rospy.logerr(e)

if __name__ == '__main__':
    rospy.init_node("Battery_node")

    battery_state = 'full'

    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        rate.sleep()
        battery_state = "empty"
        rospy.loginfo("the battery is empty!")
        set_led(battery_state)
        rate.sleep()
        battery_state = "full"
        rospy.loginfo("the battery is full")
        set_led(battery_state)
