#Write your code here
import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow  # Make sure to replace 'ui_main' with the actual name of your UI file
import cv2

available_cam_ind=[]

def available_index():
    for camera_idx in range(10):
        cap = cv2.VideoCapture(camera_idx)
        if cap.isOpened():
            print(f'Camera index available: {camera_idx}')
            available_cam_ind.append(camera_idx)
            cap.release()

available_index()

class VideoPlayer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(VideoPlayer, self).__init__()
        self.setupUi(self)

        self.video_capture = None
        self.timer = QTimer(self)
        self.start.clicked.connect(self.start_video_feed)
        self.stop.clicked.connect(self.stop_video_feed)

    def start_video_feed(self):
        if not self.video_capture:
            #Camera address can be USB index, IP cam or even video file path
            self.video_capture = cv2.VideoCapture(available_cam_ind[0]) 
            # self.video_capture = cv2.VideoCapture("horse.mp4") 
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(30)  #Update the frame every 20 ms

    def stop_video_feed(self):
        if self.video_capture:
            self.timer.stop()
            self.video_capture.release()
            self.video_capture = None
            self.camera.clear()

    def update_frame(self):
        status, frame = self.video_capture.read()
        if status:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.camera.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoPlayer()
    window.show()
    sys.exit(app.exec_())