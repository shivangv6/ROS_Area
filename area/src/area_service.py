#!/usr/bin/env python

from __future__ import print_function

from area.srv import area_of_rectangular,area_of_rectangularResponse
import rospy

def handle_area_of_rectangular(req):
    print("Returning [%s * %s = %s]"%(req.H,req.W, (req.H * req.W)))
    return area_of_rectangularResponse(req.H*req.W)

def area_of_rectangle():
    rospy.init_node('area_node')
    s = rospy.Service('topic_area',area_of_rectangular,handle_area_of_rectangular)
    print("Ready to product two floats.")
    rospy.spin()

if __name__ == "__main__":
    area_of_rectangle()
