"""
Enter your heading here
"""


import random

def guess():
      try:
            g = int(input("Please enter a number: "))
            return g
      except:
            print("Error")
            return guess()

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
      
def play():
      r = random.randint(0,100)
      lives = 7
      while(lives>0):
            ans = guess()
            if(checkNum(ans, r)):
                  break
            else:
                  lives = lives - 1
                  print("You have " + str(lives) + " lives left.")

      choice = input("Play again?")
      if(choice == "yes"):
            play()
      else:
            print("Have a good day!")

play()
