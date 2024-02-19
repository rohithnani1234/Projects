import random   #to generate random values
import os       #to use specific parameter and functions
import re       #to use regular expressions

while(1<2):
  print("\n")
  print("Rock, Paper, Scissor - Shoot!")
  
  #taking imput from the use
  userChoice=input("Choose your weapon [R]ock], [P]aper], [S]cissor, [E]xit: ")
  
  #Validating the user input
  if (not re.match("[SsRrPpEe]",userChoice)) or (len(userChoice)!=1):
    print("Please choose a letter:")
    print("[R]ock, [Paper], [S]cissor, [E]xit")
    continue
  
  #print the User's Choice
  print("You choose: "+userChoice)
  
  #Create a list of possible choices
  choices=['R','P','S']
  
  #Generating Computer's Choice
  opponenentChoice=random.choice(choices)
  
  #Print Computer's Choice
  print("I Choose: "+opponenentChoice)
  
  #check Computer's Choice and User's Choice by applying game logic
  
  if opponenentChoice==str.upper(userChoice):
    print("Tie! ")
    
  elif opponenentChoice=='R' and userChoice.upper()=='S':
    print("Scissors beats rock,I win!")
    continue
    
  elif opponenentChoice=='S' and userChoice.upper()=='P':
    print("Scissors beats paper! I win!")
    continue
    
  elif opponenentChoice=='P' and userChoice.upper()=='R':
    print("Paper beat rock , I win! ")
    continue
  
  else:
    print("You win!")