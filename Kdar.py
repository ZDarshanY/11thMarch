import random

ch=["R","P","S"] #ch=choice  R=rock P=paper S=scissor

player=input("Enter the name of Player :")
target=int(input("Enter the target :"))

sc=0 #score of computer
sp=0 #score of player

while((sc!=target)&(sp!=target)):
    CC=random.choice(ch) #CP = computer choice
    PC=input("Enter your choice :")
    if(PC==CC):
        print("Computer choice is ",CC,"Your choice is ",PC," Match tie")
        print("Score of Computer is :",sc)
        print("Score of ",player," :",sp)
    elif(PC=='R'):
        if(CC=='P'):
            sc=sc+1
            print("Computer choice is ",CC,"Your choice is ",PC," You Lose")
            print("Score of Computer is :",sc)
            print("Score of ",player," :",sp)
        else:
            sp=sp+1
            print("Computer choice is ",CC,"Your choice is ",PC," You Won")
            print("Score of Computer is :",sc)
            print("Score of ",player," :",sp)
    elif(PC=='P'):
        if(CC=='S'):
            sc=sc+1
            print("Computer choice is ",CC,"Your choice is ",PC," You Lose")
            print("Score of Computer is :",sc)
            print("Score of ",player," :",sp)
        else:
            sp=sp+1
            print("Computer choice is ",CC,"Your choice is ",PC," You Won")
            print("Score of Computer is :",sc)
            print("Score of ",player," :",sp)
    elif(PC=='S'):
        if(CC=='P'):
            sp=sp+1
            print("Computer choice is ",CC,"Your choice is ",PC," You Won")
            print("Score of Computer is :",sc)
            print("Score of ",player," :",sp)
        else:
            sc=sc+1
            print("Computer choice is ",CC,"Your choice is ",PC," You Lose")
            print("Score of Computer is :",sc)
            print("Score of ",player," :",sp)
    else:
        print("Invalid input")
if sc==target:
    print("Computer won!!!")
else:
    print(player," won!!!")
