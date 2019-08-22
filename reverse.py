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
      print(" Think of a number between 1-100 and \n I will try and guess it")
      print("Use the following codes to let me know how my guess is: ")
      print(" 1 = Too Low \n 2 = Too HIGH \n 3 = YOU GOT IT!")

#Systematically guess by taking the middle of the low and high bound. 
def guess(low, high):
      x = (high + low) / 2
      return int(x)
     
      
#Guess the number and return the value of 1, 2, or 3 to ask the user if they are close      
def checkNum(n):
      print("My guess is: " + str(n))
      check = int(input("Am I right? "))
      return check

#Main game loop
def play():

      greet()
      low = 0
      high = 100
      while(True):
            g = guess(low, high)
            c = checkNum(g)
            if(c==1):
                  low = g
            elif(c==2):
                  high = g
            else:
                  print("Sweet!  I win ;) ")
                  break
      

choices = {"yes", "yuss" , "ya", "yeah", "sure", "ok" , "y", }           
play()
