"""
File: calculator.pyw

A simple expression evaluator / calculator.
"""

from __future__ import division
import sys
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # Create the widgets
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit('Type an expression and press <Enter>')

        # Select all the text on the LineEdit so user can type immediately
        self.lineedit.selectAll()

        # Use a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)

        # Start with the LineEdit focused
        self.lineedit.setFocus()

        # Bind <Enter> to updateUi()
        self.connect(self.lineedit, SIGNAL('returnPressed()'), self.updateUi)

        # Set the window's title
        self.setWindowTitle('Calculator')

    def updateUi(self):
        # Try to evaluate the user's expression and update the TextBrowser
        try:
            text = str(self.lineedit.text())
            self.browser.append('{0} = <b>{1}</b>'.format(text, eval(text)))
        except:
            self.browser.append('<font color=red>%s is invalid!</font>' % text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()