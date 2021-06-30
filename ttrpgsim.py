import tkinter as tk
from tkinter import ttk
import math
import random
import PIL.Image
import PIL.ImageTk
import os

class Character:
    type = name = image = hp = ac = str = dex = con = int = wis = cha = prof = spellScore = savingThrows = actions = currentHP = 0

    def __repr__(self):
        return "Name: " + str(self.name) + "\n" + "Type: " + str(self.type) + "\n" + "Image: " + str(self.image) + "\n" + "HP: " + str(self.hp) + "\n" + "Current HP: " + str(self.currentHP) + "\n" + "AC: " + str(self.ac) + "\n" + "STR: " + str(self.str) + "\n" + "DEX: " + str(self.dex) + "\n" + "CON: " + str(self.con) + "\n" + "INT: " + str(self.int) + "\n" + "WIS: " + str(self.wis) + "\n" + "CHA: " + str(self.cha) + "\n" + "Proficiency Bonus: " + str(self.prof) + "\n" + "Spell Ability: " + str(self.spellScore) + "\n" + "Saving Throws: " + str(self.savingThrows) + "\n" + "Actions: " + str(self.actions) + "\n"

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
    action.name = f.readline().strip(" \n")
    if(type == 1): #Attack
        action.score = f.readline().strip(" \n")
        action.attackBonus = int(f.readline().strip(" \n"))
        damageDice = f.readline().strip(" \n").split(", ")
        action.damageDice = []
        for i in damageDice:
            action.damageDice.append(i)
        action.damageBonus = int(f.readline().strip(" \n"))
        action.crit = int(f.readline().strip(" \n"))
        damageDice = f.readline().strip(" \n").split(", ")
        action.critDice = []
        for i in damageDice:
            action.critDice.append(i)
        action.critBonus = int(f.readline().strip(" \n"))
        actionList[name] = action

    elif(type == 2): #Spell with save
        action.dc = f.readline().strip(" \n")
        damageDice = f.readline().strip(" \n").split(", ")
        action.damageDice = []
        for i in damageDice:
            action.damageDice.append(i)
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
    character.currentHP = character.hp
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
        character.actions.append(actionList[x])
        x = f.readline().strip(" \n")
    characterList[character.name] = character
    
def createDiceString(diceList):
    out = ""
    for dice in diceList:
        out += dice+"+"
    return out[:-1]
        

actionFiles = os.listdir(path="actions")
actionList = {}

#Parse all actions
for i in actionFiles:
    parseAction(i)

#Make hybrid actions actually reference the component action objects, we have to do that now since they weren't initialized before
for i in actionList:
    if(actionList[i].type == 3):
        aux = actionList[i].hybrids
        actionList[i].hybrids = []
        for j in aux:
            actionList[i].hybrids.append(actionList[j])

#print(actionList)
print("---------------------------------------------------------------------")

characterFiles = os.listdir(path="characters")
characterList = {}

for i in characterFiles:
    parseCharacter(i)

#print(characterList)
print("---------------------------------------------------------------------")

