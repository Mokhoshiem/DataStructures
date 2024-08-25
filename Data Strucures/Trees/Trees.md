# Binary Tree:
A Binary Tree is a type of tree data structure in which each node has at most two children, referred to as the left child and the right child. This distinguishes it from trees in which nodes can have any number of children. A binary tree is further classified as a strictly binary tree if every non-leaf node in the tree has non-empty left and right child nodes. A binary tree is complete if all levels of the tree, except possibly the last, are fully filled, and all nodes are as left-justified as possible. Multiple algorithms and functions employ binary trees due to their suitable properties for mathematical operations and data organization.
- Has one Root: The root is the node with no parents.
- At most two children per node.
- Exactly one path between the Root and any node.

### Singleto tree is the tree of just one node.
### An empty tree is also a binary tree.







# Depth First Search
Depth First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. The process starts at the root (in the case of a tree) or an arbitrary node (in case of a graph), and explores as far as possible along each branch before retracing steps. Essentially, DFS is about diving deep into the tree/graph from a starting point, and when no more nodes are left to explore, it backtracks, moving up the tree/graph. This repeat until all nodes have been visited. This algorithm is often used in simulation of game states, solving puzzles and finding connected components in a graph.
# Breadth First Search
Breadth-First Search (BFS) is a searching algorithm that’s used in tree or graph data structures. It starts from the root (the topmost node in the tree) and expands all neighboring nodes at the present depth prior to moving on to nodes at the next depth level. This technique uses a queue data structure to remember to explore the next vertex or node and every edge that leads to a vertex will be explored, which ensures the discovery of every vertex reachable from the source. BFS is complete in nature, which means if the searched node is in the tree, BFS is guaranteed to find it.