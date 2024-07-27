'''The Main Idea behind hashing that we pre allocate data into a specific key allocaotr in memory.
'''

class HashTable:
    def __init__(self,max) -> None:
        self.Max = max
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        
        return h % self.Max
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        if len(self.arr[h]) > 0:
            for i,element in enumerate(self.arr[h]):
                if element[0] == key:
                    self.arr[h][i] = (key,value)
                    return
        self.arr[h].append((key,value))

    def __getitem__(self,key):
        h = self.get_hash(key)
        if len(self.arr[h]) > 0:
            for i,element in enumerate(self.arr[h]):
                if element[0] == key:
                    return element[1]
        return 'Key Not Found!'
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        if len(self.arr[h]) > 0:
            for i,element in enumerate(self.arr[h]):
                if element[0] == key:
                    del self.arr[h][i]
                    print('Deleted')
                    return
        return 'Key Not Found!'


t = HashTable(5)
t['One'] = 1
t['march 6'] = 7
t['march 17'] = 10
# print(t['One'])
# print(t['Ho'])
# print(t['Seven'])

del t['One']
print(t.arr)