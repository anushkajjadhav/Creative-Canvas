# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(800, 560)
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, 0, 800, 460))
        self.label.setStyleSheet("")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(240, 500, 304, 32))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "Enhance Hand Drawing", None)
        )
        self.label.setText("")
        self.pushButton.setText(
            QCoreApplication.translate("Dialog", "Load Image", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("Dialog", "Create Sketch", None)
        )
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", "Load", None))

    # retranslateUi


# This Python file uses the following encoding: utf-8
import sys
import sys
import sys
import cv2
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import Signal


class Dialog(QDialog):

    imageLoaded = Signal(QImage)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.image_path = None
        self.result_image = None
        self.ui.pushButton.clicked.connect(self.load_image)
        self.ui.pushButton_2.clicked.connect(self.create_sketch)
        self.ui.pushButton_3.clicked.connect(self.load_and_emit_image)

    def load_image(self):
        self.image_path, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if self.image_path:
            pixmap = QPixmap(self.image_path)
            self.ui.label.setPixmap(pixmap)
            self.ui.label.setScaledContents(True)

    def create_sketch(self):
        if self.image_path:

            image = cv2.imread(self.image_path)

            grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            invert = cv2.bitwise_not(grey_img)

            blur = cv2.GaussianBlur(invert, (21, 21), 0)

            invertedblur = cv2.bitwise_not(blur)

            sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

            darkened_sketch = cv2.multiply(sketch, 1.0)

            height, width = darkened_sketch.shape
            bytes_per_line = width
            qt_image = QImage(
                darkened_sketch.data,
                width,
                height,
                bytes_per_line,
                QImage.Format_Grayscale8,
            )
            pixmap = QPixmap.fromImage(qt_image)
            self.ui.label.setPixmap(pixmap)
            self.ui.label.setScaledContents(True)

            self.result_image = qt_image

            pixmap = QPixmap.fromImage(qt_image)
            self.ui.label.setPixmap(pixmap)
            self.ui.label.setScaledContents(True)

    def load_and_emit_image(self):
        if self.result_image:

            self.imageLoaded.emit(self.result_image)

            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Dialog()
    widget.show()
    sys.exit(app.exec())
