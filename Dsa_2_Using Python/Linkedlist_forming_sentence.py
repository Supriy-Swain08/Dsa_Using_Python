class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.next=None
class SLinkedList:
    def __init__(self):
        self.head=None

    def append_at_end(self,data):
        temp=self.head
        new_node=Node(data)
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        

    def print_lis(self):
        temp=self.head
        while temp is not None:
            print(temp.dataval)
            temp=temp.next

lis=['A','n','*','/','a','p','p','l','e','*','a','/','day','*','*','k','e','e','p',
     's','/','*','a','/','/','d','o','c','t','o','r','*','A','w','a','y']
link=SLinkedList()
link.head=Node('Hy')
for i in lis:
    link.append_at_end(i)
link.print_lis()
