"""
File: connections.pyw

Demonstration of signals and slots where 
multiple objects are connected to the same 
slot, but the slot behaves differently depending 
on who called it.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.label = QLabel('No button has been pushed yet...')

        button1 = QPushButton('One')
        button2 = QPushButton('Two')
        button3 = QPushButton('Three')
        button4 = QPushButton('Four')
        button5 = QPushButton('Five')

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)

        self.setLayout(layout)

        self.connect(button1, SIGNAL('clicked()'), self.clicked)
        self.connect(button2, SIGNAL('clicked()'), self.clicked)
        self.connect(button3, SIGNAL('clicked()'), self.clicked)
        self.connect(button4, SIGNAL('clicked()'), self.clicked)
        self.connect(button5, SIGNAL('clicked()'), self.clicked)

    def clicked(self):
        button = self.sender()
        if button is None or not isinstance(button, QPushButton):
            return

        self.label.setText('You clicked button \'%s\'' % button.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()