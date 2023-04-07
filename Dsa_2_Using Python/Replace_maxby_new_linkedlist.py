class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.next=None
class SLinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
    def find_max(self):
        temp=self.head
        maximum=temp.dataval
        while temp is not None:
            if (temp.dataval) >= maximum:
                maximum_add=temp
                maximum=temp.dataval
                temp=temp.next
            elif temp.dataval<maximum :
                temp=temp.next
        return maximum_add
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.dataval,end='->')
            temp=temp.next
            
l=SLinkedList()
l.head=Node(12)
l2=SLinkedList()
l2.head=Node(12)
l.insert(95)
l.insert(140)
l.insert(110)
l.insert(40)

l2.insert(95)
l2.insert(150)
l2.insert(110)
l2.insert(40)

l.display()
print()
l2.display()
print()

l.find_max().dataval=l2.find_max().dataval
l.display()
