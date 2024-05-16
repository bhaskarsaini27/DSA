class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.lenght += 1
        return True
    
    def pop(self):
        if self.lenght == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.lenght -= 1
        if self.lenght == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def get(self, index):
        if index < 0 or index >= self.lenght:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.lenght:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.lenght:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.lenght += 1
        return True
            
my_lineked_list = LinkedList(11)
my_lineked_list.append(3)
my_lineked_list.append(23)
my_lineked_list.append(7)

print("Before Insert \n")
my_lineked_list.print_list()

print("After Insert \n")
my_lineked_list.insert(2,15)
my_lineked_list.print_list()

print("Again Insert \n")
my_lineked_list.insert(2,17)
my_lineked_list.print_list()