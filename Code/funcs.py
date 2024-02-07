from time import *
from random import randint
from PIL import Image
import glob
import os

# a clear console is a nice one
os.system('cls' if os.name == 'nt' else 'clear')

# defines useful varibles
start = 0
information = []
Format = "%H:%M:%S"
app = None
Time = 0


def FileHandling(filename):
    # file handling
    information = []
    with open(filename, 'r') as f:
        temp = f.read().split("\n")

    for i in range(0, len(temp), 2):
        temp_list = []
        # makes 2d array
        temp_list.append(temp[i].capitalize())
        temp_list.append(temp[i+1].capitalize())
        information.append(temp_list)
    return information


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


def getFiles():
    temp = []
    os.chdir("../Code")
    for file in glob.glob("*.txt"):
        temp.append(file)
    return temp
