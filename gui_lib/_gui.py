# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from image import Image


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 600)
        self.image_label = QLabel(Form)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(0, 0, 800, 600))
        self.image_label.setFrameShape(QFrame.Box)
        self.image_label.setFrameShadow(QFrame.Plain)
        self.image_label.setLineWidth(2)
        self.startBtn = QPushButton(Form)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setGeometry(QRect(860, 0, 100, 50))
        self.stopBtn = QPushButton(Form)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setGeometry(QRect(860, 50, 100, 50))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.image_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.startBtn.setText(QCoreApplication.translate("Form", u"\u958b\u59cb\u9304\u5f71", None))
        self.stopBtn.setText(QCoreApplication.translate("Form", u" \u7d50\u675f\u9304\u5f71", None))
    # retranslateUi


    @Slot(Image)
    def set_image(self, camera_image):
        print("w:",camera_image.shape[1])
        image = QImage(camera_image, camera_image.shape[1], camera_image.shape[0], camera_image.strides[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(image)
        self.image_label.setPixmap(pix)