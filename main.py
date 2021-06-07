#THINGS TO DO LIST
#Make the Dragon
#Implement damage system

#Imports, you use time thru time.sleep()
import time
import random as r
global health
global damage
# INTRO

#Setup
health = 13
damage = 13
inventory = {}
inventory = {"Food": 2, "Campfire": 1}
response = ["yes", "Y", "y", "i", "Yes", "I"]
ind = r.randint(1, 5)
tools = ["n", "n", "n", "n", "a", "a"]
tool = tools[ind]

if tool == "a":
  print("You found a suit of armor your health goes up by 10!")
  print("")
  health += 10
  inventory["Armor"] = 1

def print_tory():
  global inventory
  for (k, v) in inventory.items():
    print("%s: %d" % (k, v))

def output():
  i = "i"
  while i == "i":
    i = input("Do you want want to see your inventory ")
    print("")
    if i in response:
      print_tory()
      i = "i"
      return True
    else:
      return False
    


def Ogres():
  global health
  global Death
  ogres = r.randint(5, 10)
  flip = r.randint(1, 2)
  loot = r.randint(7, 15)
  print("______________________")
  print("Fight, You vs {} Ogres".format(ogres))
  print("______________________")
  OgreDamage = 3 * ogres
  OgreHealth = ogres * 3
  if OgreDamage > health:
    print("An ogre hit you with a club on the head! You Died.")
    print("")
    Death = True
  elif damage > OgreHealth:
    print("The ogres surrounded you, but somehow you managed to wrestle them similtaneously.")
    print("You also stole the ogres stuff and found a health boosting potion, + {} health".format(loot))
    health += loot
    print("")
    return 0
  elif flip == 1:
    print("You managed to get away with your life barely...")
    return 0
  else:
    print("It was a close fight, but an ogre managed to hit you on the head, Game Over")
    Death = True



def Dragonian():
  global DDeath
  years = r.randint(2000, 3000)
  print("")
  print("You are an ambituos person, and seek glory beyond that of a local legend.") 
  print("So you go dragon hunting and encounter a Xymallix The Grim on a mountaintop. ")
  print("A dragons power is determined by age, Xymallix is {} years old.".format(years))
  print()
  print("______________________")
  print("Fight, You vs Red Dragon")
  print("______________________")
  DragonHealth = years//100
  dhealth = DragonHealth
  if dhealth > health:
    print("Twas a battle that will go down in the history books")
    print("You challenged the dragon to a duel to the death, you cut many wounds on it's body, but alas Xymallix triumphed in the end with on fatal bite. Game Over!")
    DDeath = True
  elif health > dhealth:
    print("Twas a battle that will go down in the history books")
    print("You challenged the dragon to a duel to the death, managing to kill the fell beast wih one fatal blow to the head. ")
  else:
    print("It was a almost a tie but the dragon got you. Game Over!")
    DDeath = True

def Game():
  print("Welcome to Explore, you're an adventurer looking to make a")
  print("name for themselves, so you set of into the woods.")
  print("")
  print("In the woods you encounter a band of ogres!")
  print("")
  output()
  Ogres()
  if Death != True:
    output()
    Dragonian()
    if DDeath == True:
      print("")
      print("You died a noble death, but alas, you were soon forgotten. ")
    else:
      print("Your name is taught to every child to give them courage and you became a legend, remebered and revered for millinea. ")
  print("You died in the forest completely unknown. ")

    

Game()

