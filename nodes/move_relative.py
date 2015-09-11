#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

import roslib; roslib.load_manifest('zaber_stage')
import rospy

import actionlib

from geometry_msgs.msg import Pose
from zaber_stage.msg import MoveAction,MoveGoal

def move_relative_client():
    client = actionlib.SimpleActionClient('/zaber_stage_controller/move_relative', MoveAction)

    client.wait_for_server()

    pose = Pose()
    pose.position.x = 1000
    pose.position.y = 2000
    goal = MoveGoal(pose=pose)

    client.send_goal(goal)

    client.wait_for_result()

    return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('zaber_stage_move_relative')
        rospy.loginfo('zaber_stage moving relative...')
        result = move_relative_client()
        rospy.loginfo('zaber_stage move relative finished!')
    except rospy.ROSInterruptException:
        print "program interrupted before completion"
