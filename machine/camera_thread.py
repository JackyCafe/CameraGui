import time

from PySide6.QtCore import QTimer, Slot, QThread

from image import Image
from machine import Camera
from script.gui import MainWindow
from signal_container import SignalContainer


class CameraThread(QThread):

    def __init__(self,window: MainWindow, camera: Camera):
        super(CameraThread, self).__init__()
        self.window = window
        self.camera = camera
        if self.camera.cap is None or not self.camera.cap.isOpened():
            self.connect = False
            self.running = False
        else:
            self.connect = True
            self.running = False
        # self.camera.open()
        self.signal = SignalContainer()
        self.image = self.camera.get_image()
        self.signal.update_image.connect(self.window.set_image)




    def run(self):
        while True:
            ret, frame = self.camera.cap.read()
            end = time.time() + 10
            print(end)
        # self.image = self.camera.get_image()
            self.signal.update_image.emit(frame)