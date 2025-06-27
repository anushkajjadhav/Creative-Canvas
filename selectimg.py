from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QApplication,
)
import sys


class ImageSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Paint")
        self.selectedImagePath = None
        self.layout = QVBoxLayout(self)
        self.selectButton = QPushButton("Select Image")
        self.selectButton.clicked.connect(self.openFileDialog)
        self.layout.addWidget(self.selectButton)

    def openFileDialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Paint", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_path:
            self.selectedImagePath = file_path
            print(f"Selected image: {file_path}")
            self.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = ImageSelectionDialog()
    if dialog.exec():

        selected_image_path = dialog.selectedImagePath
        if selected_image_path:
            print(f"The selected image path is: {selected_image_path}")
    sys.exit(app.exec())
