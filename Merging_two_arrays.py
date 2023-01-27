n1=int(input("Enter the 1st list :\n"))
l1=[]
l2=[]
for i in range(0,n1):
    l=int(input())
    l1.append(l)
print(l1)
n2=int(input("Enter the 2nd list :\n"))
for i in range(0,n2):
    list=int(input())
    l2.append(list)
print(l2)
print("list after merging will be :\n")
print(l1 + l2)