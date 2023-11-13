from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFrame


class Design(QWidget):
    def __init__(self):
        super().__init__()

        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color: rgb(20, 20, 30)")
        frame.setGeometry(0, 0, 1500, 1000)

        # Создание кнопок
        self.label = QLabel(self)

        self.new_text = QtWidgets.QLabel(self)
        self.button_inst = QPushButton('HELP', self)
        self.button_inst.setFixedWidth(70)
        self.button_inst.setFixedHeight(30)
        self.button_inst.setStyleSheet(
            "QPushButton"
            "{"
            "font: bold 12px;"
            "border-radius: 10px;"
            "background-color: rgb(10, 10, 20);"
            "border-radius: 10px;"
            "color: rgb(130, 130, 140);"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")
        self.button_inst.move(100, 800)

        # self.button_history = QPushButton('HISTORY', self)
        # self.button_history.setFixedWidth(90)
        # self.button_history.setFixedHeight(30)
        # self.button_history.setStyleSheet(
        #     "font: bold 12px;"
        #     "border-radius: 10px;"
        #     "background-color: rgb(10, 10, 20);"
        #     "border-radius: 10px;"
        #     "color: rgb(130, 130, 140);"
        #     "}"
        #     "QPushButton::pressed"
        #     "{"
        #     "background-color: rgb(30, 30, 50);"
        #     "}"
        #     "QPushButton::hover"
        #     "{"
        #     "background-color: rgb(30, 30, 50);"
        #     "}")
        # self.button_inst.move(100, 800)

        self.button_open = QPushButton('Открыть', self)
        self.button_open.setFixedWidth(150)
        self.button_open.setStyleSheet(
            "color: rgb(130, 130, 140);"
            "background-color: rgb(10, 10, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")
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
            "padding: 6px;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")
        self.button_save.move(100, 800)

        # Кнопки для фильтров:
        self.button_filt = QPushButton('ФИЛЬТРЫ:', self)
        self.button_filt.setFixedWidth(100)
        self.button_filt.setFixedHeight(20)
        self.button_filt.move(150, 800)
        self.button_filt.setStyleSheet(
            "font: bold 18px;"
            "border-radius: 10px;"
            "color: rgb(170, 170, 180);")

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
            "padding: 6px;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")

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
            "padding: 6px;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")

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
            "padding: 6px;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")

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
            "padding: 6px;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")

        self.button_light = QPushButton('Светлее', self)
        self.button_light.setFixedWidth(150)
        self.button_light.move(150, 800)
        self.button_light.setStyleSheet(
            "QPushButton"
            "{"
            "color: rgb(170, 170, 180);"
            "background-color: rgb(15, 15, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")

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
            "padding: 6px;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")

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
            "padding: 6px;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")

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
            "padding: 6px;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")

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
            "padding: 6px;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")

        self.button_contrast = QPushButton("Контраст", self)
        self.button_contrast.setFixedWidth(150)
        self.button_contrast.move(150, 800)
        self.button_contrast.setStyleSheet(
            "color: rgb(170, 170, 180);"
            "background-color: rgb(15, 15, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")

        self.button_sepia = QPushButton("Сепиа", self)
        self.button_sepia.setFixedWidth(150)
        self.button_sepia.move(150, 800)
        self.button_sepia.setStyleSheet(
            "color: rgb(170, 170, 180);"
            "background-color: rgb(15, 15, 20);"
            "border-radius: 10px;"
            "border-color: rgb(250, 250, 250);"
            "font: bold 14px;"
            "min-width: 10em;"
            "padding: 6px;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}"
            "QPushButton::hover"
            "{"
            "background-color: rgb(30, 30, 50);"
            "}")

        # Смещение кнопок
        self.label.move(10, 10)
        self.button_open.move(975, 710)
        self.button_save.move(975, 750)

        # self.button_history.move(1065, 15)
        self.button_inst.move(975, 15)
        self.button_filt.move(975, 90)

        # Смещение кнопок фильтров
        self.button_blackwhite.move(975, 145)
        self.button_red.move(975, 190)
        self.button_blue.move(975, 235)
        self.button_green.move(975, 280)
        self.button_light.move(975, 325)
        self.button_dark.move(975, 370)
        self.button_negativ.move(975, 415)
        self.button_contrast.move(975, 460)
        self.button_sepia.move(975, 505)
        self.button_mirrorv.move(975, 550)
        self.button_mirrorg.move(975, 595)
