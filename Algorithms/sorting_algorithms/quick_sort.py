def partition(arr,start,end):
    pivot = arr[end]

    i = start - 1 # Starting from -1
    for j in range(start,end):
        if arr[j] <= pivot:
            i +=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return i+1

def quick_sort(arr,start,end):
    if start < end:
        pivot = partition(arr,start,end)
        quick_sort(arr,start,pivot-1)
        quick_sort(arr,pivot+1,end)


# Example usage:
if __name__ == "__main__":
    arr = [10, 7, -3, 9, -5, 5]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print("Sorted array is:")
    print(arr)

