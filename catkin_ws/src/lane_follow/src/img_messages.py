from sensor_msgs.msg import CompressedImage
import cv2 
import numpy as np
import rospy


def compressed_img_message(image_np: np.ndarray):
    msg = CompressedImage()
    msg.header.stamp = rospy.Time.now()
    msg.format = "jpeg"
    retval, encoded = cv2.imencode('.jpg', image_np)
    if not retval:
        raise RuntimeError("Unable to encode image, {}".format(image_np))
    msg.data = np.array(encoded).tostring()
    return msg

def np_from_compressed_ros_msg(ros_data) -> np.ndarray:
    np_arr = np.fromstring(ros_data.data, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)