# Data Structures:
Data Structures are a fundamental element of computer science. They provide a specific way to organize and store data so that it can be accessed and used efficiently. Different types of data structures include arrays, linked lists, stacks, queues, hash tables, trees, and graphs. Each of these has its unique characteristics and use-cases, and is optimal for certain kinds of operations. For example, arrays are excellent for random access, while linked lists work well for frequent insertions and deletions. The correct choice of data structure can significantly enhance the performance of your programs.

# Basic Data Structures:
## Array:
* An array is a linear data structure that can hold elements and arrange them. It uses contiguous memory space to store elements. In an array, we can directly access any element based on its index which makes it an efficient data structure. Arrays have two types: one-dimensional and multi-dimensional. In a one-dimensional array, data is stored in a linear form while a multi-dimensional array can store data in the form of a matrix or in 3-D format.
## Stack:
* A stack is a linear data structure that follows a particular order in which the operations are performed. The order may be LIFO (Last In First Out) or FILO (First In Last Out). Mainly three basic operations are performed in the stack:

- Push: adds an element to the collection.

- Pop: removes an element from the collection. A pop can result in stack underflow if the stack is empty.

- Peek or Top: returns the top item without removing it from the stack.

* The basic principle of stack operation is that in a stack, the element that is added last is the first one to come off, thus the name “Last in First Out”.
# Queues:
* Queues are a type of data structure in which elements are held in a sequence and access is restricted to one end. Elements are added (“enqueued”) at the rear end and removed (“dequeued”) from the front. This makes queues a First-In, First-Out (FIFO) data structure. This type of organization is particularly useful for specific situations such as printing jobs, handling requests in a web server, scheduling tasks in a system, etc. Due to its FIFO property, once a new element is inserted into the queue, all elements that were inserted before the new element must be removed before the new element can be invoked. The fundamental operations associated with queues include Enqueue (insert), Dequeue (remove) and Peek (get the top element).
# Linked Lists:
* Linked Lists are a type of data structure used for storing collections of data. The data is stored in nodes, each of which contains a data field and a reference (link) to the next node in the sequence. Structurally, a linked list is organized into a sequence or chain of nodes, hence the name. Two types of linked lists are commonly used: singly linked lists, where each node points to the next node and the last node points to null, and doubly linked lists, where each node has two links, one to the previous node and another one to the next. Linked Lists are used in other types of data structures like stacks and queues.
# Hash Tables:
* Hash Tables are specialized data structures that allow fast access to data based on a key. Essentially, a hash table works by taking a key input, and then computes an index into an array in which the desired value can be found. It uses a hash function to calculate this index. Suppose the elements are integers and the hash function returns the value at the unit’s place. If the given key is 22, it will check the value at index 2. Collisions occur when the hash function returns the same output for two different inputs. There are different methods to handle these collisions such as chaining and open addressing.