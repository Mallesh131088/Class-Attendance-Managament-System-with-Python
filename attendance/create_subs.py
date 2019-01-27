import sys
from xlwt import *
from datetime import datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
class stuAttendance(QMainWindow):
	def __init__(self, parent=None):
		super(stuAttendance, self).__init__(parent)
		"""
		self.students =[	["B131001","B131002","B131003","B131004","B131005","B131006","B131007","B131008","B131009","B131010"],
						["B131011","B131012","B131013","B131014","B131015","B131016","B131017","B131018","B131019","B131020"],
						["B131021","B131022","B131023","B131024","B131025","B131026","B131027","B131028","B131029","B131030"]
					]
		self.rollno = [		["1","2","3","4","5","6","7","8","9","10"],
							["11","12","13","14","15","16","17","18","19","20"],
							["21","22","23","24","25","26","27","28","29","30"]
					]
		"""
		self.students =[[u'B131015', u'B131016', u'B131017', u'B131030', u'B131051', u'B131053', u'B131089', u'B131095', u'B131104', u'B131109'], [u'B131110', u'B131120', u'B131123', u'B131142', u'B131150', u'B131152', u'B131173', u'B131178', u'B131179', u'B131255'], [u'B131287', u'B131300', u'B131301', u'B131305', u'B131309', u'B131371', u'B131391', u'B131420', u'B131423', u'B131476'], [u'B131502', u'B131549', u'B131577', u'B131586', u'B131598', u'B131602', u'B131608', u'B131611', u'B131615', u'B131662'], [u'B131680', u'B131690', u'B131694', u'B131718', u'B131731', u'B131744', u'B131755', u'B131756', u'B131775', u'B131781'], [u'B131797', u'B131834', u'B131850', u'B131852', u'B131870', u'B131883', u'B131894', u'B131906', u'B131911', u'B131919'], [u'B131938', u'B131955']]
		self.rollno = [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0], [11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0], [21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0], [31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0], [41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0], [51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0], [61.0, 62.0]]
			
		self.subjects = ["OOPS","DSP","DC","VLSI","MPMC"]
		for sub in self.subjects:
			wb = Workbook()
			ws = wb.add_sheet('Sheet1')

			#style the cells
			style1 = XFStyle()
			font = Font()
			font.bold = True
			style1.font = font
			
			ws.write(0,0,'ID')
			ws.write(0,1,'RollNo')

			#Write the ID's to sheet
			rowno = 2; colno = 0
			sturowno = 0
			for sturowids in self.students:
				stucolno = 0
				for stuid in sturowids:
					ws.write(rowno,colno,stuid)
					stucolno = stucolno + 1
					rowno = rowno + 1
				sturowno = sturowno + 1

			#Write RollNo's to sheet
			rowno = 2; colno = 1
			sturowno = 0
			for sturowrolls in self.rollno:
				stucolno = 0
				for stuid in sturowrolls:
					ws.write(rowno,colno,stuid)
					stucolno = stucolno + 1
					rowno = rowno + 1
				sturowno = sturowno + 1
			wb.save(sub+".xlsx")

		
def main():
	app = QApplication(sys.argv)
	ex = stuAttendance()
	ex.show()
	sys.exit(app.exec_())
if __name__ == '__main__':
	main()
