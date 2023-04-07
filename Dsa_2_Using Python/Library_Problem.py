class Library:
    def __init__(self,item_list):
        self.item_list=item_list
    def get_item_list(self):
        pass
    def sort_item_list_by_author(self,new_item_list):
        pass
    def add_new_items(self,new_item_list):
        self.item_list.insert(new_item_list)
    def sort_items_by_published_year(self):
        pass

class item:
    def __init__(self,item_name,author_name,published_year):
        self.item_name=item_name
        self.author_name=author_name
        self.published_year=published_year
    def get_item_name(self):
        return self.item_name
    def get_author_name(self):
        return self.author_name
    def get_published_year(self):
        return self.published_year

class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.next=None
class SLinkedList:
    def __init__(self):
        self.head=None
    def print_(self):
        temp=self.head
        while temp is not None:
            print(temp.dataval)
            temp=temp.next
    def insert(self,value):
        temp=self.head
        new_node=Node(value)
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node

i1=item('HarryPotter','J.K.Rolling',1900)
i2=item('Physics','SL Arora',2002)
i3=item('Chemistry','KP',2002)
i4=item('Mamu','FakirMohan',1950)
i5=item('Math','RD Sharma',2002)

l=SLinkedList()
l.head=Node([i1.get_item_name(),i1.get_author_name(),i1.get_published_year()])
l.insert([i2.get_item_name(),i2.get_author_name(),i2.get_published_year()])
l.insert([i3.get_item_name(),i3.get_author_name(),i3.get_published_year()])
l.insert([i4.get_item_name(),i4.get_author_name(),i4.get_published_year()])
l.insert([i5.get_item_name(),i5.get_author_name(),i5.get_published_year()])
l.print_()

library=Library(l)
a=input('New Book Name:')
b=input('Author name:')
c=int(input('Published Year:'))
library.add_new_items([a,b,c])
l.print_()
