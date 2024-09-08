from depth_first_search import Node

# Given a binary tree use both DFS and BFS to find if the target value is in the tree or not.

# implementing DFS

def depth_first_search(root,target):
    if root == None or target == None:
        return False
    
    result = False
    stack = [root]
    while len(stack) > 0:
        top = stack.pop()
        # print(top)
        if top.value == target:
            result = True
            break
        if top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)
    return result


def breadth_first_search(root,target):
    if root == None or target == None:
        return False
    queue = [root]

    while len(queue) > 0:
        current = queue.pop()
        # print(current)
        if current.value == target:
            return True
        if current.left:
            queue.insert(0,current.left)
        if current.right:
            queue.insert(0,current.right)
    
    return False

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
    
    print(depth_first_search(a,'a'))
    print(breadth_first_search(a,'a'))
