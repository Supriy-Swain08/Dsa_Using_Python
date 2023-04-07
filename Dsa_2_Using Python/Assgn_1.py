'''marks=[89,78,99,76,77,67,99,98,90]
marks.insert(8,78)
print(marks)
print(marks[4],marks[6])'''
#2-----------------------------------------------
'''lis=list(map(int,input("Elements Of 1st list:").split()))
lis2=list(map(int,input("Elements of 2nd List:").split()))
for i in lis:
    if 2*i in lis2:
        print(i)
'''
#3------------------------------------------------
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.next=None
class SLinkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        eapend=Node(data)
        if self.head is None:
            self.head=eapend()
            return
        last=self.head
        while(last.next):
            last=last.next
        last.nextval=eapend

List=SLinkedlist()
for i 
