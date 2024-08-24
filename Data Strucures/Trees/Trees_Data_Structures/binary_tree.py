class Node:
    def __init__(self,val):
        self.value = val
        self.right = None
        self.left = None
        
    def __repr__(self) -> str:
        return self.value

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(a.right)
