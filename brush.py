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
from PySide6.QtCore import QCoreApplication
import sys
from PySide6.QtGui import QIcon
from PySide6.QtCore import QCoreApplication, QSize


class Ui_brush(object):
    def setupUi(self, brush):
        if not brush.objectName():
            brush.setObjectName("brush")
        brush.resize(173, 76)
        self.layout = QVBoxLayout(brush)
        self.comboBox = QComboBox(brush)

        icon = QIcon()
        icon.addFile(
            "../../Downloads/images/pencil.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.comboBox.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(
            "../../Downloads/images/paint.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.comboBox.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(
            "../../Downloads/images/ink-pen.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.comboBox.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(
            "../../Downloads/images/copyrighted-art.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.comboBox.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(
            "../../Downloads/images/paint-roller.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.comboBox.addItem(icon4, "")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(10, 20, 103, 32))
        self.layout.addWidget(self.comboBox)
        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(brush.accept)
        self.layout.addWidget(self.okButton)

        self.retranslateUi(brush)

        QMetaObject.connectSlotsByName(brush)

    # setupUi

    def retranslateUi(self, brush):
        brush.setWindowTitle(QCoreApplication.translate("brush", "brush", None))
        self.comboBox.setItemText(
            0, QCoreApplication.translate("brush", "Pencil", None)
        )
        self.comboBox.setItemText(1, QCoreApplication.translate("brush", "Spray", None))
        self.comboBox.setItemText(
            2, QCoreApplication.translate("brush", "Calligraphy", None)
        )
        self.comboBox.setItemText(
            3, QCoreApplication.translate("brush", "Watercolor", None)
        )

    # retranslateUi


# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QDialog


class brush(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_brush()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = brush()
    widget.show()
    sys.exit(app.exec())
