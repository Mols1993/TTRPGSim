import tkinter as tk
from tkinter import Toplevel, ttk
import PIL.Image
from PIL.Image import init
import math, re, random, copy, PIL.ImageTk, os
import inspect

mainColor = "#0000C4"

class Character:
    #type = name = image = hp = ac = prof = savingThrows = actions = currentHP = initiative = 0

    def __init__(self):#Entonces
        self.scores = {}
        self.type = 0
        self.name = ""
        self.image = ""
        self.hp = 0
        self.ac = 0
        self.prof = 0
        self.savingThrows = []
        self.actions = []
        self.currentHP = 0
        self.initiative = 0
        self.abilities = []
        self.saveAdvantage = "Normal"
        self.targeted = False

    def __repr__(self):
        return "Name: " + str(self.name) + "\n" + "Type: " + str(self.type) + "\n" + "Image: " + str(self.image) + "\n" + "HP: " + str(self.hp) + "\n" + "Current HP: " + str(self.currentHP) + "\n" + "AC: " + str(self.ac) + "\n" + "Initiative: " + str(self.initiative) + "\n" + "STR: " + str(self.scores["STR"]) + "\n" + "DEX: " + str(self.scores["DEX"]) + "\n" + "CON: " + str(self.scores["CON"]) + "\n" + "INT: " + str(self.scores["INT"]) + "\n" + "WIS: " + str(self.scores["WIS"]) + "\n" + "CHA: " + str(self.scores["CHA"]) + "\n" + "Proficiency Bonus: " + str(self.prof) + "\n" + "Saving Throws: " + str(self.savingThrows) + "\n" + "Abilities: " + str(self.abilities) + "\n" + "Save Advantage: " + str(self.saveAdvantage) + "\n" + "Targeted: " + str(self.targeted) + "\n" + "Actions: " + str(self.actions) + "\n"

class Action:
    #type = name = score = attackBonus = damageDice = damageBonus = crit = critDice = critBonus = dcSave = dcScore = saveEffect = hybrids = prof = 0

    def __init__(self):
        self.type = 0
        self.name = ""
        self.score = ""
        self.attackBonus = 0
        self.damageDice = []
        self.damageBonus = 0
        self.crit = 0
        self.critDice = []
        self.dcSave = ""
        self.dcScore = 0
        self.saveEffect = ""
        self.hybrids = []
        self.prof = False

    def __repr__(self):
        if(self.type == 1):
            return "Name: " + str(self.name) + "\n" + "Type: " + str(self.type) + "\n" + "Score: " + str(self.score) + "\n" + "Attack Bonus: " + str(self.attackBonus) + "\n" + "Damage Dice: " + str(self.damageDice) + "\n" + "Damage Bonus: " + str(self.damageBonus) + "\n" + "Crit: " + str(self.crit) + "\n" + "Crit Dice: " + str(self.critDice) + "\n" + "Crit Bonus: " + str(self.critBonus) + "\n"
        elif(self.type == 2):
            return "Name: " + str(self.name) + "\n" + "Type: " + str(self.type) + "\n" + "Save DC: " + str(self.dcSave) + "\n" + "Damage Dice: " + str(self.damageDice) + "\n" + "Damage Bonus: " + str(self.damageBonus) + "\n" + "Save Effect: " + self.saveEffect + "\n"
        elif(self.type == 3):
            return "Name: " + str(self.name) + "\n" + "Type: " + str(self.type) + "\n" + "Hybrids: " + str(self.hybrids) + "\n"

def parseCharacter(name):
    f = open("characters/" + name, "r")
    character = Character()
    character.type = f.readline().strip(" \n").upper()
    character.name = f.readline().strip(" \n")
    character.image = f.readline().strip(" \n")
    character.hp = int(f.readline().strip(" \n"))
    character.currentHP = character.hp
    character.ac = int(f.readline().strip(" \n"))
    character.initiative = int(f.readline().strip(" \n"))
    scores = f.readline().strip(" \n").split(", ")
    character.scores["STR"] = int(scores[0])
    character.scores["DEX"] = int(scores[1])
    character.scores["CON"] = int(scores[2])
    character.scores["INT"] = int(scores[3])
    character.scores["WIS"] = int(scores[4])
    character.scores["CHA"] = int(scores[5])
    character.prof = int(f.readline().strip(" \n"))
    character.savingThrows = f.readline().strip(" \n").upper().split(", ")
    character.abilities = f.readline().strip(" \n").upper().split(", ")

    token = f.readline().strip(" \n")

    while token == "*":
        action = Action()
        type = int(f.readline().strip(" \n"))
        action.type = type
        action.name = f.readline().strip(" \n")
        if(type == 1): #Attack
            p = f.readline().strip(" \n").upper()
            action.prof = True
            if(p == "FALSE"):
                action.prof = False
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
                action.critDice.append(i)#Nice
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

        elif(type == 3): #Spell with save
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

#print(actionList)
#print("---------------------------------------------------------------------")

characterFiles = os.listdir(path="characters")
characterList = {}

for i in characterFiles:
    parseCharacter(i)

#print(characterList)
#print("---------------------------------------------------------------------")

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

charFilterFrame = tk.Frame(charFrame, height = 150, width=300)
charFilterFrame.grid(column=0, row=0, sticky="EW")

charFilterFrame.columnconfigure(0, weight=1)

charFilterButtonPC = tk.Button(charFilterFrame, text="PCs", font = ("Arial", 19), relief = tk.GROOVE, borderwidth = 4, bg="#b0b0b0")
charFilterButtonPC.grid(column=0, row=0, sticky="EW")

charFilterButtonNPC = tk.Button(charFilterFrame, text="NPCs",font = ("Arial", 19), relief = tk.GROOVE, borderwidth = 4, bg="#b0b0b0")
charFilterButtonNPC.grid(column=0, row=1, sticky="EW")

charFilterButtonBoss = tk.Button(charFilterFrame, text="Bosses",font = ("Arial", 19), relief = tk.GROOVE, borderwidth = 4, bg="#b0b0b0")
charFilterButtonBoss.grid(column=0, row=2, sticky="EW")



#########################

charListFrame = tk.Frame(charFrame, height = 760, width=300)
charListFrame.grid(column=0, row=1)
charListFrame.grid_propagate(0)

charListScrollbar = tk.Scrollbar(charListFrame, orient="vertical")
charListScrollbar.grid(column=1, row=0, sticky = "NS")

charListCanvas = tk.Canvas(charListFrame, bg=mainColor , height = 760, width=279, scrollregion = (0,0,279,760))
charListCanvas.grid(column=0, row=0, sticky="EW")
charListCanvas.grid_propagate(0)

charListCanvas.configure(yscrollcommand = charListScrollbar.set)
charListScrollbar.configure(command = charListCanvas.yview)

charListMagicFrame = tk.Frame(charListCanvas, bg=mainColor, height=760, width=279)
charListMagicFrame.grid(column=0, row=0)

