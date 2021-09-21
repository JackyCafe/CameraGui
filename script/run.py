import sys

from PySide6.QtWidgets import QApplication

from machine.camera_thread import CameraThread
from script.gui import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    camera = CameraThread()
    camera.start()
    window.show()
    exit(app.exec())


if __name__ == '__main__':
    main()
