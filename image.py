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
    QComboBox,
    QDialog,
    QLabel,
    QSizePolicy,
    QWidget,
)

from PySide6.QtWidgets import QPushButton


class Ui_draw(object):
    def setupUi(self, draw):
        if not draw.objectName():
            draw.setObjectName("draw")
        draw.resize(800, 500)
        self.label = QLabel(draw)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, 0, 820, 401))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("")
        self.comboBox = QComboBox(draw)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(330, 420, 131, 41))

        self.okButton = QPushButton("OK", draw)
        self.okButton.setObjectName("okButton")
        self.okButton.setGeometry(QRect(365, 470, 61, 31))

        self.retranslateUi(draw)

        QMetaObject.connectSlotsByName(draw)

    # setupUi

    def retranslateUi(self, draw):
        draw.setWindowTitle(
            QCoreApplication.translate("draw", "Browse Pre-Drawn Images", None)
        )
        self.label.setText("")
        self.comboBox.setItemText(
            0, QCoreApplication.translate("draw", "horse.png", None)
        )
        self.comboBox.setItemText(
            1, QCoreApplication.translate("draw", "house.png", None)
        )
        self.comboBox.setItemText(
            2, QCoreApplication.translate("draw", "icecream.png", None)
        )
        self.comboBox.setItemText(
            3, QCoreApplication.translate("draw", "rabbit.png", None)
        )
        self.comboBox.setItemText(
            4, QCoreApplication.translate("draw", "rainbow.png", None)
        )
        self.comboBox.setItemText(
            5, QCoreApplication.translate("draw", "tortoise.png", None)
        )

    # retranslateUi


import sys
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal


class draw(QDialog):

    imageSelected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_draw()
        self.ui.setupUi(self)

        self.images = {
            "horse.png": QPixmap("horse.png"),
            "house.png": QPixmap("house.png"),
            "icecream.png": QPixmap("icecream.png"),
            "rabbit.png": QPixmap("rabbit.png"),
            "rainbow.png": QPixmap("rainbow.png"),
            "tortoise.png": QPixmap("tortoise.png"),
        }

        self.ui.comboBox.currentIndexChanged.connect(self.load_image)

        self.ui.okButton.clicked.connect(self.emit_image_path)

        self.load_image()

    def load_image(self):

        selected_item = self.ui.comboBox.currentText()

        if selected_item in self.images:
            pixmap = self.images[selected_item]
            self.ui.label.setPixmap(pixmap)
            self.ui.label.setAlignment(Qt.AlignCenter)
            self.ui.label.setScaledContents(True)
        else:

            self.ui.label.clear()

    def emit_image_path(self):

        selected_item = self.ui.comboBox.currentText()

        self.imageSelected.emit(selected_item)

        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = draw()
    widget.show()
    sys.exit(app.exec())