charListCanvas.create_window((0,0), window=charListMagicFrame, anchor="nw")

activeCharFrame = tk.Frame(mainWindow, height = 910, width = 600, relief = tk.GROOVE, borderwidth = 1)
activeCharFrame.grid(column=1, row=0)
activeCharFrame.grid_propagate(0)

activeDataFrame = tk.Frame(activeCharFrame, height = 300, width = 600)
activeDataFrame.grid(column=0, row=0)
activeDataFrame.grid_propagate(0)
activeDataFrame.columnconfigure(0, weight=1)

attackListFrame = tk.Frame(activeCharFrame, height = 400, width = 600)
attackListFrame.grid(column=0, row=1)
attackListFrame.grid_propagate(0)

combatLogFrame = tk.Frame(activeCharFrame, height = 210, width = 600)
combatLogFrame.grid(column=0, row=2)
combatLogFrame.grid_propagate(0)

otherCharsFrame = tk.Frame(mainWindow, height = 910, width = 400, relief = tk.GROOVE, borderwidth = 1)
otherCharsFrame.grid(column=2, row=0)
otherCharsFrame.grid_propagate(0)

turnsFrame = tk.Frame(mainWindow, height = 910, width = 300, relief = tk.GROOVE, borderwidth = 1)
turnsFrame.grid(column=3, row=0)
turnsFrame.grid_propagate(0)
turnsFrame.rowconfigure(0, weight=0)
turnsFrame.rowconfigure(1, weight=1)

def saveType1StatChanges(event, score, attackBonus, damageDice, damageBonus, crit, critDice, critBonus, prof, character, action, window):
    score = score.get()
    attackBonus = int(attackBonus.get("@0, 0", tk.END).strip(" \n"))
    damageDice = damageDice.get("@0, 0", tk.END).strip(" \n").split(", ")
    damageBonus = int(damageBonus.get("@0, 0", tk.END).strip(" \n"))
    crit = int(crit.get("@0, 0", tk.END).strip(" \n"))
    critDice = critDice.get("@0, 0", tk.END).strip(" \n").split(", ")
    critBonus = int(critBonus.get("@0, 0", tk.END).strip(" \n"))
    prof = prof.get()
    if(prof):
        prof = True
    else:
        prof = False

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
    act.prof = prof

    createMoveList(activeCharacter)
    createDefendersList()

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
    createDefendersList()

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

        subFrame1_3 = tk.Frame(frame1)
        subFrame1_3.grid(row = 0, column = 3, sticky = "ew")

        profLabel = tk.Label(subFrame1_3, text = "Proficient:", font = ("Arial", 10))
        profLabel.grid(row = 0, column = 0)

        v = tk.IntVar()
        profCheck = ttk.Checkbutton(subFrame1_3, variable = v)
        profCheck.grid(row = 0, column = 1)
        if(action.prof):
            v.set(1)
        else:
            v.set(0)

        frame2 = tk.Frame(mainFrame)
        frame2.grid(row = 3, column = 0, sticky = "ew")
        frame2.columnconfigure(0, weight = 1)

        saveButton = tk.Button(frame2, text = "Save", font = ("Arial", 16))
        saveButton.grid(row = 0, column = 0)

        #type = name = score = attackBonus = damageDice = damageBonus = crit = critDice = critBonus = dcSave = saveEffect = hybrids = 0
        saveButton.bind(saveButton.bind("<Button-1>", lambda event = event, score = attackScoreDropdown, attackBonus = attackBonusInput, damageDice = damageDiceInput, damageBonus = damageBonusInput, crit = critRangeInput, critDice = critDiceInput, critBonus = critBonusInput, prof = v, character = activeCharacter.name, action = action.name, window = root: saveType1StatChanges(event, score, attackBonus, damageDice, damageBonus, crit, critDice, critBonus, prof, character, action, window)))

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

    elif action.type == 3:
        frame0 = tk.Frame(mainFrame)
        frame0.grid(row = 1, column = 0)
        frame0.columnconfigure(0, weight = 1)
        frame0.columnconfigure(1, weight = 1)
        frame0.columnconfigure(2, weight = 1)
        frame0.columnconfigure(3, weight = 1)

        subFrame0_0 = tk.Frame(frame0)
        subFrame0_0.grid(row = 0, column = 0, sticky = "ew")

        dcSaveLabel = tk.Label(subFrame0_0, text = "Check DC:", font = ("Arial", 10))
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

        dcScoreLabel = tk.Label(subFrame0_1, text = "Check Score:", font = ("Arial", 10))
        dcScoreLabel.grid(row = 0, column = 0)

        dcScoreInput = tk.Text(subFrame0_1, height = 1, width = 3)
        dcScoreInput.grid(row = 0, column = 1)
        dcScoreInput.insert(tk.INSERT, action.dcScore)

        subFrame0_2 = tk.Frame(frame0)
        subFrame0_2.grid(row = 0, column = 2, sticky = "ew")

        saveEffectLabel = tk.Label(subFrame0_2, text = "Failed Effect:", font = ("Arial", 10))
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


def saveCharStatChanges(event, char, type, currentHP, maxHP, ac, str, dex, con, intt, wis, cha, prof, initiative, saves, window):

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
    initiative = int(initiative.get("@0, 0", tk.END).strip(" \n"))
    saves = saves.get("@0, 0", tk.END).strip(" \n").upper().split(", ")

    #type = name = image = hp = ac = str = dex = con = intt = wis = cha = prof = spellScore = savingThrows = actions = currentHP = 0


    char.type = type
    char.currentHP = currentHP
    char.hp = maxHP
    char.ac = ac
    char.scores["STR"] = str
    char.scores["DEX"] = dex
    char.scores["CON"] = con
    char.scores["INT"] = intt
    char.scores["WIS"] = wis
    char.scores["CHA"] = cha
    char.prof = prof
    char.initiative = initiative
    char.savingThrows = saves

    setActiveCharFrame(None, activeCharacter)
    createDefendersList()
    window.destroy()

def editCharWindowParser(event, name):
    #This absolute unit of a line traverses the hierarchy tree from the "Edit" button to the character name in the activeDataFrame
    #charName = event.widget.master.master.winfo_children()[0].winfo_children()[1].winfo_children()[0]["text"]
    #editCharWindow(characterList[charName])
    print("This does nothing now")

