import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QMenuBar,
    QDialog,
    QSlider,
    QVBoxLayout,
    QPushButton,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QMenuBar,
    QDialog,
    QSlider,
    QVBoxLayout,
    QPushButton,
)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class SliderDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Adjust Size")
        layout = QVBoxLayout(self)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(1)
        self.slider.setMaximum(10)
        self.slider.setSingleStep(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.valueChanged.connect(self.updateLabel)
        layout.addWidget(self.slider)

        self.valueLabel = QLabel("1", self)
        self.valueLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.valueLabel)

        self.okButton = QPushButton("OK", self)
        self.okButton.clicked.connect(self.accept)
        layout.addWidget(self.okButton)

        self.slider.setMinimumSize(200, 30)

    def updateLabel(self, value):
        """Update the label with the current slider value."""
        self.valueLabel.setText(str(value))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        menuBar = self.menuBar()
        settingsMenu = menuBar.addMenu("&Settings")

        adjustAction = settingsMenu.addAction("Adjust Size")
        adjustAction.triggered.connect(self.showSliderDialog)

    def showSliderDialog(self):
        dialog = SliderDialog(self)
        if dialog.exec():

            sliderValue = dialog.slider.value()
            print(f"Slider value: {sliderValue}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
