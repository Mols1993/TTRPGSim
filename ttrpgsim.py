import tkinter as tk
from tkinter import Toplevel, ttk
import math
import random
import copy
import PIL.Image
from PIL.Image import init
import PIL.ImageTk
import os

class Character:
    type = name = image = hp = ac = str = dex = con = intt = wis = cha = prof = spellScore = savingThrows = actions = currentHP = initiative = 0

    def __repr__(self):
        return "Name: " + str(self.name) + "\n" + "Type: " + str(self.type) + "\n" + "Image: " + str(self.image) + "\n" + "HP: " + str(self.hp) + "\n" + "Current HP: " + str(self.currentHP) + "\n" + "AC: " + str(self.ac) + "\n" + "Initiative: " + str(self.initiative) + "\n" + "STR: " + str(self.str) + "\n" + "DEX: " + str(self.dex) + "\n" + "CON: " + str(self.con) + "\n" + "INT: " + str(self.intt) + "\n" + "WIS: " + str(self.wis) + "\n" + "CHA: " + str(self.cha) + "\n" + "Proficiency Bonus: " + str(self.prof) + "\n" + "Spell Ability: " + str(self.spellScore) + "\n" + "Saving Throws: " + str(self.savingThrows) + "\n" + "Actions: " + str(self.actions) + "\n"

class Action:
    type = name = score = attackBonus = damageDice = damageBonus = crit = critDice = critBonus = dcSave = dcScore = saveEffect = hybrids = 0

    def __repr__(self):
        if(self.type == 1):
            return "Name: " + str(self.name) + "\n" + "Type: " + str(self.type) + "\n" + "Score: " + str(self.score) + "\n" + "Attack Bonus: " + str(self.attackBonus) + "\n" + "Damage Dice: " + str(self.damageDice) + "\n" + "Damage Bonus: " + str(self.damageBonus) + "\n" + "Crit: " + str(self.crit) + "\n" + "Crit Dice: " + str(self.critDice) + "\n" + "Crit Bonus: " + str(self.critBonus) + "\n"
        elif(self.type == 2):
            return "Name: " + str(self.name) + "\n" + "Type: " + str(self.type) + "\n" + "Save DC: " + str(self.dcSave) + "\n" + "Damage Dice: " + str(self.damageDice) + "\n" + "Damage Bonus: " + str(self.damageBonus) + "\n" + "Save Effect: " + self.saveEffect + "\n"
        elif(self.type == 3):
            return "Name: " + str(self.name) + "\n" + "Type: " + str(self.type) + "\n" + "Hybrids: " + str(self.hybrids) + "\n"

#def parseAction(name):
#    f = open("actions/" + name, "r")
#    action = Action()
#    type = int(f.readline().strip(" \n"))
#    action.type = type
#    action.name = f.readline().strip(" \n")
#    if(type == 1): #Attack
#        action.score = f.readline().strip(" \n")
#        action.attackBonus = int(f.readline().strip(" \n"))
#        damageDice = f.readline().strip(" \n").split(", ")
#        action.damageDice = []
#        for i in damageDice:
#            action.damageDice.append(i)
#        action.damageBonus = int(f.readline().strip(" \n"))
#        action.crit = int(f.readline().strip(" \n"))
#        damageDice = f.readline().strip(" \n").split(", ")
#        action.critDice = []
#        for i in damageDice:
#            action.critDice.append(i)
#        action.critBonus = int(f.readline().strip(" \n"))
#        actionList[name] = action
#
#    elif(type == 2): #Spell with save
#        action.dcSave = f.readline().strip(" \n")
#        damageDice = f.readline().strip(" \n").split(", ")
#        action.damageDice = []
#        for i in damageDice:
#            action.damageDice.append(i)
#        action.damageBonus = int(f.readline().strip(" \n"))
#        action.saveEffect = f.readline().strip(" \n")
#        actionList[name] = action
#
#    elif(type == 3): #Combined attack + save
#        action.hybrids = []
#        x = f.readline().strip(" \n")
#        while x:
#            action.hybrids.append(x)
#            x = f.readline().strip(" \n")
#        actionList[name] = action

