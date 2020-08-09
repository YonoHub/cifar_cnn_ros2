import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from std_msgs.msg import Int8
from sensor_msgs.msg import Image
import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras import models, layers


class CIFAR(Node):
    def __init__(self):
        super().__init__("cifar_node")
        self.subscription = self.create_subscription(
            Image, "/image", self.__clk, 10)
        self.subscription  # prevent unused variable warning
        self.publisher_ = self.create_publisher(Int8, '/cifar_out', 10)
        filepath = os.path.dirname(os.path.realpath(__file__))
        self.bridge = CvBridge()
        self.model = tf.keras.models.load_model(filepath+"/my_model.h5")
        self.model.summary()

    def __clk(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg)
        img_res = cv2.resize(image, (32, 32))
        img_res = img_res / 255
        prediction = Int8()
        prediction.data = int(
            np.argmax(self.model.predict(np.expand_dims(img_res, 0))))
        self.publisher_.publish(prediction)


def main(args=None):
    rclpy.init(args=args)
    cifar = CIFAR()
    rclpy.spin(cifar)
    cifar.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
