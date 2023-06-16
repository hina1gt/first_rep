import PyQt5
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont


class root(QWidget):

    def __init__(self, parent=None):
        super(root, self).__init__(parent)
        self.resize(1280, 720)
        self.setWindowTitle("first task")
        self.label = QLabel(self, text='Hello world')
        self.label.move(600, 50)
        font = QFont()
        font.setFamily('Roboto')
        font.setPointSize(20)
        self.label.setFont(font)

        self.label = QLabel(self, text='Python language')
        self.label.move(430, 250)
        font = QFont()
        font.setFamily('Arial')
        font.setPointSize(40)
        self.label.setFont(font)

        self.label = QLabel(self, text='First GUI App')
        self.label.move(350, 450)
        font = QFont()
        font.setFamily('Calibri')
        font.setPointSize(70)
        self.label.setFont(font)
def application():
    app = QApplication(sys.argv)
    ex = root()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()