import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 500, 400)
        self.btn = QPushButton(self)
        self.btn.move(100, 100)
        self.btn.resize(80,20)
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.CreateYellowEllipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def CreateYellowEllipse(self, qp):
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        f = random.randint(30, 70)
        qp.drawEllipse(random.randint(50, 300), random.randint(50, 300), f, f)
        qp.drawEllipse(random.randint(50, 300), random.randint(50, 300), f, f)
        qp.drawEllipse(random.randint(50, 300), random.randint(50, 300), f, f)
        qp.drawEllipse(random.randint(50, 300), random.randint(50, 300), f, f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
