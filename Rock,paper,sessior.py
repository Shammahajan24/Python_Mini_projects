print('''Choose any one:-
       1.rock
       2.paper,
       3.sizor''')
player1=input("player 1 choose:")
player2=input("player 2 choose:")
if player1==player2:
    print("Draw!!!")
elif (player1=='rock'and player2=='paper')or (player1=='paper'and player2=='sizor') or (player1=='sizor'and player2=='rock') :
    print("player 2 win!!!")    
elif (player1=='paper'and player2=='rock')or(player1=='sizor'and player2=='paper'):
    print("palyer 1 winn!!!")
elif(player1=='rock'and player2=='sizor'):
    print("palyer 1 winn!!!")
else:
    print("Wrong input!!!")       
   