def parseCharacter(name):
    f = open("characters/" + name, "r")
    character = Character()
    character.type = f.readline().strip(" \n")
    character.name = f.readline().strip(" \n")
    character.image = f.readline().strip(" \n")
    character.hp = int(f.readline().strip(" \n"))
    character.currentHP = character.hp
    character.ac = int(f.readline().strip(" \n"))
    character.initiative = int(f.readline().strip(" \n"))
    scores = f.readline().strip(" \n").split(", ")
    character.str = int(scores[0])
    character.dex = int(scores[1])
    character.con = int(scores[2])
    character.intt = int(scores[3])
    character.wis = int(scores[4])
    character.cha = int(scores[5])
    character.prof = int(f.readline().strip(" \n"))
    character.spellScore = f.readline().strip(" \n").upper()
    character.savingThrows = f.readline().strip(" \n").upper().split(", ")
    character.actions = []

    token = f.readline().strip(" \n")

    while token == "*":
        action = Action()
        type = int(f.readline().strip(" \n"))
        action.type = type
        action.name = f.readline().strip(" \n")
        if(type == 1): #Attack
            action.score = f.readline().strip(" \n").upper()
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
            character.actions.append(action)

        elif(type == 2): #Spell with save
            action.dcSave = f.readline().strip(" \n").upper()
            action.dcScore = int(f.readline().strip(" \n"))
            damageDice = f.readline().strip(" \n").split(", ")
            action.damageDice = []
            for i in damageDice:
                action.damageDice.append(i)
            action.damageBonus = int(f.readline().strip(" \n"))
            action.saveEffect = f.readline().strip(" \n").upper()
            character.actions.append(action)
        
        token = f.readline().strip(" \n")
    
    characterList[character.name] = character
    

def createDiceString(diceList):
    out = ""
    for dice in diceList:
        out += dice+"+"
    return out[:-1]
        

#actionFiles = os.listdir(path="actions")
#actionList = {}

#Parse all actions
#for i in actionFiles:
#    parseAction(i)

#Make hybrid actions actually reference the component action objects, we have to do that now since they weren't initialized before
#for i in actionList:
#    if(actionList[i].type == 3):
#        aux = actionList[i].hybrids
#        actionList[i].hybrids = []
#        for j in aux:
#            actionList[i].hybrids.append(actionList[j])

#print(actionList)
#print("---------------------------------------------------------------------")

characterFiles = os.listdir(path="characters")
characterList = {}

for i in characterFiles:
    parseCharacter(i)

#print(characterList)
#print("---------------------------------------------------------------------")

def saveType1StatChanges(event, score, attackBonus, damageDice, damageBonus, crit, critDice, critBonus, character, action, window):
    score = score.get()
    attackBonus = int(attackBonus.get("@0, 0", tk.END).strip(" \n"))
    damageDice = damageDice.get("@0, 0", tk.END).strip(" \n").split(", ")
    damageBonus = int(damageBonus.get("@0, 0", tk.END).strip(" \n"))
    crit = int(crit.get("@0, 0", tk.END).strip(" \n"))
    critDice = critDice.get("@0, 0", tk.END).strip(" \n").split(", ")
    critBonus = int(critBonus.get("@0, 0", tk.END).strip(" \n"))

    act = None

    for i in activeCharacter.actions:
        if i.name == action:
            act = i

    act.score = score
    act.attackBonus = attackBonus
    act.damageDice = damageDice
    act.damageBonus = damageBonus
    act.crit = crit
    act.critDice = critDice
    act.critBonus = critBonus

    createMoveList(activeCharacter)

    window.destroy()

def saveType2StatChanges(event, dcSave, dcScore, saveEffect, damageDice, damageBonus, character, action, window):
    dcSave = dcSave.get()
    dcScore = int(dcScore.get("@0, 0", tk.END).strip(" \n"))
    saveEffect = saveEffect.get("@0, 0", tk.END).upper().strip(" \n")
    damageDice = damageDice.get("@0, 0", tk.END).strip(" \n").split(", ")
    damageBonus = int(damageBonus.get("@0, 0", tk.END).strip(" \n"))

    act = None

    for i in activeCharacter.actions:
        if i.name == action:
            act = i

    act.dcSave = dcSave
    act.dcScore = dcScore
    act.saveEffect = saveEffect
    act.damageDice = damageDice
    act.damageBonus = damageBonus

    createMoveList(activeCharacter)

    window.destroy()

