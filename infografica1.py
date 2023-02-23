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

# Построение графиков на разных осях. 2 Графика. Первый с исходными данными, второй график с отстортированными

plt.figure(figsize=(9, 9))
plt.subplot(2, 1, 1)
plt.plot(x, y1, x, y1, "ro")               # построение графика
plt.title("Зависимости: y1 = Исходные данные, y2 = сортированные данные") # заголовок
plt.ylabel("y1", fontsize=14) # ось ординат
plt.grid(which="major", linewidth=1.2)                # включение отображение основной сетки
plt.grid(which="minor", linestyle="--", color="gray", linewidth=0.5) # Включение отображения мини сетки
plt.subplot(2, 1, 2)
plt.plot(x, y2, x, y2, "ro")               # построение графика
plt.xlabel("x", fontsize=14)  # ось абсцисс
plt.ylabel("y2", fontsize=14) # ось ординат
plt.grid(which="major", linewidth=1.2)                # включение отображение основной сетки
plt.grid(which="minor", linestyle="--", color="gray", linewidth=0.5) # Включение отображения мини сетки
plt.show()