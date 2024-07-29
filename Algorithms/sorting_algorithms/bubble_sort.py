import random
def bubble_sorter(elements):
    '''This is an O(n^2) solution
    '''
    size = len(elements)
    for i in range(size-1):
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp


def mod_bubble_sorter(elements):
    '''This has o(n) if the array is already sorted.
    '''
    size = len(elements)
    swapped = False # If False means the array is sorted.
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped = True
    if not swapped:
        return


els1 = [100,5,3,4,2,1,15,30,10,55,40,30,20,10,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,1000,99,98,97,96,95,-5]
print(els1)
bubble_sorter(els1)
print(els1)
random.shuffle(els1)
print(els1)
mod_bubble_sorter(els1)
print(els1)

els2 = ['Daily','Weekly','Annual','Monthly','No Way']
print(els2)
bubble_sorter(els2)
print(els2)
random.shuffle(els2)
print(els2)
mod_bubble_sorter(els2)
print(els2)