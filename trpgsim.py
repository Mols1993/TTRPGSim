import tkinter as tk
from tkinter import ttk
import math
import random
import PIL.Image
import PIL.ImageTk

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



mainWindow.mainloop()