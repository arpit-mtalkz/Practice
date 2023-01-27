def greatestOfThree(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
n1=int(input())
n2=int(input())
n3=int(input())
got=greatestOfThree(n1,n2,n3)
print(got)