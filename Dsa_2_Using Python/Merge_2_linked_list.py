class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.next=None
class SLinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        temp=self.head
        new_node=Node(data)
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
    def getsize(self):
        temp=self.head
        c=1
        if temp is not None:
            c+=1
            temp=temp.next
            
        return c+1
def display(l,l2,n):
    temp=l.head
    temp2=l2.head
    c=0
    while temp is not None or temp2 is not None:
        if c<n or c>=(l2.getsize()+n):
            print(temp.dataval,end='->')
            temp=temp.next
            c+=1
        
        else:
            print(temp2.dataval,end='->')
            temp2=temp2.next
            c+=1            
    
l=SLinkedList()
l2=SLinkedList()

l.head=Node(1)
l2.head=Node(9)

l.insert(2)
l.insert(4)
l.insert(3)
l.insert(5)

l2.insert(8)
l2.insert(11)

n=int(input('Enter the merge Position:'))
display(l,l2,n)




