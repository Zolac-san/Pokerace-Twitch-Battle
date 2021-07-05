from command import Command, CommandType

"""
command : 
    - (hold/release) haut : n
    - (hold/release) bas : s
    - (hold/release) gauche : w
    - (hold/release) droite : e
    - (hold/release) a
    - (hold/release) b
    - (hold/release) R
    - (hold/release) L
    - start
    - select

    - wait : p
    - restart
"""
class MessageDecoder():
    def decode(message):
        #message = message.strim()
        commandList = [] # max 2
        if(message == "p"):
            commandList.append((Command.WAIT,))
        elif(message == "start"):
            commandList.append((Command.START,CommandType.PRESS))
        elif(message == "select"):
            commandList.append((Command.SELECT,CommandType.PRESS))
        elif(message == "restart"):
            commandList.append((Command.RESTART,))
        else:
            commandPossible =  message.split(" ")[0:2]
            commandMove = False
            for cmd in commandPossible:
                #press
                c = None
                t = None
                if(len(cmd)==1):
                    c = MessageDecoder.strToCommand(cmd)
                    t =CommandType.PRESS
                if(len(cmd)==2):
                    c = MessageDecoder.strToCommand(cmd[0])
                    t = MessageDecoder.strToCommandType(cmd[1])
                if(c == Command.UP or c==Command.UP or c==Command.UP or c==Command.UP):
                    if(commandMove):
                        c = None
                    else:
                        commandMove = True
                if( c != None and t != None):
                    mem = c
                    commandList.append((c,t))

        return commandList


    def strToCommand(s):
        if(s=="z"):
            return Command.UP
        elif(s=="s"):
            return Command.DOWN
        elif(s=="q"):
            return Command.LEFT
        elif(s=="d"):
            return Command.RIGHT
        elif(s=="a"):
            return Command.A
        elif(s=="b"):
            return Command.B
        elif(s=="l"):
            return Command.L
        elif(s=="r"):
            return Command.R
        else:
            return None

    def strToCommandType(s):
        if(s=="+"):
            return CommandType.HOLD
        elif(s=="-"):
            return CommandType.RELEASE
        else:
            return None