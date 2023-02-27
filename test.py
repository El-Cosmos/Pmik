import openpyxl
import Xl

wb = openpyxl.reader.excel.load_workbook(filename="Shet.xlsx", data_only=True)

wb.active = 1
sheet = wb.active

sheet['A1'] = "Страна"
sheet['B1'] = "Население"

row = 2
for i in range(9):
    print(Xl.sorting_people.get(Xl.x[i]),":",Xl.x[i])
    sheet[row][0].value = Xl.sorting_people.get(Xl.x[i])
    sheet[row][1].value = Xl.x[i]
    row+=1

wb.save("Shet.xlsx")
wb.close
