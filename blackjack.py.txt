from replit import clear
import random
import art
import time

deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
Player = 'Player'
Dealer = 'Dealer'

continueGame = 'y'
def draw():
  draw = random.randint(0,12)
  return deck[draw]

def total(cards):
  aces = []
  total = 0
  number = 0
  for card in cards:
    total+=card
    if card == 11:
      aces.append(number)
    number+=1
  print(aces)
  if total>21 and len(aces)>0:
    cards[aces[0]] = 1
    total=total-10
  return total

def printHand(cards,total, player):
   print(f"{player} cards {cards} {total}")
def refreshScreen(dealercards, dealertotal, playercards, playertotal):
  clear()
  print(art.logo)
  printHand(playercards, playertotal, Player)
  printHand(dealercards, dealertotal, Dealer)

def startGame():
  usercards = []
  dealercards = []
  usercards.append(draw())
  usercards.append(draw())
  usertotal = total(usercards)
  printHand(usercards,usertotal, Player)
  dealercards.append(draw())
  dealertotal=total(dealercards)
  refreshScreen(dealercards, dealertotal, usercards,usertotal)
  if(usertotal==21):
    print("21! You win!")
    return
  hit = 'n'
  hit = input("Hit? : ")
  while hit == 'y':
     usercards.append(draw())
     usertotal = total(usercards)
     refreshScreen(dealercards, dealertotal, usercards,usertotal)
     if usertotal > 21:
       print("You busted - You Lose")
       return
     else:
       hit = input ("Hit? ")
  while dealertotal < 16:
    dealercards.append(draw())
    dealertotal = total(dealercards)
    refreshScreen(dealercards, dealertotal, usercards,usertotal)
    time.sleep(1)
  refreshScreen(dealercards, dealertotal, usercards,usertotal)
  if(dealertotal>21):
    print("Dealer busts - You Win!")
    return
  if(dealertotal>usertotal):
    print("Dealer wins")
  elif(dealertotal==usertotal):
    print("Draw")
  else:
    print("You win")
  return
  

while continueGame == 'y':
  print(art.logo)
  startGame()
  continueGame= input("Play another game? : ")
  clear()




