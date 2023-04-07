#store the address of first node in HeadNode
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinkedlist:
    def __init__(self):
        self.headval=None #Here headval is the reference variable acts as the pointer to next

    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    def atbeginning(self,newdata):
        enew=Node(newdata)
        enew.nextval=self.headval
        self.headval=enew
        
    def atend(self,endNew):
        eendNew=Node(endNew)
        if self.headval is None:
            self.headval=eendNew
            return
        laste=self.headval
        while(laste.nextval):
            laste=laste.nextval
        laste.nextval=eendNew

    def atPosition(self,count,data3):
        epos=Node(data3)
        mid=self.headval
        c=1
        while(c!=count and mid is not None):
            mid=mid.nextval
            c+=1
        mid2=mid.nextval
        mid.nextval=epos
        epos.nextval=mid2
    def delete_at_start(self):
        if self.headval is None:
            print("There is no element to delete")
            return
        self.headval=self.headval.nextval
    def delete_at_end(self):
        if self.headval is None:
            print("There is no element in the LinkedList")
            return
        n=self.headval
        while n.nextval.nextval is not None:
            n=n.nextval
        n.nextval=None
    def delete_by_value(self,ddata):
        if self.headval is None:
            print("list is Empty")
            return
        if self.headval.dataval==ddata:
            self.headval==self.headval.nextval
            return
        m=self.headval
        while m.nextval is not None:
            if m.nextval.dataval==ddata:
                m.nextval=m.nextval.nextval
                return
            m=m.nextval
    def reavlist(self):
        pass       
            
                

List=SLinkedlist()
List.headval=Node("Mon")
#print(List.headval)
e2=Node("Tue")
e3=Node("Wed")
List.headval.nextval=e2
e2.nextval=e3
List.atbeginning('Sun')
print('After Inserting In front')
List.listprint()
List.atend('Thu')
print('After Inserting in End')
List.listprint()
print('After Inserting At an Position')
List.atPosition(int(input()),'10')
List.listprint()
print('\n',"After Deletion")
'''List.delete_at_start()
List.delete_at_end()'''
List.delete_by_value('10')
List.listprint()
