def Linearsearch(array,n,x):
    for i in range(0,n):
        if (array[i]==x):
            return i
    return -1
lis=list(map(int,input('Enter The Numbers For List:').split()))
num=int(input("Number To search:"))
if(Linearsearch(lis,len(lis),num)==-1):
    print('Item not found')
else:
    print('Item found at:',Linearsearch(lis,len(lis),num)+1)
