from depth_first_search import Node
import math

def find_min_BF(root=None):
    queue = [root]
    if root is None: return None

    result = root.value
    while len(queue) > 0:
        current = queue.pop()
        if current.value < result :
            result = current.value
        if current.left : queue.insert(0,current.left)
        if current.right : queue.insert(0,current.right)

    return result

def find_min_DF(root=None):
    if root is None : return None
    result = root.value
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        if current.value < result:
            result = current.value
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return result


if __name__ == '__main__':
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(2)
    f = Node(50)
    

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    # print(find_min_BF(a))
    print(find_min_DF(a))