def selection_sort(array,size):
    for step in range(size):
        min_index=step
        for i in range(step+1,size):
            if array[i]<array[min_index]:
                min_index=i
        (array[step],array[min_index])=(array[min_index],array[step])
data=[20,12,10,15,2]
size=len(data)
selection_sort(data,size)
print(data)
