# 

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
    QAction,
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
    QLabel,
    QMainWindow,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QWidget,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QWidget,
    QVBoxLayout,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)

        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        icon = QIcon()
        icon.addFile(
            "../../Downloads/images/add-folder.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionOpen.setIcon(icon)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setShortcutVisibleInContextMenu(True)
        self.actionOpen_2 = QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        icon1 = QIcon()
        icon1.addFile(
            "../../Downloads/images/open-folder.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionOpen_2.setIcon(icon1)
        self.actionOpen_2.setIconVisibleInMenu(True)
        self.actionOpen_2.setShortcutVisibleInContextMenu(True)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        icon2 = QIcon()
        icon2.addFile(
            "../../Downloads/images/download.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionSave.setIcon(icon2)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setShortcutVisibleInContextMenu(True)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.setIcon(icon2)
        self.actionSave_As.setIconVisibleInMenu(True)
        self.actionSave_As.setShortcutVisibleInContextMenu(True)
        self.actionShapes = QAction(MainWindow)
        self.actionShapes.setObjectName("actionShapes")
        icon5 = QIcon()
        icon5.addFile(
            "../../Downloads/images/shapes.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionShapes.setIcon(icon5)
        self.actionShapes.setIconVisibleInMenu(True)
        self.actionShapes.setShortcutVisibleInContextMenu(True)
        self.actionSize = QAction(MainWindow)
        self.actionSize.setObjectName("actionSize")
        icon6 = QIcon()
        icon6.addFile(
            "../../Downloads/images/measuring-tape.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.actionSize.setIcon(icon6)
        self.actionSize.setIconVisibleInMenu(True)
        self.actionSize.setShortcutVisibleInContextMenu(True)
        self.actionBrush = QAction(MainWindow)
        self.actionBrush.setObjectName("actionBrush")
        icon7 = QIcon()
        icon7.addFile(
            "../../Downloads/images/wheel.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionBrush.setIcon(icon7)
        self.actionBrush.setIconVisibleInMenu(True)
        self.actionBrush.setShortcutVisibleInContextMenu(True)
        self.actionBrush_2 = QAction(MainWindow)
        self.actionBrush_2.setObjectName("actionBrush_2")
        icon8 = QIcon()
        icon8.addFile(
            "../../Downloads/images/paint-brush.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionBrush_2.setIcon(icon8)
        self.actionBrush_2.setIconVisibleInMenu(True)
        self.actionBrush_2.setShortcutVisibleInContextMenu(True)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        icon9 = QIcon()
        icon9.addFile(
            "../../Downloads/images/close.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionClose.setIcon(icon9)
        self.actionClose.setIconVisibleInMenu(True)
        self.actionClose.setShortcutVisibleInContextMenu(True)

        self.actionEraser = QAction(MainWindow)
        self.actionEraser.setObjectName("actionEraser")
        icon10 = QIcon()
        icon10.addFile(
            "../../Downloads/images/eraser.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionEraser.setIcon(icon10)
        self.actionEraser.setIconVisibleInMenu(True)
        self.actionEraser.setShortcutVisibleInContextMenu(True)

        self.actionConvert = QAction(MainWindow)
        self.actionConvert.setObjectName("actionConvert")
        icon11 = QIcon()
        icon11.addFile(
            "../../Downloads/images/magician.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionConvert.setIcon(icon11)
        self.actionConvert.setIconVisibleInMenu(True)
        self.actionConvert.setShortcutVisibleInContextMenu(True)

        self.actionBrowse = QAction(MainWindow)
        self.actionBrowse.setObjectName("actionBrowse")
        icon12 = QIcon()
        icon12.addFile(
            "../../Downloads/images/video.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionBrowse.setIcon(icon12)
        self.actionBrowse.setIconVisibleInMenu(True)
        self.actionBrowse.setShortcutVisibleInContextMenu(True)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, 0, 900, 600))
        self.label.setStyleSheet("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 24))
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuEdit_2 = QMenu(self.menubar)
        self.menuEdit_2.setObjectName("menuEdit_2")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuTools_2 = QMenu(self.menubar)
        self.menuTools_2.setObjectName("menuTools_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuTools_2.menuAction())
        self.menuEdit.addAction(self.actionOpen)
        self.menuEdit.addAction(self.actionOpen_2)
        self.menuEdit.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionSave_As)
        self.menuEdit.addAction(self.actionClose)
        self.menuTools.addAction(self.actionShapes)
        self.menuTools.addAction(self.actionSize)
        self.menuTools.addAction(self.actionBrush)
        self.menuTools.addAction(self.actionBrush_2)
        self.menuTools.addAction(self.actionEraser)
        self.menuTools_2.addAction(self.actionConvert)
        self.menuTools_2.addAction(self.actionBrowse)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Canva", None)
        )
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", "New", None))
        # if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(
            QCoreApplication.translate("MainWindow", "Meta+N", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionOpen_2.setText(
            QCoreApplication.translate("MainWindow", "Open", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionOpen_2.setShortcut(
            QCoreApplication.translate("MainWindow", "Meta+O", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", "Save", None))
        # if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(
            QCoreApplication.translate("MainWindow", "Meta+S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(
            QCoreApplication.translate("MainWindow", "Save As", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut(
            QCoreApplication.translate("MainWindow", "Meta+A", None)
        )
        # endif // QT_CONFIG(shortcut)
        # endif // QT_CONFIG(shortcut)
        self.actionShapes.setText(
            QCoreApplication.translate("MainWindow", "Shapes", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionShapes.setShortcut(
            QCoreApplication.translate("MainWindow", "S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSize.setText(QCoreApplication.translate("MainWindow", "Size", None))
        # if QT_CONFIG(shortcut)
        self.actionSize.setShortcut(QCoreApplication.translate("MainWindow", "D", None))
        # endif // QT_CONFIG(shortcut)
        self.actionBrush.setText(
            QCoreApplication.translate("MainWindow", "Colour", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionBrush.setShortcut(
            QCoreApplication.translate("MainWindow", "C", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionBrush_2.setText(
            QCoreApplication.translate("MainWindow", "Brush", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionBrush_2.setShortcut(
            QCoreApplication.translate("MainWindow", "B", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionClose.setText(
            QCoreApplication.translate("MainWindow", "Close", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(
            QCoreApplication.translate("MainWindow", "Meta+Q", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionEraser.setText(
            QCoreApplication.translate("MainWindow", "Eraser", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionEraser.setShortcut(
            QCoreApplication.translate("MainWindow", "E", None)
        )

        self.actionConvert.setText(
            QCoreApplication.translate("MainWindow", "Enhance Hand Drawing", None)
        )
        self.actionConvert.setShortcut(
            QCoreApplication.translate("MainWindow", "Meta+E", None)
        )

        self.actionBrowse.setText(
            QCoreApplication.translate("MainWindow", "Browse Pre-Drawn Images", None)
        )
        self.actionBrowse.setShortcut(
            QCoreApplication.translate("MainWindow", "Meta+B", None)
        )

        # endif // QT_CONFIG(shortcut)
        self.label.setText("")
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", "Tools", None))
        self.menuTools_2.setTitle(
            QCoreApplication.translate("MainWindow", "Image Alchemy", None)
        )

    # retranslateUi


import sys
import cv2
import numpy as np
import mediapipe as mp
import subprocess
import os
from PySide6.QtCore import QTimer, Qt, QPointF, QLineF
from PySide6.QtGui import (
    QKeyEvent,
    QPen,
    QColor,
    QImage,
    QPixmap,
    QShortcut,
    QKeySequence,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QGraphicsScene,
    QGraphicsPixmapItem,
    QGraphicsLineItem,
)
from dialog import Dialogg
from PySide6.QtWidgets import QDialog
import matplotlib.pyplot as plt
from selectimg import ImageSelectionDialog
from slider import SliderDialog
from PySide6.QtWidgets import QApplication, QMainWindow, QColorDialog
from color import MainWindow as ColorPickerWindow
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow
from brush import brush
from shape import shape
import platform
from image import draw
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMainWindow, QApplication
from sketch import Dialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.is_drawing = True
        self.drawing_enabled = True
        self.ui.actionClose.triggered.connect(self.closeAllWindows)
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.mpDraw = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(0)

        self.init_canvas_size()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(20)
        # Drawing setup
        self.is_drawing = False
        self.last_point = None
        self.draw_color = (255, 0, 0)
        self.close_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.close_shortcut.activated.connect(self.closeAllWindows)

        self.ui.actionSave_As.triggered.connect(self.openSaveAsDialog)

        self.ui.actionSave_As.triggered.connect(self.openSaveAsDialog)

        self.shortcutSaveAs = QShortcut(QKeySequence("Ctrl+A"), self)
        self.shortcutSaveAs.activated.connect(self.openSaveAsDialog)
        self.ui.actionSave.triggered.connect(self.save_drawing)
        self.ui.actionOpen_2.triggered.connect(self.openImage)
        self.ui.actionOpen.triggered.connect(self.clearDrawings)

        self.ui.actionOpen.triggered.connect(self.clearDrawings)

        self.newShortcut = QShortcut(QKeySequence("Ctrl+N"), self)
        self.newShortcut.activated.connect(self.clearDrawings)

        self.ui.actionOpen_2.triggered.connect(self.openImage)
        self.ui.actionOpen_2.setShortcut("Ctrl+O")

        self.saveShortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.saveShortcut.activated.connect(self.save_drawing)

        self.ui.actionSize.triggered.connect(self.openSizeDialog)
        self.line_thickness = 5
        self.ui.actionBrush.triggered.connect(self.openColorPicker)
        self.eraser_enabled = False
        self.ui.actionEraser.triggered.connect(self.toggle_eraser)
        self.original_draw_color = self.draw_color
        self.ui.actionBrush_2.triggered.connect(self.show_brush_dialog)
        self.current_brush_type = "Pencil"
        self.eraser_enabled = False
        self.ui.actionShapes.triggered.connect(self.show_shapes_dialog)

        self.ui.actionBrowse.triggered.connect(self.open_image_window)
        self.images = {}

        self.ui.actionConvert.triggered.connect(self.open_sketch_window)

        self.sketch_dialog = Dialog()
        self.sketch_dialog.imageLoaded.connect(self.display_result_image)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:

            self.drawing_enabled = not self.drawing_enabled
        elif event.key() == Qt.Key_D:

            self.openSizeDialog()
        elif event.key() == Qt.Key_E:

            self.toggle_eraser()
        elif event.key() == Qt.Key_B:
            self.show_brush_dialog()
        else:

            super().keyPressEvent(event)

    def init_canvas_size(self):

        window_width = self.size().width()
        window_height = self.size().height()

        self.canvas = np.zeros((window_height, window_width, 3), dtype=np.uint8) + 255

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if self.canvas.shape[:2] != frame.shape[:2]:
            self.canvas = cv2.resize(self.canvas, (frame.shape[1], frame.shape[0]))

        result = self.hands.process(framergb)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                fingertip = hand_landmarks.landmark[
                    self.mpHands.HandLandmark.INDEX_FINGER_TIP
                ]
                ix, iy = int(fingertip.x * frame.shape[1]), int(
                    fingertip.y * frame.shape[0]
                )
                for lm in hand_landmarks.landmark:
                    x, y = int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

                self.mpDraw.draw_landmarks(
                    frame, hand_landmarks, self.mpHands.HAND_CONNECTIONS
                )
                if self.drawing_enabled and self.last_point is not None:
                    if self.eraser_enabled:

                        self.draw_pencil(
                            self.canvas,
                            self.last_point,
                            (ix, iy),
                            (255, 255, 255),
                            self.line_thickness,
                        )
                    else:

                        if self.current_brush_type == "Pencil":
                            self.draw_pencil(
                                self.canvas,
                                self.last_point,
                                (ix, iy),
                                self.draw_color,
                                self.line_thickness,
                            )
                        elif self.current_brush_type == "Spray":
                            self.draw_spray(
                                self.canvas,
                                (ix, iy),
                                self.draw_color,
                                radius=15,
                                density=100,
                            )
                        elif self.current_brush_type == "Calligraphy":
                            self.draw_calligraphy(
                                self.canvas,
                                self.last_point,
                                (ix, iy),
                                self.draw_color,
                                thickness=self.line_thickness,
                            )
                        elif self.current_brush_type == "Watercolor":
                            self.draw_watercolor(
                                self.canvas,
                                self.last_point,
                                (ix, iy),
                                self.draw_color,
                                thickness=self.line_thickness,
                            )
                    self.last_point = (ix, iy)
                else:
                    self.is_drawing = True
                    self.last_point = (ix, iy)
        else:
            self.is_drawing = False
            self.last_point = None

        blended_frame = cv2.addWeighted(frame, 0.9, self.canvas, 0.1, 0)

        self.display_frame(blended_frame)

        cv2.imshow("Paint", self.canvas)

    def display_frame(self, frame):
        """Converts and displays the blended frame in the PyQt window using the QLabel."""

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        q_img = QImage(
            frame_rgb.data,
            frame_rgb.shape[1],
            frame_rgb.shape[0],
            frame_rgb.strides[0],
            QImage.Format_RGB888,
        )

        pixmap = QPixmap.fromImage(q_img)
        self.ui.label.setPixmap(
            pixmap.scaled(
                self.ui.label.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation
            )
        )

    def closeEvent(self, event):
        self.cap.release()
        cv2.destroyAllWindows()
        super().closeEvent(event)

    def closeAllWindows(self):

        self.cap.release()
        cv2.destroyAllWindows()

        self.close()

    def openSaveAsDialog(self):
        dialog = Dialogg(self)
        dialog.show()
        if dialog.exec() == QDialog.Accepted:
            selected_format = dialog.get_selected_format().lower()
            base_filepath = os.path.join(os.getcwd(), "my_drawing")
            extension = selected_format
            if selected_format == "jpeg":
                extension = "jpg"

            filepath = f"{base_filepath}.{extension}"
            counter = 1

            while os.path.exists(filepath):
                filepath = f"{base_filepath}{counter}.{extension}"
                counter += 1

            if selected_format == "png" or selected_format == "jpeg":
                cv2.imwrite(filepath, self.canvas)
            elif selected_format == "pdf":
                canvas_rgb = cv2.cvtColor(self.canvas, cv2.COLOR_BGR2RGB)
                plt.figure(
                    figsize=(self.canvas.shape[1] / 100, self.canvas.shape[0] / 100),
                    dpi=100,
                )
                plt.imshow(canvas_rgb, interpolation="nearest")
                plt.axis("off")
                plt.savefig(filepath, bbox_inches="tight", pad_inches=0)
                plt.close()

            print(f"Drawing saved as {filepath}")

    def save_drawing(self):
        base_filepath = os.path.join(os.getcwd(), "my_drawing")
        counter = 1
        filepath = f"{base_filepath}.png"

        while os.path.exists(filepath):
            filepath = f"{base_filepath}{counter}.png"
            counter += 1

        cv2.imwrite(filepath, self.canvas)
        print(f"Drawing saved to {filepath}")

    def openImage(self):
        dialog = ImageSelectionDialog(self)
        if dialog.exec():
            image_path = dialog.selectedImagePath
            if image_path:

                self.canvas = cv2.imread(image_path)

                cv2.imshow("Paint", self.canvas)

    def clearDrawings(self):

        self.init_canvas_size()
        self.ui.label.clear()
        blank_image = np.zeros_like(self.canvas) + 255
        cv2.imshow("Paint", blank_image)

    def openSizeDialog(self):
        dialog = SliderDialog(self)
        if dialog.exec():

            sliderValue = dialog.slider.value()

            self.line_thickness = sliderValue
            print(f"Line thickness set to: {self.line_thickness}")

    def openColorPicker(self):
        self.colorPickerWindow = ColorPickerWindow()
        self.colorPickerWindow.showColorPicker(self.onColorSelected)

    def onColorSelected(self, color):

        self.draw_color = (color.blue(), color.green(), color.red())
        print(f"Updated drawing color to BGR format: {self.draw_color}")

    def toggle_eraser(self):
        self.eraser_enabled = not self.eraser_enabled
        if self.eraser_enabled:
            self.original_draw_color = self.draw_color
            self.draw_color = (255, 255, 255)
        else:
            self.draw_color = self.original_draw_color
        print(
            "Eraser mode is now " + ("enabled" if self.eraser_enabled else "disabled")
        )

    def show_brush_dialog(self):
        self.brushDialog = brush(self)
        if self.brushDialog.exec():
            selected_brush = self.brushDialog.ui.comboBox.currentText()
            self.current_brush_type = selected_brush
            print(f"Selected brush: {selected_brush}")

    def draw_pencil(self, image, start, end, color, thickness):
        cv2.line(image, start, end, color, thickness)

    def draw_spray(self, image, point, color, radius=10, density=30):
        for _ in range(density):
            angle = np.random.uniform(0, 2 * np.pi)
            radius = np.random.uniform(0, radius)
            x = int(point[0] + radius * np.cos(angle))
            y = int(point[1] + radius * np.sin(angle))
            cv2.circle(image, (x, y), 0, color, -1)

    def draw_calligraphy(self, image, start, end, color, thickness=5):
        angle = np.arctan2(end[1] - start[1], end[0] - start[0]) + np.pi / 2
        offset = np.array([np.sin(angle), np.cos(angle)]) * thickness
        points = np.array(
            [start + offset, start - offset, end - offset, end + offset]
        ).astype(np.int32)
        cv2.fillConvexPoly(image, points, color)

    def draw_watercolor(self, image, start, end, color, thickness=20):

        overlay = image.copy()
        cv2.line(overlay, start, end, color, thickness * 2, lineType=cv2.LINE_AA)

        cv2.addWeighted(overlay, 0.5, image, 0.5, 0, image)

        cv2.line(image, start, end, color, thickness, lineType=cv2.LINE_AA)

        cv2.GaussianBlur(image, (9, 9), 0, dst=image)

        cv2.line(image, start, end, color, thickness, lineType=cv2.LINE_AA)

    def show_shapes_dialog(self):
        self.shapesDialog = shape(self)
        if self.shapesDialog.exec():
            selected_shape = self.shapesDialog.ui.comboBox.currentText()
            self.current_shape_type = selected_shape
            print(f"Selected shape: {selected_shape}")

            if selected_shape in [
                "Rectangle",
                "Circle",
                "Triangle",
                "Hexagon",
                "Star",
                "Ellipse",
                "Square",
            ]:

                finger_position = self.last_point
                if finger_position is not None:
                    shape_size = 50
                    shape_color = self.draw_color

                    self.draw_shape(
                        self.canvas,
                        selected_shape,
                        finger_position,
                        shape_size,
                        shape_color,
                    )

                    self.draw_shape(
                        self.canvas,
                        selected_shape,
                        finger_position,
                        shape_size,
                        shape_color,
                    )

    def draw_shape(self, image, shape_type, center, size, color):
        if shape_type == "Square":
            side_length = size
            cv2.rectangle(
                image,
                (center[0] - side_length // 2, center[1] - side_length // 2),
                (center[0] + side_length // 2, center[1] + side_length // 2),
                color,
                -1,
            )
        elif shape_type == "Rectangle":
            width, height = 100, 50
            cv2.rectangle(
                image,
                (center[0] - width // 2, center[1] - height // 2),
                (center[0] + width // 2, center[1] + height // 2),
                color,
                -1,
            )
        elif shape_type == "Circle":
            cv2.circle(image, center, size, color, -1)
        elif shape_type == "Triangle":
            points = np.array(
                [
                    center,
                    (center[0] + size, center[1] + size),
                    (center[0] - size, center[1] + size),
                ]
            )
            cv2.drawContours(image, [points], 0, color, -1)
        elif shape_type == "Hexagon":
            hexagon_points = self.get_hexagon_points(center, size)
            cv2.drawContours(image, [hexagon_points], 0, color, -1)
        elif shape_type == "Star":
            star_points = self.get_star_points(center, size)
            cv2.drawContours(image, [star_points], 0, color, -1)
        elif shape_type == "Ellipse":

            width = 150
            height = 100
            cv2.ellipse(image, center, (width // 2, height // 2), 0, 0, 360, color, -1)

    def get_hexagon_points(self, center, size):
        points = []
        for i in range(6):
            x = center[0] + size * np.cos(np.pi / 3 * i)
            y = center[1] + size * np.sin(np.pi / 3 * i)
            points.append([int(x), int(y)])
        return np.array(points)

    def get_star_points(self, center, size):
        points = []
        for i in range(5):
            x1 = center[0] + size * np.cos(2 * np.pi * i / 5 - np.pi / 2)
            y1 = center[1] + size * np.sin(2 * np.pi * i / 5 - np.pi / 2)
            points.append((int(x1), int(y1)))
            x2 = center[0] + (size / 2) * np.cos(2 * np.pi * (i + 0.5) / 5 - np.pi / 2)
            y2 = center[1] + (size / 2) * np.sin(2 * np.pi * (i + 0.5) / 5 - np.pi / 2)
            points.append((int(x2), int(y2)))
        return np.array(points)

    def open_image_window(self):

        image_window = draw(self)

        image_window.imageSelected.connect(self.update_canvas_with_image)
        image_window.exec()

    def update_canvas_with_image(self, image_path):
        if image_path:

            image = cv2.imread(image_path)

            if image is not None:

                image = cv2.resize(image, (self.canvas.shape[1], self.canvas.shape[0]))

                self.canvas = image

                self.display_frame(image)

                cv2.imshow("Paint", image)

                print("Image loaded successfully")
            else:
                print("Failed to load image")
        else:
            print("No image path provided")

    def open_sketch_window(self):

        self.sketch_dialog.exec()

    def display_result_image(self, image):

        if image.format() == QImage.Format_Grayscale8:

            image_np = np.copy(image.constBits()).reshape(image.height(), image.width())

            sketch_bgr = cv2.cvtColor(image_np, cv2.COLOR_GRAY2BGR)

            self.canvas = sketch_bgr

            self.display_frame(sketch_bgr)

            cv2.imshow("Paint", sketch_bgr)

        else:
            print("Received image is not a sketch.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.init_canvas_size()
    sys.exit(app.exec())
