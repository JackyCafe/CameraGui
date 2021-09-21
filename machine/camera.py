import cv2
from image import Image


class Camera:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def open(self) ->None:
        if self.cap is None or not self.cap.isOpened():
            self.connect = False
            self.running = False
        else:
            self.connect = True
            self.running = False

    def get_image(self) -> Image:
        ret, frame = self.cap.read()
        return frame

    def close(self) ->None:
        self.cap.release()