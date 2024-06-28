MIN_RUN = 32

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    len1, len2 = mid - left + 1, right - mid
    left_part, right_part = [], []
    for i in range(0, len1):
        left_part.append(arr[left + i])
    for i in range(0, len2):
        right_part.append(arr[mid + 1 + i])

    i, j, k = 0, 0, left

    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_part[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right_part[j]
        k += 1
        j += 1

def tim_sort(arr):
    n = len(arr)

    for i in range(0, n, MIN_RUN):
        insertion_sort(arr, i, min((i + MIN_RUN - 1), (n - 1)))

    size = MIN_RUN
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(n - 1, start + size - 1)
            right = min((start + size * 2 - 1), (n - 1))
            if mid < right:
                merge(arr, start, mid, right)
        size *= 2

# Example usage:
if __name__ == "__main__":
    array = [5, 21, 7, 23, 19, 13, 25, 18, 12, 15, 1, 10]
    print("Original array:", array)
    tim_sort(array)
    print("Sorted array:", array)
