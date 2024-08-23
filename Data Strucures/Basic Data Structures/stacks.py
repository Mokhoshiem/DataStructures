# A stack is a linear data structure that follows a particular order in which the operations are performed.
# The order may be LIFO.
# Mainly there are 3 operations to be done with the stack:
#  - push : adds an element on top of the stack.
#  - pop : removes the top element of the stack.
#  - peek: gets the top element without removing it.

class Stack:
    def __init__(self,stack=[]):
        self.__items = list(stack) if stack != [] else stack
        self.__top = None
    
    def push(self,element):
        self.__items.append(element)
        self.__top = 0 if self.__top is None else self.__top + 1 

    def pop(self):
        self.__items.remove(self.__items[self.__top]) if self.__top is not None else None
        self.__top = None if self.__top == 0 or self.__top == None else self.__top - 1
    
    @property
    def top(self):
        # return self.__top
        return self.__items[self.__top] if self.__top is not None else None
    @property
    def stack(self):
        return False if self.__top is None else True

my_stack = Stack()
print(my_stack.stack)
print(my_stack.top)
my_stack.push(10)
print(my_stack.top)
my_stack.push(100)
print(my_stack.top)
my_stack.push(1000)
print(my_stack.top)
my_stack.push(10000)
print(my_stack.stack)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack.top)
print(my_stack.stack)