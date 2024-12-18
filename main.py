# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random

charName = ""
confirmation = "n"
classSelection = 42
doorInput = ""
doorSelection1 = 69




class GameClass:
    className, weaponName = "", ""
    weaponDmg, mHealth, cHealth = 0, 10, 10

    def printer(self):
        print("Class: " + self.className)
        print("Weapon: " + self.weaponName)
        print(self.weaponName + " Damage: " + str(self.weaponDmg))
        print("Max Health: " + str(self.mHealth))
        print("Current Health: " + str(self.cHealth))

    def __init__(self, name, wName, wDam, max, cur):
        self.className = name
        self.weaponName = wName
        self.weaponDmg = wDam
        self.mHealth = max
        self.cHealth = cur


shitClass = GameClass("Apathetic Gringo", "Breath", 1, 3, 3)
fighterClass = GameClass("Fighter", "Fists", 5, 20, 20)
mageClass = GameClass("Mage", "Lightning", 15, 10, 10)

zombieClass = GameClass("Zombie", "Bite", 8, 12, 12)
skeletonClass = GameClass("Skeleton", "Paunch", 4, 8, 8)
goreMashClass = GameClass("GoreMash", "SpaceRape", 729, 8000, 8000)

class Enemy:
    eName = ""
    elClass = shitClass
    def __init__(self, name, goClass):
        self.name = name
        self.elClass = goClass

zombie = Enemy("Zombie", zombieClass)
skeleton = Enemy("Skeleton", skeletonClass)
mage = Enemy("Enemy Mage", mageClass)
fighter = Enemy("Enemy Fighter", fighterClass)
gringo = Enemy("Worthless POS", shitClass)
goreMash = Enemy("GoreMash von Sulziquixsh, Raper of Space and Defiler of Future Graves", goreMashClass)



class GameChar:
    name = ""
    potions = 1
    eClass = shitClass

    def killBoost(self):
        newPotion = random.randint(0, 1)
        if (newPotion == 1):
            print("\nYou found a potion. Now you have " + str(self.potions))
        self.potions += newPotion
        self.eClass.mHealth += 2
        print("Your max health and max damage have increased by 2\nYou are fully healed")
        self.eClass.cHealth = self.eClass.mHealth
        self.eClass.weaponDmg += 2

    def printer(self):
        print("Your name is " + self.name)
        self.eClass.printer()



    def __init__(self, name, goClass):
        self.name = name
        self.eClass = goClass

player = GameChar("Terry", shitClass)

introText = "Hello, to begin, first enter your name\n"
introText2 = "Excellent, your name is "
introText3 = "Choose class, 1 for fighter, 2 for mage, 3 for pain\n"
enterText = "\n\n\nYou've fallen into a pit. The top sealed as you fell.\nThe place seems to be an endless grid of hallways and doors\nThe only way out is to try each one and hope for a way out"
killText = "With it dead, you leave the room."
dieText = "YOU ARE DEAD"
doneText = "There are 4 doors nearby, they look identical. Pick one.\n 1, 2, 3, or 4.\n"
openText = "The door opens\n"
vicText = "Beyond is sunlight emerging from a worn and withered stairwell.\n\nInconvenenty however, your arrested for tresspassing in the pit.\nYou are told you will likely serve a life sentence."

def doorChooser(chooser):
    doorSelection = chooser
    actionSel = 0
    escape = False
    while doorSelection not in (1,2,3,4):
        #escape = False
        doorInput = input(doneText)
        if doorInput.isdigit():
            doorSelection = int(doorInput)

            enemyList = [zombie, skeleton, mage, fighter, gringo, goreMash]
            enemyPicked = enemyList[random.randint(0, 5)]
            roomDesc = "You open door " + str(doorSelection) + " and it leads to an empty stone room.\nThere is a " + enemyPicked.name + " in there.\nIt looks pissed.\n"
            while escape == False:
                print(roomDesc)
                while enemyPicked.elClass.cHealth > 0:

                    while actionSel not in (1,2,3):
                        print("You have " + str(player.potions) + " Potions\n")
                        print("You can attack (1), use a potion if you have one (2), or run (3)\nWhat do you do?")
                        actionSel1 = input()
                        if actionSel1.isdigit():
                            actionSel = int(actionSel1)

                            if actionSel == 1:
                                poker = random.randint(1, player.eClass.weaponDmg)
                                enemyPicked.elClass.cHealth -= poker
                                print("You attacked " + enemyPicked.name + " with " + player.eClass.weaponName + " for " + str(poker) + " damage")
                                print("They have " + str(enemyPicked.elClass.cHealth) + " points remaining")
                                if(enemyPicked.elClass.cHealth <= 0):
                                    print("\nENEMY IS DEAD\n")
                                    player.killBoost()
                                    print("\n There's nothing else in the room, so you head back into the hall.\nYou continue walking along and find another set of doors.")
                                    escape = True
                                    #break
                                #actionSel = 0
                                #ran = False
                                #escape = False
                            elif actionSel == 2 and player.potions != 0:
                                player.potions -= 1
                                print("You drink a potion, you fully healed\n Potions remaining: " + str(player.potions))
                                player.eClass.cHealth = player.eClass.mHealth
                                print("You are now at " + str(player.eClass.cHealth) + " points")
                                #actionSel = 0
                                #ran = False
                                escape = False

                            elif actionSel == 2 and player.potions == 0:
                                print("You have no potions")
                                #actionSel = 1
                                escape = False
                            elif actionSel == 3:
                                escape = True
                                print("You ran away and the door shut")
                                enemyPicked.elClass.cHealth = 0
                                #actionSel = 0
                                #ran = False
                                break
                            if escape == False and enemyPicked.elClass.cHealth > 0:
                                enemyPoker = random.randint(1, enemyPicked.elClass.weaponDmg)
                                player.eClass.cHealth -= enemyPoker
                                print(enemyPicked.name + " attacks you via " + enemyPicked.elClass.weaponName + " dealing " + str(enemyPoker) + " damage to you\n")
                                print("You have " + str(player.eClass.cHealth) + " points remaining")
                                actionSel = 0
                                if(player.eClass.cHealth <= 0):
                                    input(dieText)
                                    exit(0)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Startup... ! Game Start")
    while confirmation != "y":
        charName = input(introText)
        confirmation = input("are you sure you want your name to be " + charName + "?\nType y top confirm.")

    #print(charName)
    print(introText2 + charName)
    while classSelection != 1 and classSelection != 2:
        classInput = input(introText3)
        if classInput.isdigit():
            classSelection = int(classInput)
            #print(classSelection)
            if classSelection == 1:
                player.name = charName
                player.eClass = fighterClass
                break
            elif classSelection == 2:
                player.name = charName
                player.eClass = mageClass
                break
            elif classSelection == 3:
                player.name = charName
                player.eClass = shitClass
                break
            else:
                classSelection = 69

    player.printer()
    print(enterText)
    while player.eClass.cHealth > 0:
        doorChooser(doorSelection1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/




'''
def main():
     print("This program illustrates a chaotic function")
     x = 0.0
     a = input("Enter a number between 1 and 0:  ")
     if a.isdigit():
         x = a
     for i in range(10):
            x = 3.9 * x * (1 - x)
            print(x)
main()
'''

def strToInt(cheeki):
    breeki = None
    if cheeki.isdigit():
        breeki = int(cheeki)
        return breeki
    else:
        print("ERROR - strToInt error")
        return 80085

def strToFloat(cheeki):
    breeki = None
    if cheeki.isdigit():
        breeki = float(cheeki)
        return breeki
    else:
        print("ERROR - strToFloat error")
        return 80085.69