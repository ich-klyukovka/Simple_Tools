import TestVersion as tool

array = tool.randomPack(0, 100, 10)  # Функция заполнения массива, где
# (минимальное число в массиве, максимальное число, количество чисел)
tool.bubble_sort(array)  # Сортировка массива методом пузырька, где (массив)
print(array)
array = tool.randomPack(0, 100, 10)
tool.select_sort(array)  # Сортировка массива методом выбора, где (массив)
print(array)
array = tool.randomPack(0, 100, 10)
tool.coctail_shaker_sort(array)  # Сортировка массива методом перемешивания, где (массив)
print(array)
array = tool.randomPack(0, 100, 10)
tool.comb_sort(array)  # Сортировка массива расчёской, где (массив)
print(array)
array = tool.randomPack(0, 100, 10)
tool.merge_sort(array)  # Сортировка массива методом слияния, где (массив)
print(array)
array = tool.randomPack(0, 100, 10)
tool.insertion_sort(array)  # Сортировка массива методом вставок, где (массив)
print(array)
array = tool.randomPack(0, 100, 10)
tool.quickSort(array)  # Быстрая сортировка массива, где (массив).
print(array)
print()

matrix = tool.randomDoublePack(0, 100, 5, 5)  # Заполнение матрицы 5*5 числами от 0 до 100
tool.show(matrix)  # Вывод матрицы
print()
tool.swipeStr(matrix, 0, 4)  # Поменяли 0 строку с 4 (матрица 5*5, но нумерация с 0)
tool.show(matrix)  # Вывод матрицы
print()
print(tool.takeColumn(matrix, 4))  # Взятый 4-й стролбец матрицы
print()
tool.rotate(matrix)  # Поворот матрицы на 90 градусов
tool.show(matrix)  # Вывод матрицы
