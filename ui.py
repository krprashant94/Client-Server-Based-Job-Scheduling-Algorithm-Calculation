# import tracemalloc
# tracemalloc.start()

import sys
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class MainApp(QMainWindow):
	def __init__(self):
		super(MainApp, self).__init__()
		loadUi('ui_skliton.ui', self)
		self.move(50, 0)
		self.show()

		self.pushButton_3.clicked.connect(self.rr)
		self.pushButton_4.clicked.connect(self.sjf)
		self.pushButton_5.clicked.connect(self.sjfp)
		self.pushButton_6.clicked.connect(self.fcfs)
		self.pushButton_7.clicked.connect(self.lrtf)
		self.pushButton_8.clicked.connect(self.ps)

		self.pushButton_9.clicked.connect(self.java)
		self.pushButton_10.clicked.connect(self.python)


	def rr(self):
		os.chdir("./Server")
		os.system("start java  RRServer")
	def sjf(self):
		os.chdir("./Server")
		os.system("start java  SJFServer")
	def sjfp(self):
		os.chdir("./Server")
		os.system("start java  SJFPServer")
	def fcfs(self):
		os.chdir("./Server")
		os.system("start java  GFGServer")
	def lrtf(self):
		os.system("start python LRTF.py")
	def ps(self):
		os.system("start python prority_sheduling.py")

	def java(self):
		os.chdir("./Client")
		os.system("start java  Client")
	def python(self):
		os.system("start python client.py")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainApp()
	sys.exit(app.exec_())