def editCharWindow(char):
    character = char
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
    strInput.insert(tk.INSERT, character.scores["STR"])

    subFrame1_1 = tk.Frame(frame1)
    subFrame1_1.grid(row = 0, column = 1, sticky = "ew")

    dexLabel = tk.Label(subFrame1_1, text = "DEX:", font = ("Arial", 10))
    dexLabel.grid(row = 0, column = 0)

    dexInput = tk.Text(subFrame1_1, height = 1, width = 3)
    dexInput.grid(row = 0, column = 1)
    dexInput.insert(tk.INSERT, character.scores["DEX"])

    subFrame1_2 = tk.Frame(frame1)
    subFrame1_2.grid(row = 0, column = 2, sticky = "ew")

    conLabel = tk.Label(subFrame1_2, text = "CON:", font = ("Arial", 10))
    conLabel.grid(row = 0, column = 0)

    conInput = tk.Text(subFrame1_2, height = 1, width = 3)
    conInput.grid(row = 0, column = 1)
    conInput.insert(tk.INSERT, character.scores["CON"])

    subFrame1_3 = tk.Frame(frame1)
    subFrame1_3.grid(row = 0, column = 3, sticky = "ew")

    intLabel = tk.Label(subFrame1_3, text = "INT:", font = ("Arial", 10))
    intLabel.grid(row = 0, column = 0)

    intInput = tk.Text(subFrame1_3, height = 1, width = 3)
    intInput.grid(row = 0, column = 1)
    intInput.insert(tk.INSERT, character.scores["INT"])

    subFrame1_4 = tk.Frame(frame1)
    subFrame1_4.grid(row = 0, column = 4, sticky = "ew")

    wisLabel = tk.Label(subFrame1_4, text = "WIS:", font = ("Arial", 10))
    wisLabel.grid(row = 0, column = 0)

    wisInput = tk.Text(subFrame1_4, height = 1, width = 3)
    wisInput.grid(row = 0, column = 1)
    wisInput.insert(tk.INSERT, character.scores["WIS"])

    subFrame1_5 = tk.Frame(frame1)
    subFrame1_5.grid(row = 0, column = 5, sticky = "ew")

    chaLabel = tk.Label(subFrame1_5, text = "CHA:", font = ("Arial", 10))
    chaLabel.grid(row = 0, column = 0)

    chaInput = tk.Text(subFrame1_5, height = 1, width = 3)
    chaInput.grid(row = 0, column = 1)
    chaInput.insert(tk.INSERT, character.scores["CHA"])

    #frame2 contains proficiency and saves stats
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

    saveButton.bind("<Button-1>", lambda event, char = character, type = typeDropdown, currentHP = currentHPInput, maxHP = maxHPInput, ac = acInput, str = strInput, dex = dexInput, con = conInput, int = intInput, wis = wisInput, cha = chaInput, prof = profInput, initiative = initiativeInput, saves = savesInput, window = root: saveCharStatChanges(event, char, type, currentHP, maxHP, ac, str, dex, con, int, wis, cha, prof, initiative, saves, window))

    
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
    character.rolledInit = rollInitiative(character)
    
    simulatedCharacters.append(character)
    activeCharacter = simulatedCharacters[-1]

    setActiveCharFrame(None, activeCharacter)
    createTurnList()

#3d8, INTd8, 8dINT

def setActiveCharFrame(event, character):
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

    hpWidth = max(0, (charSelected.currentHP / charSelected.hp) * 460)

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

    strLabel = tk.Label(frame2, text = "STR: " + str(charSelected.scores["STR"]), font = ("Arial", 19), fg = colors["STR"])
    dexLabel = tk.Label(frame2, text = "DEX: " + str(charSelected.scores["DEX"]), font = ("Arial", 19), fg = colors["DEX"])
    conLabel = tk.Label(frame2, text = "CON: " + str(charSelected.scores["CON"]), font = ("Arial", 19), fg = colors["CON"])
    intLabel = tk.Label(frame2, text = "INT: " + str(charSelected.scores["INT"]), font = ("Arial", 19), fg = colors["INT"])
    wisLabel = tk.Label(frame2, text = "WIS: " + str(charSelected.scores["WIS"]), font = ("Arial", 19), fg = colors["WIS"])
    chaLabel = tk.Label(frame2, text = "CHA: " + str(charSelected.scores["CHA"]), font = ("Arial", 19), fg = colors["CHA"])
    profLabel = tk.Label(frame2, text = "Prof: " + str(charSelected.prof), font = ("Arial", 19), fg = "blue")
    editButton = tk.Button(frame2, text = "Edit", font = ("Arial", 19))
    editButton.bind("<Button-1>", lambda event, char = charSelected: editCharWindow(char = char))

    strLabel.grid(row = 0, column = 0)
    dexLabel.grid(row = 0, column = 1)
    conLabel.grid(row = 0, column = 2)
    intLabel.grid(row = 1, column = 0)
    wisLabel.grid(row = 1, column = 1)
    chaLabel.grid(row = 1, column = 2)
    profLabel.grid(row = 2, column = 0)
    editButton.grid(row = 2, column = 2)
    
    createMoveList(activeCharacter)
    resetTargets()
    resetAdvantages()
    createDefendersList()
    createTurnList()



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
        
    if(len(charList) > 7):
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

def toggleCharfilter(filter, event):
    if(filter == "PC"):
        global flagPCfilter
        if(flagPCfilter):
            event.widget.configure(bg="#b0b0b0")
        else:
            event.widget.configure(bg="#f0f0f0")
        flagPCfilter= not flagPCfilter
        createCharList()
    elif(filter == "NPC"):
        global flagNPCfilter
        if(flagNPCfilter):
            event.widget.configure(bg="#b0b0b0")
        else:
            event.widget.configure(bg="#f0f0f0")
        flagNPCfilter = not flagNPCfilter
        createCharList()
    elif(filter == "BOSS"):
        global flagBOSSfilter
        if(flagBOSSfilter):
            event.widget.configure(bg="#b0b0b0")
        else:
            event.widget.configure(bg="#f0f0f0")
        flagBOSSfilter = not flagBOSSfilter
        createCharList()
        
charFilterButtonPC.bind("<Button-1>", lambda event: toggleCharfilter("PC", event))
charFilterButtonNPC.bind("<Button-1>", lambda event: toggleCharfilter("NPC", event))
charFilterButtonBoss.bind("<Button-1>", lambda event: toggleCharfilter("BOSS", event))


createCharList()




#SECTION B

activeCharacter = None
simulatedCharacters = []
selectedAttack = None
selectedAttackAdvantage = "Normal"

def calculateHit(defendingCharacter):
    
    score = getScore(selectedAttack.score, activeCharacter)
    partial = 20.0-defendingCharacter.ac+selectedAttack.attackBonus+getModifier(score)
      
    if(selectedAttack.prof):
        partial += activeCharacter.prof
    
    hit = partial/20.0
    #print(hit)
    crit = calculateCrit()
    if(hit < crit/100):
        hit = crit / 100
    if(selectedAttackAdvantage == "Disadvantage"):
        return hit*hit*100
    elif(selectedAttackAdvantage == "Advantage"):
        return (1-(1-hit)*(1-hit))*100
    else:
        return hit*100
    
    
def calculateCrit():
    crit = selectedAttack.crit * 0.05
    if(selectedAttackAdvantage == "Disadvantage"):
        return crit*crit*100
    elif(selectedAttackAdvantage == "Advantage"):
        return (1-(1-crit)*(1-crit))*100
    else:
        return crit*100
    
