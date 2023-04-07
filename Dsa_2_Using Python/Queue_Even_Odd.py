class Queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.elements=[None]*self.max_size
        self.front=0
        self.rear=-1
    def is_full(self):
        if self.rear==self.max_size-1:
            return True
        return False
    def is_empty(self):
        if self.front>self.rear:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print('Queue is Full')
        self.rear+=1
        self.elements[self.rear]=data
    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
        d=self.elements[self.front]
        self.front+=1
        return int(d)

    def display(self):
        for index in range(self.front,self.rear+1):
            print(self.elements[index],end='')

q=Queue(7)
e=Queue(7)
o=Queue(7)
for i in range(0,7):
    q.enqueue(int(input()))
for i in range(0,7):
    data=q.dequeue()
    if(data%2==0):
        e.enqueue(data)
    else:
        o.enqueue(data)
e.display()
print()
o.display()

