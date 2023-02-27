import openpyxl
from array import *
import sorting
import pandas as pd

wb = openpyxl.reader.excel.load_workbook(filename="Shet.xlsx", data_only=True)
#print(wb.sheetnames)
wb.active = 0
sheet = wb.active
#print(sheet['A1'].value)
#for i in range(1,12):
 #   print(sheet['A'+str(i)].value,sheet['B'+str(i)].value)

contry = {}
people = {}

for i in range(2,12):
    contry.update({sheet['A'+str(i)].value: sheet['B'+str(i)].value})
    people.update({sheet['B'+str(i)].value: sheet['A'+str(i)].value})

print(contry)
print("\n")
print(people)
print("\n")

sorted_contry = dict(sorted(contry.items(), key=lambda item: item[1]))# сортировка внутренняя(которую нельзя)
print(sorted_contry)
print("\n")
print(contry.values())


*x, = contry.values()

sorting.bubbleSort(x)



sorting_people = {}

for i in range(len(x)):
    key, value = x[i], people[x[i]]
    sorting_people[key] = value


print("Это сортированный словарь:", sorting_people)
print("\n")

#sorting_people.update(people.values(x[0]))
#print(sorting_people)
#print("\n")
#for i in range(len(x)):
   # print(x[i],":", people.pop(x[i]))

df = pd.DataFrame(sorting_people)
df.to_excel('./Shet2.xlsx', sheet_name='Sorted', index=False)