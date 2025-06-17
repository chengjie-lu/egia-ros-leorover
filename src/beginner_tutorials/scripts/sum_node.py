#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray, Int32

def callback(msg):
    if len(msg.data) >= 2:
        total = msg.data[0] + msg.data[1]
        rospy.loginfo("Received: %s, Sum = %d", msg.data, total)
        sum_pub.publish(total)

def listener():
    rospy.init_node('sum_node', anonymous=True)
    rospy.Subscriber('two_numbers', Int32MultiArray, callback)
    global sum_pub
    sum_pub = rospy.Publisher('sum', Int32, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    listener()
