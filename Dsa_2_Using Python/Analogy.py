def check_anagram(str1,str2):
    c=0
    for i in str1:
        if i!=" " and i in str2:
            if str1.index(i)!=str2.index(i):
                c+=1
            elif str1.index(i)=str2.index(i):
                return False
    if c>0:
        return True
str1=input()
str2=input()
print(check_anagram(str1,str2))
