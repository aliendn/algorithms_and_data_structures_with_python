def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage:
if __name__ == "__main__":
    array = [64, 25, 12, 22, 11]
    print("Original array:", array)
    sorted_array = selection_sort(array)
    print("Sorted array:", sorted_array)
