class BakeHouse:
    def __init__(self,occupied_table_list):
        self.occupied_table_list=occupied_table_list
    def get_occupied_table_list(self):
        temp=self.occupied_table_list.head
        while temp is not None:
            if temp.dataval[1]==True:
                print(temp.dataval[0])
                temp=temp.next
            else:
                temp=temp.next
    def allocate_table(self):
        temp=self.occupied_table_list.head
        while temp is not None:
            if temp.dataval[1]==False:
                print('occupied seat is: ')
                print(temp.dataval[0])
                break
            else:
                temp=temp.next
                
    def deallocate_table(self,table_number):
        temp=self.occupied_table_list.head
        while temp is not None:
            if temp.dataval[0]==table_number:
                temp.dataval[1]=False
                print(table_number,'is Deallocated')
                break
            else:
                temp=temp.next

            
class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.next=None
class SLinkedList:
    def __init__(self):
        self.head=None
    def insert_(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node

s=SLinkedList()
s.head=Node([1,True])
s.insert_([2,True])
s.insert_([3,True])
s.insert_([4,True])
s.insert_([5,False])
s.insert_([6,False])
s.insert_([7,False])
s.insert_([8,False])
s.insert_([9,False])
s.insert_([10,False])
t=BakeHouse(s)
t.get_occupied_table_list()
t.allocate_table()
t.deallocate_table(2)
print('After Deallocating:')
t.get_occupied_table_list()
