class Train:
    def __init__(self,train_name,compartment_list):
        self.train_name=train_name
        self.compartment_list=compartment_list
    def get_train_name(self):
        return self.name
    def  get_compartment_list(self):
        return self.compartment_list
    def count_compartments(self):
        return len(self.compat_list)
    def check_vacancy(self):
        return self.compartment_list.check()

class compartments:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.next=None
class SLinkedList:

    def __init__(self):
        self.head=None
    def insert_(self,listvalue):
        temp=self.head
        new_node=compartments(listvalue)
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node

    def print_compat(self):
        temp=self.head
        while temp is not None:
            print(temp.dataval)
            temp=temp.next
    def check(self):
        c=0
        temp=self.head
        while temp is not None:
            if(temp.dataval[1]<=temp.dataval[2]/2):
                c+=1
            temp=temp.next
        return c
    
c1=['SL',250,400]
c2=['2AC',125,280]
c3=['3AC',120,300]
c4=['FC',160,300]
c5=['1AC',106,210]

l=SLinkedList()
l.head=compartments(c1)
l.insert_(c2)
l.insert_(c3)
l.insert_(c4)
l.insert_(c5)

t=Train('rajyarani',l)
print(t.check_vacancy())
