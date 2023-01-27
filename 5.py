'''Replace in string'''
letter='''Hello Name
You have fixed your appointment on Date
Thank You'''
name1=input("Enter your name\n")
date1=input("Enter date\n")
letter=letter.replace("Name",name1)
letter=letter.replace("Date",date1)
print(letter)