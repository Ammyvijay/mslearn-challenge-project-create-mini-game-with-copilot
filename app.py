
print("Rock Paper Scissor Game : \n\n1. Rock\n2. Paper\n3. Scissor\n")

def game(user):
    print(f"{user}, Enter the Number :")
    num=int(input())
    s=None
    if(num==1):
       s="Rock" 
    elif(num==2):
       s="Paper"
    elif(num==3):
       s="Scissor"
    else:
       print(f"{user} is not pressed correctly! Enter Proper Number!!\n")

    if s:
        print(f"{user} is pressed {s}")
    return s

Start=True
player1=input("Enter the Player 1 Name :")
player2=input("Enter the Player 2 Name :")

s1=None
s2=None

while(Start==True):        
    while s1 is None:
       s1=game(player1)
    while s2 is None:
       s2=game(player2)

    if s1==s2:
       print("Game Draw")
    break
