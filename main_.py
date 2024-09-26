import  random
'''
1 is for snake
-1 is for water
0 is for gun
'''

computer = random.choice([1,-1,0])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1,"g": 0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}

# check if the user input is valid
if youstr not in youDict:
    print("Invalid choice! Please choose 's' for snake, 'w' for water, or 'g' for gun.")
else:
    you = youDict[youstr]
# by now we have two number (variables) which is you and computer
print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")
 
if(computer == you):
    print("Its a Draw")

else:
    if(computer == -1 and you ==1): 
       print("You win!")
    elif(computer == -1 and you ==0):
       print("You lose!")
    elif(computer == 1 and you ==-1): 
       print("You lose!")
    elif(computer == 1 and you == 0): 
       print("You win!")
    elif(computer == 0 and you ==-1): 
       print("You win!")
    elif(computer == 0 and you ==1): 
       print("You lose!")

    else:    
       print("something went wrong!")     
       