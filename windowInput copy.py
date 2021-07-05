import tkinter as tk
from command import Command, CommandType
from threading import Thread
class WindowInput(tk.Tk):

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
        self.frame = tk.Frame(self, bg=WindowInput.transparentColor)
        self.frame.pack(anchor='n', fill="both", expand=True, side="left")

    def run(self):
        self.mainloop()

    def setCommand(self,listCommands, listCommandsHisto):
        #self.clear()
        #Histo
        newFrame = tk.Frame(self,bg=WindowInput.transparentColor)

        for i in range(8-len(listCommandsHisto)):
            label = tk.Label(newFrame, text="  ",anchor='w' ,bg=WindowInput.transparentColor,font="Arial 12 bold", fg="#FFFFFF")
            label.grid(row=i, column=0,sticky='nesw')
        startIndex = 8-len(listCommandsHisto)
        for i in range(len(listCommandsHisto)):

            commands = listCommandsHisto[i][1]
            player = listCommandsHisto[i][0]
            label = tk.Label(newFrame, text="  "+player,anchor='w' ,bg=WindowInput.transparentColor,font="Arial 12 bold", fg="#FFFFFF")
            label.grid(row=startIndex+i, column=0,sticky='nesw')

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
            label.grid(row=startIndex+i, column=1,sticky='news')
        #Current
        indexStart = 8
        for i in range(len(listCommands)):
            commands = listCommands[i][1]
            player = listCommands[i][0]
            background = ("#444444",WindowInput.transparentColor)[i!=0]

            label = tk.Label(newFrame, text="  "+player,anchor='w' ,bg=background,font="Arial 12 bold", fg="#FFFFFF")
            label.grid(row=indexStart+i, column=0,sticky='nesw')

            
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
            label = tk.Label(newFrame, text=text+"  ",anchor='e' ,bg=background, font="Arial 14 bold",  fg="#FFFFFF")
            label.grid(row=indexStart+i, column=1,sticky='news')

        if(len(listCommands) == 0):
            label = tk.Label(newFrame, text="  ",anchor='w' ,bg="#444444",font="Arial 12 bold", fg="#FFFFFF")
            label.grid(row=indexStart, column=0,sticky='nesw')
            label = tk.Label(newFrame, text="  ",anchor='e' ,bg="#444444", font="Arial 14 bold",  fg="#FFFFFF")
            label.grid(row=indexStart, column=1,sticky='news')
        newFrame.columnconfigure(0,weight=1)
        newFrame.pack(anchor='n', fill="both", expand=True, side="left")
        newFrame.tkraise()
        self.frame.pack_forget()
        #self.frame.destroy()
        self.frame = newFrame

        
    def clear(self):
        for w in self.winfo_children():
            w.destroy()
        
#↑↓→←

if(__name__ == "__main__"):
    w = WindowInput(1)
    
    w.setCommand(["Colin","loris","maxime"],[[(Command.UP,CommandType.PRESS)],[(Command.A,CommandType.HOLD)], [(Command.UP,CommandType.RELEASE),(Command.B,CommandType.RELEASE)]])
    w.mainloop()