def calculateSave(defendingCharacter):
    
    score = getScore(selectedAttack.dcSave, defendingCharacter)
    partial = 20.0-selectedAttack.dcScore+getModifier(score)
    
    if(selectedAttack.dcSave in defendingCharacter.savingThrows):
        partial += defendingCharacter.prof
        
    save = partial/20.0
    if(defendingCharacter.saveAdvantage == "Disadvantage"):
        return save*save*100
    elif(defendingCharacter.saveAdvantage == "Advantage"):
        return (1-(1-save)*(1-save))*100
    else:
        return save*100
        

def getScore(score, character):
    return character.scores[score]

def getModifier(score):
    result = (score-10)/2
    return int(result)


def selectAttack(attack, event):
    global  selectedAttack
    if (selectedAttack != attack):
        selectedAttack = attack
        if(selectedAttack.type == 1):
            state = event.widget.master.winfo_children()[4].get()
            global selectedAttackAdvantage 
            selectedAttackAdvantage = state
            createDefendersList()
        else:
            createDefendersList()
    else:
        selectedAttack = None
        createDefendersList()
        
def targetChar(target, event):
    if(target.targeted):
        target.targeted = False
        event.widget.configure(text = "Not Targeted", font = ("Arial", 14), bg = "#f0f0f0")
    
    else:
        target.targeted = True
        event.widget.configure(text = "Targeted", font = ("Arial", 14), bg = "#C40000")
        
def comboBoxType1Update(attack, event):
    state = event.widget.get()
    if(selectedAttack == attack):
        global selectedAttackAdvantage
        selectedAttackAdvantage = state
        createDefendersList()
        
def comboBoxType2Update(defender, event):
    state = event.widget.get()
    defender.saveAdvantage = state
    save = calculateSave(defender)
    event.widget.master.winfo_children()[1].configure(text = str(round(save, 2)) + "% to pass Save", font = ("Arial", 14))

def comboBoxType3Update(defender, event):
    state = event.widget.get()
    defender.saveAdvantage = state
    save = calculateSave(defender)
    event.widget.master.winfo_children()[1].configure(text = str(round(save, 2)) + "% to pass Check", font = ("Arial", 14))


def createMoveList(activeCharacter):

    for widget in attackListFrame.winfo_children():
        widget.destroy()

    attackListScrollbar = tk.Scrollbar(attackListFrame, orient="vertical")
    attackListScrollbar.grid(column=1, row=0, sticky = "NS")

    attackListCanvas = tk.Canvas(attackListFrame, bg="#00C400", height=400, width=579, scrollregion = (0,0,579,400))
    attackListCanvas.grid(column=0, row=0, sticky="EW")
    attackListCanvas.grid_propagate(0)

    attackListCanvas.configure(yscrollcommand = attackListScrollbar.set)
    attackListScrollbar.configure(command = attackListCanvas.yview)

    attackListMagicFrame = tk.Frame(attackListCanvas, bg=mainColor, height=400, width=579)
    attackListMagicFrame.grid(column=0, row=0)
    attackListMagicFrame.grid_propagate(0)

    attackListCanvas.create_window((0,0), window=attackListMagicFrame, anchor="nw")
    
    count = 0
    for action in  activeCharacter.actions:
        if (action.type == 1 or action.type == 2):
            count += 1
    if (count > 4):
        attackListCanvas.configure(scrollregion = (0,0,579,100*count))
        attackListMagicFrame.configure(height=100*count)
    
    count = 0
    for action in activeCharacter.actions:
        if (action.type == 1):
            newActionFrame = tk.Frame(attackListMagicFrame, height=100, width=579, relief = tk.GROOVE, borderwidth = 4)
            newActionFrame.grid(column=0, row=count)
            newActionFrame.grid_propagate(0)
            
            newActionButton = tk.Button(newActionFrame, text = action.name, font = ("Arial", 18))
            newActionButton.bind("<Button-1>", lambda event, name = action: selectAttack(attack = name, event = event))
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
            newCombobox.bind('<<ComboboxSelected>>', lambda event, name = action: comboBoxType1Update(attack = name, event = event))
            
            newAttackButton = tk.Button(newActionFrame, text = "Attack!", font = ("Arial", 15))
            newAttackButton.grid(column=3, row=0, sticky = "ew")
            newAttackButton.bind("<Button-1>", lambda event, action = action: executeType1(action))
            
            newEditButton = tk.Button(newActionFrame, text = "Edit", font = ("Arial", 15))
            newEditButton.grid(column=3, row=1, sticky = "ew")
            newEditButton.bind("<Button-1>", lambda event, name = action.name: editActionWindow(event = event, name = name))
            
            newActionFrame.columnconfigure(0, weight = 2)
            newActionFrame.columnconfigure(1, weight = 2)
            newActionFrame.columnconfigure(2, weight = 2)
            newActionFrame.columnconfigure(3, weight = 2)
            
            count += 1
        elif (action.type == 2 or action.type == 3):
            newActionFrame = tk.Frame(attackListMagicFrame, height=100, width=579, relief = tk.GROOVE, borderwidth = 4)
            newActionFrame.grid(column=0, row=count)
            newActionFrame.grid_propagate(0)

            newActionButton = tk.Button(newActionFrame, text = action.name, font = ("Arial", 18))
            newActionButton.bind("<Button-1>", lambda event, name = action: selectAttack(attack = name, event = event))
            newActionButton.grid(column=0, row=0, rowspan=2)

            if(action.type == 2):
                newTypeLabel = tk.Label(newActionFrame, text = action.dcSave+" save" , font = ("Arial", 15))
                newTypeLabel.grid(column=1, row=0)
            elif(action.type == 3):
                newTypeLabel = tk.Label(newActionFrame, text = action.dcSave+" check" , font = ("Arial", 15))
                newTypeLabel.grid(column=1, row=0)

            newDCLabel = tk.Label(newActionFrame, text = "DC: " + str(action.dcScore), font = ("Arial", 15))
            newDCLabel.grid(column=1, row=1)

            newDamageLabel = tk.Label(newActionFrame, text= "Damage: "+createDiceString(action.damageDice)+"+"+str(action.damageBonus), font= ("Arial", 15))
            newDamageLabel.grid(column=2, row=0)

            if(action.type == 2):
                newSaveTypeLabel = tk.Label(newActionFrame, text= "Save effect: "+action.saveEffect, font = ("Arial, 15"))
                newSaveTypeLabel.grid(column=2, row=1)
            elif(action.type == 3):
                newSaveTypeLabel = tk.Label(newActionFrame, text= "Fail effect: "+action.saveEffect, font = ("Arial, 15"))
                newSaveTypeLabel.grid(column=2, row=1)

            newAttackButton = tk.Button(newActionFrame, text = "Attack!", font = ("Arial", 15))
            newAttackButton.grid(column=3, row=0, sticky = "ew")
            if(action.type == 2):
                newAttackButton.bind("<Button-1>", lambda event, action = action: executeType2(action))
            elif(action.type == 3):
                newAttackButton.bind("<Button-1>", lambda event, action = action: executeType3(action))

            newEditButton = tk.Button(newActionFrame, text = "Edit", font = ("Arial", 15))
            newEditButton.grid(column=3, row=1, sticky = "ew")
            newEditButton.bind("<Button-1>", lambda event, name = action.name: editActionWindow(event = event, name = name))

            newActionFrame.columnconfigure(0, weight = 2)
            newActionFrame.columnconfigure(1, weight = 2)
            newActionFrame.columnconfigure(2, weight = 2)
            newActionFrame.columnconfigure(3, weight = 2)

            count += 1

