#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from area.srv import *

def area_client(x, y):
    rospy.wait_for_service('topic_area')
    try:
        area = rospy.ServiceProxy('topic_area', area_of_rectangular)
        resp1 = area(x, y)
        return resp1.Area
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s*%s"%(x, y))
    print("%s * %s = %s"%(x, y, area_client(x, y)))
