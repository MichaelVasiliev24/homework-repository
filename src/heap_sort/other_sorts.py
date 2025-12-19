def bubble_sort(arr):
    """Сортировка пузырьком (Bubble sort)"""
    if len(arr) <= 1:
        return arr

    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


def merge_sort(arr):
    """Сортировка слиянием (Merge sort)"""
    if len(arr) <= 1:
        return arr

    temp = [0] * len(arr)
    merge_sort_recursive(arr, temp, 0, len(arr) - 1)
    return arr


def merge_sort_recursive(arr, temp, left, right):
    """Рекурсивная вспомогательная функция для сортировки слиянием"""
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort_recursive(arr, temp, left, mid)
    merge_sort_recursive(arr, temp, mid + 1, right)

    merge(arr, temp, left, mid, right)


def merge(arr, temp, left, mid, right):
    """Слияние двух отсортированных частей"""
    i, j, k = left, mid + 1, left

    for m in range(left, right + 1):
        temp[m] = arr[m]

    while i <= mid and j <= right:
        if temp[i] <= temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j += 1
        k += 1

    while i <= mid:
        arr[k] = temp[i]
        i += 1
        k += 1
