class Node:

    def __init__(self,data):
        self.data
        self.next =None
        self.prev =Node


class DoublyLinkedList:

    def __init__(self):
        self.head =None

    def append(self, data):

        new_node = Node(data)
        if not self.head:
            self.head =new_node
            return
        
        last =self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev =last


    def display(self):

        current = self.head
        while current:
            print(current.data)
            current =current.next
        print("None")

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()  