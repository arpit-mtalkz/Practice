str=input()
for i in range(len(str)):
    ch=str[i]
    if ch.isdigit():
        if i>0 or i<len(str)-1:
            str=str[:i-1]+str[i+1]+str[i]+str[i-1]+str[i+2:]
            i+=2
            print(str)