def editActionWindow(event, name):
    action = None
    for i in activeCharacter.actions:
        if i.name == name:
            action = i

    root = Toplevel()
    root.title("Edit Stats")

    mainFrame = tk.Frame(root)
    mainFrame.grid(row = 0, column = 0)
    mainFrame.columnconfigure(0, weight = 1)

    nameLabel = tk.Label(mainFrame, text = activeCharacter.name + ": " + action.name, font = ("Arial", 22))
    nameLabel.grid(row = 0, column = 0, sticky = "ew")

    if action.type == 1:
        frame0 = tk.Frame(mainFrame)
        frame0.grid(row = 1, column = 0)
        frame0.columnconfigure(0, weight = 1)
        frame0.columnconfigure(1, weight = 1)
        frame0.columnconfigure(2, weight = 1)
        frame0.columnconfigure(3, weight = 1)

        subFrame0_0 = tk.Frame(frame0)
        subFrame0_0.grid(row = 0, column = 0, sticky = "ew")

        attackScoreLabel = tk.Label(subFrame0_0, text = "Score:", font = ("Arial", 10))
        attackScoreLabel.grid(row = 0, column = 0)

        attackScoreDropdown = ttk.Combobox(subFrame0_0, values = ("STR", "DEX", "CON", "INT", "WIS", "CHA"), state = "readonly")
        attackScoreDropdown.grid(row = 0, column = 1)
        if action.score == "STR":
            attackScoreDropdown.current(0)
        elif action.score == "DEX":
            attackScoreDropdown.current(1)
        elif action.score == "CON":
            attackScoreDropdown.current(2)
        elif action.score == "INT":
            attackScoreDropdown.current(3)
        elif action.score == "WIS":
            attackScoreDropdown.current(4)
        elif action.score == "CHA":
            attackScoreDropdown.current(5)

        subFrame0_1 = tk.Frame(frame0)
        subFrame0_1.grid(row = 0, column = 1, sticky = "ew")

        attackBonusLabel = tk.Label(subFrame0_1, text = "Attack Bonus:", font = ("Arial", 10))
        attackBonusLabel.grid(row = 0, column = 0)

        attackBonusInput = tk.Text(subFrame0_1, height = 1, width = 3)
        attackBonusInput.grid(row = 0, column = 1)
        attackBonusInput.insert(tk.INSERT, action.attackBonus)

        subFrame0_2 = tk.Frame(frame0)
        subFrame0_2.grid(row = 0, column = 2, sticky = "ew")

        damageDiceLabel = tk.Label(subFrame0_2, text = "Damage Dice:", font = ("Arial", 10))
        damageDiceLabel.grid(row = 0, column = 0)

        damageDiceText = ", ".join(action.damageDice)
        damageDiceInput = tk.Text(subFrame0_2, height = 1, width = 20)
        damageDiceInput.grid(row = 0, column = 1)
        damageDiceInput.insert(tk.INSERT, damageDiceText)

        subFrame0_3 = tk.Frame(frame0)
        subFrame0_3.grid(row = 0, column = 3, sticky = "ew")

        damageBonusLabel = tk.Label(subFrame0_3, text = "Damage Bonus:", font = ("Arial", 10))
        damageBonusLabel.grid(row = 0, column = 0)

        damageBonusInput = tk.Text(subFrame0_3, height = 1, width = 3)
        damageBonusInput.grid(row = 0, column = 1)
        damageBonusInput.insert(tk.INSERT, action.damageBonus)

        frame1 = tk.Frame(mainFrame)
        frame1.grid(row = 2, column = 0, sticky = "ew")
        frame1.columnconfigure(0, weight = 1)
        frame1.columnconfigure(1, weight = 1)
        frame1.columnconfigure(2, weight = 1)

        subFrame1_0 = tk.Frame(frame1)
        subFrame1_0.grid(row = 0, column = 0, sticky = "ew")

        critRangeLabel = tk.Label(subFrame1_0, text = "Crit Range:", font = ("Arial", 10))
        critRangeLabel.grid(row = 0, column = 0)

        critRangeInput = tk.Text(subFrame1_0, height = 1, width = 3)
        critRangeInput.grid(row = 0, column = 1)
        critRangeInput.insert(tk.INSERT, action.crit)

        subFrame1_1 = tk.Frame(frame1)
        subFrame1_1.grid(row = 0, column = 1, sticky = "ew")

        critDiceLabel = tk.Label(subFrame1_1, text = "Crit Dice:", font = ("Arial", 10))
        critDiceLabel.grid(row = 0, column = 0)

        critDiceText = ", ".join(action.critDice)
        critDiceInput = tk.Text(subFrame1_1, height = 1, width = 20)
        critDiceInput.grid(row = 0, column = 1)
        critDiceInput.insert(tk.INSERT, critDiceText)

        subFrame1_2 = tk.Frame(frame1)
        subFrame1_2.grid(row = 0, column = 2, sticky = "ew")

        critBonusLabel = tk.Label(subFrame1_2, text = "Crit Bonus:", font = ("Arial", 10))
        critBonusLabel.grid(row = 0, column = 0)

        critBonusInput = tk.Text(subFrame1_2, height = 1, width = 3)
        critBonusInput.grid(row = 0, column = 1)
        critBonusInput.insert(tk.INSERT, action.critBonus)

        frame2 = tk.Frame(mainFrame)
        frame2.grid(row = 3, column = 0, sticky = "ew")
        frame2.columnconfigure(0, weight = 1)

        saveButton = tk.Button(frame2, text = "Save", font = ("Arial", 16))
        saveButton.grid(row = 0, column = 0)

        #type = name = score = attackBonus = damageDice = damageBonus = crit = critDice = critBonus = dcSave = saveEffect = hybrids = 0
        saveButton.bind(saveButton.bind("<Button-1>", lambda event = event, score = attackScoreDropdown, attackBonus = attackBonusInput, damageDice = damageDiceInput, damageBonus = damageBonusInput, crit = critRangeInput, critDice = critDiceInput, critBonus = critBonusInput, character = activeCharacter.name, action = action.name, window = root: saveType1StatChanges(event, score, attackBonus, damageDice, damageBonus, crit, critDice, critBonus, character, action, window)))

    elif action.type == 2:
        frame0 = tk.Frame(mainFrame)
        frame0.grid(row = 1, column = 0)
        frame0.columnconfigure(0, weight = 1)
        frame0.columnconfigure(1, weight = 1)
        frame0.columnconfigure(2, weight = 1)
        frame0.columnconfigure(3, weight = 1)

        subFrame0_0 = tk.Frame(frame0)
        subFrame0_0.grid(row = 0, column = 0, sticky = "ew")

        dcSaveLabel = tk.Label(subFrame0_0, text = "Save DC:", font = ("Arial", 10))
        dcSaveLabel.grid(row = 0, column = 0)

        dcSaveDropdown = ttk.Combobox(subFrame0_0, values = ("STR", "DEX", "CON", "INT", "WIS", "CHA"), state = "readonly")
        dcSaveDropdown.grid(row = 0, column = 1)
        if action.dcSave == "STR":
            dcSaveDropdown.current(0)
        elif action.dcSave == "DEX":
            dcSaveDropdown.current(1)
        elif action.dcSave == "CON":
            dcSaveDropdown.current(2)
        elif action.dcSave == "INT":
            dcSaveDropdown.current(3)
        elif action.dcSave == "WIS":
            dcSaveDropdown.current(4)
        elif action.dcSave == "CHA":
            dcSaveDropdown.current(5)

        subFrame0_1 = tk.Frame(frame0)
        subFrame0_1.grid(row = 0, column = 1, sticky = "ew")

        dcScoreLabel = tk.Label(subFrame0_1, text = "Save Score:", font = ("Arial", 10))
        dcScoreLabel.grid(row = 0, column = 0)

        dcScoreInput = tk.Text(subFrame0_1, height = 1, width = 3)
        dcScoreInput.grid(row = 0, column = 1)
        dcScoreInput.insert(tk.INSERT, action.dcScore)

        subFrame0_2 = tk.Frame(frame0)
        subFrame0_2.grid(row = 0, column = 2, sticky = "ew")

        saveEffectLabel = tk.Label(subFrame0_2, text = "Save Effect:", font = ("Arial", 10))
        saveEffectLabel.grid(row = 0, column = 0)

        saveEffectInput = tk.Text(subFrame0_2, height = 1, width = 20)
        saveEffectInput.grid(row = 0, column = 1)
        saveEffectInput.insert(tk.INSERT, action.saveEffect)

        frame1 = tk.Frame(mainFrame)
        frame1.grid(row = 2, column = 0, sticky = "ew")
        frame1.columnconfigure(0, weight = 1)
        frame1.columnconfigure(2, weight = 1)

        subFrame1_0 = tk.Frame(frame1)
        subFrame1_0.grid(row = 0, column = 0, sticky = "ew")

        damageDiceLabel = tk.Label(subFrame1_0, text = "Damage Dice:", font = ("Arial", 10))
        damageDiceLabel.grid(row = 0, column = 0)

        damageDiceText = ", ".join(action.damageDice)
        damageDiceInput = tk.Text(subFrame1_0, height = 1, width = 20)
        damageDiceInput.grid(row = 0, column = 1)
        damageDiceInput.insert(tk.INSERT, damageDiceText)

        subFrame1_1 = tk.Frame(frame1)
        subFrame1_1.grid(row = 0, column = 1, sticky = "ew")

        damageBonusLabel = tk.Label(subFrame1_1, text = "Damage Bonus:", font = ("Arial", 10))
        damageBonusLabel.grid(row = 0, column = 0)

        damageBonusInput = tk.Text(subFrame1_1, height = 1, width = 3)
        damageBonusInput.grid(row = 0, column = 1)
        damageBonusInput.insert(tk.INSERT, action.damageBonus)

        frame2 = tk.Frame(mainFrame)
        frame2.grid(row = 3, column = 0, sticky = "ew")
        frame2.columnconfigure(0, weight = 1)

        saveButton = tk.Button(frame2, text = "Save", font = ("Arial", 16))
        saveButton.grid(row = 0, column = 0)

        #type = name = score = attackBonus = damageDice = damageBonus = crit = critDice = critBonus = dcSave = dcScore = saveEffect = hybrids = 0
        saveButton.bind(saveButton.bind("<Button-1>", lambda event = event, dcSave = dcSaveDropdown, dcScore = dcScoreInput, saveEffect = saveEffectInput, damageDice = damageDiceInput, damageBonus = damageBonusInput, character = activeCharacter.name, action = action.name, window = root: saveType2StatChanges(event, dcSave, dcScore, saveEffect, damageDice, damageBonus, character, action, window)))


