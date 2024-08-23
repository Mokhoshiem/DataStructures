import json

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self) -> str:
        dic = {'data':self.data,'next':self.next if self.next else None}
        return json.dumps(dic)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_to_beginning(self, data):
        """Adds a node with the specified data to the beginning of the linked list."""
        node = Node(data, self.head)
        self.head = node
    
    def add_to_end(self, data):
        """Adds a node with the specified data to the end of the linked list."""
        if self.head is None:
            self.add_to_beginning(data)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def add_from_iter(self, data_list):
        """Adds multiple nodes from an iterable to the end of the linked list."""
        for data in data_list:
            self.add_to_end(data)
    
    def add_at(self, index, data):
        """Adds a node with the specified data at the given index."""
        if index < 0 or index >= self.get_length():
            raise Exception('Index Out Of Range!')
        
        if index == 0:
            self.add_to_beginning(data)
            return

        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def remove_at(self, index):
        """Removes the node at the given index."""
        if index < 0 or index >= self.get_length():
            raise Exception('Index Out Of Range!')
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def add_after_value(self,searchValue,data):
        """Inserts a value after specified value returns 1 if true and 0 if false"""
        itr = self.head
        status = 0
        while itr.next:
            if itr.data == searchValue:
                node = Node(data,itr.next)
                itr.next = node
                status = 1
                break
            itr = itr.next
        return status
    
    def remove_after_value(self,searchValue):
        """Removes a value after specified value returns 1 if true and 0 if false"""
        itr = self.head
        status = 0
        while itr.next:
            if itr.data == searchValue:
                itr.next = itr.next.next
                status = 1
                break
            itr = itr.next
        return status

        
    def print(self):
        """Prints the linked list in a readable format."""
        if self.head is None:
            print('Linked List is Empty!')
            return

        listStr = ''
        itr = self.head
        while itr:
            listStr += f' {itr.data} -->'
            itr = itr.next
        
        return listStr
    
    def get_length(self) -> int:
        """Returns the length of the linked list."""
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

class DoublyNode:
    def __init__(self, data=None, next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        dic = {'data':self.data,'next':self.next.data if self.next else None,'prev':self.prev.data if self.prev else None}
        return json.dumps(dic)

class DoublyLinkedList:
    NODES = []

    def __init__(self):
        self.head = None
    
    def add_to_beginning(self,data):
        if self.head is None:
            node = DoublyNode(data=data,next=self.head,prev=None)
            self.head = node
            DoublyLinkedList.NODES.insert(0,node)
            return
        
        node = DoublyNode(data=data,next=self.head,prev=None)
        self.head.prev = node
        if self.head.next:
            self.head.next.prev = self.head
        
        self.head = node
        DoublyLinkedList.NODES.insert(0,node)
        return
    
    def add_to_end(self,data):
        if self.head is None:
            self.add_to_beginning(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node = DoublyNode(data=data,next=None,prev=itr)
        itr.next = node
        DoublyLinkedList.NODES.append(node)

    def print_forward(self):
        if self.head is None:
            return 'Linked List is Empty'
        
        listStr = ''
        itr = self.head
        while itr:
            listStr += f' {itr.data} -->'
            itr = itr.next

        return listStr
    
    def add_at_index(self,index,data):
        status = 0
        if index < 0 or index >= self.get_length():
            raise Exception('Index Out Of Range')
        
        if index == 0:
            self.add_to_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = DoublyNode(data=data,prev=itr,next=itr.next)
                itr.next.prev = node if itr.next else None
                itr.next = node
                status = 1
                DoublyLinkedList.NODES.insert(index,node)
                break
            
            itr = itr.next
            count += 1
        return status

    def remove_at(self,index):
        status = 0
        if index < 0 or index >= self.get_length():
            raise Exception('Index Out Of Range')
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            status = 1
            DoublyLinkedList.NODES.pop(index)
            return status
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                if itr.next.next:
                    itr.next.next.prev = itr
                itr.next = itr.next.next
                status = 1
                DoublyLinkedList.NODES.pop(index)
                break
            itr = itr.next
            count += 1
        return status

    def print_backward(self):
        if self.head is None:
            return 'Linked List is Empty'
        
        listStr = []
        itr = self.head
        while itr:
            listStr.append(itr.data)
            itr = itr.next

        result_string = ''
        for data in reversed(listStr):
            result_string += f' <- {data}'
        return result_string
    
    def get_length(self):
        if self.head is None:
            return 0
        
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def add_from_iterable(self,list):
        status = 0
        for l in list:
            self.add_to_end(l)
            status = 1
        return status
    
    def insert_after_value(self,searchValue,value):
        status = 0
        itr = self.head
        while itr:
            if itr.data == searchValue:
                node = DoublyNode(data=value,prev=itr,next=itr.next)
                if itr.next:
                    itr.next.prev = node
                try:
                    idx = DoublyLinkedList.NODES.index(itr)
                    DoublyLinkedList.NODES.insert(idx+1,node)
                except Exception as e:
                    print(e)
                itr.next = node
                status = 1
            itr = itr.next
        return status
    
    def remove_after_value(self,searchValue):
        status = 0
        itr = self.head
        while itr:
            if itr.data == searchValue:
                if itr.next.next:
                    itr.next.next.prev = itr
                
                itr.next = itr.next.next
                try:
                    idx = DoublyLinkedList.NODES.index(itr)
                    DoublyLinkedList.NODES.pop(idx+1)
                except Exception as e:
                    print(e)
                status = 1

            itr = itr.next
        return status