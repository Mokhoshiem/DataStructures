from collections import deque

class Queue:
    def __init__(self) -> None:
        self.__queue = deque()

    def enque(self,value):
        self.__queue.appendleft(value)
    
    def deque(self):
        self.__queue.pop()

    @property
    def peek(self):
        peek = None
        if self.size > 0:
            peek = self.__queue[-1]
        
        return peek
    
    @property
    def size(self):
        return len(self.__queue)

    def empty(self):
        return len(self.__queue) == 0
    
    def __repr__(self) -> str:
        return str(self.__queue)
    
