def merge_two_lists(a,b,arr):


    len_a,len_b = len(a),len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
            k += 1
        else:
            arr[k] = b[j]
            j += 1
            k+= 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1
    
def merge_sort(arr):
    size = len(arr)
    mid = size // 2

    if size <= 1:
        return

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    merge_two_lists(left,right,arr)

if __name__ == '__main__':
    test_cases = [
        [100,5,1,500,10,3,20,2,510,20,10],
        [],
        [3],
        [10,3,1,7,8,23,98,29],
        [9,8,7,2],
        [1,2,3,4,5]
    ]
    for c in test_cases:
        merge_sort(c)

    print(test_cases)