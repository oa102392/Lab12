goggles = 0
oxygenTank = 0
bananas = 0
pokemon = 0
key = 0


def main():
  intro()
  gates()

  
  

def intro():
  printNow("***Welcome to the Abandoned Zoo***" )
  printNow("You have snuck into the zoo looking for excitement")
  printNow("But it is empty, with no one or no animals around")
  printNow("You are allowed to move freely using the commands:")
  printNow("north, south, east, west")
  printNow(" You can also pick things up with the command pickup")
  printNow("Type help to redisplay the introduction")
  
  
def gates():
  printNow("----------THE GATES---------")
  printNow("You are standing in front of the rusted gates of a once popular zoo")
  printNow("You once heard there was a golden egg hidden in one of the exhibits")
  printNow("With this knowledge will you choose to move north into the abandoned zoo?")
  while true:
    command = requestString("Please Choose Your Direction or Command:")
    if command == "north":
      entrance()
      break
    elif command == "help":
      intro()
    elif command == "exit":
      exit()
    else: 
      printNow("Please re-enter a valid command")
  

def entrance():
  printNow("----------THE ENTRANCE----------")
  printNow("You walk inside the zoo and notice a large map ahead")
  printNow("The map shows Tigers to the west, gorillas to the")
  printNow("east, and several other exhibits to the north.")
  printNow("You also know the exit is south from you.")
  while true:
    command = requestString("Please Choose Your Direction or Command:")
    if command == "west":
      tigerExhibit()
      break
    elif command == "east":
      gorillaExhibit()
      break
    elif command == "north":
      ventureFurther()
      break
    elif command == "south":
      gates()
      break
    elif command == "help":
      intro()
    elif command == "exit":
      exit()
    else: 
      printNow("Please re-enter a valid command")
  
  
def tigerExhibit():
  if oxygenTank == 0:
    tigerDes1()
  else:
    tigerDes2()
  
def gorillaExhibit():
  printNow("----------GORILLA EXHIBIT---------")
  printNow("You almost slip on a banana as you enter")
  printNow("The entire exhibit is filled with used bananas")
  printNow("But there is nothing else here of interest")
  printNow("Would you like to go back to the entrance?")
  printNow("Then go back south")
  while true:
    command = requestString("Please Choose Your Direction or Command:")
    if command == "south":
      entrance()
      break
    elif command == "help":
      intro()
    elif command == "exit":
      exit()
    else: 
      printNow("Please re-enter a valid command")    
      
def crocExhibit():
  printNow("----------CROCODILE EXHIBIT---------")
  printNow("The exhibit is flooded. Your shoes are now wet.")
  printNow("It seems empty here but you cannot tell because the water is murky")
  printNow("Would you like to go back to the entrance?")
  printNow("Then go back south")
  while true:
    command = requestString("Please Choose Your Direction or Command:")
    if command == "south":
      entrance()
      break
    elif command == "help":
      intro()
    elif command == "exit":
      exit()
    else: 
      printNow("Please re-enter a valid command")          
  

  
def tigerDes1():
  printNow("----------TIGER EXHIBIT---------")
  printNow("Dead trees and plants are all that remain in the exhibit")
  printNow("There are no signs of life here. All that is left is an oxygen tank")
  printNow("Would you like to go back to the entrance?")
  printNow("Then head back south")
  while true:
    command = requestString("Please Choose Your Direction or Command:")
    if command == "south":
      entrance()
      break
    elif command == "pickup":
      printNow("You have obtained an oxygen tank!")
      global oxygenTank 
      oxygenTank += 1
      tigerDes2()
      break
    elif command == "help":
      intro()
    elif command == "exit":
      exit()
    else: 
      printNow("Please re-enter a valid command")
      
def tigerDes2():
  printNow("----------TIGER EXHIBIT---------")
  printNow("Dead trees and plants are all that remain in the exhibit")
  printNow("There are no signs of life here.")
  printNow("Would you like to go back to the entrance?")
  printNow("Then head back south")
  while true:
    command = requestString("Please Choose Your Direction or Command:")
    if command == "south":
      entrance()
      break
    elif command == "help":
      intro()
    elif command == "exit":
      exit()
    else: 
      printNow("Please re-enter a valid command")

def ventureFurther():
  printNow("----------FURTHER IN---------")
  printNow("To the north you see the croc exhibit.")
  printNow("To the west is the aviary. Inside you hear a faint chirping.")
  printNow("To the east, you see the hippo exhibit.")
  printNow("South will take you back to the beginning of the zoo")
  while true:
    command = requestString("Please Choose Your Direction or Command:")
    if command == "north":
      if key == 0:
        printNow("The door is locked. You must find the key first to enter!")
        ventureFurther()
        break
      else:
        crocExhibit()
        break
      break
    if command == 'west':
      aviary()
      break
    if command == 'east':
      hippos()
      break
    if command == 'south':
      entrance()
      break
    elif command == "help":
      intro()
    elif command == "exit":
      exit()
    else: 
      printNow("Please re-enter a valid command")


def aviary():
  printNow("----------AVIARY---------")
  printNow("The aviary seems to have fallen appart. There are holes")
  printNow("in the ceiling. You hear a faint chirping sound coming")
  printNow("from the back corner of the room and a small bird appears.")
  printNow("Would you like to try to pick up the bird or head back")
  printNow("to the main entryway to the east?")
  while true:
    command = requestString("Please Choose Your Direction or Command:")
    if command == "east":
      ventureFurther()
      break
    if command == 'pickup':
      printNow("You have befriended a creature to help you on your quest!")
      global pokemon 
      pokemon += 1
      aviary2()
      break
    elif command == "help":
      intro()
    elif command == "exit":
      exit()
    else: 
      printNow("Please re-enter a valid command")
      
def aviary2():
  printNow("----------AVIARY---------")
  printNow("The aviary seems to have fallen appart. There are holes")
  printNow("in the ceiling, but no signs of life anymore. Would you")
  printNow("like to head back to the main entryway to the east?")
  while true:
    command = requestString("Please Choose Your Direction or Command:")
    if command == "east":
      ventureFurther()
      break
    elif command == "help":
      intro()
    elif command == "exit":
      exit()
    else: 
      printNow("Please re-enter a valid command")

def hippos():
  printNow("----------HIPPO EXHIBIT---------")
  printNow("The hippo tank seems to have turned green with age. A small")
  printNow("hippo comes out of the water. He has a key around his neck.")
  printNow("Would you like to try to befriend the hippo and remove the key")
  printNow("by choosing pickup or go back to the entryway to the west")
  while true:
    command = requestString("Please Choose Your Direction or Command:")
    if command == "west":
      ventureFurther()
      break
    if command == 'pickup':
      printNow("You have befriended a creature to help you on your quest!")
      global pokemon 
      pokemon += 1
      global key
      key += 1
      hippos2()
      break
    elif command == "help":
      intro()
    elif command == "exit":
      exit()
    else: 
      printNow("Please re-enter a valid command")
      
def hippos2():
  printNow("----------HIPPO EXHIBIT---------")
  printNow("The hippo tank seems to have turned green with age. There are")
  printNow("no signs of life here. Would you like to return to the entryway")
  printNow("to the west?")
  while true:
    command = requestString("Please Choose Your Direction or Command:")
    if command == "west":
      ventureFurther()
      break
    elif command == "help":
      intro()
    elif command == "exit":
      exit()
    else: 
      printNow("Please re-enter a valid command")
  
def exit():
  printNow("You have tripped on your shoelaces and died. Goodbye")
  sys.exit()
  