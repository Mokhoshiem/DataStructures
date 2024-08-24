class Node:
    def __init__(self,val):
        self.value = val
        self.right = None
        self.left = None
        
    def __repr__(self) -> str:
        return self.value

def depth_first_values(root)->list:
    stack = [root]
    path = []
    while len(stack) > 0:
        current = stack.pop()
        path.append(current)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return path


if __name__ == '__main__':
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

    print(depth_first_values(a))