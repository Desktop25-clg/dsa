class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def print_ll(self):
        if self.head is None:
            print("Empty List")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, "-> ", end="")
                temp = temp.next
            print("None")

    def view_length(self):
        return self.length

    # Insertion
    def insert_end(self, data):
        if self.head == None:
            self.head = Node(data)
            self.length += 1
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)  # type: ignore
            self.length += 1

    def insert_begin(self, data):
        if self.head == None:
            self.head = Node(data)
            self.length += 1
        else:
            new_node = Node(data)
            new_node.next = self.head  # type: ignore
            self.head = new_node
            self.length += 1

    def insert_at_postion(self, data, position):
        if self.head is None:
            self.head = Node(data)
            self.length += 1
        elif position <= self.length:
            temp = self.head
            new_node = Node(data)
            for i in range(position-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
        else:
            print("The Give Positon is out of the index")

    # Deletion
    def delete_begin(self):
        if self.head == None:
            return self.head
        elif self.length == 1:
            self.head = None
            self.length -= 1
            return self.head
        else:
            self.head = self.head.next
            self.length -= 1
            return self.head

    def delete_end(self):
        if self.head == None:
            return self.head
        elif self.length == 1:
            self.head = None
            self.length -= 1
            return self.head
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
            self.length -= 1
            return self.head

    def delete_at_position(self, position):
        if self.head == None:
            return self.head
        elif self.length == 1:
            self.length -= 1
            self.head = None
            return self.head
        elif position >= 0 and position < self.length:
            temp = self.head
            for loop in range(position-1):
                temp = temp.next
            temp.next = temp.next.next
            self.length -= 1
            return self.head
        else:
            print("Position out of index")

    # Reversing the list iteratively
    def reverse_ll(self):
        if self.head is None:
            return "Linked List is Empty"
        reverse = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = reverse
            reverse = temp
            temp = next_node

        self.head = reverse
