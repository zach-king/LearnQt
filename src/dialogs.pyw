"""
File: dialogs.pyw

Demo for various PyQt dialogs.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        layout = QVBoxLayout()
        button = QPushButton('Properties')
        layout.addWidget(button)
        self.setLayout(layout)
        self.connect(button, SIGNAL('clicked()'), self.setPenProperties)
        self.width = 1
        self.beveled = False
        self.style = 'Solid'

    def setPenProperties(self):
        dialog = PenPropertiesDlg(self)
        dialog.widthSpinBox.setValue(self.width)
        dialog.beveledCheckBox.setChecked(self.beveled)
        dialog.styleComboBox.setCurrentIndex(
            dialog.styleComboBox.findText(self.style))
        if dialog.exec_():
            self.width = dialog.widthSpinBox.value()
            self.beveled = dialog.beveledCheckBox.isChecked()
            self.style = str(dialog.styleComboBox.currentText())
            self.updateData()

    def updateData(self):
        print('Width: %d' % self.width)
        print('Beveled: ' + str(self.beveled))
        print('Style: %s' % self.style)


class PenPropertiesDlg(QDialog):
    def __init__(self, parent=None):
        super(PenPropertiesDlg, self).__init__(parent)

        widthLabel = QLabel('&Width:')
        self.widthSpinBox = QSpinBox()
        widthLabel.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.widthSpinBox.setRange(0, 24)
        self.beveledCheckBox = QCheckBox('&Beveled edges')
        styleLabel = QLabel('&Style:')
        self.styleComboBox = QComboBox()
        styleLabel.setBuddy(self.styleComboBox)
        self.styleComboBox.addItems(['Solid', 'Dashed', 'Dotted', 'DashDotted', 'DashDotDotted'])
        okButton = QPushButton('&OK')
        cancelButton = QPushButton('Cancel')

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout = QGridLayout()
        layout.addWidget(widthLabel, 0, 0)
        layout.addWidget(self.widthSpinBox, 0, 1)
        layout.addWidget(self.beveledCheckBox, 0, 2)
        layout.addWidget(styleLabel, 1, 0)
        layout.addWidget(self.styleComboBox, 1, 1, 1, 2)
        layout.addLayout(buttonLayout, 2, 0, 1, 3)
        self.setLayout(layout)

        self.connect(okButton, SIGNAL('clicked()'), self, SLOT('accept()'))
        self.connect(cancelButton, SIGNAL('clicked()'), self, SLOT('reject()'))
        self.setWindowTitle('Pen Properties')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()