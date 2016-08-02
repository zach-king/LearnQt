"""
File: signals_and_slots.pyw

A demonstration of the high-level usage of 
PyQt signals and slots.
"""


from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        dial = QDial()
        dial.setNotchesVisible(True)
        zerospinbox = ZeroSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(zerospinbox)
        self.setLayout(layout)

        self.connect(dial, SIGNAL('valueChanged(int)'), zerospinbox, SLOT('setValue(int)'))
        self.connect(zerospinbox, SIGNAL('atzero'), self.announce)
        self.connect(zerospinbox, SIGNAL('valueChanged(int)'), dial, SLOT('setValue(int)'))
        
        self.setWindowTitle('Signals and Slots')

    def announce(self, zeros):
        print('ZeroSpinBox has been at zero %d times' % zeros)


class ZeroSpinBox(QSpinBox):
    zeros = 0

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)
        self.connect(self, SIGNAL('valueChanged(int)'), self.checkzero)

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.emit(SIGNAL('atzero'), self.zeros)


class TaxRate(QObject):
    def __init__(self):
        super(TaxRate, self).__init__()
        self.__rate = 17.5

    def rate(self):
        return self.__rate

    def setRate(self, rate):
        if rate != self.__rate:
            self.__rate = rate
            self.emit(SIGNAL('rateChanged'), self.__rate)


def rateChanged(value):
    print('TaxRate changed to %.2f%%' % value)



if __name__ == '__main__':
    # Non-GUI example
    vat = TaxRate()
    vat.connect(vat, SIGNAL('rateChanged'), rateChanged)
    vat.setRate(17.5)   # No change will occur (new rate is the same)
    vat.setRate(8.5)    # A change will occur (new rate is different)

    # GUI example
    app = QApplication([__file__,])
    form = Form()
    form.show()
    app.exec_()