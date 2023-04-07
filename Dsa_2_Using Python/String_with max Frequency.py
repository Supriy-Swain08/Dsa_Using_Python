text=input('Enter The Text Separated By a Space:').split()
text2=[]
res=[]
count=0
length=0
result=[]
for i in text:
    text2.append(i.upper())
for string in text2:
    a=text2.count(string)
    if a>=count:
        count=a
for string in text2:
    if text2.count(string)==count:
        res.append(string)
for j in res:
    if len(j)>=length:
        length=len(j)
        result=j
        
print(j)
        
