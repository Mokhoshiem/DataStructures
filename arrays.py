#  Arrays are simple data structure that stores data based on index.
#  There are two types of arrays Static and Dynamic Arrays.
#  Static Arrays have fixed size.
#  Dynamic Arrays use fixed size at first lets say 8 bytes and when reaching the limit if we need to add more elements it add an additional size (size * 2) and extends.
#  We can edit, add, delete in an array.
# Looking up an element by index has complexity O(1). If We loop to find the value O(n).
# Adding an element to the end is O(1). Adding to any othe index O(n) because we will move all elements after that index.
#  Removing an element O(n) for the same reason above.

# Using python list:
#  You have an expenes list for month from Jan to March as followimg(2200, 2350, 2600, 2130,, 2190)
#  Create a list to store those expenses to find out the following:
# 1- In Feb. mow many dollars you spent extra than Jan?
# 2- Find out your total expenses in the first quarter.
# 3- Find out if you spent exactly 2000 dollars?
# 4- June just finished and you need to store its expense as value of $1980.
# 5- You returned an item you bought in April and you got $200 refund, update april expenses.

expenses = [2200, 2350, 2600, 2130, 2190]
print(f'Expenses: {expenses}')

diff_in_feb = expenses[1] - expenses[0]
print(f'Diff in Feb from Jan is: {diff_in_feb}')

first_quarter_expenses = sum(expenses[:3])
print(f'first_quarter_expenses are: {first_quarter_expenses}')

print('2000 Found' if 2000 in expenses else '2000 No Found')

expenses.append(1980)
print(f'Added June to expenses: {expenses}')

expenses[3] = expenses[3]-200
print(f'Updated April : {expenses}')


class MyStaticArray:
    '''A static Array Class with deault length of 5 elements
    Parameters:
        - arr is optional
        - n length of the array
    Usage:
        - You have to enter one arguement to create a static array either you enter a list or the number of elements.
        - eg: my_array = MyStaticArray([1,2,3,4])
        - eg: my_array = MyStaticArray(n=4)
    '''
    def __init__(self,arr=[],n=5):
        self.__elements = len(arr) if arr != [] else n
        self.__current = 0
        self.__content = [0 for i in range(n)] if arr == [] else arr
        # self.initializer()
    
    def update_value(self,index,value):
        if index < self.__elements:
            self.__content[index] = value
        else:
            raise IndexError(f'Your index is out of the range. Your max index is: {self.__elements - 1}')
    
    def append_value(self,value):
        if self.__current < self.__elements:
            self.__content[self.__current] = value
            self.__current += 1
        else:
            raise IndexError(f'Your array reached the limit. Your max index is: {self.__elements - 1}')
        
    def get_value(self,index):
        try : 
            return self.__content[index]
        except IndexError:
            raise IndexError(f'Index is out of range. Array\'s max index is {self.__elements-1}')
    
    @property
    def array(self):
        return self.__content

x = MyStaticArray(n=5)
x.append_value(50)
x.append_value(500)
x.append_value(150)
x.append_value(1550)
x.append_value(510)
# x.append_value(50)
print(x.array)
print(x.get_value(2))
print(x.get_value(10))