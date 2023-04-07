class Node:
    def __init__(self,dataval):
        self.prev=None
        self.dataval=dataval
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_at_beginning(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

    def insert_at_end(self,value):
        new_node=Node(value)
        if x.isEmpty():
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp

    def insert_at_position(self,value,position):
            temp=self.head
            count=1
            while temp is not None:
                if count==position :
                    break
                count+=1
                temp=temp.next
            if position==1:
                self.insert_at_beginning(value)
            elif temp is None:
                print('No such Position')
            elif temp.next is None:
                self.insert_at_end(value)
            else:
                new_node=Node(value)
                new_node.next=temp
                new_node.prev=temp.prev
                temp.prev.next=new_node
                temp.prev=new_node

    def delete_from_first(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None
    def delete_from_position(self,pos):
        temp=self.head
        if self.isEmpty():
            print("No element To delete")
        elif pos==1:
            self.delete_from_first()
        else:
            count=1
            while temp is not None:
                if count==pos:
                    break
                temp=temp.next
                count+=1
            if temp.next is None:
                self.delete_from_last()
            elif temp is None:
                print('No such Position')
            else:
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
                temp.prev=None
                temp.next=None
        
    def delete_from_last(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.prev.next=None
        temp.prev=None
                
                     
    def print_linked_list(self):
        first=self.head
        while first is not None:
            print(first.dataval)
            first=first.next

x=DoublyLinkedList()
print(x.isEmpty())
x.insert_at_beginning(10)
x.insert_at_beginning(20)
x.insert_at_beginning(30)
x.insert_at_beginning(40)
x.print_linked_list()
print('At end:')
x.insert_at_end(100)
x.insert_at_end(90)
x.insert_at_end(80)
x.insert_at_end(70)
x.print_linked_list()
print('At Position:')
x.insert_at_position(1000,4)
x.print_linked_list()
print('After Deleting from end')
x.delete_from_last()
x.print_linked_list()
print('After Deleting from start')
x.delete_from_first()
x.print_linked_list()
print('After Deleting from position:2')
x.delete_from_position(4)
x.print_linked_list()
