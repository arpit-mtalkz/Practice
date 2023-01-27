#using function
def factorial(num):
    product=1
    for i in range(1,num+1):
        product=product*(i)
    return product
num=int(input())
fact=factorial(num)
print(fact)

#using recursion
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial_recursive(n-1)
n=int(input())
factorial1=factorial_recursive(n)
print(factorial1)