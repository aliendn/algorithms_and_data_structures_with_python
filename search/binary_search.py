def binary_search(arr: list, value: int, start: int, end: int) -> int:
    if arr[end] < value or arr[start] > value:
        return -1
    else:
        mid = (start + end) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return binary_search(arr=arr, value=value, start=start, end=mid - 1)
        else:
            return binary_search(arr=arr, value=value, start=mid + 1, end=end)


if __name__ == "__main__":
    data = [0, 4, 8, 10, 25, 26, 49, 54, 67, 87, 93]
    bs = binary_search(arr=data, value=92, start=0, end=10)
    print(bs)