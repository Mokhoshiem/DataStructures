def merge_two_lists(a,b,arr,key,ascending):

    len_a,len_b,key,ascending = len(a),len(b),key,ascending
    i = j = k = 0

    while i < len_a and j < len_b:
        
        if ascending == True:
            if a[i][key] <= b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
        else:
            if a[i][key] >= b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

def merge_sort(arr,key,ascending=True):
    size = len(arr)
    mid = size // 2

    if size <= 1:
        return
    
    left, right = arr[:mid],arr[mid:]
    merge_sort(left,key=key,ascending=ascending)
    merge_sort(right,key=key,ascending=ascending)
    merge_two_lists(left,right,arr=arr,key=key,ascending=ascending)

if __name__ == '__main__':
    test = [
        {'Name':'Ahmed','Age':'32','Size':'L'},
        {'Name':'Khaled','Age':'30','Size':'L'},
        {'Name':'Mahmoud','Age':'35','Size':'M'},
        {'Name':'Ahmed','Age':'33','Size':'S'},
        {'Name':'Mourad','Age':'31','Size':'XL'}
    ]

    merge_sort(test,key='Age')
    print(test)
    merge_sort(test,key='Age',ascending=False)
    print(test)