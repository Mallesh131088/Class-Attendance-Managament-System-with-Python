from xlrd import *
from xlwt import *
from xlutils.copy import copy
from datetime import datetime
from os import *
import pynotify
from crypt import crypt

def update_att(attArray,sub):
	filename = sub+".xlsx"
	oldbook = open_workbook(filename)
	oldsheet = oldbook.sheet_by_index(0)
	maxcolno = oldsheet.ncols
	newbook = copy(oldbook)
	newsheet = newbook.get_sheet(0)

	#style the cells
	style1 = XFStyle()
	font = Font()
	font.bold = True
	style1.font = font

	#change header font style
	#for i in range(maxcolno):
	#	write_rich_text(0,i,style= style1)

	newsheet.write(0,maxcolno,datetime.now().strftime("%Y-%m-%d"),style = style1)
	rowno = 2
	for stuAtt in attArray:
		newsheet.write(rowno,maxcolno,stuAtt)
		rowno = rowno + 1
	newbook.save(filename)
	#pynotify.Notification("CR_Authentication","Attendance Success").show()

def checkPass(userpass):
	#crypt_pass = str(crypt(userpass,'./'))
	crypt_pass = userpass
	#pynotify.init("NewNotification")
	if( crypt_pass == 'mallesh'):
		return True
	else:
		#pynotify.Notification("CR_Authentication","Sorry! Enter Password again").show()
		return False