def checkInitEntry(c, what, new):
    character = list(filter(lambda i: i.name == c, simulatedCharacters))[0]
    if(what.isdigit()):
        if(new == ""):
            new = 0
        character.rolledInit = int(new)
        return True
    else:
        return False


def createTurnList():
    
    for widget in turnsFrame.winfo_children():
        widget.destroy()

    turnContainerFrame = tk.Frame(turnsFrame, height=860, width=300)
    turnContainerFrame.grid(row=0, column=0)

    turnListScrollbar = tk.Scrollbar(turnContainerFrame, orient="vertical")
    turnListScrollbar.grid(column=1, row=0, sticky = "NS")

    turnListCanvas = tk.Canvas(turnContainerFrame, bg="#00C400", height=860, width=279, scrollregion = (0,0,279,810))
    turnListCanvas.grid(column=0, row=0, sticky="EW")
    turnListCanvas.grid_propagate(0)

    turnListCanvas.configure(yscrollcommand = turnListScrollbar.set)
    turnListScrollbar.configure(command = turnListCanvas.yview)

    turnListMagicFrame = tk.Frame(turnListCanvas, bg=mainColor, height=860, width=279)
    turnListMagicFrame.grid(column=0, row=0)
    turnListMagicFrame.grid_propagate(0)

    turnListCanvas.create_window((0,0), window=turnListMagicFrame, anchor="nw")

    turnControlFrame = tk.Frame(turnsFrame, height=50, width=300)
    turnControlFrame.grid(row=1, column=0, sticky="NEWS")
    turnControlFrame.columnconfigure(0, weight=1)
    turnControlFrame.columnconfigure(1, weight=1)
    turnControlFrame.columnconfigure(2, weight=1)
    turnControlFrame.rowconfigure(0, weight=1)

    sortButton = tk.Button(turnControlFrame, text="Sort", font=("Arial", 10))
    sortButton.grid(row=0, column=0, sticky="NEWS")
    sortButton.configure(command = sortByInit)
    
    rerollButton = tk.Button(turnControlFrame, text="Reroll All", font=("Arial", 10))
    rerollButton.grid(row=0, column=1, sticky="NEWS")
    rerollButton.configure(command = rerollInitiative)

    nextButton = tk.Button(turnControlFrame, text="Next Turn", font=("Arial", 10))
    nextButton.grid(row=0, column=2, sticky="NEWS")
    nextButton.configure(command = nextTurn)

    if(len(simulatedCharacters) > 8):
        turnListCanvas.configure(scrollregion = (0,0, 279, 100*(len(simulatedCharacters))))
        turnListMagicFrame.configure(height=100*(len(simulatedCharacters)))

    count = 0

    for simchar in simulatedCharacters:

        if simchar == activeCharacter:
            frameColor = "#b0b0b0"
        else:
            frameColor = "#f0f0f0"

        charFrame = tk.Frame(turnListMagicFrame, height=100, width=279, relief = tk.GROOVE, borderwidth = 4, bg=frameColor)
        charFrame.grid(column=0, row=count)
        charFrame.grid_propagate(0)
        charFrame.columnconfigure(0, weight=1)
        charFrame.columnconfigure(1, weight=1)
        charFrame.columnconfigure(2, weight=1)

        subFrame1 = tk.Frame(charFrame, width = 169, height = 92, bg=frameColor)
        subFrame1.grid(column=0, row=0)
        subFrame1.grid_propagate(0)

        nameFrame = tk.Frame(subFrame1, width = 169 , height = 60, bg=frameColor)
        nameFrame.grid(column=0, row=0, sticky = "w")
        nameFrame.grid_propagate(0)

        try:
            portrait = PIL.Image.open("portraits/" + simchar.image)
        except:
            portrait = PIL.Image.open("portraits/default.png")

        portrait = portrait.resize((50,50), PIL.Image.ANTIALIAS)
        TKportrait = PIL.ImageTk.PhotoImage(portrait)

        portraitLabel = tk.Label(nameFrame, image = TKportrait)
        portraitLabel.image = TKportrait
        portraitLabel.grid(row=0, column=0, padx=2, pady=2)

        nameLabel = tk.Label(nameFrame, text = simchar.name , font = ("Arial", 10), bg=frameColor, wraplength = 110)
        nameLabel.grid(row=0 , column = 1, sticky = "ew")

        buttonsFrame = tk.Frame(subFrame1, width = 169, height = 32)
        buttonsFrame.grid(column=0, row=1)
        buttonsFrame.grid_propagate(0)
        buttonsFrame.columnconfigure(0, weight = 1)
        buttonsFrame.rowconfigure(0, weight = 1)

        setButton = tk.Button(buttonsFrame, text = "Set Active", font=("Arial", 9))
        setButton.grid(row=0, column = 0, sticky = "NEWS")
        setButton.bind("<Button-1>", lambda event, char = simchar: setAsActive(char))

        subFrame2 = tk.Frame(charFrame, width=30, height = 92 , bg=frameColor)
        subFrame2.grid(row = 0, column = 1, sticky = "ns")
        subFrame2.rowconfigure(0, weight = 1)
        subFrame2.rowconfigure(1, weight = 1)
        subFrame2.columnconfigure(0, weight = 1)

        arrowUp = PIL.Image.open("images/arrowUp.png")
        arrowDown = PIL.Image.open("images/arrowDown.png")
        resize = 25
        arrowUp = arrowUp.resize((resize, resize), PIL.Image.ANTIALIAS)
        arrowUp = PIL.ImageTk.PhotoImage(arrowUp)
        arrowDown = arrowDown.resize((resize, resize), PIL.Image.ANTIALIAS)
        arrowDown = PIL.ImageTk.PhotoImage(arrowDown)

        upButton = tk.Button(subFrame2, image = arrowUp)
        upButton.image = arrowUp
        upButton.grid(row=0, column = 0, sticky = "NEWS")
        upButton.bind("<Button-1>", lambda event, char = simchar: moveTurnUP(char))

        downButton = tk.Button(subFrame2, image = arrowDown)
        downButton.image = arrowDown
        downButton.grid(row=1, column = 0, sticky = "NEWS")
        downButton.bind("<Button-1>", lambda event, char = simchar: moveTurnDOWN(char))

        subFrame3 = tk.Frame(charFrame, width=72, height = 92 , bg=frameColor)
        subFrame3.grid(row=0, column=2)
        subFrame3.grid_propagate(0)
        subFrame3.rowconfigure(0, weight=1)
        subFrame3.rowconfigure(1, weight=1)
        subFrame3.columnconfigure(0, weight=1)

        initFrame = tk.Frame(subFrame3, height= 60, width=72, bg=frameColor)
        initFrame.grid(row=0, column=0)
        initFrame.grid_propagate(0)
        initFrame.columnconfigure(0, weight=1)
        initFrame.rowconfigure(0, weight=1)

        #initLabel = tk.Label(initFrame, text=str(simchar.rolledInit), font=("Arial", 34), bg=frameColor)
        #initLabel.grid(row=0, column=0, sticky = "NEWS")
        func = initFrame.register(checkInitEntry)
        initEntry = ttk.Entry(initFrame, validate = "key", validatecommand = (func, simchar.name, "%S", "%P"), font=("Arial", 34))
        initEntry.grid(row=0, column=0, sticky = "nsew")
        initEntry.insert(tk.INSERT, simchar.rolledInit)


        editFrame = tk.Frame(subFrame3, height = 32,  width= 72)
        editFrame.grid(row=1, column=0)
        editFrame.grid_propagate(0)
        editFrame.columnconfigure(0, weight=1)
        editFrame.rowconfigure(0, weight=1)

        editButton = tk.Button(editFrame, text="Reroll", font=("Arial", 9))
        editButton.grid(row=0, column=0, sticky="NEWS")
        editButton.bind("<Button-1>", lambda event, character = simchar: rerollInitiative(character = character))
        editButton.grid_propagate(0)

        count += 1
        
