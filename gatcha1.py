import numpy as np
import random
import time
import pandas as pd

def user_create():
    # routine for creating a user dataframe
    i=0
    
def user_load():
    # routine for loading a user dataframe
    i=0

def user_save():
    # routine for saving a user dataframe
    i=0

def rolling():
    roll = random.randint(1,100)
    if roll <= 3:
        print("You pulled an SSR!")
    if (roll > 3) & (roll <=30):
        print("You pulled an SR!")
    else:
        print("You pulled a R!") 
flag = 0

def roll11():
    for i in range(0,11):
        rolling()
        print(i)

while(flag==0):
    roll11()
    time.sleep(1)
