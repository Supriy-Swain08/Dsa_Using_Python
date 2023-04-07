
def Find_new(text,vocabulary):
    l=[]
    for i in text:
        if i not in vocabulary:
            l.append(i)
    return set(l)
text=input().split()
vocabulary=input().split(',')
print(sorted(list(Find_new(text,vocabulary))))
