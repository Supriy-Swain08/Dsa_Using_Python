def rotation(num):
    str1=str(num)
    size=len(str1)
    lis=[]
    for i in range(0,size):
        data=str1[1:]+str1[0]
        lis.append(int(data))
        str1=data
    return lis
def is_prime(value):
    
    for i in range(2,value):
        if value%i==0:
            return False
        return True
    
r=int(input())
for m in range(2,r):
    a=rotation(m)
    c=0
    for i in a:
        if is_prime(i)==True:
            c+=1
        if c==len(a):
            print(m)
        else:
            pass
