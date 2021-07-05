import socket
#import logging
import threading
from emoji import demojize
from listener import Listener

server = "irc.twitch.tv"
port = 6667


"""
event on:
    - connect
    - message
    - disconnect
"""

class TwitchChat(Listener):
    def __init__(self, token, botName, channel ):
        self.token = token
        self.botName = botName
        self.channel = channel
        self.__running = False
        self.__connected = False

    def start(self):
        if(self.__running):
            return
        self.__running = True
        self.__connected = False
        
        self.__connect()
        self.__readingMessage()

    def __connect(self):
        self.__irc = socket.socket()
        self.__irc.connect((server, port))
        self.__irc.send(f"PASS {self.token}\n".encode('utf-8'))
        self.__irc.send(f"NICK {self.botName}\n".encode('utf-8'))
        self.__irc.send(f"JOIN #{self.channel}\n".encode('utf-8'))
        while(not self.__connected and self.__running):
            resp = self.__irc.recv(2048).decode('utf-8')
            #logging.info(resp)
            if("End of /NAMES list" in resp):
                self.__connected = True
                self.trigger("connect")
                print("Connect")

    def __readingMessage(self):
        while(self.__running):
            resp = self.__irc.recv(2048).decode('utf-8')
            for line in resp.split("\r\n"):
                if line == "":
                    continue
                elif line == "PING :tmi.twitch.tv":
                    self.sendMessage("PONG :tmi.twitch.tv")
                    continue
                else:
                    response = demojize(line)
                    response = response[1:]
                    username = response.split("!",1)[0]
                    message = str(response.split(":",1)[1])
                    self.trigger("message", (username,message))

    def stop(self):
        if(self.__running):
            self.__running = False
            self.__connected = False
            self.__irc.send(f"PART #{self.channel}\n".encode('utf-8'))
            self.trigger("disconnect")

    def sendMessage(self, message):
        if(self.__connected and self.__running):
            self.__irc.send((message +"\n").encode("utf-8"))
            #logging.info("Sending : "+message)