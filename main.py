import socket
#import logging
from emoji import demojize
from twichChat import TwitchChat
from pokeraceEngine import Pokerace
from threading import Thread
from configuration import config
"""
logging.basicConfig(filename="./logname.log",
                            filemode='w+',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)"""



BOTNAME = config["botName"]
CHANNEL = config["twitchChannel"]
TOKEN = config["tokenIRCTwitch"] 



pokerace = Pokerace()
twicth = TwitchChat(TOKEN,BOTNAME,CHANNEL)


def onMessage(username, message):
    print(username, message)
    pokerace.messageDecode(username,message)
    


    




twicth.on("message",onMessage)


twicth.start()
