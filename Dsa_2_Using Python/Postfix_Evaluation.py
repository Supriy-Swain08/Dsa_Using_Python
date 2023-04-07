class Evaluate:
    def  __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        self.array=[]
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if self.isEmpty():
            return '$'
        else:
            self.top-=1
            return self.array.pop()
    def push(self,value):
        self.top+=1
        self.array.append(value)
    def evaluate(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                d1=self.pop()
                d2=self.pop()
                self.push(str(eval(d2+i+d1)))
        return int(self.pop())
exp='231*+9-'
obj=Evaluate(len(exp))
print("answer:",obj.evaluate(exp))
