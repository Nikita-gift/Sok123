import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QColor, QPainter


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Circle Drawer")
        self.setGeometry(100, 100, 800, 600)

        self.button = QPushButton("Draw Circle", self)
        self.button.clicked.connect(self.draw_random_circle)  # Исправлено: подключаем метод

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.circle_radius = 0
        self.circle_color = QColor(0, 0, 0)

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.circle_radius > 0:
            painter.setBrush(self.circle_color)
            painter.drawEllipse((self.width() - self.circle_radius) // 2,
                                (self.height() - self.circle_radius) // 2,
                                self.circle_radius, self.circle_radius)

    def draw_random_circle(self):
        self.circle_radius = random.randint(20, 200)
        self.circle_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.update()  # Обновляем интерфейс для перерисовки


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec_())