def addCharacter(event):
    charSelected = event.widget.master.winfo_children()[1]["text"]
    charSelected = characterList[charSelected]
    global activeCharacter
    activeCharacter = charSelected

    for i in activeDataFrame.winfo_children():
        i.destroy()

    activeDataFrame.rowconfigure(2, weight = 1)

    nameLabel = tk.Label(activeDataFrame, text = charSelected.name, font = ("Arial", 22))
    nameLabel.grid(row = 0, column = 0, sticky = "ew")

    frame1 = tk.Frame(activeDataFrame)
    frame1.grid(row = 1, column = 0, sticky = "ew")
    frame1.rowconfigure(1, weight=1)

    try:
        portrait = PIL.Image.open("portraits/" + charSelected.image)
    except:
        portrait = PIL.Image.open("portraits/default.png")

    portrait = portrait.resize((80,80), PIL.Image.ANTIALIAS)
    TKportrait = PIL.ImageTk.PhotoImage(portrait)
    portraitLabel = tk.Label(frame1, image = TKportrait)
    portraitLabel.image = TKportrait
    portraitLabel.grid(row = 0, column = 0)

    frame1Sub1 = tk.Frame(frame1, width = 520)
    frame1Sub1.grid(row = 0, column = 1)
    frame1Sub1.columnconfigure(0, weight=1)

    hpGreen = PIL.Image.open("images/hpGreen.png")
    hpRed = PIL.Image.open("images/hpRed.png")

    hpWidth = (charSelected.currentHP / charSelected.hp) * 500

    hpGreen = hpGreen.resize((int(hpWidth + 1), 50), PIL.Image.ANTIALIAS)
    hpGreen = PIL.ImageTk.PhotoImage(hpGreen)

    hpRed = hpRed.resize((int(500 - hpWidth + 1), 50), PIL.Image.ANTIALIAS)
    hpRed = PIL.ImageTk.PhotoImage(hpRed)

    hpBarFrame = tk.Frame(frame1Sub1, padx = 5)
    hpBarFrame.grid(row = 0, column = 0)

    hpGreenLabel = tk.Label(hpBarFrame, image = hpGreen, bd = -2)
    hpGreenLabel.image = hpGreen
    if(hpGreen.width() > 1):
        hpGreenLabel.grid(row = 0, column = 0)

    hpRedLabel = tk.Label(hpBarFrame, image = hpRed, bd = -2)
    hpRedLabel.image = hpRed
    if(hpRed.width() > 1):
        hpRedLabel.grid(row = 0, column = 1)

    frame1Sub2 = tk.Frame(frame1Sub1)
    frame1Sub2.grid(row = 1, column = 0, columnspan = 2)
    frame1Sub2.columnconfigure(0, weight=1)
    frame1Sub2.columnconfigure(1, weight=1)

    hpLabel = tk.Label(frame1Sub2, text = "HP: " + str(int(charSelected.currentHP)) + "/" + str(charSelected.hp), font = ("Arial", 19))
    hpLabel.grid(row = 0, column = 0, sticky = "ew")

    acLabel = tk.Label(frame1Sub2, text = "AC: " + str(charSelected.ac), font = ("Arial", 19))
    acLabel.grid(row = 0, column = 1, sticky = "ew")

    frame2 = tk.Frame(activeDataFrame)
    frame2.grid(row = 2, column = 0, sticky = "nsew")
    frame2.columnconfigure(0, weight = 1)
    frame2.columnconfigure(1, weight = 1)
    frame2.columnconfigure(2, weight = 1)
    frame2.rowconfigure(0, weight = 1)
    frame2.rowconfigure(1, weight = 1)
    frame2.rowconfigure(2, weight = 1)

    colors = {
        "str": "black",
        "dex": "black",
        "con": "black",
        "int": "black",
        "wis": "black",
        "cha": "black"
        }
    for i in charSelected.savingThrows:
        colors[i] = "blue"

    strLabel = tk.Label(frame2, text = "STR: " + str(charSelected.str), font = ("Arial", 19), fg = colors["str"])
    dexLabel = tk.Label(frame2, text = "DEX: " + str(charSelected.dex), font = ("Arial", 19), fg = colors["dex"])
    conLabel = tk.Label(frame2, text = "CON: " + str(charSelected.con), font = ("Arial", 19), fg = colors["con"])
    intLabel = tk.Label(frame2, text = "INT: " + str(charSelected.int), font = ("Arial", 19), fg = colors["int"])
    wisLabel = tk.Label(frame2, text = "WIS: " + str(charSelected.wis), font = ("Arial", 19), fg = colors["wis"])
    chaLabel = tk.Label(frame2, text = "CHA: " + str(charSelected.cha), font = ("Arial", 19), fg = colors["cha"])
    profLabel = tk.Label(frame2, text = "Prof: " + str(charSelected.prof), font = ("Arial", 19), fg = "blue")
    editButton = tk.Button(frame2, text = "Edit", font = ("Arial", 19))

    strLabel.grid(row = 0, column = 0)
    dexLabel.grid(row = 0, column = 1)
    conLabel.grid(row = 0, column = 2)
    intLabel.grid(row = 1, column = 0)
    wisLabel.grid(row = 1, column = 1)
    chaLabel.grid(row = 1, column = 2)
    profLabel.grid(row = 2, column = 0)
    editButton.grid(row = 2, column = 2)
    
    createMoveList(activeCharacter)


