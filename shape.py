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
from PySide6.QtWidgets import QApplication, QComboBox, QDialog, QSizePolicy, QWidget
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QComboBox


class Ui_shape(object):
    def setupUi(self, shape):
        if not shape.objectName():
            shape.setObjectName("shape")
        shape.resize(173, 76)
        self.layout = QVBoxLayout(shape)
        self.comboBox = QComboBox(shape)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(160, 90, 103, 32))
        self.layout.addWidget(self.comboBox)
        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(shape.accept)
        self.layout.addWidget(self.okButton)

        self.retranslateUi(shape)

        QMetaObject.connectSlotsByName(shape)

    # setupUi

    def retranslateUi(self, shape):
        shape.setWindowTitle(QCoreApplication.translate("shape", "shape", None))
        self.comboBox.setItemText(
            0, QCoreApplication.translate("shape", "Square", None)
        )
        self.comboBox.setItemText(
            1, QCoreApplication.translate("shape", "Rectangle", None)
        )
        self.comboBox.setItemText(
            2, QCoreApplication.translate("shape", "Triangle", None)
        )
        self.comboBox.setItemText(
            3, QCoreApplication.translate("shape", "Circle", None)
        )
        self.comboBox.setItemText(
            4, QCoreApplication.translate("shape", "Hexagon", None)
        )
        self.comboBox.setItemText(5, QCoreApplication.translate("shape", "Star", None))
        self.comboBox.setItemText(
            6, QCoreApplication.translate("shape", "Ellipse", None)
        )

    # retranslateUi


# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QDialog


class shape(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_shape()
        self.ui.setupUi(self)
        self.selected_format = None
        self.ui.okButton.clicked.connect(self.set_selected_format)

    def set_selected_format(self):
        print("Setting selected format...")
        self.selected_format = self.ui.comboBox.currentText()
        self.accept()
        print("After accept")
        self.close()

    def get_selected_format(self):
        return self.selected_format


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = shape()
    widget.show()
    sys.exit(app.exec())
