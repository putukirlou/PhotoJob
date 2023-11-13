import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QWidget
from PyQt5.QtGui import QPixmap

from support import PhotoShop
from widgets import Design


class ImageProcessor(QWidget):
    def __init__(self):
        super().__init__()

        # Подключение к базе данных
        connection = sqlite3.connect("your_database.db")
        cursor = connection.cursor()

        # Интерфейс
        self.setWindowTitle("PhotoJob")
        self.setGeometry(200, 50, 1200, 800)
        self.setFixedSize(1200, 800)
        self.design = Design()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.design)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.ps = PhotoShop(self.design.label)

        # Подключение слотов к сигналам
        self.design.button_open.clicked.connect(self.open_image)
        self.design.button_save.clicked.connect(self.save_image)

        self.design.button_red.clicked.connect(self.noneError)
        self.design.button_red.clicked.connect(lambda: self.ps.red())
        self.design.button_blackwhite.clicked.connect(self.noneError)
        self.design.button_blackwhite.clicked.connect(lambda:
                                                      self.ps.apply_black_and_white_filter())
        self.design.button_blue.clicked.connect(self.noneError)
        self.design.button_blue.clicked.connect(lambda: self.ps.blue())
        self.design.button_green.clicked.connect(self.noneError)
        self.design.button_green.clicked.connect(lambda: self.ps.green())
        self.design.button_light.clicked.connect(self.noneError)
        self.design.button_light.clicked.connect(lambda: self.ps.light())
        self.design.button_dark.clicked.connect(self.noneError)
        self.design.button_dark.clicked.connect(lambda: self.ps.dark())
        self.design.button_mirrorv.clicked.connect(self.noneError)
        self.design.button_mirrorv.clicked.connect(lambda: self.ps.mirror_v())
        self.design.button_mirrorg.clicked.connect(self.noneError)
        self.design.button_mirrorg.clicked.connect(lambda: self.ps.mirror_g())
        self.design.button_negativ.clicked.connect(self.noneError)
        self.design.button_negativ.clicked.connect(lambda: self.ps.negativ())
        self.design.button_contrast.clicked.connect(self.noneError)
        self.design.button_contrast.clicked.connect(lambda: self.ps.contrast())
        self.design.button_sepia.clicked.connect(self.noneError)
        self.design.button_sepia.clicked.connect(lambda: self.ps.sepia())

        self.design.button_inst.clicked.connect(self.show_text)

    # Функции
    def show_text(self):
        with open('instruction.txt', 'r', encoding='utf-8') as file:
            text_content = file.read()

        msg_box = QMessageBox(self)
        msg_box.setStyleSheet("QLabel { color: rgb(30, 30, 40);}")
        msg_box.setWindowTitle("Инструкция")
        msg_box.setText(text_content)
        msg_box.exec_()

    def save_image(self):
        if self.design.label.pixmap():  # Проверяем, есть ли изображение для сохранения
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить изображение", "",
                                                       "Изображения (*.jpg *.png *.jpeg)", options=options)
            if file_name:
                self.design.label.pixmap().save(file_name)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setStyleSheet("QLabel { color: rgb(30, 30, 40);}")
            msg.setText("Не выбрано изображение для сохранения")
            msg.setWindowTitle("Внимание ЭЭЭУ")
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

            x = (self.width() - pixmap.width() - 250) // 2
            y = (self.height() - pixmap.height()) // 2

            self.design.label.setPixmap(pixmap)
            self.design.label.setGeometry(
                x, y, pixmap.width(), pixmap.height())

    def noneError(self):
        if self.design.label.pixmap():  # Проверяем, есть ли изображение для сохранения
            pass
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setStyleSheet("QLabel { color: rgb(30, 30, 40);}")
            msg.setText("Не выбрано изображение для обработки")
            msg.setWindowTitle("Внимание ЭЭЭУ")
            msg.exec_()


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
