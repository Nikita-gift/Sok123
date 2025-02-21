import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)

        self.button = self.findChild(QPushButton, 'buttonSokolovich')
        self.button.clicked.connect(self.draw_circles)

        self.circles = []

    def draw_circles(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))  # Желтый цвет
        for (x, y, diameter) in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
