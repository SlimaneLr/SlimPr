from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 230, 500, 400)
        self.setWindowTitle('Python')
        self.setWindowIcon(QIcon('images/005 python.png'))
        self.button()

    def button(self):
        hbox = QHBoxLayout()
        btn = QPushButton('click', self)
        btn.clicked.connect(self.clicked_btn)

        self.label = QLabel('<== Click me')

        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def clicked_btn(self):
        self.label.setText('NICE')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