############################

def resetAdvantages():
    for i in simulatedCharacters:
        i.saveAdvantage = "Normal"

def resetTargets():
    for i in simulatedCharacters:
        i.targeted = False

#Section D
def createDefendersList():

    defendListFrame = otherCharsFrame
    for widget in otherCharsFrame.winfo_children():
        widget.destroy()

    defendListScrollbar = tk.Scrollbar(defendListFrame, orient="vertical")
    defendListScrollbar.grid(column=1, row=0, sticky = "NS")

    defendListCanvas = tk.Canvas(defendListFrame, bg="#00C400", height=910, width = 379, scrollregion = (0, 0, 379, 910))
    defendListCanvas.grid(column=0, row=0, sticky="EW")
    defendListCanvas.grid_propagate(0)

    defendListCanvas.configure(yscrollcommand = defendListScrollbar.set)
    defendListScrollbar.configure(command = defendListCanvas.yview)

    defendListMagicFrame = tk.Frame(defendListCanvas, bg=mainColor, height=910, width=379)
    defendListMagicFrame.grid(column=0, row=0)
    defendListMagicFrame.grid_propagate(0)

    defendListCanvas.create_window((0,0), window=defendListMagicFrame, anchor="nw")
    
    if(selectedAttack is None):
        frameHeight = 100
        if(len(simulatedCharacters) > 10):
            defendListCanvas.configure(scrollregion = (0,0, 379, 100*(len(simulatedCharacters)-1)))
            defendListMagicFrame.configure(height=100*(len(simulatedCharacters)-1))
    else:
        frameHeight = 180
        if(len(simulatedCharacters) > 6):
            defendListCanvas.configure(scrollregion = (0,0, 379, 180*(len(simulatedCharacters)-1)))
            defendListMagicFrame.configure(height=180*(len(simulatedCharacters)-1))

    count = 0
    for simchar in simulatedCharacters:
        if(simchar == activeCharacter):
            continue
        defenderFrame = tk.Frame(defendListMagicFrame, height=frameHeight, width=379, relief = tk.GROOVE, borderwidth = 4)
        defenderFrame.grid(column=0, row=count)
        defenderFrame.grid_propagate(0)

        statFrame = tk.Frame(defenderFrame, height = 100, width = 379)
        statFrame.grid(column=0, row=0)
        statFrame.grid_propagate(0)
        statFrame.columnconfigure(0, weight = 0)
        statFrame.columnconfigure(1, weight = 1)

        try:
            portrait = PIL.Image.open("portraits/" + simchar.image)
        except:
            portrait = PIL.Image.open("portraits/default.png")

        portrait = portrait.resize((80,80), PIL.Image.ANTIALIAS)
        TKportrait = PIL.ImageTk.PhotoImage(portrait)

        portraitLabel = tk.Label(statFrame, image = TKportrait)
        portraitLabel.image = TKportrait
        portraitLabel.grid(row=0, column = 0, padx = 4, pady=4)

        subFrame = tk.Frame(statFrame)
        subFrame.grid(row=0, column= 1, sticky = "EWNS")
        subFrame.grid_propagate(0)
        subFrame.columnconfigure(0, weight = 1)
        subFrame.rowconfigure(0, weight = 1)
        subFrame.rowconfigure(1, weight = 1)
        subFrame.rowconfigure(2, weight = 1)

        nameLabel = tk.Label(subFrame, text = simchar.name , font = ("Arial", 17))
        nameLabel.grid(row=0, column=0, sticky = "ew")

        hpGreen = PIL.Image.open("images/hpGreen.png")
        hpRed = PIL.Image.open("images/hpRed.png")

        hpWidth = max(0, (simchar.currentHP / simchar.hp) * 265)

        hpGreen = hpGreen.resize((int(hpWidth + 1), 25), PIL.Image.ANTIALIAS)
        hpGreen = PIL.ImageTk.PhotoImage(hpGreen)

        hpRed = hpRed.resize((int(265 - hpWidth + 1), 25), PIL.Image.ANTIALIAS)
        hpRed = PIL.ImageTk.PhotoImage(hpRed)

        hpBarFrame = tk.Frame(subFrame, padx = 5)
        hpBarFrame.grid(row = 1, column = 0)

        hpGreenLabel = tk.Label(hpBarFrame, image = hpGreen, bd = -2)
        hpGreenLabel.image = hpGreen
        if(hpGreen.width() > 1):
            hpGreenLabel.grid(row = 0, column = 0)

        hpRedLabel = tk.Label(hpBarFrame, image = hpRed, bd = -2)
        hpRedLabel.image = hpRed
        if(hpRed.width() > 1):
            hpRedLabel.grid(row = 0, column = 1)

        hpACFrame = tk.Frame(subFrame)
        hpACFrame.grid(row = 2, column=0, columnspan = 2)
        hpACFrame.columnconfigure(0, weight = 1)
        hpACFrame.columnconfigure(1, weight = 1)

        hpLabel = tk.Label(hpACFrame, text = "HP: " + str(int(simchar.currentHP)) + "/" + str(simchar.hp), font = ("Arial", 14))
        hpLabel.grid(row = 0, column = 0, sticky = "ew")

        acLabel = tk.Label(hpACFrame, text = "AC" + str(simchar.ac), font = ("Arial", 14))
        acLabel.grid(row = 0, column = 1, sticky = "ew")
        
        if(selectedAttack is not None):

            probabilityFrame = tk.Frame(defenderFrame, height = 40, width = 379)
            probabilityFrame.grid(row=1, column=0)
            probabilityFrame.grid_propagate(0)
            probabilityFrame.columnconfigure(0, weight = 2)
            probabilityFrame.columnconfigure(1, weight = 1)

            if(selectedAttack.type == 1):

                hit = calculateHit(simchar)
                #print(hit)
                hitLabel = tk.Label(probabilityFrame, text = str(round(hit, 2)) + "% Hit", font = ("Arial", 20))
                hitLabel.grid(row=0, column=0, rowspan=2)

                crit = calculateCrit()
                critLabel = tk.Label(probabilityFrame, text = str(round(crit, 2)) + "% Crit", font = ("Arial", 14))
                critLabel.grid(row=1, column=1)

            if(selectedAttack.type == 2):
    
                rollCombobox = ttk.Combobox(probabilityFrame)
                rollCombobox.grid(row = 0, column = 0)
                rollCombobox["values"] = ("Normal", "Advantage", "Disadvantage")
                if(simchar.saveAdvantage == "Normal"):
                    rollCombobox.current(0)
                elif(simchar.saveAdvantage == "Advantage"):
                    rollCombobox.current(1)
                elif(simchar.saveAdvantage == "Disadvantage"):
                    rollCombobox.current(2)
                rollCombobox["state"] = "readonly"
                rollCombobox.bind('<<ComboboxSelected>>', lambda event, name = simchar: comboBoxType2Update(defender = name, event = event))
    
                save = calculateSave(simchar)
                saveLabel = tk.Label(probabilityFrame, text = str(round(save, 2)) + "% to pass Save", font = ("Arial", 14))
                saveLabel.grid(row = 0, column=1)
    
            if(selectedAttack.type == 3):
                rollCombobox = ttk.Combobox(probabilityFrame)
                rollCombobox.grid(row = 0, column = 0)
                rollCombobox["values"] = ("Normal", "Advantage", "Disadvantage")
                if(simchar.saveAdvantage == "Normal"):
                    rollCombobox.current(0)
                elif(simchar.saveAdvantage == "Advantage"):
                    rollCombobox.current(1)
                elif(simchar.saveAdvantage == "Disadvantage"):
                    rollCombobox.current(2)
                rollCombobox["state"] = "readonly"
                rollCombobox.bind('<<ComboboxSelected>>', lambda event, name = activeCharacter: comboBoxType3Update(defender = name, event = event))
    
                save = calculateSave(activeCharacter)
                saveLabel = tk.Label(probabilityFrame, text = str(round(save, 2)) + "% to pass Check", font = ("Arial", 14))
                saveLabel.grid(row = 0, column=1)
    
    
            buttonFrame = tk.Frame(defenderFrame, height = 40, width = 379)
            buttonFrame.grid(row=2, column=0)
            buttonFrame.grid_propagate(0)
            buttonFrame.columnconfigure(0, weight = 1)
            buttonFrame.columnconfigure(1, weight = 1)
    
            targetButton = tk.Button(buttonFrame)
            if(simchar.targeted):
                targetButton.configure(text = "Targeted", font = ("Arial", 14), bg = "#C40000")
            else:
                targetButton.configure(text = "Not Targeted", font = ("Arial", 14))
            targetButton.grid(row = 0, column = 0, sticky = "NEWS")
            targetButton.bind("<Button-1>", lambda event, name = simchar: targetChar(name, event))
    
            editButton = tk.Button(buttonFrame, text = "Edit", font = ("Arial", 14))
            editButton.grid(row = 0, column = 1, sticky = "NEWS")
            editButton.bind("<Button-1>", lambda event, char = simchar: editCharWindow(char))

        count += 1

