import time
from PySide6.QtCore import QThread
import cv2
from signal_container import SignalContainer


class CameraThread(QThread):
    rawdata = SignalContainer()  # 建立傳遞信號，需設定傳遞型態為 np.ndarray

    def __init__(self):
        super(CameraThread, self).__init__()
        self.cam = cv2.VideoCapture(0)
        if self.cam is None or not self.cam.isOpened():
            self.connect = False
            self.running = False
        else:
            self.connect = True
            self.running = False

    def run(self):
        """ 執行多執行緒
                   - 讀取影像
                   - 發送影像
                   - 簡易異常處理
               """
        print("do run")
        print("self.running:",self.running)
        print("self.connect:", self.connect)
        # 當正常連接攝影機才能進入迴圈
        while self.running and self.connect:
            ret, img = self.cam.read()  # 讀取影像
            if ret:
                self.rawdata.update_image.emit(img)  # 發送影像
            else:  # 例外處理
                print("Warning!!!")
                self.connect = False

    def open(self):
        """ 開啟攝影機影像讀取功能 """
        if self.connect:
            self.running = True  # 啟動讀取狀態

    def stop(self):
        """ 暫停攝影機影像讀取功能 """
        if self.connect:
            self.running = False  # 關閉讀取狀態

    def close(self):
        """ 關閉攝影機功能 """
        if self.connect:
            self.running = False  # 關閉讀取狀態
            time.sleep(1)
            self.cam.release()  # 釋放攝影機

