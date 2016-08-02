"""
File: compound_interest.pyw
Author: Zachary King

A calculator app for compound interest.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.principal = QDoubleSpinBox()
        self.principal.setPrefix('$ ')
        self.principal.setRange(0.01, 10000000.00)
        self.rate = QDoubleSpinBox()
        self.rate.setSuffix(' %')
        self.rate.setRange(0.01, 100.00)
        self.years = QSpinBox()
        self.years.setRange(1, 100)
        self.amount = QLabel('$ 0.00')

        layout = QGridLayout()
        layout.addWidget(QLabel('Principal:'), 0, 0)
        layout.addWidget(self.principal, 0, 1)
        layout.addWidget(QLabel('Rate:'), 1, 0)
        layout.addWidget(self.rate, 1, 1)
        layout.addWidget(QLabel('Years:'), 2, 0)
        layout.addWidget(self.years, 2, 1)
        layout.addWidget(QLabel('Amount:'), 3, 0)
        layout.addWidget(self.amount, 3, 1)
        self.setLayout(layout)

        # Connections...
        self.connect(self.principal, SIGNAL('valueChanged(double)'), self.calculate)
        self.connect(self.rate, SIGNAL('valueChanged(double)'), self.calculate)
        self.connect(self.years, SIGNAL('valueChanged(int)'), self.calculate)

        self.setWindowTitle('Compound Interest')

    def calculate(self, value):
        principal = self.principal.value()
        rate = self.rate.value()
        years = self.years.value()
        new_value = principal * ((1 + (rate / 100.0)) ** years)
        self.amount.setText('$ %.2f' % new_value)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()