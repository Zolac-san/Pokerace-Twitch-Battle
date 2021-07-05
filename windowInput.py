import tkinter as tk
from command import Command, CommandType
from threading import Thread
class WindowInput(tk.Tk):

    lengthHisto = 8

    transparentColor = "#000000"

    commandToStr = {
        Command.A : " A",
        Command.B : " B",
        Command.L : " L",
        Command.R : " R",
        Command.UP : "↑",
        Command.DOWN : "↓",
        Command.LEFT : "←",
        Command.RIGHT : "→",
        Command.SELECT : "SELECT",
        Command.START : "START",
        Command.RESTART : "RESTART",
        Command.WAIT : "⟲"
    }
    #⛂⛀
    commandTypeToStr = {
        CommandType.PRESS : "",
        CommandType.HOLD : "⛀",
        CommandType.RELEASE : "⛂"
    }

    def __init__(self, num):
        tk.Tk.__init__(self)
        self.num = num
        self.title(f"inputTeam{num}")
        self.geometry("150x520")
        self.configure(bg=WindowInput.transparentColor)
        self.setupBlank()
        self.placeNewBgSelect()
        self.lastBlanck = True



    def setupBlank(self):
        for i in range(0,self.lengthHisto+1):
            self.addBlanck()

    def addBlanck(self):
        newFrame = tk.Frame(self)
        label = tk.Label(newFrame, text="",anchor='w' ,bg=WindowInput.transparentColor,font="Arial 12 bold", fg="#FFFFFF")
        label.pack(anchor='n', fill="both", expand=True, side="top")
        newFrame.pack(anchor='n', fill="x", expand=False, side="top")

    def insertNewCommand(self,username,commands):
        
        newFrame = tk.Frame(self,bg=WindowInput.transparentColor)
        label = tk.Label(newFrame, text="  "+username,anchor='w' ,bg=WindowInput.transparentColor,font="Arial 12 bold", fg="#FFFFFF")
        label.grid(row=0, column=0,sticky='nesw')

        text = ""
        if(len(commands) == 1):
            if(len(commands[0]) == 1):
                text = WindowInput.commandToStr[commands[0][0]]
            else:
                text = WindowInput.commandTypeToStr[commands[0][1]] + " " + WindowInput.commandToStr[commands[0][0]]
        else:
            if(commands[0][1] == commands[1][1]):
                text = WindowInput.commandTypeToStr[commands[0][1]] + " " + WindowInput.commandToStr[commands[0][0]] + "+"+WindowInput.commandToStr[commands[1][0]]
            else:
                text = WindowInput.commandTypeToStr[commands[0][1]] + " " + WindowInput.commandToStr[commands[0][0]] + " + " +WindowInput.commandTypeToStr[commands[1][1]] + " " + WindowInput.commandToStr[commands[1][0]]

        label = tk.Label(newFrame, text=text+"  ",anchor='e' ,bg=WindowInput.transparentColor, font="Arial 14 bold",  fg="#FFFFFF")
        label.grid(row=0, column=1,sticky='news')
        newFrame.columnconfigure(0,weight=1)
        
        if(self.lastBlanck):
            self.lastBlanck = False
            self.winfo_children()[-2].destroy()
            self.placeNewBgSelect()

        newFrame.pack(anchor='n', fill="x", expand=False, side="top")
        

    def placeNewBgSelect(self):
        l = self.winfo_children()
        print(len(l),":",l)
        self.__changeColor(l[self.lengthHisto-1],WindowInput.transparentColor)
        self.__changeColor(l[self.lengthHisto],"#444444")


    def __changeColor(self,frame,color):
        for w in frame.winfo_children():
            w.config(bg=color)

    def passToNextCommand(self):
        l = self.winfo_children()
        if(len(l)==9):
            self.lastBlanck = True
            self.addBlanck()
        
        l[0].destroy()
        self.placeNewBgSelect()

    
        
#↑↓→←

if(__name__ == "__main__"):
    w = WindowInput(1)
    
    w.setCommand(["Colin","loris","maxime"],[[(Command.UP,CommandType.PRESS)],[(Command.A,CommandType.HOLD)], [(Command.UP,CommandType.RELEASE),(Command.B,CommandType.RELEASE)]])
    w.mainloop()