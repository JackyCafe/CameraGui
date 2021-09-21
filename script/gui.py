from PySide6.QtCore import Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QMainWindow

from gui_lib import Ui_Form
from image import Image
from machine.camera_thread import CameraThread


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self,):
        super().__init__()
        self.setupUi(self)
        self.frame_num = 0
        self.ProcessCam = CameraThread()  # 建立相機物件
        self.ProcessCam.rawdata.update_image.connect(self.set_image)  # 槽功能：取得並顯示影像

        # self.ProcessCam.start()
        self.startBtn.clicked.connect(self.startVideo)
        self.stopBtn.clicked.connect(self.stopVideo)

    # def getRaw(self, data):  # data 為接收到的影像
    #     """ 取得影像 """
    #     self.showData(data)  # 將影像傳入至 showData()

    @Slot(Image)
    def set_image(self, camera_image):
        image = QImage(camera_image, camera_image.shape[1], camera_image.shape[0],  camera_image.strides[0], QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)
        self.image_label.setPixmap(pix)

    def startVideo(self):
        if self.ProcessCam.connect:
            self.ProcessCam.running = True
            self.ProcessCam.open()
            self.ProcessCam.start()
            self.startBtn.setEnabled(True)
        else:
            self.startBtn.setEnabled(False)

    def stopVideo(self):
        if self.ProcessCam.connect:
            self.ProcessCam.stop()
            self.startBtn.setEnabled(True)
        else:
            self.startBtn.setEnabled(False)