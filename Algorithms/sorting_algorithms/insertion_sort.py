def insertion_sort(arr: list):
    sorted_array = []
    for element in arr:
        if len(sorted_array) == 0:
            sorted_array.append(element)
        else:
            inserted = False
            for index, value in enumerate(sorted_array):
                if element <= value:
                    sorted_array.insert(index, element)
                    inserted = True
                    break
            if not inserted:
                sorted_array.append(element)
    return sorted_array

def inline_insertion_sort(arr:list):
    for element in arr:
        for i,el in enumerate(arr):
            # print(f'Comparing: {element} To: {el} index of {i}')
            if element <= el:
                popped_element = arr.pop(arr.index(element))
                arr.insert(i,popped_element)
                break

if __name__ == '__main__':
    arrs = [[10,2,5,3,1,10],
            [],
            [5],
            [-1,-2,5,2],
            [1,2,3,4,5,6]]
    # arr_sorted = insertion_sort(arr)
    # print(arr_sorted)
    for arr in arrs:
        inline_insertion_sort(arr)
    print(arrs)
    inline_insertion_sort(arrs)
    print(arrs)

