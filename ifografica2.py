#построение двух графиков рядом
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,AutoMinorLocator)
import numpy as np
import read_write_file
import sorting

# Исходные данные
data = read_write_file.read_numbers("1.txt")
x = []
y1 = data
m = sorting.quickSort(data)
for i in range(len(data)):
    x.append(i)

# Сортированные данные

y2 = [m[i] for i in x] # Заполняем y2 всеми данными, что есть в сортировке

# Построение графиков

plt.plot(x, y1, x, y1, "ro", x, y2, x, y2, "go" ) # построение графика где точки это исходные значения
plt.title("Зависимости: y1 = Исходные данные, y2 = сортированные данные") # заголовок
plt.grid(True)                # включение отображение основной сетки
#plt.grid(True, which="minor", color="gray", linestyle='--') # Включение отображения мини-сетки
#plt.legend(loc='best', fontsize=12)
plt.show()