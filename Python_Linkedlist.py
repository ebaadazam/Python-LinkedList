#DATA STRUCTURE AND ALGORITHM IN PYTHON

#Singly Linked list
class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True

    def insert_at_end(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node  # point head to new node if it is empty
            count = 1
            print(count, 'Node has been inserted!')
        else:
            count = 1
            count += 1
            temp = self.head   # initialize temp with head
            while temp.link != None:
                temp = temp.link
                count += 1
            temp.link = new_node   # put the new node in the link part of the last node
            print(count, 'Node has been inserted!')



    def insert_at_loc(self, loc, item):
        count = 1
        new_node = Node(item)
        temp = self.head
        while count != loc:
            temp = temp.link
            count += 1
        new_node.link = temp.link
        temp.link = new_node


    def insert_at_begin(self, item):
        new_node = Node(item)
        new_node.link = self.head
        self.head = new_node  # self.head is pointing to new Node
        print(new_node.data, 'valued Node inserted at the beginning!')
        return ''

    def pop(self):
        if self.head.link == None:  # means there is no element after the first element, there is only 1 elem
            del head
        else:
            temp = self.head
            while temp.link.link != None:
                temp = temp.link
            del temp.link
            temp.link = None

    def pop_front(self):
        temp = self.head
        self.head = self.head.link
        del temp

    def pop_at_loc(self, loc):
        count = 0
        if self.head == None:  # means if the list is empty
            return None
        if loc == 0:
            return obj.pop_front()
        temp = self.head
        while count != loc:
            temp = temp.link
            count += 1
        temp2 = temp.link
        temp.link = temp2.link
        del temp2

    def display_node(self):
        temp = self.head  # initialize temp with head
        print('Linked List elements are:')
        while temp.link != None:
            print(temp.data)
            temp = temp.link
        print(temp.data)
        return ''

obj = SinglyLinkedList()
obj.insert_at_end(100)
obj.insert_at_end(300)
obj.insert_at_end(500)
obj.insert_at_end(700)
obj.insert_at_end(900)
print(obj.display_node())

# obj.pop()
# print(obj.display_node())
#
# obj.insert_at_begin(50)
# print(obj.display_node())
#
# obj.insert_at_loc(3, 350)
# print(obj.display_node())
#
# obj.pop_at_loc(4)
# print(obj.display_node())



#Doubly Linked List
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # points to the first node
        self.tail = None  # points to the last node, made it for the purpose of reversing the list

    def is_empty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        self.tail = new_node  # by default tail will be pointing to the first node i.e, new_node and if another element is inserted then tail will point to that
        if self.is_empty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            new_node.prev = temp
            temp.next = new_node


    def prepend(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        print('Node has been inserted at the beginning of the linked list!')


    def append_at_loc(self, loc, item):
        new_node = Node(item)
        if loc == 0:
            return doublyll.prepend(item)
        else:
            temp = self.head
            count = 1
            while count != loc:
                temp = temp.next
                count += 1
            new_node.next = temp.next
            temp.next = new_node
            new_node.prev = temp
            if new_node.next is not None:
                new_node.next.prev = new_node


    def pop(self):
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        del temp.next
        temp.next = None

    def pop_front(self):
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        del temp


    def pop_at_loc(self, loc):
        count = 0
        if self.head == None:
            return None
        if loc == 0:
            return doublyll.pop_front()
        temp = self.head
        while count != loc:
            temp = temp.next
            count += 1
        temp.prev.next = temp.next
        temp.next = temp.prev
        del temp



    def display(self):
        temp = self.head
        print("Doubly Linked List elements are: ")
        while temp.next != None:
            print(temp.data)
            temp = temp.next
        print(temp.data)
        return ''

    def display_reverse(self):
        temp = self.tail
        print("Doubly Linked List elements but in reverse order: ")
        while temp.prev != None:
            print(temp.data)
            temp = temp.prev
        print(temp.data)
        return ''

doublyll = DoublyLinkedList()
doublyll.append(10)
doublyll.append(20)
doublyll.append(30)
doublyll.append(40)
doublyll.append(50)

# Displaying the list after appending all the items
print(doublyll.display())

# Displaying the list in reverse order using tail attribute which by default contains the last node
print(doublyll.display_reverse())

doublyll.pop_at_loc(3)
print(doublyll.display())