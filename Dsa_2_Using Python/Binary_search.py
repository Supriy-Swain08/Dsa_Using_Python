def Binarysearch(array,x,low,high):
    while low <= high:
        mid=low+(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return -1
lis=list(map(int,input('Enter list elements:').split()))
n=int(input('Element to search:'))
result=Binarysearch(lis,n,0,len(lis)-1)
if(result==-1):
    print('Item not found')
else:
    print('Item found at:',result+1)
