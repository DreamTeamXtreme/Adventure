import random
from utils import show, clear
from lists import getRandomEnemyName, getRandomAttackVerb
from enemy import *
from combatUI import *
from item import tryForDrop
#  TODO: consult other adventure games to see what a good attack:HP ratio is

class Combat:
    def __init__(self, player, biome=None, alert=True, enemy=None, startCombatNow=True):
        self.player = player
        self.biome = biome
        if not enemy == None: 
            self.enemy = enemy
        else: 
            self.enemy = Enemy(player,biome) # make random enemy with given biome
        self.dropchance = 0 # TODO drops
        if alert: self.alert()
        if startCombatNow: self.startCombat()

        # TODO: May later be affected by level as well as biome

    def alert(self):
        # map.getTileDescription prints something about where you are.
        print "From over your shoulder you notice",
        print self.enemy.name,
        print "attempting to", # TODO flavor text about realizing your're being attacked
        attack = getRandomAttackVerb() 
        if attack[-1] == "*": # if attack finishes the sentence
            print attack[:-1] # remove *
        else :
            print attack,
            print "you!"
        show("@You're being attacked!@red@") 

    def startCombat(self):
        c = CombatUI(self.player, self.enemy)
        c.run()
        clear()
        if c.result == "win":
            show("You defeated " + self.enemy.name + "!")
            self.player.addExperience(self.enemy.xpworth) # gain xp
            self.player.regenHealth()# gain health
            if tryForDrop(10): # TODO after inventory
                show("You got some loot!")
        elif c.result == "lose":
            self.player.death()
        elif c.result == "escaped":
            show("You escaped from " + self.enemy.name + "! That was a close one!")
        return
        
        