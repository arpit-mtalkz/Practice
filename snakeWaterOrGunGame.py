import random

def gameWin(computer, you):
    if computer==you:
        return None
    elif computer=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif computer=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif computer=='g':
        if you=='s':
            return False
        if you=='w':
            return True

print("Computer Turn: Snake(s) Water(w) or Gun(g)")
randNo=random.randint(1,3)
if randNo==1:
    computer ='s' 
elif randNo==2:
    computer='w'
elif randNo==3:
    computer='g'
you=input("Your's turn: Snake(s) Water(w) or Gun(g)")
a=gameWin(computer,you)
if a==None:
    print("This game is a tie")
elif a:
    print("You Win!")
else:
    print("You Loose!") 
