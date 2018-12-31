# The purpose of this file is to hold utility functions that are commonly used

from __future__ import unicode_literals, print_function
import os   # Used to clear terminal
import random
# from colorama import *
import time
import pickle 
# init(autoreset=True) # init colors and reset to white each time
from prompt_toolkit import print_formatted_text, HTML

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal

def show(text):
    #  Displays text, waits for 'enter' before continuing.
    t = text.split('@')
    if len(t) == 1: #no @ in string
        print(text)
        raw_input("... ")
    else: # color
        printWithColor(t[1],t[2], before=t[0], after = t[3])
        raw_input("... ")

def printc(text):
    #  Given syntax like "this word is @colored@yellow@" will color all text between first two @'s. ie colored becomes yellow
    # please only one color per call
    t = text.split('@')
    if len(t) == 1: #no @ in string
        print(text)
    else: # color
        try:
            if t[4] == None:
                printWithColor(t[1],t[2], before=t[0], after = t[3])
        except IndexError:
            printWithColor(t[0],t[1], after = t[2])
        else: printc( t[4:] )

# prints colored text
def printWithColor(text, color, before="", after=""):
    s = before
    if color == "red":
        s +=  '<ansired>' + text + '</ansired>'
    elif color == "green":
        s +=  '<ansigreen>' + text + '</ansigreen>'
    elif color == "yellow":
        s +=  '<ansiyellow>' + text + '</ansiyellow>'
    elif color == "blue":
        s +=  '<ansiblue>' + text + '</ansiblue>'
    elif color == "magenta":
        s +=  '<ansimagenta>' + text + '</ansimagenta>'
    elif color == "cyan":
        s +=  '<ansicyan>' + text + '</ansicyan>'
    else:
        s +=  '<ansiwhite>' + text + '</ansiwhite>'
    s += after
    print_formatted_text(HTML(s))

# formats text in ways besides color. only bold and underline and reverse seem to work in my vs code terminal
def formatText(text, format):
    if format == "bold" or format == "b":
        s = '<b>' + text + '</b>'
        print_formatted_text(HTML(s))
    elif format == "blink":
        s = '<blink>' + text + '</blink>'
        print_formatted_text(HTML(s))
    elif format == "italic" or format == "i":
        s = '<i>' + text + '</i>'
        print_formatted_text(HTML(s))
    elif format == "reverse" or format == "r": # swap text color and background color
        s = '<reverse>' + text + '</reverse>'
        print_formatted_text(HTML(s))
    elif format == "underline" or format == "u":
        s = '<underline>' + text + '</underline>'
        print_formatted_text(HTML(s))
    elif format == "hidden" or format == "h":
        s = '<hidden>' + text + '</hidden>'
        print_formatted_text(HTML(s))

# tests
# formatText("bold", "bold")
# formatText("blink", "blink") # doesnt work for me
# formatText("italic", "italic") # doesnt work for me
# formatText("reverse", "reverse") 
# formatText("underline", "underline") 
# formatText("hidden", "hidden") # still visible

# returns true if input = choice or input = first char of choice
def checkInput(inp, choice):
    if inp == choice or inp == choice[0]:
        return True
    else: return False

def wait(seconds):
    time.sleep(seconds)

def yesno(player):
    #  Returns True if user input is yes, returns False if no.
    while True:
        userinput = input(player)
        if userinput == "yes" or userinput == "y":
            return True
        elif userinput == "no" or userinput == "n":
            return False
        else:
            printc("@'yes'@yellow@ or @'no'@yellow@.")

def dichotomy(option1, option2):
    # Returns True if user input is option1, returns False if option2.
    # Make sure the options are in stripped lowercase form
    while True:
        userinput = raw_input("> ").lower().strip()
        if userinput == option1:
            return True
        elif userinput == option2:
            return False
        else:
            print("You must choose 'yes' or 'no'.")

# Might be useful later in the game
def checklevel(xp):
    for x in range(1,10001):
        if xp < (x**1.68)*100:
            return x - 1

# takes an array returns a random index
def getRandomIndex(arr):
    return arr[random.randint(0, len(arr)-1)]

def input(player):
    while True:
        inp = raw_input("> ").lower().strip()
        if player.devmode and inp == "debug damage":
            player.takeDamage(int(raw_input("How much damage? : ")))
        elif player.devmode and inp == "debug level up":
            player.levelUp()
        elif player.devmode and inp == "debug add xp":
            player.addExperience(int(raw_input("How much XP?: ")), raw_input("Scale? (True or False): "))
        elif inp == "hp":
            print("You have " + str(player.hp) + " out of " + str(player.maxhp) +  " HP. "),
            print("("),
            print(str(int(round(float(player.hp)/float(player.maxhp), 2) * 100))),
            print("% )")
        elif inp == "i" or inp == "inventory":
            player.openInventory()
        elif inp == "me":
            print("You are a level " + str(player.level) + " " + player.aspect['occ'] + " with " + str(player.dogecoin) + " dogecoin to your name.")
        elif inp == "save":
            pickle.dump(player, open("AdventureQuestSave.meme", "w"))
            show("Game saved!")
        elif inp == "load":
            player = pickle.load(open("AdventureQuestSave.meme", "r"))
            show("Game loaded!")
        else:
            return inp
    
# HOW TO PRINT COLOR
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text') # doesnt work?