m=int(input("Enter your marks in number :\n"))

if m>=90:
    grade="Ex"
elif m>=80:
    grade="A"
elif m>=70:
    grade="B"
elif m>=60:
    grade="C"
elif m>=50:
    grade="D"
else:
    grade="F"
print("your grade is :" ,grade)