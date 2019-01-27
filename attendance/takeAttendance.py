import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from update import *
#execfile('update.py')

class stuAttendance(QMainWindow):
	def __init__(self, parent=None):
		super(stuAttendance, self).__init__(parent)
		self.srnos = [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0], [11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0], [21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0], [31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0], [41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0], [51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0], [61.0, 62.0]]
		self.student_ids = [[u'B131015', u'B131016', u'B131017', u'B131030', u'B131051', u'B131053', u'B131089', u'B131095', u'B131104', u'B131109'], [u'B131110', u'B131120', u'B131123', u'B131142', u'B131150', u'B131152', u'B131173', u'B131178', u'B131179', u'B131255'], [u'B131287', u'B131300', u'B131301', u'B131305', u'B131309', u'B131371', u'B131391', u'B131420', u'B131423', u'B131476'], [u'B131502', u'B131549', u'B131577', u'B131586', u'B131598', u'B131602', u'B131608', u'B131611', u'B131615', u'B131662'], [u'B131680', u'B131690', u'B131694', u'B131718', u'B131731', u'B131744', u'B131755', u'B131756', u'B131775', u'B131781'], [u'B131797', u'B131834', u'B131850', u'B131852', u'B131870', u'B131883', u'B131894', u'B131906', u'B131911', u'B131919'], [u'B131938', u'B131955']]
		"""
		self.student_ids =[	["B131001","B131002","B131003","B131004","B131005","B131006","B131007","B131008","B131009","B131010"],
						["B131011","B131012","B131013","B131014","B131015","B131016","B131017","B131018","B131019","B131020"],
						["B131021","B131022","B131023","B131024","B131025","B131026","B131027","B131028","B131029","B131030"]
					]
		"""

		self.gridlayout = QGridLayout()
		self.subjects = ["OOPS","DSP","DC","VLSI","MPMC"]
		self.subCombo = QComboBox()
		self.subCombo.addItems(self.subjects)
		self.gridlayout.addWidget(self.subCombo)
		rowno = 1
		self.stucheckbox = []
		for row in self.student_ids:
			colno = 1
			rowcheckbox = []
			for stuid in row:
				self.idno = QCheckBox(stuid)
				self.idno.setChecked(True)
				self.gridlayout.addWidget(self.idno,rowno,colno)
				rowcheckbox.append(self.idno)
				colno = colno + 1
			self.stucheckbox.append(rowcheckbox)
			rowno = rowno + 1
		submit = QPushButton("Submit")
		submit.clicked.connect(self.submitTrigger)
		quitbtn = QPushButton("Quit")
		quitbtn.clicked.connect(QCoreApplication.instance().quit)
		self.gridlayout.addWidget(submit,rowno,colno-1)
		self.gridlayout.addWidget(quitbtn,rowno,colno)
		widget1 = QWidget()
		widget1.setLayout(self.gridlayout)
		self.setCentralWidget(widget1)
		self.setWindowTitle("EMBASE Attendance")
		self.setGeometry(100,100,350,400)

	def submitTrigger(self):
		self.passwidget = QDialog()
		self.passlayout = QHBoxLayout()
		#take input from CR
		self.passlabel = QLabel("Enter Password : ")
		self.passlayout.addWidget(self.passlabel)
		self.passline = QLineEdit()
		self.passline.setEchoMode(QLineEdit.Password)
		self.passlayout.addWidget(self.passline)
		self.passwidget.setLayout(self.passlayout)

		#submit/cancel button options to show
		self.confsub = QPushButton("OK")
		self.passlayout.addWidget(self.confsub)
		self.confsub.clicked.connect(self.authSubmit)
		self.confcancel = QPushButton("Cancel")
		self.confcancel.clicked.connect(self.authCancel)
		self.passlayout.addWidget(self.confcancel)

		self.passwidget.setWindowTitle("CR Authentication")
		self.passwidget.setGeometry(450,350,400,100)
		self.passwidget.setWindowModality(Qt.ApplicationModal)
		self.passwidget.exec_()

	def authSubmit(self):
		if checkPass(str(self.passline.text())) == False:
			self.passline.setStyleSheet("color : red;")
			return False

		subject = self.subCombo.currentText()
		
		rowno = 0;xlrow = 0
		attArray = []
		for row in self.student_ids:
			colno = 0;xlcol = 0
			for stuid in row:
				idcheckbox = self.stucheckbox[rowno][colno]
				state = idcheckbox.isChecked()
				#worksheet.write(xlrow,xlcol,stuid)
				#worksheet.write(xlrow,xlcol+1,state)
				if(state == True):
					state = 'P'
				else:
					state = 'A'
				attArray.append(state)
				colno = colno + 1;xlcol = xlcol + 1
			rowno = rowno + 1; xlrow = xlrow + 1
		update_att(attArray,subject)
		self.passwidget.done(1)

	def authCancel(self):
		self.passwidget.accept()
	def cancelTrigger(self):
		print("In authCancel")
		self.passwidget.done(1)

def main():
	app = QApplication(sys.argv)
	ex = stuAttendance()
	ex.show()
	sys.exit(app.exec_())
if __name__ == '__main__':
	main()
