'''string made of the first 2 and last 2 characters of a given string'''
string=input()
l=len(string)
newstr=""
for i in range(0,len(string)):
    if l<3:
        break
    else:
        if i in(0,1,l-1,l-2):
            newstr=newstr+string[i]
print("input string is :",string)
print("output strin :",newstr)      