def diceRoller(dice, bonus = 0):
    rollResults = 0
    for i in dice:
        d = re.findall(r'[0-9]+', i)
        diceNum = int(d[0])
        diceType = int(d[1])

        for j in range(diceNum):
            rollResults = rollResults + random.randint(1, diceType)
    rollResults = rollResults + bonus
    return rollResults

combatLog = []

def cullUpdates():
    #print(int(combatLogText.index('end-1c').split('.')[0]))
    del combatLog[0]
    combatLogText.config(state = tk.NORMAL)
    combatLogText.delete('1.0', tk.END)
    for i in combatLog:
        combatLogText.insert(tk.INSERT, i + "\n")
    combatLogText.config(state = tk.DISABLED)
    
def rollInitiative(character):
    bonus = getModifier(character.scores["DEX"])+character.initiative
    return diceRoller(["1d20"], bonus)

def sortByInit():
    simulatedCharacters.sort(key=lambda x: x.rolledInit, reverse=True)
    createTurnList()
    
def rerollInitiative(character = None):
    if(character == None):
        for simchar in simulatedCharacters:
            simchar.rolledInit = rollInitiative(simchar)
        createTurnList()
    else:
        character.rolledInit = rollInitiative(character)
        createTurnList()
    
def nextTurn():
    global activeCharacter
    idx = simulatedCharacters.index(activeCharacter)
    if(idx == (len(simulatedCharacters)-1)):
        setAsActive(simulatedCharacters[0])
    else:
        setAsActive(simulatedCharacters[idx+1])

def setAsActive(character):
    global activeCharacter
    activeCharacter = character
    setActiveCharFrame(None, activeCharacter)
    
def moveTurnUP(character):
    idx = simulatedCharacters.index(character)
    if(idx != 0):
        simulatedCharacters[idx-1], simulatedCharacters[idx] = simulatedCharacters[idx], simulatedCharacters[idx-1]
        createTurnList()
        
def moveTurnDOWN(character):
    idx = simulatedCharacters.index(character)
    if(idx != (len(simulatedCharacters)-1)):
        simulatedCharacters[idx+1], simulatedCharacters[idx] = simulatedCharacters[idx], simulatedCharacters[idx+1]
        createTurnList()

def updateLog(log):
    #print(log)
    combatLog.append(log)
    combatLogText.config(state = tk.NORMAL)
    combatLogText.delete('1.0', tk.END)
    for i in combatLog:
        combatLogText.insert(tk.INSERT, i + "\n")
    combatLogText.config(state = tk.DISABLED)
    #print(combatLogText.dlineinfo("end-2l"))
    while(combatLogText.dlineinfo("end-1l") == None):
        cullUpdates()


