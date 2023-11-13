from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QMessageBox, QGridLayout, QFrame, QTabWidget
from PyQt5.QtGui import QPixmap, QImage, QColor, QIcon, QPainter, QTransform
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImageWriter, QKeyEvent
from PyQt5.QtCore import QTimer

import sys
from PIL import Image, ImageFilter, ImageEnhance


class ImageProcessor(QWidget):
    def __init__(self):
        super().__init__()

        # Интерфейс
        self.setWindowTitle("PhotoJob")
        self.setGeometry(200, 50, 1200, 800)
        self.setFixedSize(1200, 800)
        self.new_text = QtWidgets.QLabel(self)
        self.setStyleSheet("background-color: rgb(20, 20, 30);")

        self.label = QLabel(self)

        self.button_inst = QPushButton('i', self)
        self.button_inst.setFixedWidth(35)
        self.button_inst.setFixedHeight(35)
        self.button_inst.setStyleSheet(
            "font: bold 20px;"
            "border-radius: 10px;"
            "background-color: rgb(10, 10, 20);"
            "border-radius: 10px;"
            "color: rgb(130, 130, 140);")
        self.button_inst.move(100, 800)

        # Создаем кнопки
        self.button_open = QPushButton('Открыть', self)
        self.button_open.setFixedWidth(150)
        self.button_open.setStyleSheet(
            "color: rgb(130, 130, 140);"
            "background-color: rgb(10, 10, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;")
        self.button_open.move(100, 800)

        self.button_save = QPushButton('Сохранить', self)
        self.button_save.setFixedWidth(150)
        self.button_save.setStyleSheet(
            "color: rgb(130, 130, 140);"
            "background-color: rgb(10, 10, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;")
        self.button_save.move(100, 800)

        # Кнопки для фильтров:
        self.button_blackwhite = QPushButton('ЧерноБелое', self)
        self.button_blackwhite.setFixedWidth(150)
        self.button_blackwhite.move(100, 800)
        self.button_blackwhite.setStyleSheet(
            "color: rgb(170, 170, 180);"
            "background-color: rgb(15, 15, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;")

        self.button_filt = QPushButton('ФИЛЬТРЫ:', self)
        self.button_filt.setFixedWidth(100)
        self.button_filt.setFixedHeight(20)
        self.button_filt.move(150, 800)
        self.button_filt.setStyleSheet(
            "font: bold 18px;"
            "border-radius: 10px;"
            "color: rgb(170, 170, 180);")

        self.button_red = QPushButton('+ Краснота', self)
        self.button_red.setFixedWidth(150)
        self.button_red.move(150, 800)
        self.button_red.setStyleSheet(
            "color: rgb(170, 170, 180);"
            "background-color: rgb(15, 15, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;")

        self.button_blue = QPushButton('+ Синева', self)
        self.button_blue.setFixedWidth(150)
        self.button_blue.move(150, 800)
        self.button_blue.setStyleSheet(
            "color: rgb(170, 170, 180);"
            "background-color: rgb(15, 15, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;")

        self.button_green = QPushButton('+ Зеленота', self)
        self.button_green.setFixedWidth(150)
        self.button_green.move(150, 800)
        self.button_green.setStyleSheet(
            "color: rgb(170, 170, 180);"
            "background-color: rgb(15, 15, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;")

        self.button_light = QPushButton('Светлее', self)
        self.button_light.setFixedWidth(150)
        self.button_light.move(150, 800)
        self.button_light.setStyleSheet(
            "color: rgb(170, 170, 180);"
            "background-color: rgb(15, 15, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;")

        self.button_dark = QPushButton('Темнее', self)
        self.button_dark.setFixedWidth(150)
        self.button_dark.move(150, 800)
        self.button_dark.setStyleSheet(
            "color: rgb(170, 170, 180);"
            "background-color: rgb(15, 15, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;")

        self.button_mirrorv = QPushButton('Зекркало  |', self)
        self.button_mirrorv.setFixedWidth(150)
        self.button_mirrorv.move(150, 800)
        self.button_mirrorv.setStyleSheet(
            "color: rgb(170, 170, 180);"
            "background-color: rgb(15, 15, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;")

        self.button_mirrorg = QPushButton('Зеркало  --', self)
        self.button_mirrorg.setFixedWidth(150)
        self.button_mirrorg.move(150, 800)
        self.button_mirrorg.setStyleSheet(
            "color: rgb(170, 170, 180);"
            "background-color: rgb(15, 15, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;")

        self.button_negativ = QPushButton('Негатив', self)
        self.button_negativ.setFixedWidth(150)
        self.button_negativ.move(150, 800)
        self.button_negativ.setStyleSheet(
            "color: rgb(170, 170, 180);"
            "background-color: rgb(15, 15, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;")

        # Смещение
        self.label.move(10, 10)
        self.button_open.move(950, 710)
        self.button_save.move(950, 750)

        self.button_blackwhite.move(950, 145)
        self.button_red.move(950, 190)
        self.button_blue.move(950, 235)
        self.button_green.move(950, 280)
        self.button_light.move(950, 325)
        self.button_dark.move(950, 370)
        self.button_negativ.move(950, 415)
        self.button_mirrorv.move(950, 460)
        self.button_mirrorg.move(950, 505)

        self.button_inst.move(950, 15)
        self.button_filt.move(950, 90)

        # Подключение слотов к сигналам
        self.button_open.clicked.connect(self.open_image)
        self.button_save.clicked.connect(self.save_image)

        self.button_red.clicked.connect(self.noneError)
        self.button_red.clicked.connect(self.red)
        self.button_blackwhite.clicked.connect(self.noneError)
        self.button_blackwhite.clicked.connect(
            self.apply_black_and_white_filter)
        self.button_blue.clicked.connect(self.noneError)
        self.button_blue.clicked.connect(self.blue)
        self.button_green.clicked.connect(self.noneError)
        self.button_green.clicked.connect(self.green)
        self.button_light.clicked.connect(self.noneError)
        self.button_light.clicked.connect(self.light)
        self.button_dark.clicked.connect(self.noneError)
        self.button_dark.clicked.connect(self.dark)
        self.button_mirrorv.clicked.connect(self.noneError)
        self.button_mirrorv.clicked.connect(self.mirror_v)
        self.button_mirrorg.clicked.connect(self.noneError)
        self.button_mirrorg.clicked.connect(self.mirror_g)
        self.button_negativ.clicked.connect(self.noneError)
        self.button_negativ.clicked.connect(self.negativ)

    def show_buttons(self):
        # Остановить таймер и показать контейнер с кнопками
        self.timer.stop()
        self.button_container.show()

    def keyPressEvent(self, event: QKeyEvent):
        # Обработка события нажатия клавиши
        if event.key() == QtCore.Qt.Key_Z and event.modifiers() == QtCore.Qt.ControlModifier:
            self.undo_filter()

    def undo_filter(self):
        if self.image_original is not None:
            self.label.setPixmap(QPixmap.fromImage(self.image_original))
            self.image_filtered = None

    def save_image(self):
        if self.label.pixmap():  # Проверяем, есть ли изображение для сохранения
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить изображение", "",
                                                       "Изображения (*.jpg *.png *.jpeg)", options=options)
            if file_name:
                self.label.pixmap().save(file_name)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Не выбрано изображение для сохранения")
            msg.setWindowTitle("Внимание")
            msg.exec_()

    def noneError(self):
        if self.label.pixmap():  # Проверяем, есть ли изображение для сохранения
            pass
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Не выбрано изображение для обработки")
            msg.setWindowTitle("Внимание ЭЭУУ")
            msg.exec_()

    def open_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "",
                                                   "Изображения (*.jpg *.png *.jpeg)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            pixmap = pixmap.scaledToWidth(900)
            if pixmap.height() > 700:
                pixmap = pixmap.scaledToHeight(700)

            self.label.setPixmap(pixmap)
            self.label.resize(pixmap.width(), pixmap.height())

            grid_layout = QGridLayout()
            grid_layout.addWidget(self.label, 0, 0, 1, 1)
            self.setLayout(grid_layout)
            # pixmap = pixmap.scaledToHeight(600)

    def red(self):
        if not self.label.pixmap():
            return

        image = self.label.pixmap().toImage()
        for x in range(image.width()):
            for y in range(image.height()):
                color = QColor(image.pixelColor(x, y))
                new_red = min(color.red() + 50, 255)
                new_color = QColor(new_red, color.green(), color.blue())
                image.setPixelColor(x, y, new_color)

        self.label.setPixmap(QPixmap.fromImage(image))

    def blue(self):
        if not self.label.pixmap():
            return

        image = self.label.pixmap().toImage()
        for x in range(image.width()):
            for y in range(image.height()):
                color = QColor(image.pixelColor(x, y))
                new_blue = min(color.blue() + 50, 255)
                new_color = QColor(color.red(), color.green(), new_blue)
                image.setPixelColor(x, y, new_color)

        self.label.setPixmap(QPixmap.fromImage(image))

    def green(self):
        if not self.label.pixmap():
            return

        image = self.label.pixmap().toImage()
        for x in range(image.width()):
            for y in range(image.height()):
                color = QColor(image.pixelColor(x, y))
                new_green = min(color.green() + 50, 255)
                new_color = QColor(color.red(), new_green, color.blue())
                image.setPixelColor(x, y, new_color)

        self.label.setPixmap(QPixmap.fromImage(image))

    def light(self):
        if not self.label.pixmap():
            return

        image = self.label.pixmap().toImage()
        for x in range(image.width()):
            for y in range(image.height()):
                color = QColor(image.pixelColor(x, y))
                new_red = max(color.red() + 50, 0)
                new_green = max(color.green() + 50, 0)
                new_blue = max(color.blue() + 50, 0)
                new_color = QColor(new_red, new_green, new_blue)
                image.setPixelColor(x, y, new_color)

        self.label.setPixmap(QPixmap.fromImage(image))

    def dark(self):
        if not self.label.pixmap():
            return

        image = self.label.pixmap().toImage()
        for x in range(image.width()):
            for y in range(image.height()):
                color = QColor(image.pixelColor(x, y))
                new_red = max(color.red() - 50, 0)
                new_green = max(color.green() - 50, 0)
                new_blue = max(color.blue() - 50, 0)
                new_color = QColor(new_red, new_green, new_blue)
                image.setPixelColor(x, y, new_color)

        self.label.setPixmap(QPixmap.fromImage(image))

    def apply_black_and_white_filter(self):
        if not self.label.pixmap():
            return

        image = self.label.pixmap().toImage()
        for x in range(image.width()):
            for y in range(image.height()):
                color = QColor(image.pixelColor(x, y))
                average = (color.red() + color.green() + color.blue()) // 3
                image.setPixelColor(x, y, QColor(average, average, average))

        self.label.setPixmap(QPixmap.fromImage(image))

    def mirror_g(self):
        if not self.label.pixmap():
            return

        pixmap = self.label.pixmap()
        transform = QTransform().scale(-1, 1)  # Отражение по горизонтали
        mirrored_pixmap = pixmap.transformed(transform)

        self.label.setPixmap(mirrored_pixmap)

    def mirror_v(self):
        if not self.label.pixmap():
            return

        pixmap = self.label.pixmap()
        transform = QTransform().scale(1, -1)  # Отражение по вертикали
        mirrored_pixmap = pixmap.transformed(transform)

        self.label.setPixmap(mirrored_pixmap)

    def negativ(self):
        if not self.label.pixmap():
            return

        image = self.label.pixmap().toImage()
        for x in range(image.width()):
            for y in range(image.height()):
                color = QColor(image.pixelColor(x, y))
                new_color = QColor(255 - color.red(), 255 -
                                   color.green(), 255 - color.blue())
                image.setPixelColor(x, y, new_color)

        self.label.setPixmap(QPixmap.fromImage(image))


if __name__ == '__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(
            QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(
            QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    mainWindow = ImageProcessor()
    mainWindow.show()
    sys.exit(app.exec_())
