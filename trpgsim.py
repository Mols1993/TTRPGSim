import tkinter as tk
from tkinter import ttk
import math
import random
import PIL.Image
import PIL.ImageTk
import os

class Character:
    type = name = image = hp = ac = str = dex = con = int = wis = cha = prof = spellScore = savingThrows = actions = 0

    def __repr__(self):
        return "Name: " + str(self.name) + "\n" + "Type: " + str(self.type) + "\n" + "Image: " + str(self.image) + "\n" + "HP: " + str(self.hp) + "\n" + "AC: " + str(self.ac) + "\n" + "STR: " + str(self.str) + "\n" + "DEX: " + str(self.dex) + "\n" + "CON: " + str(self.con) + "\n" + "INT: " + str(self.int) + "\n" + "WIS: " + str(self.wis) + "\n" + "CHA: " + str(self.cha) + "\n" + "Proficiency Bonus: " + str(self.prof) + "\n" + "Spell Ability: " + str(self.spellScore) + "\n" + "Saving Throws: " + str(self.savingThrows) + "\n" + "Actions: " + str(self.actions) + "\n"

class Action:
    type = name = score = attackBonus = damageDice = damageBonus = crit = critDice = critBonus = dc = saveEffect = hybrids = 0

    def __repr__(self):
        if(self.type == 1):
            return "Name: " + str(self.name) + "\n" + "Type: " + str(self.type) + "\n" + "Score: " + str(self.score) + "\n" + "Attack Bonus: " + str(self.attackBonus) + "\n" + "Damage Dice: " + str(self.damageDice) + "\n" + "Damage Bonus: " + str(self.damageBonus) + "\n" + "Crit: " + str(self.crit) + "\n" + "Crit Dice: " + str(self.critDice) + "\n" + "Crit Bonus: " + str(self.critBonus) + "\n"
        elif(self.type == 2):
            return "Name: " + str(self.name) + "\n" + "Type: " + str(self.type) + "\n" + "Save DC: " + str(self.dc) + "\n" + "Damage Dice: " + str(self.damageDice) + "\n" + "Damage Bonus: " + str(self.damageBonus) + "\n" + "Save Effect: " + self.saveEffect + "\n"
        elif(self.type == 3):
            return "Name: " + str(self.name) + "\n" + "Type: " + str(self.type) + "\n" + "Hybrids: " + str(self.hybrids) + "\n"

def parseAction(name):
    f = open("actions/" + name, "r")
    action = Action()
    type = int(f.readline().strip(" \n"))
    action.type = type
    action.name = name
    if(type == 1): #Attack
        action.score = f.readline().strip(" \n")
        action.attackBonus = int(f.readline().strip(" \n"))
        action.damageDice = f.readline().strip(" \n")
        action.damageBonus = int(f.readline().strip(" \n"))
        action.crit = int(f.readline().strip(" \n"))
        action.critDice = f.readline().strip(" \n")
        action.critBonus = int(f.readline().strip(" \n"))
        actionList[name] = action

    elif(type == 2): #Spell with save
        action.dc = f.readline().strip(" \n")
        action.damageDice = f.readline().strip(" \n")
        action.damageBonus = int(f.readline().strip(" \n"))
        action.saveEffect = f.readline().strip(" \n")
        actionList[name] = action

    elif(type == 3): #Combined attack + save
        action.hybrids = []
        x = f.readline().strip(" \n")
        while x:
            action.hybrids.append(x)
            x = f.readline().strip(" \n")
        actionList[name] = action

def parseCharacter(name):
    f = open("characters/" + name, "r")
    character = Character()
    character.type = f.readline().strip(" \n")
    character.name = f.readline().strip(" \n")
    character.image = f.readline().strip(" \n")
    character.hp = int(f.readline().strip(" \n"))
    character.ac = int(f.readline().strip(" \n"))
    scores = f.readline().strip(" \n").split(", ")
    character.str = int(scores[0])
    character.dex = int(scores[1])
    character.con = int(scores[2])
    character.int = int(scores[3])
    character.wis = int(scores[4])
    character.cha = int(scores[5])
    character.prof = int(f.readline().strip(" \n"))
    character.spellScore = f.readline().strip(" \n")
    character.savingThrows = f.readline().strip(" \n").split(", ")
    character.actions = []
    x = f.readline().strip(" \n")
    while x:
        character.actions.append(x)
        x = f.readline().strip(" \n")
    characterList[name] = character

actionFiles = os.listdir(path="actions")
actionList = {}

for i in actionFiles:
    parseAction(i)

print(actionList)
print("---------------------------------------------------------------------")

characterFiles = os.listdir(path="characters")
characterList = {}

for i in characterFiles:
    parseCharacter(i)

print(characterList)

mainWindow = tk.Tk()
mainWindow.title("Tabletop Battle Sim")
mainWindow.geometry("1600x910")

charFrame = tk.Frame(mainWindow, bg = "#C40000", height = 910, width = 300)
charFrame.grid(column=0, row=0)

activeCharFrame = tk.Frame(mainWindow, height = 910, width = 600)
activeCharFrame.grid(column=1, row=0)

activeDataFrame = tk.Frame(activeCharFrame, bg = "#0C00C4", height = 300, width = 600)
activeDataFrame.grid(column=0, row=0)

attacksFrame = tk.Frame(activeCharFrame, bg = "#18C400", height = 400, width = 600)
attacksFrame.grid(column=0, row=1)

combatLogFrame = tk.Frame(activeCharFrame, bg = "#AC3BF6", height = 210, width = 600)
combatLogFrame.grid(column=0, row=2)

otherCharsFrame = tk.Frame(mainWindow, bg="#EBF63B", height = 910, width = 400)
otherCharsFrame.grid(column=2, row=0)

turnsFrame = tk.Frame(mainWindow, bg="#11E9ff", height = 910, width = 300)
turnsFrame.grid(column=3, row=0)



#mainWindow.mainloop()