mainWindow = tk.Tk()
mainWindow.title("Tabletop Battle Sim")
mainWindow.geometry("1600x910")

#SECTION A

flagPCfilter = False
flagNPCfilter = False
flagBOSSfilter = False

charFrame = tk.Frame(mainWindow, height = 910, width = 300)
charFrame.grid(column=0, row=0)
charFrame.grid_propagate(0)

charFilterFrame = tk.Frame(charFrame, bg="#B6B6B6", height = 150, width=300)
charFilterFrame.grid(column=0, row=0, sticky="EW")

charFilterFrame.columnconfigure(0, weight=1)

charFilterButtonPC = tk.Button(charFilterFrame, text="PCs", font = ("Arial", 19), relief = tk.GROOVE, borderwidth = 4)
charFilterButtonPC.grid(column=0, row=0, sticky="EW")

charFilterButtonNPC = tk.Button(charFilterFrame, text="NPCs",font = ("Arial", 19), relief = tk.GROOVE, borderwidth = 4)
charFilterButtonNPC.grid(column=0, row=1, sticky="EW")

charFilterButtonBoss = tk.Button(charFilterFrame, text="Bosses",font = ("Arial", 19), relief = tk.GROOVE, borderwidth = 4)
charFilterButtonBoss.grid(column=0, row=2, sticky="EW")



#########################

charListFrame = tk.Frame(charFrame, bg="#C40000", height = 760, width=300)
charListFrame.grid(column=0, row=1)
charListFrame.grid_propagate(0)

charListScrollbar = tk.Scrollbar(charListFrame, orient="vertical")
charListScrollbar.grid(column=1, row=0, sticky = "NS")

charListCanvas = tk.Canvas(charListFrame, bg="#00C400", height = 760, width=279, scrollregion = (0,0,279,1000))
charListCanvas.grid(column=0, row=0, sticky="EW")
charListCanvas.grid_propagate(0)

charListCanvas.configure(yscrollcommand = charListScrollbar.set)
charListScrollbar.configure(command = charListCanvas.yview)

charListMagicFrame = tk.Frame(charListCanvas, bg="#0000C4", height=1000, width=279)
charListMagicFrame.grid(column=0, row=0)

charListCanvas.create_window((0,0), window=charListMagicFrame, anchor="nw")

######################

def createCharList():
    charKeys = characterList.keys()
    charList = []
    for char in charKeys:
        if(characterList[char].type == "PC" and flagPCfilter): continue
        if(characterList[char].type == "NPC" and flagNPCfilter): continue
        if(characterList[char].type == "BOSS" and flagBOSSfilter): continue
        charList.append(char)

    for widget in charListMagicFrame.winfo_children():
        widget.destroy()
        
    if(len(charList) > 10):
        newHeight = len(charList)*100
        charListCanvas.configure(scrollregion = (0,0,279,newHeight))
        charListMagicFrame.configure(height = newHeight)
    
    count = 0
    for char in charList:
        newCharFrame = tk.Frame(charListMagicFrame, height=100, width=279, relief = tk.GROOVE, borderwidth = 4)
        newCharFrame.grid(column = 0, row = count)
        newCharFrame.grid_propagate(0)
        newCharFrame.columnconfigure(1, weight=3)
        
        try:
            portrait = PIL.Image.open("portraits/"+characterList[char].image)
        except:
            portrait = PIL.Image.open("portraits/default.png")

        portrait = portrait.resize((80,80), PIL.Image.ANTIALIAS)
        TKportrait = PIL.ImageTk.PhotoImage(portrait)

        portraitLabel = tk.Label(newCharFrame, image = TKportrait)
        portraitLabel.image = TKportrait
        portraitLabel.grid(column=0, row=0, rowspan = 2, padx = 4, pady = 4)

        nameLabel = tk.Label(newCharFrame, text = characterList[char].name, font = ("Arial", 15))
        nameLabel.grid(column=1, row=0)

        addButton = tk.Button(newCharFrame, text = "Add", font = ("Arial", 18))
        addButton.bind("<Button-1>", addCharacter)
        addButton.grid(column=1, row=1)
        count += 1

