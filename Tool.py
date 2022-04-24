import random


class Types:
    i = 0
    end = 0
    maximum = 0
    left = 0
    right = 0
    low = 0
    high = 0

    # Для рускоязычных товарищей, сортировка пузырьком.
    # Сравниваем первый и второй кто больше и меняем местами. Затем увеличиваем индекс проверяемых элементов.
    # Когда он максимальный, возвращаемся к первому.
    def bubble_sort(self, m):
        self.i = self.end = 0
        while self.i <= (len(m) - self.end) - 1:
            if m[self.i] > m[self.i + 1]:
                m[self.i], m[self.i + 1] = m[self.i + 1], m[self.i]
            else:
                pass
            self.i = self.i + 1
            if self.i >= len(m) - self.end - 1:
                self.i = 0
                self.end += 1
            if self.end == len(m):
                self.i = 0
                self.end = 0
                break

    # Сортировка выбором. Ищем максимальный элемент и меняем его местами с последним неотсортированным
    def select_sort(self, m):
        self.i = self.end = 0
        while self.i <= (len(m) - self.end) - 1:
            if m[self.i] > self.maximum:
                self.maximum = m[self.i]
                self.iendd = self.i
            self.i += 1
            if self.i == (len(m) - self.end):
                if self.iendd == (len(m) - self.end):
                    pass
                else:
                    m[(len(m) - self.end) - 1], m[self.iendd] = m[self.iendd], m[(len(m) - self.end) - 1]
                self.iendd = 0
                self.i = 0
                self.end = self.end + 1
                self.maximum = 0
            if self.end == len(m):
                self.i = 0
                self.end = 0
                self.maximum = 0
                break

    # Сортировка выбором, но код взят с wiki
    def select_sort_fromWiki(self, m):
        for i in range(len(m) - 1):
            for k in range(i + 1, len(m)):
                if m[k] < m[i]:
                    m[k], m[i] = m[i], m[k]

    # Шейкерная сортировка или сортировка перемешиванием. Сортировка пузырьком, но когда достигли последнего эл-та, то
    # идем по уменьшению
    def coctail_shaker_sort(self, m):
        self.left = 0
        self.right = len(m) - 1
        while self.left <= self.right:
            for i in range(self.left, self.right, +1):
                if m[i] > m[i + 1]:
                    m[i], m[i + 1] = m[i + 1], m[i]
            self.right -= 1

            for i in range(self.right, self.left, -1):
                if m[i - 1] > m[i]:
                    m[i], m[i - 1] = m[i - 1], m[i]
            self.left += 1
        self.left = 0
        self.right = 0

    # Сортировка расчёсской. Основная идея «расчёски» в том, чтобы первоначально брать большое расстояние
    # между сравниваемыми элементами и по мере упорядочивания массива сужать это расстояние вплоть до минимального.
    # А-ля пузырьком
    def comb_sort(self, m):
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
    def merge_sort(self, A):
        if len(A) == 1 or len(A) == 0:
            return A
        L = self.merge_sort(A[:len(A) // 2])
        R = self.merge_sort(A[len(A) // 2:])
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
    def insertion_sort(self, m):
        for i in range(1, len(m)):
            temp = m[i]
            j = i - 1
            while (j >= 0 and temp < m[j]):
                m[j + 1] = m[j]
                j = j - 1
            m[j + 1] = temp

    # Кусочек быстрой сортировки
    def partition(self, array, low, high):
        pivot = array[high]
        self.i = low - 1
        for self.j in range(low, high):
            if array[self.j] <= pivot:
                self.i = self.i + 1
                (array[self.i], array[self.j]) = (array[self.j], array[self.i])
        (array[self.i + 1], array[high]) = (array[high], array[self.i + 1])
        return self.i + 1

    # Быстрая сортировка. Выбрать из массива элемент, называемый опорным. Это может быть любой из элементов массива.
    # От выбора опорного элемента не зависит корректность алгоритма, но в отдельных случаях может сильно зависеть его
    # эффективность

    # Сравнить все остальные элементы с опорным и переставить их в массиве так, чтобы разбить массив на три
    # непрерывных отрезка, следующих друг за другом: «элементы меньшие опорного», «равные» и «большие»

    # Для отрезков «меньших» и «больших» значений выполнить рекурсивно ту же последовательность операций, если длина
    # отрезка больше единицы.
    def quickSort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quickSort(array, low, pi - 1)
            self.quickSort(array, pi + 1, high)

    # Заполнение массива случайными числами заданного диапазона
    def randomPack(self, d1, d2, l):
        self.i = 0
        a = [random.randint(d1, d2) for self.i in range(l)]
        return a


tool = Types()
