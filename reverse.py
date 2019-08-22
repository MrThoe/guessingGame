"""
My Python Guessing Game Example2
**This time the comuter guesses and I make the number**
@Author: Allen Thoe
@Param: num, rand, choice
Date: 8/21/2019
"""

import random

#Start the game byt explaining how to play to the user
def greet():
      print(" Think of a number I will try and guess it")
      print("Use the following codes to let me know how my guess is: ")
      print(" 1 = 'Too Low' \n 2 = 'Too HIGH' \n 3 = 'YOU GOT IT!'")

#Systematically guess by taking the middle of the low and high bound. 
def guess(low, high):
      x = (high + low) / 2
      return int(x)
     
      
#Guess the number and return the value of 1, 2, or 3 to ask the user if they are close      
def checkNum(n):
      print("My guess is: " + str(n))
      check = int(input("Am I right? "))
      return check

#Get the low and high numbers from the user
def getLow():
      try:
            l = int(input("Please enter the LOWER bound for the game: "))
            return l
      except:
            print("I'm sorry, that's not a valid response. \nPlease try again.")
            return getLow()

def getHigh(theLow):
      try:
            l = int(input("Now for the UPPER bound for the game: "))
            if(l <= theLow):
                  print("That makes no sense, please choose a number greater than the LOWER bound.")
                  return getHigh(theLow)
            else:
                  return l
      except:
            print("I'm sorry, that's not a valid response. \nPlease try again.")
            return getHigh(theLow)
      

#Main game loop
def play():

      greet()
      low = getLow()
      high = getHigh(low)

      while(True):
            g = guess(low, high)
            c = checkNum(g)
            if(c==1):
                  low = g
            elif(c==2):
                  high = g
            elif(c==3):
                  print("Sweet!  I win ;) ")
                  break
            else:
                  print("That is not one of the choices....")
                  print("I can only understand '1','2', or '3'")
                  print("To let me know how my guess is use these codes...")
                  print(" 1 = 'Too Low' \n 2 = 'Too HIGH' \n 3 = 'YOU GOT IT!'")

      #Replay?
      ans = input("Should we play again? \n")
      if(ans in choices):
            play()
      else:
            print("Ok good bye, thanks for playing ; )")
            
choices = {"yes", "yuss" , "ya", "yeah", "sure", "ok" , "y", "please" , "uh-huh"}           
play()
