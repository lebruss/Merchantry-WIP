#merchant game
#caleb james russell
#march 11 2023

'''
player has money
player has a mode of transportation, which can be upgraded
there are different cities
each city has a market where you buy and sell things
different cities will have different prices for each item
Maybe sometimes, an item will not be available in a city. It will then be valuable
Maybe there will be pirates who attack you while traveling
Setting:    takes place in Republic of Georgia
            you start in Kutaisi
            2023
money is Georgian lari ₾
compile the game to an .exe also that lets the user play the game without pre-installed Python
Don't worry about learning to code, but just learn how to do each thing you want to do
'''

import time
import random
import os

#starting variables
currentDay = 1

#Functions------------------------------
#blankScreen(): clear the terminal screen between menu decisions
def blankScreen():
    os.system('cls||clear')

def inventory():
    blankScreen()
    print("Inventory")
    time.sleep(1)

'''
if save data exists in current directory: load the variables
else: give intro with asking name etc.
'''

#player name
name = input('What is your name?')

#literal string interpolation
print(f"Hello, {name}. Welcome to being a merchant")
input()
blankScreen()

#"City" class
class City:
   def __init__(self, name):
      self.name = name
#list of Cities-------------------------
Kutaisi = City("Kutaisi ქუთაისი")
currentCity = Kutaisi#starting city is Kutaisi

#"Goods" class
class Good:
  def __init__(self, name):
    self.name = name
#list of Goods--------------------------
tyemali = Good("Tyemali ტყემალი")
#print(tyemali.name)
#time.sleep(1)


#main menu
while True:
    blankScreen()
    print(f"Current city: {currentCity.name}")#Print the name of your current city
    print(f"Day: {currentDay}")
    print(f"1. Visit market")
    print(f"2. Travel")
    print(f"3. Rest")
    print(f"4. Inventory")
    menuChoice = str(input())

    #menuChoices
    if menuChoice == "3":#rest
       currentDay = currentDay + 1#"sleep" and increase the Day by 1
       continue
    elif menuChoice == "4":#inventory
        inventory()
    else:
       continue