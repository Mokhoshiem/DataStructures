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


if __name__ == '__main__':
    arr = [10,2,5,3,1,10]
    arr_sorted = insertion_sort(arr)
    print(arr_sorted)