from depth_first_search import Node

def sum_binary(root=None):
    '''Depth First Algorithm that works recursively
    '''
    if root is None:
        return 0
    lefts = sum_binary(root.left)
    rights = sum_binary(root.right)

    return root.value + lefts + rights

def sum_binary_BF(root=None):
    '''Breadth First Algorithm that works iteratively
    '''
    result = 0
    queue = [root]

    if root is None: return 0
    while len(queue) > 0:
        current = queue.pop()
        result += current.value
        if current.left:queue.insert(0,current.left)
        if current.right:queue.insert(0,current.right)
    
    return result

if __name__ == '__main__':
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(sum_binary(c))
    print(sum_binary_BF(b))