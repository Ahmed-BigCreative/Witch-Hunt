from ctypes.wintypes import ULONG
from time import sleep
from pathways import *
import random
skip = False
import sys,time
from tkinter import N

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)




def path_1():
    sleep(2)
    print("Welcome to pathway one, you have joined the war on the side of the angels")


def path_2():
    sleep(2)
    print("Welcome to pathway two, you have joined the war on the side of the witches")
    sprint("3 days later...")
    sprint("You wake up and open your window")

def path_3():
    sleep(1)
    print("Welcome to pathway three, you have not joined a side of the war. Welcome to the land of demons and beasts, good luck.")