def executeType1(action):
    targetedCharacters = list(filter(lambda i: i.targeted, simulatedCharacters))
    logString = activeCharacter.name + " used " + action.name + " with " + str(len(targetedCharacters)) + " targets"
    updateLog(logString)
    for i in targetedCharacters:
        target = i
        toHit = diceRoller(["1d20"])
        if(selectedAttackAdvantage == "Advantage"):
            toHit = max(toHit, diceRoller(["1d20"]))
        elif(selectedAttackAdvantage == "Disadvantage"):
            toHit = min(toHit, diceRoller(["1d20"]))
        
        crit = False
        if(toHit > 20 - action.crit):
            crit = True
        toHit = toHit + action.attackBonus + math.floor((activeCharacter.scores[action.score] - 10) / 2)
        if(action.prof):
            toHit = toHit + activeCharacter.prof

        if(toHit + action.attackBonus >= target.ac or crit):
            damage = diceRoller(action.damageDice, action.damageBonus)
            critDamage = 0
            critText = ""
            if(crit):
                critDamage = diceRoller(action.critDice, action.critBonus)
                critText = "critically "
            damage = damage + critDamage
            target.currentHP = target.currentHP - damage
            
            logString = activeCharacter.name + "(Roll: " + str(toHit) + ") " + critText + "hit " + target.name + " (AC: " + str(target.ac) + ")"
            updateLog(logString)

            logString = action.name + " did " + str(damage) + " damage"
            updateLog(logString)
        else:
            logString = activeCharacter.name + "(Roll: " + str(toHit) + ") missed " + target.name + " (AC: " + str(target.ac) + ")"
            updateLog(logString)
    
    createDefendersList()

def executeType2(action):
    targetedCharacters = list(filter(lambda i: i.targeted, simulatedCharacters))
    logString = activeCharacter.name + " used " + action.name + " with " + str(len(targetedCharacters)) + " targets"
    updateLog(logString)
    damage = diceRoller(action.damageDice, action.damageBonus)
    for i in targetedCharacters:
        target = i
        state = i.saveAdvantage
        save = diceRoller(["1d20"])
        if(state == "Advantage"):
            save = max(save, diceRoller(["1d20"]))
        elif(state == "Disadvantage"):
            save = min(save, diceRoller(["1d20"]))

        if(action.dcSave in target.savingThrows):
            save = save + target.prof

        save = save + math.floor((target.scores[action.dcSave] - 10) / 2)
        
        logString = target.name + "(Save: " + str(save) + ") failed the save (DC: " + str(action.dcScore) + ") for FULL effect and took " + str(damage) + " damage"

        if(save >= action.dcScore):
            if(action.saveEffect == "HALF"):
                if("EVASION" not in target.abilities):
                    damage = math.floor(damage / 2)
                    logString = target.name + "(Save: " + str(save) + ") passed the save (DC: " + str(action.dcScore) + ") for HALF effect and took " + str(damage) + " damage"
                else:
                    damage = 0
                    logString = target.name + "(Save: " + str(save) + ") passed the save (DC: " + str(action.dcScore) + "), used EVASION for NONE effect and took 0 damage"
            elif(action.saveEffect == "NONE"):
                damage = 0
                logString = target.name + "(Save: " + str(save) + ") passed the save (DC: " + str(action.dcScore) + ") for NONE effect and took 0 damage"
            elif(action.saveEffect == "OTHER"):
                logString = target.name + "(Save: " + str(save) + ") passed the save (DC: " + str(action.dcScore) + ") for OTHER effect and took " + str(damage) + " damage"

        if(save < action.dcScore and "EVASION" in target.abilities):
            damage =  math.floor(damage / 2)
            logString = target.name + "(Save: " + str(save) + ") failed the save (DC: " + str(action.dcScore) + "), used EVASION for HALF effect and took " + str(damage) + " damage"

        target.currentHP = target.currentHP - damage

        updateLog(logString)
    
    createDefendersList()

def executeType3(action):
    targetedCharacters = list(filter(lambda i: i.targeted, simulatedCharacters))
    logString = activeCharacter.name + " used " + action.name + " with " + str(len(targetedCharacters)) + " targets"
    updateLog(logString)
    for i in targetedCharacters:
        target = i
        state = i.saveAdvantage
        save = diceRoller(["1d20"])
        if(state == "Advantage"):
            save = max(save, diceRoller(["1d20"]))
        elif(state == "Disadvantage"):
            save = min(save, diceRoller(["1d20"]))

        save = save + math.floor((activeCharacter.scores[action.dcSave] - 10) / 2)

        damage = diceRoller(action.damageDice, action.damageBonus)

        if(save < action.dcScore):
            if(action.saveEffect == "HALF"):
                damage = math.floor(damage / 2)
                logString = activeCharacter.name + "(Roll: " + str(save) + ", DC: " + str(action.dcScore) + ") missed " + target.name + " for HALF effect"
                updateLog(logString)
                logString = action.name + " did " + str(damage) + " damage"
                updateLog(logString)
            elif(action.saveEffect == "NONE"):
                damage = 0
                logString = activeCharacter.name + "(Roll: " + str(save) + ", DC: " + str(action.dcScore) + ") missed " + target.name + " for NONE effect"
                updateLog(logString)
                logString = action.name + " did " + str(damage) + " damage"
                updateLog(logString)
            elif(action.saveEffect == "OTHER"):
                logString = activeCharacter.name + "(Roll: " + str(save) + ", DC: " + str(action.dcScore) + ") missed " + target.name + " for OTHER effect"
                updateLog(logString)
                logString = action.name + " did " + str(damage) + " damage"
                updateLog(logString)
        else:
            logString = activeCharacter.name + "(Roll: " + str(save) + ", DC: " + str(action.dcScore) + ") hit " + target.name
            updateLog(logString)
            logString = action.name + " did " + str(damage) + " damage"
            updateLog(logString)

        target.currentHP = target.currentHP - damage
    
    createDefendersList()

combatLogScrollbar = tk.Scrollbar(combatLogFrame, orient="vertical")
combatLogScrollbar.grid(column=1, row=0, sticky = "NS")

combatLogTextCanvas = tk.Canvas(combatLogFrame, bg="#FFFFFF", height=210, width=579, scrollregion = (0,0,579,325))
combatLogTextCanvas.grid(row = 0, column = 0, sticky="ew")
combatLogTextCanvas.columnconfigure(0, weight = 1)
combatLogTextCanvas.grid_propagate(0)

combatLogTextCanvas.configure(yscrollcommand = combatLogScrollbar.set)
combatLogScrollbar.configure(command = combatLogTextCanvas.yview)

combatLogTextFrame = tk.Frame(combatLogTextCanvas, bg="#FFFFFF", height=910, width=579)
combatLogTextFrame.grid(row = 0, column = 0)
combatLogTextFrame.grid_propagate(0)

combatLogTextCanvas.create_window((0,0), window=combatLogTextFrame, anchor="nw")

combatLogText = tk.Text(combatLogTextFrame, height = 20, width = 72, bg = "#000000", fg = "#00FF00", wrap = tk.WORD, state = tk.DISABLED)
combatLogText.grid(row = 0, column = 0, sticky = "ew")

mainWindow.mainloop()