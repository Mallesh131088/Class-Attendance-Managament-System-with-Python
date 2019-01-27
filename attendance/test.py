"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from pynotify import *

class wLayout(object):
	def __init__(self):
		self.win = QWidget()
		self.grid = QGridLayout()
		for i in range(5):
			for j in range(4):
				self.grid.addWidget(QPushButton("L"+str(i)+str(j)),i,j)
		self.win.setGeometry(100,100,200,100)
		self.vbox = QVBoxLayout()
		#vbox.setStretch()
		self.win.setLayout(self.grid)
	def display(self):
		Notification("laksdfad").show()

import sys
if __name__ == '__main__':
	app = QApplication(sys.argv)
	layout = wLayout()
	layout.display()
	sys.exit(app.exec_())
"""

#!/usr/bin/env python

import pynotify

pynotify.init("MyApplication")

a = pynotify.Notification("Test notification", "Lorem ipsum op")
a.show()
raw_input("Press return to update the notification")
a.update("Updated notification", "Ipsum lorem still op")
a.show()