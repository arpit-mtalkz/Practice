#using list
a=input()
hexa=""
list=[]
j=0

for i in a:
    list.append(i)

for i in list:
    s=ord(list[j])
    part=hex(s).lstrip("0x").rstrip("L")
    hexa=hexa+" "+part
    j=j+1
print(hexa)