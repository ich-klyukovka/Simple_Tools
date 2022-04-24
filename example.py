from Tool import *  # Импортируем файл, как библиотеку

array = tool.randomPack(0, 100, 10)  # Функция заполнения массива, где
# (минимальное число в массиве, максимальное число, количество чисел)
tool.bubble_sort(array)  # Сортировка массива методом пузырька, где (массив)
print(array)
array = tool.randomPack(0, 100, 10)
tool.select_sort(array)  # Сортировка массива методом выбора, где (массив)
print(array)
array = tool.randomPack(0, 100, 10)
tool.select_sort_fromWiki(array)  # Сортировка массива методом выбора с сайта wiki, где (массив)
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
tool.quickSort(array, 0, len(array) - 1)  # Быстрая сортировка массива, где (массив, константа=0, длинна массива-1). 
# Прошу заметить, что в скобках должны быть именно эти аргументы 
print(array)
