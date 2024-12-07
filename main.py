import sys
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from random import randint
from UI import Ui_Form


class WidgetsHideNSeek(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.drawKrug)
        self.flag = False

    def drawKrug(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        try:
            if self.flag:
                qp = QPainter()
                qp.begin(self)
                for _ in range(5):
                    color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
                    qp.setPen(color)
                    qp.setBrush(color)
                    cx = randint(20, 380)
                    cy = randint(81, 280)
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
