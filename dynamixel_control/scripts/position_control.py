#!/usr/bin/env python

import rospy
from dynamixel_workbench_msgs.srv import JointCommand

angle = JointCommand()

if __name__ == '__main__':
    rospy.init_node('position_control', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    angle_service = rospy.ServiceProxy('joint_command', JointCommand)
    while not rospy.is_shutdown():
        angle.unit = "raw"
        angle.id = 12
        angle.goal_position = float(raw_input("Enter the angle:"))
        angle_service('raw', 12, angle.goal_position)
        rate.sleep()
