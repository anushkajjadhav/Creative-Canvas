from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QColorDialog
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window with Color Picker")

        menuBar = self.menuBar()
        toolsMenu = menuBar.addMenu("&Tools")

        colorPickerAction = toolsMenu.addAction("Change Color")
        colorPickerAction.triggered.connect(self.showColorPicker)

    def showColorPicker(self, colorSelectedCallback=None):

        color = QColorDialog.getColor(Qt.white, self, "Choose Color")

        if color.isValid():
            print(f"Selected Color: {color.name()}")
            if colorSelectedCallback:
                colorSelectedCallback(color)


if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
