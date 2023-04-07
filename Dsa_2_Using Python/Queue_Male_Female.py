class People:
    def __init__(self,Name,Age,Gender):
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
    def return_List(self):
        return [self.Name,self.Age,self.Gender]
class Queue:
    def __init__(self,max_size):
        self.rear=-1
        self.front=0
        self.max_size=max_size
        self.elements=[None]*self.max_size
    def is_empty(self):
        if self.front>self.rear:
            return True
        return False
    def is_full(self):
        if self.rear==self.max_size-1:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print('Queue is Full')
        else:
            
            self.rear+=1
            self.elements[self.rear]=data
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            data=self.elements[self.front]
            self.front+=1
            return data
    def check(self,gender):
        for i in range(self.front,self.rear+1):
            if((self.elements[i])[2]==gender):
                print(self.elements[i])
            
q=Queue(4)
for i in range(0,int(input('Howmany People:'))):
    q.enqueue(People(input("Name:"),int(input('Age:')),input('Gender:')).return_List())
q.check(input())
