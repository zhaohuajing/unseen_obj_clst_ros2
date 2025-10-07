#!/usr/bin/env python3

from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

self.pub = self.create_publisher(Image, 'segmentation_mask', 10)
self.bridge = CvBridge()

# After subprocess produces mask.png
cv_img = cv2.imread('mask.png', cv2.IMREAD_GRAYSCALE)
msg = self.bridge.cv2_to_imgmsg(cv_img, encoding="mono8")
self.pub.publish(msg)

