from windowGame import WindowGame
from threading import Thread
from windowInput import WindowInput
from time import sleep, time
from command import Command


class Team():

    def __init__(self,num):
        print(f"Setup team {num}")
        self.num = num
        self.window = WindowGame(num)
        self.players = []
        self.captain = None
        self.index = 0
        self.tmpListCommands = []
        self.listCommands = []
        self.listCommandsHisto = []
        self.lastExec = time()
        

        self.window.launch()
        
        #self.threadCommand = Thread(target=self.readCommand)
        #self.threadCommand.start()
        self.threadWindowInput = Thread(target=self.runWindowInput)
        self.threadWindowInput.start()

        self.thread = Thread(target=self.start)
        self.thread.start()


    def start(self):
        
        while True:
            if(len(self.tmpListCommands) > 0):
                command = self.tmpListCommands.pop(0)
                self.listCommands.append(command)
                self.windowInput.insertNewCommand(command[0],command[1])
            
            t = time()
            if(len(self.listCommands) > 0 and (t - self.lastExec) >= 1.15 ):
                self.lastExec = t
                c = self.listCommands.pop(0)
                self.window.command(c[1])
                self.windowInput.passToNextCommand()
                

    def runWindowInput(self):
        self.windowInput = WindowInput(self.num)
        self.windowInput.mainloop()


    def addPlayer(self,name):
        if( len(self.players)== 0 ):
            self.captain = name
        self.players.append(name)

    def insertCommand(self,username, lcommand):
        if(lcommand[0][0] == Command.RESTART and username != self.captain):
            return
        indexPlayer = self.players.index(username)
        if(indexPlayer == self.index and len(self.listCommands) <8):
            self.tmpListCommands.append((username,lcommand))
            self.index = (self.index+1)%len(self.players)
            
    """
    def readCommand(self):
        delaiCommand = 1.0
        while True:
            if(len(self.listCommands) != 0):
                c = self.listCommands.pop(0)
                self.listCommandsHisto.append(c)
                if(len(self.listCommandsHisto)>8):
                    self.listCommandsHisto.pop(0)
                #self.listCommandsPlayer.pop(0)
                self.window.command(c[1])
                sleep(1)
    """
    def __str__(self):
        return f"Team {self.num} : {', '.join(self.players)}"
