from enum import Enum


class Command(Enum):
    A = 0
    B = 1
    UP = 2
    DOWN = 3
    LEFT = 4
    RIGHT = 5
    R = 6
    L = 7
    START = 8
    SELECT = 9
    WAIT = 10
    RESTART = 11

class CommandType(Enum):
    PRESS = 0
    HOLD = 1
    RELEASE = 2