def toggleCharfilter(filter):
    if(filter == "PC"):
        global flagPCfilter
        flagPCfilter= not flagPCfilter
        createCharList()
    elif(filter == "NPC"):
        global flagNPCfilter 
        flagNPCfilter = not flagNPCfilter
        createCharList()
    elif(filter == "BOSS"):
        global flagBOSSfilter 
        flagBOSSfilter = not flagBOSSfilter
        createCharList()
        
charFilterButtonPC.configure(command = lambda: toggleCharfilter("PC"))
charFilterButtonNPC.configure(command = lambda: toggleCharfilter("NPC"))
charFilterButtonBoss.configure(command = lambda: toggleCharfilter("BOSS"))


createCharList()




#SECTION B

activeCharacter = None

activeCharFrame = tk.Frame(mainWindow, height = 910, width = 600)
activeCharFrame.grid(column=1, row=0)
activeCharFrame.grid_propagate(0)

activeDataFrame = tk.Frame(activeCharFrame, bg = "blue", height = 300, width = 600)
activeDataFrame.grid(column=0, row=0)
activeDataFrame.grid_propagate(0)
activeDataFrame.columnconfigure(0, weight=1)


#Section C

attackListFrame = tk.Frame(activeCharFrame, bg = "green", height = 400, width = 600)
attackListFrame.grid(column=0, row=1)
attackListFrame.grid_propagate(0)


