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


class Ui_Dialogg(object):
    def setupUi(self, Dialogg):
        if not Dialogg.objectName():
            Dialogg.setObjectName("Dialogg")
        Dialogg.resize(173, 76)
        self.layout = QVBoxLayout(Dialogg)
        self.comboBox = QComboBox(Dialogg)
        icon = QIcon()
        icon.addFile(
            "../../Downloads/images/png-file-.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.comboBox.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(
            "../../Downloads/images/jpeg.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.comboBox.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(
            "../../Downloads/images/pdf copy.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.comboBox.addItem(icon2, "")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(30, 20, 101, 41))
        self.layout.addWidget(self.comboBox)
        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(Dialogg.accept)
        self.layout.addWidget(self.okButton)
        self.retranslateUi(Dialogg)

        QMetaObject.connectSlotsByName(Dialogg)

    # setupUi

    def retranslateUi(self, Dialogg):
        Dialogg.setWindowTitle(
            QCoreApplication.translate("Dialogg", "Select an Format", None)
        )
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialogg", "PNG", None))
        self.comboBox.setItemText(
            1, QCoreApplication.translate("Dialogg", "JPEG", None)
        )
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialogg", "PDF", None))

    # retranslateUi


# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QDialog


class Dialogg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialogg()
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
    widget = Dialogg()
    widget.show()
    sys.exit(app.exec())
