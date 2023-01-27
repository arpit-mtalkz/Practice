ascii=input()
hexa=""
for i in range(len(ascii)):
    ch=ascii[i]
    s=ord(ch)
    part=hex(s).lstrip("0x").rstrip("L")
    hexa=hexa+" "+part
print(hexa)