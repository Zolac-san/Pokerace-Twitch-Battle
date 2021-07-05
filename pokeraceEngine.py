from team import Team
from commandDecoder import MessageDecoder
import csv
from threading import Thread
from configuration import config

class Pokerace():
    def __init__(self):
        self.playersTeams ={}
        self.teams = []
        self.teamsThreads = []
        self.loadTeams()


    def loadTeams(self):
        self.teams = []
        i = 1
        
        for row in config["teams"]:
            if(i > 4):
                break
            team = Team(i)
            
            for name in row:
                self.playersTeams[name] = team
                team.addPlayer(name)
            self.teams.append(team)
            i+=1

    def messageDecode(self,username, message):
        commands = MessageDecoder.decode(message)
    
        if( username in self.playersTeams and len(commands)>0):
            self.playersTeams[username].insertCommand(username,commands)



if( __name__ == "__main__"):
    m = Model()
    for t in m.teams:
        print(t)