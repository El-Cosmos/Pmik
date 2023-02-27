import openpyxl

wb = openpyxl.reader.excel.load_workbook(filename="Shet.xlsx", data_only=True)
#print(wb.sheetnames)
wb.active = 1
sheet = wb.active

sheet['A2'] = "Мексика"
sheet['B2'] = 133862892