n1=int(input("Enter the 1st list :\n"))
l1=[]
l2=[]
for i in range(0,n1):
    l=int(input())
    l1.append(l)
print(l1)
n2=int(input("Enter the 2nd list :\n"))
for i in range(0,n2):
    lis=int(input())
    l2.append(lis)
print(l2)
l3=l1+l2
l4=set(l3)
s=list(l4)
print("list after merging will be :\n")
print(s)