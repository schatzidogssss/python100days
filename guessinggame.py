from art import logo
from replit import clear
import random

level = { "easy":10,
          "hard":5}

def guess(guess, number):
  if guess < number: 
    print("too low")
    return False
  elif guess > number:
    print("too high")
    return False
  else:
    print("That's correct")
    return True
def runGame():
  print('Welcome to guess the number game')
  print("I'm thinking of a number between 1 and 100")
  levelinput = input("Enter 'easy' or 'hard' : ")
  tries = level[levelinput]
  number = random.randint(2,100)
  #print(f"Hint {number}")
  for count in range(0, tries) :
    correct = guess(int(input("Make a guess: ")),number)
    if correct:
      return
    if (tries-(count+1))==0:
      print("Out of guesses")
      return
    print("Guess again")
    print(f"You have {tries-(count+1)} guesses left")
print (logo)
runGame()




