import random


# Для рускоязычных товарищей, сортировка пузырьком.
# Сравниваем первый и второй кто больше и меняем местами. Затем увеличиваем индекс проверяемых элементов.
# Когда он максимальный, возвращаемся к первому.
def bubble_sort(m):
    i = end = 0
    while i <= (len(m) - end) - 1:
        if m[i] > m[i + 1]:
            m[i], m[i + 1] = m[i + 1], m[i]
        else:
            pass
        i = i + 1
        if i >= len(m) - end - 1:
            i = 0
            end += 1
        if end == len(m):
            break


# Сортировка выбором. Ищем максимальный элемент и меняем его местами с последним неотсортированным

def select_sort(m):
    for i in range(len(m) - 1):
        for k in range(i + 1, len(m)):
            if m[k] < m[i]:
                m[k], m[i] = m[i], m[k]


# Шейкерная сортировка или сортировка перемешиванием. Сортировка пузырьком, но когда достигли последнего эл-та, то
# идем по уменьшению
def coctail_shaker_sort(m):
    left = 0
    right = len(m) - 1
    while left <= right:
        for i in range(left, right, +1):
            if m[i] > m[i + 1]:
                m[i], m[i + 1] = m[i + 1], m[i]
        right -= 1

        for i in range(right, left, -1):
            if m[i - 1] > m[i]:
                m[i], m[i - 1] = m[i - 1], m[i]
        left += 1


# Сортировка расчёсской. Основная идея «расчёски» в том, чтобы первоначально брать большое расстояние
# между сравниваемыми элементами и по мере упорядочивания массива сужать это расстояние вплоть до минимального.
# А-ля пузырьком
def comb_sort(m):
    alen = len(m)
    gap = (alen * 10 // 13) if alen > 1 else 0
    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = False
        for i in range(alen - gap):
            if m[i + gap] < m[i]:
                m[i], m[i + gap] = m[i + gap], m[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped


# Сортировка слиянием. Сначала делим список на кусочки (по 1 элементу), затем сравниваем каждый элемент с
# соседним, сортируем и объединяем. В итоге, все элементы отсортированы и объединены вместе.
def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    L = merge_sort(A[:len(A) // 2])
    R = merge_sort(A[len(A) // 2:])
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(A)):
        A[i] = C[i]
    return A


# Сортировка вставками. элементы входной последовательности просматриваются по одному, и каждый новый поступивший
# элемент размещается в подходящее место среди ранее упорядоченных элементов
def insertion_sort(m):
    for i in range(1, len(m)):
        temp = m[i]
        j = i - 1
        while j >= 0 and temp < m[j]:
            m[j + 1] = m[j]
            j = j - 1
        m[j + 1] = temp


# Кусочек быстрой сортировки
def partition(TakenArray, low, high):
    pivot = TakenArray[high]
    i = low - 1
    for j in range(low, high):
        if TakenArray[j] <= pivot:
            i = i + 1
            (TakenArray[i], TakenArray[j]) = (TakenArray[j], TakenArray[i])
    (TakenArray[i + 1], TakenArray[high]) = (TakenArray[high], TakenArray[i + 1])
    return i + 1


# Быстрая сортировка. Выбрать из массива элемент, называемый опорным. Это может быть любой из элементов массива.
# От выбора опорного элемента не зависит корректность алгоритма, но в отдельных случаях может сильно зависеть его
# эффективность

# Сравнить все остальные элементы с опорным и переставить их в массиве так, чтобы разбить массив на три
# непрерывных отрезка, следующих друг за другом: «элементы меньшие опорного», «равные» и «большие»

# Для отрезков «меньших» и «больших» значений выполнить рекурсивно ту же последовательность операций, если длина
# отрезка больше единицы.
def quickSort(TakenArray):
    low = 0
    high = len(TakenArray) - 1
    if low < high:
        pi = partition(TakenArray, low, high)
        q2(TakenArray, low, pi - 1)
        q2(TakenArray, pi + 1, high)


def q2(TakenArray, low, high):
    if low < high:
        pi = partition(TakenArray, low, high)
        q2(TakenArray, low, pi - 1)
        q2(TakenArray, pi + 1, high)


# Заполнение массива случайными числами заданного диапазона
def randomPack(d1, d2, quantity):
    a = [random.randint(d1, d2) for i in range(quantity)]
    return a


def show(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()


def randomDoublePack(d1, d2, quantity, quantity1):
    a = [[random.randint(d1, d2) for j in range(quantity1)] for i in range(quantity)]
    return a


def swipeStr(matrix, n, m):
    matrix[n], matrix[m] = matrix[m], matrix[n]


def takeColumn(matrix, n):
    return [row[n] for row in matrix]


def rotate(matrix):
    return tuple(zip(*matrix[::-1]))
