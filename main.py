import read_write_file
import sorting
import infografica1

data = read_write_file.read_numbers("numbers.txt")


print("Исходные данные      ", data)
print("Сортировка пузырьком ", sorting.bubbleSort(data))
print("Сортировка вставками ", sorting.insertionSort(data))
print("Сортировка выбором   ", sorting.selectionSort(data))
print("Сортировка быстрая   ", sorting.quickSort(data))