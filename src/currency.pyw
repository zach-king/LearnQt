"""
File: currency.pyw

Simple currency conversion app.
"""


import sys
from urllib import request
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        date = self.getdata()
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 10000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        self.toLabel = QLabel('1.00')

        grid = QGridLayout()
        grid.addWidget(dateLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinbox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)

        self.connect(self.fromComboBox,
            SIGNAL('currentIndexChanged(int)'), self.updateUi)
        self.connect(self.toComboBox,
            SIGNAL('currentIndexChanged(int)'), self.updateUi)
        self.connect(self.fromSpinBox,
            SIGNAL('valueChanged(double)'), self.updateUi)
        self.setWindowTitle('Currency')


    def updateUi(self):
        to = str(self.toComboBox.currentText())
        from_ = str(self.fromComboBox.currentText())
        amount = (self.rates[from_] / self.rates[to]) * self.fromSpinBox.value()
        self.toLabel.setText('%0.2f' % amount)

    def getdata(self):
        raise NotImplementedError('-- TODO --')
        # self.rates = []
        # try:
        #     date = 'Unknown'
        #     fh = request.urlopen('http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv')
