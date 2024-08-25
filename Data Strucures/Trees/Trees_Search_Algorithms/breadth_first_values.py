from depth_first_search import Node

def breadth_first_values(root):
    if root == None:
        return []
    result = []
    queue = [root]

    while len(queue) > 0:
        current = queue.pop()
        result.append(current)
        if current.left : queue.insert(0,current.left)
        if current.right : queue.insert(0,current.right)

    return result

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
    
    print(breadth_first_values(a))