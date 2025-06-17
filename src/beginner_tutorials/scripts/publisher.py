#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray

def publisher():
    pub = rospy.Publisher('two_numbers', Int32MultiArray, queue_size=10)
    rospy.init_node('number_publisher', anonymous=True)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        msg = Int32MultiArray()
        msg.data = [3, 4]
        pub.publish(msg)
        rospy.loginfo("Published: %s", msg.data)
        rate.sleep()

if __name__ == '__main__':
    publisher()