def saveCharStatChanges(event, name, type, currentHP, maxHP, ac, str, dex, con, intt, wis, cha, prof, spellScore, initiative, saves, window):

    type = type.get()
    currentHP = int(currentHP.get("@0, 0", tk.END).strip(" \n"))
    maxHP = int(maxHP.get("@0, 0", tk.END).strip(" \n"))
    ac = int(ac.get("@0, 0", tk.END).strip(" \n"))
    str = int(str.get("@0, 0", tk.END).strip(" \n"))
    dex = int(dex.get("@0, 0", tk.END).strip(" \n"))
    con = int(con.get("@0, 0", tk.END).strip(" \n"))
    intt = int(intt.get("@0, 0", tk.END).strip(" \n"))
    wis = int(wis.get("@0, 0", tk.END).strip(" \n"))
    cha = int(cha.get("@0, 0", tk.END).strip(" \n"))
    prof = int(prof.get("@0, 0", tk.END).strip(" \n"))
    spellScore = spellScore.get().upper()
    initiative = int(initiative.get("@0, 0", tk.END).strip(" \n"))
    saves = saves.get("@0, 0", tk.END).strip(" \n").upper().split(", ")

    #type = name = image = hp = ac = str = dex = con = intt = wis = cha = prof = spellScore = savingThrows = actions = currentHP = 0


    activeCharacter.type = type
    activeCharacter.currentHP = currentHP
    activeCharacter.hp = maxHP
    activeCharacter.ac = ac
    activeCharacter.str = str
    activeCharacter.dex = dex
    activeCharacter.con = con
    activeCharacter.intt = intt
    activeCharacter.wis = wis
    activeCharacter.cha = cha
    activeCharacter.prof = prof
    activeCharacter.spellScore = spellScore
    activeCharacter.initiative = initiative
    activeCharacter.savingThrows = saves

    addCharacter(None, activeCharacter)
    print(simulatedCharacters)
    window.destroy()

