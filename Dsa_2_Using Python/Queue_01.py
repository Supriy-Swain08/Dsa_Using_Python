'''class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if (self.__max_size)-1==self.__rear:
            return True
        return False

    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False

    def enqueue(self,data):
        if self.is_full():
            print("Queue is Full!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
            print("Data Entered Successfully!")

    def dequeue(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return str(data)+"Dequeued"


    def display(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            for index in range(self._front,self._rear+1):
                print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size
n=int(input("Enter Size of Queue:\n0 to Exit:\n"))
stk=Queue(n)
choice=1
while(choice):
    choice=int(input("1.Enqueue\n2.Dequeue\n3.Display\n4.Max Size\n5.Check If Empty\n6.Check If Full\n0.Exit\nEnter Your Choice:"))
    if choice==1:
        data=int(input("Enter Data to Enter:"))
        stk.enqueue(data)
    elif choice==2:
        print(stk.dequeue())
    elif choice==3:
        stk.display()
    elif choice==4:
        print(stk.get_max_size())
    elif choice==5:
        print(stk.is_empty())
    elif choice==6:
        print(stk.is_full())
    elif choice==0:
        print("Thanks for Using!")
        break
    else:
        print("Invalid Input")
        break
    print("----------------------------------------------------------------------------------")
'''
'''class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if (self.__max_size)-1==self.__rear:
            return True
        return False

    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False

    def enqueue(self,data):
        if self.is_full():
            print("Queue is Full!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
            #print("Data Entered Successfully!")
  
    def dequeue(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return str(data)+"Dequeued"


    def display(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            for index in range(self.__front,self.__rear+1):
                print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size
n=int(input("Enter size of the Queue:"))
child=Queue(n)
out=Queue(n)
for i in range(n):
    data=int(input())
    child.enqueue(data)
    for j in range(1,11):
        if(data%j !=0):
            break
    else:
        out.enqueue(data)
child.display()
out.display()
'''
#_________________________________________________________________________________________________________
'''lis1=input().split(",")
lis2=input().split(",")
lis3=lis2[::-1]
for i in range (0,len(lis1)):
    if(lis1[i]=='None' and lis3[i]=='None'):
        continue
    elif(lis1[i]=='None'):
        print(lis3[i],end="")
    elif(lis3[i]=='None'):
        print(lis1[i],end="")
    else:
        print(lis1[i]+lis3[i],end="")
    '''
#___________________________________________________________________________________________________________
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if (self.__max_size)-1==self.__rear:
            return True
        return False

    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False

    def enqueue(self,data):
        if self.is_full():
            print("Queue is Full!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
            #print("Data Entered Successfully!")
  
    def dequeue(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data


    def display(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            for index in range(self.__front,self.__rear+1):
                print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size
n=int(input("Enter size of the Queue1:"))
m=int(input("Enter size of the Queue2:"))
child=Queue(n)
child2=Queue(m)
out=Queue(n+m)
for i in range(n):
    data1=int(input("Enter the Integers:"))
    child.enqueue(data1)
for j in range(m):
    data2=input("Enter the characters:")
    child2.enqueue(data2)
minf=min(child.get_max_size(),child2.get_max_size())
af=child.get_max_size()
bf=child2.get_max_size()
if(af==minf):
    for x in range(0,af):
        print(11)
        out.enqueue(child.dequeue())
        out.enqueue(child2.dequeue())
    for y in range(af,m+n-af):
        print(22)
        out.enqueue(child2.dequeue())

out.display()
