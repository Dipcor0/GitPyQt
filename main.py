import sys
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from random import randint


class WidgetsHideNSeek(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.drawKrug)
        self.flag = False

    def drawKrug(self):
        print('12')
        self.flag = True
        self.update()

    def paintEvent(self, event):
        try:
            if self.flag:
                qp = QPainter()
                qp.begin(self)
                qp.setPen(QColor(255, 255, 0))
                qp.setBrush(QColor(255, 255, 0))
                for _ in range(5):
                    cx = randint(0, 400)
                    cy = randint(61, 300)
                    r = randint(20, 50)
                    qp.drawEllipse(cx, cy, r, r)
                qp.end()
            self.flag = False
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetsHideNSeek()
    ex.show()
    sys.exit(app.exec())
