class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last=last.next

        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("Node")

    def delete(self,key):
        current = self.head

        if current and current.data ==key:
            self.head = current.next
            current =None
            return
        
        prv = None
        while current and current.data !=key:

            prv = current
            current =current.next
        
        if current is None:

            return
        
        prv.next =current.next
        current =None


li = LinkedList()

li.append(10)
li.append(20)
li.append(30)
li.display()
li.delete(20)
li.display()