def createMoveList(activeCharacter):

    for widget in attackListFrame.winfo_children():
        widget.destroy()

    attackListScrollbar = tk.Scrollbar(attackListFrame, orient="vertical")
    attackListScrollbar.grid(column=1, row=0, sticky = "NS")

    attackListCanvas = tk.Canvas(attackListFrame, bg="#00C400", height=400, width=579, scrollregion = (0,0,579,1000))
    attackListCanvas.grid(column=0, row=0, sticky="EW")
    attackListCanvas.grid_propagate(0)

    attackListCanvas.configure(yscrollcommand = attackListScrollbar.set)
    attackListScrollbar.configure(command = attackListCanvas.yview)

    attackListMagicFrame = tk.Frame(attackListCanvas, bg="#0000C4", height=1000, width=579)
    attackListMagicFrame.grid(column=0, row=0)
    attackListMagicFrame.grid_propagate(0)

    attackListCanvas.create_window((0,0), window=attackListMagicFrame, anchor="nw")
    
    count = 0
    for action in  activeCharacter.actions:
        if (action.type == 1 or action.type == 2):
            count += 1
    if (count > 10):
        attackListCanvas.configure(scrollregion = (0,0,579,100*count))
        attackListMagicFrame.configure(height=100*count)
    
    count = 0
    for action in activeCharacter.actions:
        if (action.type == 1):
            newActionFrame = tk.Frame(attackListMagicFrame, height=100, width=579, relief = tk.GROOVE, borderwidth = 4)
            newActionFrame.grid(column=0, row=count)
            newActionFrame.grid_propagate(0)
            
            newActionButton = tk.Button(newActionFrame, text = action.name, font = ("Arial", 18))
            newActionButton.grid(column=0, row=0, rowspan=2)
            
            if(action.attackBonus >= 0):
                newHitLabel = tk.Label(newActionFrame, text = "Hit +"+str(action.attackBonus), font = ("Arial", 15))
            else:
                newHitLabel = tk.Label(newActionFrame, text = "Hit "+str(action.attackBonus), font = ("Arial", 15))
            newHitLabel.grid(column=1, row=0)
            
            newCritLabel = tk.Label(newActionFrame, text = "Crit: "+str(action.crit), font = ("Arial", 15))
            newCritLabel.grid(column=1, row=1)
            
            newDamageLabel = tk.Label(newActionFrame, text= "Damage: "+createDiceString(action.damageDice)+"+"+str(action.damageBonus), font= ("Arial", 15))
            newDamageLabel.grid(column=2, row=0)
            
            newCombobox = ttk.Combobox(newActionFrame)
            newCombobox.grid(column=2, row=1)
            newCombobox["values"] = ("Normal", "Advantage", "Disadvantage")
            newCombobox.current(0)
            newCombobox["state"] = "readonly"
            
            newAttackButton = tk.Button(newActionFrame, text = "Attack!", font = ("Arial", 15))
            newAttackButton.grid(column=3, row=0)
            
            newEditButton = tk.Button(newActionFrame, text = "Edit", font = ("Arial", 15))
            newEditButton.grid(column=3, row=1)
            
            newActionFrame.columnconfigure(0, weight = 2)
            newActionFrame.columnconfigure(1, weight = 1)
            newActionFrame.columnconfigure(2, weight = 2)
            newActionFrame.columnconfigure(3, weight = 2)
            
            count += 1
        elif (action.type == 2):
            newActionFrame = tk.Frame(attackListMagicFrame, height=100, width=579, relief = tk.GROOVE, borderwidth = 4)
            newActionFrame.grid(column=0, row=count)
            newActionFrame.grid_propagate(0)

            newActionButton = tk.Button(newActionFrame, text = action.name, font = ("Arial", 18))
            newActionButton.grid(column=0, row=0, rowspan=2)

            newTypeLabel = tk.Label(newActionFrame, text = action.dc+" save" , font = ("Arial", 15))
            newTypeLabel.grid(column=1, row=0)

            newDCLabel = tk.Label(newActionFrame, text = "DC: ?", font = ("Arial", 15))
            newDCLabel.grid(column=1, row=1)

            newDamageLabel = tk.Label(newActionFrame, text= "Damage: "+createDiceString(action.damageDice)+"+"+str(action.damageBonus), font= ("Arial", 15))
            newDamageLabel.grid(column=2, row=0)

            newSaveTypeLabel = tk.Label(newActionFrame, text= "Save type: "+action.saveEffect, font = ("Arial, 15"))
            newSaveTypeLabel.grid(column=2, row=1)

            newAttackButton = tk.Button(newActionFrame, text = "Attack!", font = ("Arial", 15))
            newAttackButton.grid(column=3, row=0)

            newEditButton = tk.Button(newActionFrame, text = "Edit", font = ("Arial", 15))
            newEditButton.grid(column=3, row=1)

            newActionFrame.columnconfigure(0, weight = 2)
            newActionFrame.columnconfigure(1, weight = 1)
            newActionFrame.columnconfigure(2, weight = 2)
            newActionFrame.columnconfigure(3, weight = 2)

            count += 1
            


############################

combatLogFrame = tk.Frame(activeCharFrame, bg = "#AC3BF6", height = 210, width = 600)
combatLogFrame.grid(column=0, row=2)
combatLogFrame.grid_propagate(0)

otherCharsFrame = tk.Frame(mainWindow, bg="#EBF63B", height = 910, width = 400)
otherCharsFrame.grid(column=2, row=0)
otherCharsFrame.grid_propagate(0)

turnsFrame = tk.Frame(mainWindow, bg="#11E9ff", height = 910, width = 300)
turnsFrame.grid(column=3, row=0)
turnsFrame.grid_propagate(0)



mainWindow.mainloop()