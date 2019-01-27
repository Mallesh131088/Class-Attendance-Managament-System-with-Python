from xlwt import *
from xlrd import *
from xlutils import *

wb = open_workbook("ids_sno.xlsx");
ws = wb.sheet_by_index(0)

col = 1
colvar = 0
srnos = []
for row in range(7):
	row_srnos = []
	while((col-(colvar*10))%14 < 13 and col < ws.nrows):
		row_srnos.append(ws.cell_value(col,0))
		col = col + 1
	srnos.append(row_srnos)
	colvar = colvar + 1
print(srnos)

#Create ID's array similar to serial no's array

col = 1
colvar = 0
ids = []
for row in range(7):
	row_ids = []
	while((col-(colvar*10))%12 < 11 and col < ws.nrows):
		row_ids.append(ws.cell_value(col,1))
		col = col + 1
	ids.append(row_ids)
	colvar = colvar + 1
print(ids)

ids_srnos_created = open("ids_srnos_created.py",'w')

print(ids_srnos_created, srnos)
print(ids_srnos_created, ids)
