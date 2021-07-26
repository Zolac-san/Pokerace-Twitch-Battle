import subprocess
from time import sleep
import os
from command import Command, CommandType
from configuration import config

class WindowGame():

    commandToKeyboard = {
        Command.A : "x",
        Command.B : "z",
        Command.L : "a",
        Command.R : "s",
        Command.UP : "Up",
        Command.DOWN : "Down",
        Command.LEFT : "Left",
        Command.RIGHT : "Right",
        Command.SELECT : "Backspace",
        Command.START : "Return"
    }

    def __init__(self,num):
        self.process = None
        self.__idWindow = None
        self.num = num
        self.launched = False
        self.numSave = 1

    def launch(self):
        if(self.process == None):
            self.process = subprocess.Popen(["mgba",f"./team{self.num}/{self.numSave}.gba", "-4","-C","fpsTarget=120"])
            sleep(2.5)
            subprocess.call(f"xdotool search --name \"mGBA\" set_window --name \"poke{self.num}\"", shell=True)
            self.__idWindow = int(subprocess.check_output(f"xdotool search --name \"poke{self.num}\"", shell=True))

    def shutdown(self):
        if(self.process != None):
            self.process.terminate()
            self.process = None
            self.__idWindow = None


    def __sendInput(self,command,key):
        os.system(f"xdotool {command} --window {self.__idWindow} --delay 150 {key}")

    def __pressKey(self,key):
        self.__sendInput("key",key)

    def ___holdKey(self, key):
        self.__sendInput("keydown",key)

    def __releaseKey(self,key):
        self.__sendInput("keyup",key)

    def command(self,listCommand):
        if(len(listCommand) == 1):
            self.__execOnecommand(listCommand[0])
        elif(len(listCommand) == 2):
            if(listCommand[0][1] == listCommand[1][1]):
                keyToPress = self.commandToKeyboard[listCommand[0][0]] + "+" +self.commandToKeyboard[listCommand[1][0]]
                if(listCommand[0][1] == CommandType.PRESS):
                    self.__pressKey(keyToPress)
                elif(listCommand[0][1] == CommandType.HOLD):
                    self.___holdKey(keyToPress)
                elif(listCommand[0][1] == CommandType.RELEASE):
                    self.__releaseKey(keyToPress)
            else:
                for command in listCommand:
                    self.__execOnecommand(command)
    
    def __execOnecommand(self, command):
        if(command[0] == Command.WAIT):
            pass
        elif(command[0] == Command.RESTART):
            self.restart()
        else:
            keyToPress = self.commandToKeyboard[command[0]]
            if(command[1] == CommandType.PRESS):
                self.__pressKey(keyToPress)
            elif(command[1] == CommandType.HOLD):
                self.___holdKey(keyToPress)
            elif(command[1] == CommandType.RELEASE):
                self.__releaseKey(keyToPress)



    def restart(self):
        self.numSave += 1
        self.shutdown()
        if(self.numSave <= config["nbSave"] ):
            self.launch()


if( __name__ == "__main__"):
    w = WindowGame(1)
    w.launch()
    sleep(30)
    w.shutdown()
    