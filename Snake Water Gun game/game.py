while True:
 import random
 number=[1,2,3]
 print("-------------------3Welcome to the world of snake water gun game...................")
 mydict={1:'Snake',2:'Water',3:'Gun',4:'Exit..........'}
 user=int(input('''Choose the option:
           1.Snake
           2.Water
           3.Gun
           4.Exit     '''))
 if user==4:
    break  
 computer=random.choice(number)
 print(f'''Your Choice:{mydict[user]}
computer Choice:{mydict[computer]}''')
#---------- Check conditions ------------
 if user==computer:
        print("Draw!!")     
 else:
        if user==1 and computer==2:
          print("You Wins!!!")
        elif user==2 and computer==3:
          print("You Wins!!!")
        elif user==1 and computer==3:
          print("Computer Wins!!!")
        elif user==2 and computer==1:
          print("Computer Wins!!!") 
        elif user==3 and computer==2:
          print("Computer Wins!!!")
        elif user==3 and computer==1:
          print("You Wins!!!")
        else:
           print("something went wrong")
           break

    
        