def editCharWindowParser(event, name):
    #This absolute unit of a line traverses the hierarchy tree from the "Edit" button to the character name in the activeDataFrame
    #charName = event.widget.master.master.winfo_children()[0].winfo_children()[1].winfo_children()[0]["text"]
    #editCharWindow(characterList[charName])
    print("This does nothing now")

#PC
#Hark Mamill
#image.png
#52
#17
#15, 16, 17, 18, 19, 20
#4
#int
#con, int

def editCharWindow(name):
    character = activeCharacter
    root = Toplevel()
    root.title("Edit Stats")

    mainFrame = tk.Frame(root)
    mainFrame.grid(row = 0, column = 0)
    mainFrame.columnconfigure(0, weight = 1)

    nameLabel = tk.Label(mainFrame, text = character.name, font = ("Arial", 22))
    nameLabel.grid(row = 0, column = 0, sticky = "ew")

    
    #frame0 conatins the type, HP and AC stats
    frame0 = tk.Frame(mainFrame)
    frame0.grid(row = 1, column = 0, sticky = "ew")
    frame0.columnconfigure(0, weight = 1)
    frame0.columnconfigure(1, weight = 1)
    frame0.columnconfigure(2, weight = 1)

    subFrame0_0 = tk.Frame(frame0)
    subFrame0_0.grid(row = 0, column = 0, sticky = "ew")

    typeLabel = tk.Label(subFrame0_0, text = "Type:", font = ("Arial", 10))
    typeLabel.grid(row = 0, column = 0)

    typeDropdown = ttk.Combobox(subFrame0_0, values = ("PC", "NPC", "BOSS"), state = "readonly")
    typeDropdown.grid(row = 0, column = 1)
    if character.type == "PC":
        typeDropdown.current(0)
    elif character.type == "NPC":
        typeDropdown.current(1)
    elif character.type == "BOSS":
        typeDropdown.current(2)

    subFrame0_1 = tk.Frame(frame0)
    subFrame0_1.grid(row = 0, column = 1, sticky = "ew")

    hpLabel = tk.Label(subFrame0_1, text = "HP:", font = ("Arial", 10))
    hpLabel.grid(row = 0, column = 0)

    currentHPInput = tk.Text(subFrame0_1, height = 1, width = 4)
    currentHPInput.grid(row = 0, column = 1)
    currentHPInput.insert(tk.INSERT, character.currentHP)

    slashLabel = tk.Label(subFrame0_1, text = "/", font = ("Arial", 10))
    slashLabel.grid(row = 0, column = 2)

    maxHPInput = tk.Text(subFrame0_1, height = 1, width = 4)
    maxHPInput.grid(row = 0, column = 3)
    maxHPInput.insert(tk.INSERT, character.hp)

    subFrame0_2 = tk.Frame(frame0)
    subFrame0_2.grid(row = 0, column = 2, sticky = "ew")

    acLabel = tk.Label(subFrame0_2, text = "AC:", font = ("Arial", 10))
    acLabel.grid(row = 0, column = 0)

    acInput = tk.Text(subFrame0_2, height = 1, width = 3)
    acInput.grid(row = 0, column = 1)
    acInput.insert(tk.INSERT, character.ac)

    #frame1 contains the STR, DEX, CON, INT, WIS and CHA stats
    frame1 = tk.Frame(mainFrame)
    frame1.grid(row = 2, column = 0, sticky = "ew")
    frame1.columnconfigure(0, weight = 1)
    frame1.columnconfigure(1, weight = 1)
    frame1.columnconfigure(2, weight = 1)
    frame1.columnconfigure(3, weight = 1)
    frame1.columnconfigure(4, weight = 1)
    frame1.columnconfigure(5, weight = 1)

    subFrame2_0 = tk.Frame(frame1)
    subFrame2_0.grid(row = 0, column = 0, sticky = "ew")

    strLabel = tk.Label(subFrame2_0, text = "STR:", font = ("Arial", 10))
    strLabel.grid(row = 0, column = 0)

    strInput = tk.Text(subFrame2_0, height = 1, width = 3)
    strInput.grid(row = 0, column = 1)
    strInput.insert(tk.INSERT, character.str)

    subFrame1_1 = tk.Frame(frame1)
    subFrame1_1.grid(row = 0, column = 1, sticky = "ew")

    dexLabel = tk.Label(subFrame1_1, text = "DEX:", font = ("Arial", 10))
    dexLabel.grid(row = 0, column = 0)

    dexInput = tk.Text(subFrame1_1, height = 1, width = 3)
    dexInput.grid(row = 0, column = 1)
    dexInput.insert(tk.INSERT, character.dex)

    subFrame1_2 = tk.Frame(frame1)
    subFrame1_2.grid(row = 0, column = 2, sticky = "ew")

    conLabel = tk.Label(subFrame1_2, text = "CON:", font = ("Arial", 10))
    conLabel.grid(row = 0, column = 0)

    conInput = tk.Text(subFrame1_2, height = 1, width = 3)
    conInput.grid(row = 0, column = 1)
    conInput.insert(tk.INSERT, character.con)

    subFrame1_3 = tk.Frame(frame1)
    subFrame1_3.grid(row = 0, column = 3, sticky = "ew")

    intLabel = tk.Label(subFrame1_3, text = "INT:", font = ("Arial", 10))
    intLabel.grid(row = 0, column = 0)

    intInput = tk.Text(subFrame1_3, height = 1, width = 3)
    intInput.grid(row = 0, column = 1)
    intInput.insert(tk.INSERT, character.intt)

    subFrame1_4 = tk.Frame(frame1)
    subFrame1_4.grid(row = 0, column = 4, sticky = "ew")

    wisLabel = tk.Label(subFrame1_4, text = "WIS:", font = ("Arial", 10))
    wisLabel.grid(row = 0, column = 0)

    wisInput = tk.Text(subFrame1_4, height = 1, width = 3)
    wisInput.grid(row = 0, column = 1)
    wisInput.insert(tk.INSERT, character.wis)

    subFrame1_5 = tk.Frame(frame1)
    subFrame1_5.grid(row = 0, column = 5, sticky = "ew")

    chaLabel = tk.Label(subFrame1_5, text = "CHA:", font = ("Arial", 10))
    chaLabel.grid(row = 0, column = 0)

    chaInput = tk.Text(subFrame1_5, height = 1, width = 3)
    chaInput.grid(row = 0, column = 1)
    chaInput.insert(tk.INSERT, character.cha)

    #frame2 contains proficiency, spell score and saves stats
    frame2 = tk.Frame(mainFrame)
    frame2.grid(row = 3, column = 0, sticky = "ew")
    frame2.columnconfigure(0, weight = 1)
    frame2.columnconfigure(1, weight = 1)
    frame2.columnconfigure(2, weight = 1)

    subFrame2_0 = tk.Frame(frame2)
    subFrame2_0.grid(row = 0, column = 0, sticky = "ew")

    profLabel = tk.Label(subFrame2_0, text = "Proficiency:", font = ("Arial", 10))
    profLabel.grid(row = 0, column = 0)

    profInput = tk.Text(subFrame2_0, height = 1, width = 3)
    profInput.grid(row = 0, column = 1)
    profInput.insert(tk.INSERT, character.prof)

    subFrame2_1 = tk.Frame(frame2)
    subFrame2_1.grid(row = 0, column = 1, sticky = "ew")

    spellScoreLabel = tk.Label(subFrame2_1, text = "Spell Score:", font = ("Arial", 10))
    spellScoreLabel.grid(row = 0, column = 0)

    spellScoreDropdown = ttk.Combobox(subFrame2_1, values = ("STR", "DEX", "CON", "INT", "WIS", "CHA"), state = "readonly")
    spellScoreDropdown.grid(row = 0, column = 1)
    if character.spellScore == "STR":
        spellScoreDropdown.current(0)
    elif character.spellScore == "DEX":
        spellScoreDropdown.current(1)
    elif character.spellScore == "CON":
        spellScoreDropdown.current(2)
    elif character.spellScore == "INT":
        spellScoreDropdown.current(3)
    elif character.spellScore == "WIS":
        spellScoreDropdown.current(4)
    elif character.spellScore == "CHA":
        spellScoreDropdown.current(5)

    subFrame2_2 = tk.Frame(frame2)
    subFrame2_2.grid(row = 0, column = 2, sticky = "ew")

    initiativeLabel = tk.Label(subFrame2_2, text = "Initiative:", font = ("Arial", 10))
    initiativeLabel.grid(row = 0, column = 0)

    initiativeInput = tk.Text(subFrame2_2, height = 1, width = 3)
    initiativeInput.grid(row = 0, column = 1)
    initiativeInput.insert(tk.INSERT, character.initiative)

    subFrame2_3 = tk.Frame(frame2)
    subFrame2_3.grid(row = 0, column = 3, sticky = "ew")

    savesLabel = tk.Label(subFrame2_3, text = "Saves:", font = ("Arial", 10))
    savesLabel.grid(row = 0, column = 0)

    savesInput = tk.Text(subFrame2_3, height = 1, width = 20)
    savesInput.grid(row = 0, column = 1)

    savesText = ", ".join(character.savingThrows)
    savesInput.insert(tk.INSERT, savesText)

    #frame3 has the save button
    frame3 = tk.Frame(mainFrame)
    frame3.grid(row = 4, column = 0, sticky = "ew")
    frame3.columnconfigure(0, weight = 1)

    saveButton = tk.Button(frame3, text = "Save", font = ("Arial", 16))
    saveButton.grid(row = 0, column = 0)

    #print(spellScore)

    saveButton.bind("<Button-1>", lambda event, name = character.name, type = typeDropdown, currentHP = currentHPInput, maxHP = maxHPInput, ac = acInput, str = strInput, dex = dexInput, con = conInput, int = intInput, wis = wisInput, cha = chaInput, prof = profInput, spellScore = spellScoreDropdown, initiative = initiativeInput, saves = savesInput, window = root: saveCharStatChanges(event, name, type, currentHP, maxHP, ac, str, dex, con, int, wis, cha, prof, spellScore, initiative, saves, window))

    
