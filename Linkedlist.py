class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.nxt:
            itr = itr.nxt
        itr.nxt = Node(data, None)
        
    def insert_values(self, values):
        self.head = None
        for v in values:
            self.insert_at_end(v)

    
    def get_length(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.nxt
        return count
    

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Index out of range')
        
        if index == 0:
            self.head = self.head.nxt

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.nxt = itr.nxt.nxt
                break
            count += 1
            itr = itr.nxt

    def insert_at(self, index, value):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of range")
        if index == 0:
            self.insert_at_beginning(value)

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(value, itr.nxt)
                itr.nxt = node
                break
            itr = itr.nxt
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            print(f"This {data_after} is not found\nLinkedList is empty")

        found = False
        if self.head.data == data_after:
            node = Node(data_to_insert, self.head.nxt.nxt)
            found = True
            self.head.nxt = node
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.nxt)
                found = True
                itr.nxt = node
            itr = itr.nxt

        if not found:
            print("Given data was not found")
        


    def print(self):
        if self.head is None:
            print("Linkedlist is empty")
            return
        itr = self.head
        itr_val = ""
        while itr:
            itr_val += str(itr.data) + " -> "
            itr = itr.nxt
            
        print(itr_val[:-4])




tmp = LinkedList()
tmp.insert_at_beginning(5)
tmp.insert_at_beginning(4)
tmp.insert_at_beginning(3)
tmp.insert_at_beginning(2)
tmp.insert_at_beginning(1)
tmp.insert_at_end(1997)
tmp.print()


values = ["apple", "Banana", "Orange", "Mango","Chocolate",]

ll = LinkedList()
ll.insert_values(values)
ll.print()
length = ll.get_length()
print(length)
# ll.remove_at(3)
# ll.remove_at(0)
# ll.print()
ll. insert_at(2, "Drinks")
ll.print()
ll.insert_after_value("Drink", "Milk")
ll.insert_after_value("Banana", "Water")
ll.print()
