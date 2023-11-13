from PyQt5.QtGui import QPixmap, QColor, QTransform


class PhotoShop():
    def __init__(self, label):
        self.label = label
    # Функции фильтров
    # Сепиа

    def sepia(self):
        if not self.label.pixmap():
            return

        image = self.label.pixmap().toImage()
        for x in range(image.width()):
            for y in range(image.height()):
                color = QColor(image.pixelColor(x, y))
                new_red = min(color.red() + 50, 255)
                new_green = min(color.green() + 30, 255)
                new_blue = min(color.blue() + 10, 255)
                new_color = QColor(new_red, new_green, new_blue)
                image.setPixelColor(x, y, new_color)

        self.label.setPixmap(QPixmap.fromImage(image))

    # Контраст
    def contrast(self):
        if not self.label.pixmap():
            return

        contrast_factor = 1.5

        image = self.label.pixmap().toImage()
        for x in range(image.width()):
            for y in range(image.height()):
                color = QColor(image.pixelColor(x, y))
                new_red = self.apply_contrast(color.red(), contrast_factor)
                new_green = self.apply_contrast(color.green(), contrast_factor)
                new_blue = self.apply_contrast(color.blue(), contrast_factor)
                image.setPixelColor(x, y, QColor(new_red, new_green, new_blue))

        self.label.setPixmap(QPixmap.fromImage(image))

    def apply_contrast(self, value, factor):
        return min(255, max(0, int(factor * (value - 128) + 128)))

    # Краснее
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

        return self.label.setPixmap(QPixmap.fromImage(image))

    # Синевее
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

    # Зеленее
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

    # Светлее
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

    # Темнее
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

    # ЧБ
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

    # Зеркалить по горизонтали
    def mirror_g(self):
        if not self.label.pixmap():
            return

        pixmap = self.label.pixmap()
        transform = QTransform().scale(-1, 1)
        mirrored_pixmap = pixmap.transformed(transform)

        self.label.setPixmap(mirrored_pixmap)

    # Зеркалить по вертикали
    def mirror_v(self):
        if not self.label.pixmap():
            return

        pixmap = self.label.pixmap()
        transform = QTransform().scale(1, -1)
        mirrored_pixmap = pixmap.transformed(transform)

        self.label.setPixmap(mirrored_pixmap)

    # Негатив
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
