from time import *
from random import randint
from PIL import Image
import os

# a clear console is a nice one
os.system('cls' if os.name == 'nt' else 'clear')

# defines useful varibles
start = 0
information = []
Format = "%H:%M:%S"
file_name = 'keywords.txt'
app = None
Time = 0

# file handling
with open(file_name, 'r') as f:
    temp = f.read().split("\n")


for i in range(0, len(temp), 2):
    temp_list = []
    # makes 2d array
    temp_list.append(temp[i].capitalize())
    temp_list.append(temp[i+1].capitalize())
    information.append(temp_list)


def changeFile():
    # add change file code here
    pass


def start_timer():
    # starts/resets the timer
    global start
    start = time()


def get_timer():
    # get the timer at the perticular time
    end = time()
    now = end-start
    Timer = gmtime(now)
    Time = strftime(Format, Timer)
    return Time