def addCharacterToSimulated(event, name):
    global simulatedCharacters
    global activeCharacter

    character = copy.deepcopy(characterList[name])
    n = character.name + " 1"
    c = 2

    for i in simulatedCharacters:
        if i.name == n:
            n = character.name + " " + str(c)
            c = c + 1

    character.name = n

    simulatedCharacters.append(character)
    activeCharacter = simulatedCharacters[-1]

    addCharacter(None, activeCharacter)



def addCharacter(event, character):
    charSelected = character

    for i in activeDataFrame.winfo_children():
        i.destroy()

    activeDataFrame.rowconfigure(2, weight = 1)

    frame1 = tk.Frame(activeDataFrame)
    frame1.grid(row = 1, column = 0, sticky = "ew")
    frame1.rowconfigure(1, weight = 1)

    try:
        portrait = PIL.Image.open("portraits/" + charSelected.image)
    except:
        portrait = PIL.Image.open("portraits/default.png")

    portrait = portrait.resize((120,120), PIL.Image.ANTIALIAS)
    TKportrait = PIL.ImageTk.PhotoImage(portrait)
    portraitLabel = tk.Label(frame1, image = TKportrait)
    portraitLabel.image = TKportrait
    portraitLabel.grid(row = 0, column = 0)

    frame1Sub1 = tk.Frame(frame1, width = 520)
    frame1Sub1.grid(row = 0, column = 1)
    frame1Sub1.columnconfigure(0, weight = 1)

    
    nameLabel = tk.Label(frame1Sub1, text = charSelected.name, font = ("Arial", 22))
    nameLabel.grid(row = 0, column = 0, sticky = "ew")

    hpGreen = PIL.Image.open("images/hpGreen.png")
    hpRed = PIL.Image.open("images/hpRed.png")

    hpWidth = (charSelected.currentHP / charSelected.hp) * 460

    hpGreen = hpGreen.resize((int(hpWidth + 1), 50), PIL.Image.ANTIALIAS)
    hpGreen = PIL.ImageTk.PhotoImage(hpGreen)

    hpRed = hpRed.resize((int(460 - hpWidth + 1), 50), PIL.Image.ANTIALIAS)
    hpRed = PIL.ImageTk.PhotoImage(hpRed)

    hpBarFrame = tk.Frame(frame1Sub1, padx = 5)
    hpBarFrame.grid(row = 1, column = 0)

    hpGreenLabel = tk.Label(hpBarFrame, image = hpGreen, bd = -2)
    hpGreenLabel.image = hpGreen
    if(hpGreen.width() > 1):
        hpGreenLabel.grid(row = 0, column = 0)

    hpRedLabel = tk.Label(hpBarFrame, image = hpRed, bd = -2)
    hpRedLabel.image = hpRed
    if(hpRed.width() > 1):
        hpRedLabel.grid(row = 0, column = 1)

    frame1Sub2 = tk.Frame(frame1Sub1)
    frame1Sub2.grid(row = 2, column = 0, columnspan = 2)
    frame1Sub2.columnconfigure(0, weight = 1)
    frame1Sub2.columnconfigure(1, weight = 1)

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
        "STR": "black",
        "DEX": "black",
        "CON": "black",
        "INT": "black",
        "WIS": "black",
        "CHA": "black"
        }
    for i in charSelected.savingThrows:
        colors[i] = "blue"

    strLabel = tk.Label(frame2, text = "STR: " + str(charSelected.str), font = ("Arial", 19), fg = colors["STR"])
    dexLabel = tk.Label(frame2, text = "DEX: " + str(charSelected.dex), font = ("Arial", 19), fg = colors["DEX"])
    conLabel = tk.Label(frame2, text = "CON: " + str(charSelected.con), font = ("Arial", 19), fg = colors["CON"])
    intLabel = tk.Label(frame2, text = "INT: " + str(charSelected.intt), font = ("Arial", 19), fg = colors["INT"])
    wisLabel = tk.Label(frame2, text = "WIS: " + str(charSelected.wis), font = ("Arial", 19), fg = colors["WIS"])
    chaLabel = tk.Label(frame2, text = "CHA: " + str(charSelected.cha), font = ("Arial", 19), fg = colors["CHA"])
    profLabel = tk.Label(frame2, text = "Prof: " + str(charSelected.prof), font = ("Arial", 19), fg = "blue")
    editButton = tk.Button(frame2, text = "Edit", font = ("Arial", 19))
    editButton.bind("<Button-1>", lambda event, name = charSelected.name: editCharWindow(name = name))

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
        addButton.bind("<Button-1>", lambda event, name = addButton.master.winfo_children()[1]["text"]: addCharacterToSimulated(event = event, name = name))
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
simulatedCharacters = []

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
            newAttackButton.grid(column=3, row=0, sticky = "ew")
            
            newEditButton = tk.Button(newActionFrame, text = "Edit", font = ("Arial", 15))
            newEditButton.grid(column=3, row=1, sticky = "ew")
            newEditButton.bind("<Button-1>", lambda event, name = action.name: editActionWindow(event = event, name = name))
            
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

            newTypeLabel = tk.Label(newActionFrame, text = action.dcSave+" save" , font = ("Arial", 15))
            newTypeLabel.grid(column=1, row=0)

            newDCLabel = tk.Label(newActionFrame, text = "DC: " + str(action.dcScore), font = ("Arial", 15))
            newDCLabel.grid(column=1, row=1)

            newDamageLabel = tk.Label(newActionFrame, text= "Damage: "+createDiceString(action.damageDice)+"+"+str(action.damageBonus), font= ("Arial", 15))
            newDamageLabel.grid(column=2, row=0)

            newSaveTypeLabel = tk.Label(newActionFrame, text= "Save type: "+action.saveEffect, font = ("Arial, 15"))
            newSaveTypeLabel.grid(column=2, row=1)

            newAttackButton = tk.Button(newActionFrame, text = "Attack!", font = ("Arial", 15))
            newAttackButton.grid(column=3, row=0, sticky = "ew")

            newEditButton = tk.Button(newActionFrame, text = "Edit", font = ("Arial", 15))
            newEditButton.grid(column=3, row=1, sticky = "ew")
            newEditButton.bind("<Button-1>", lambda event, name = action.name: editActionWindow(event = event, name = name))

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