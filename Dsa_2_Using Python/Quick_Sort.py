def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    array[i+1],array[high]=array[high],array[i+1]
    return i+1
def quicksort(arr,low,high):
    if low<high:
        index=partition(arr,low,high)
        quicksort(arr,low,index-1)
        quicksort(arr,index+1,high)
data=[19,17,15,12,16,8,4,11,13]
h=len(data)-1
quicksort(data,0,h)
print(data)
