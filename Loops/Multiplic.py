num=int(input("Eneter the number : "))
for i in range (1,11):
    #print(str(num) + "X" + str(i) + "=" + str(i*num))
#alternate we can use f string
    print(f"{num}X{i}={i*num}")