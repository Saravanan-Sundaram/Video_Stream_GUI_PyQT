# Write your code here
import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui_main import (
    Ui_MainWindow,
)
import cv2
import os
from datetime import datetime

available_cam_ind = [0]


def available_index():
    for camera_idx in range(10):
        cap = cv2.VideoCapture(camera_idx)
        if cap.isOpened():
            available_cam_ind.append(camera_idx)
            cap.release()


# available_index()


class VideoPlayer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(VideoPlayer, self).__init__()  # Initialize the base class QMainWindow
        self.setupUi(self)

        self.video_capture = None
        self.capture_image_count = 0
        self.timer = QTimer(self)
        self.start.clicked.connect(self.start_video_feed)
        self.stop.clicked.connect(self.stop_video_feed)
        self.capture.clicked.connect(self.capture_the_image)

    def start_video_feed(self):
        """It stream the video by reading from the video source .
        Video source can it be a USB,IP cam or Local file video"""

        if not self.video_capture and available_cam_ind:
            # Camera address can be USB index, IP cam or even video file path
            self.video_capture = cv2.VideoCapture(available_cam_ind[0])
            # self.video_capture = cv2.VideoCapture("horse.mp4")

            self.timer.timeout.connect(self.update_frame)
            self.timer.start(30)  # Update the frame every 20 ms

    def stop_video_feed(self):
        """It stops the video stream , and release the video listening.
        Also it clears the frame from the window"""

        if self.video_capture:
            self.timer.stop()
            self.video_capture.release()
            self.video_capture = None
            self.camera.clear()

    def capture_the_image(self):
        """It capture the image and save it in local"""
        if self.video_capture:
            image_dir = "image_data/"
            if not os.path.exists(image_dir):
                os.mkdir(image_dir)

            self.capture_image_count += 1
            current_date_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S:%f")
            image_name = f"{current_date_time}_{self.capture_image_count}"
            filename = image_dir + image_name + ".jpg"

            status, frame = self.video_capture.read()
            if status:
                height, width = 480, 640
                frame = cv2.resize(frame, (width, height))
                cv2.imwrite(filename, frame)

    def update_frame(self):
        """Frames are read and the frame is set to the Image label"""

        status, frame = self.video_capture.read()
        if status:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(
                frame.data, width, height, bytes_per_line, QImage.Format_RGB888
            )
            pixmap = QPixmap.fromImage(q_image)
            self.camera.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoPlayer()
    window.show()
    sys.exit(app.exec_())
