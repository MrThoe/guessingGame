"""
My Python Guessing Game Example
@Author: Allen Thoe
@Param: num, rand, choice
Date: 8/21/2019
"""


import random

#This function takes user input and RETURNS their guess
def guess():
      try:
            g = int(input("Please enter a number: "))
            return g
      except:
            print("Error")
            return guess()

#This function checks the number AND returns True or False 
def checkNum(num, rand):
      if(num==rand):
            print("You win")
            return True
      elif(num < rand):
            print("Too LOW")
            return False
      else:
            print("Too HIGH")
            return False

#This is the MAIN code block of the game
def play():
      #Local Variables for the game (Created each time they play)
      r = random.randint(0,100)
      lives = 7
      
      #Main game loop
      while(lives>0):
            ans = guess()
            if(checkNum(ans, r)):   #The condition IS the output of CheckNum
                  break  #This breaks the While loop since the game is won
            else:
                  lives = lives - 1
                  print("You have " + str(lives) + " lives left.")

      #Game ended....ask user to play again or exit
      choice = input("Play again?")
      choice = choice.lower()  #Take all the letters in the string and makes them lowecase
      if(choice in choices):
            play()
      else:
            print("Have a good day!")

choices = {"yes", "yuss" , "ya", "yeah", "sure", "ok" , "y", "yea"} #List of all possible choices to play again           
play()
