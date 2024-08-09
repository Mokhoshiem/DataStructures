def merge_two_lists(a,b):
    sorted_list = []
    len_a,len_b = len(a),len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
        
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list
    

def merge_sort(arr):
    size = len(arr)
    mid = size // 2
    if size <= 1:
        return arr
    
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge_two_lists(left,right)
    
if __name__ == '__main__':
    arr = [5,2,30,50,150,10,150]
    sorted_list = merge_sort(arr)
    print(sorted_list)

