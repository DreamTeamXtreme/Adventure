from world import *
from utils import *
import sys
sys.path.append('../') # i dont really know whats going on here but it lets you import from sibling directories
from SlotMachine import *


def maintown(player):
    player.addVisit(player.aspect['town']) # places inside of this here while loop return to the while loop when they are finished
    player.addToTeleportableAreas(player.aspect['town'], maintown)
    while True:
        print("You stand in the homey town of {0}, just passed the hills of {1}, a lovely place.").format(player.aspect['town'] , player.aspect['hills'])
        print("You could go 'home' and check that out.")
        print("The 'tavern' is always a cool place to hang out.")
        print("The 'store' is probably open at this time of day.")
        print("The 'blacksmith' might appreciate you buying something.")
        print("Or you could always 'leave' your humble town to explore the world.")
        print("Where do you want to go?")
        place = input()
        if place == "home" or place == "h":
            home(player)
        elif place == "tavern" or place == "t":
            tavern(player)
        elif place == "store" or place == "s":
            store(player)
        elif place == "blacksmith" or place == "b":
            blacksmith(player)
        elif place == "leave" or place == "l":
            if player.getVisits("maintown") == 1:
                show("Off to find your grandpa eh? Mom said to head EAST.")
            else:
                show("You decide to leave your home town for greener pastures.")
            break # this break right here is really important
        else:
            print("You've got to pick one of the places listed.")
            print("")

def home(player):
    show("You enter your house through the familiar front door, taking in "
         "the sights of your childhood abode, reminiscing about all the "
         "dank shit you did as a kid.")
    while True:
        print("You could 'explore' your house some more, 'sleep', 'play' a console game, or just 'leave'.")
        action = input()
        if action == "explore" or action == "e":
            if player.getVisits("Explore House", "add") == 1:
                show("You head upstairs to your room and look around for a bit. "
                     "You realize that you left your can of Mtn Dew laying on top "
                     "of your dresser.")
                show("You grab the can just in case you need it later.")
                # TODO: add the can to your inventory
            else:
                show("You look around the house, but shockingly can't find anywhere you haven't already explored")
        elif action == "sleep" or action == "s":
            show("After a long day's work adventuring, you're tired. You decide to climb into your old childhood bed to get some rest.")
            show("Your mother tucks you in and kisses you on the forehead.")
            show("Good night sweetie, don't let the bed bugs bite!")
            player.sleep()
            show("You turn to leave. \"Bye sweetie, be home for dinner!\" your mother says.")
            show("You shoot her with the double finger guns and head out as she collapses to the floor.")
            break
        elif action == "play" or action == "p":
            player.addVisit("House Console Game")
            if player.getVisits("House Console Game") == 1:
                show("You decide to kill some time by playing some Call of Duty: Black Ops 4: Pro Edition: Platinum Hits Version")
                show("After popping the disc into your GameSphere 420, you realize that it needs to install.")
                show("You watch the loading bar move at an astoundingly slow pace. This could take a while.")
                show("Standing up, you decide to do something fun in the mean time.")
            else:
                show("You walk over to your GameSphere 420 to see if your game is done installing.")
                show("Oh, look at that!")
                show("It isn't.")
                show("You decide to wait some more.")
        elif action == "leave" or action == "l":
            show("You look around your house for a bit, before deciding to leave.")
            print("Your mother looks up from the " + getRandomDankClothing()  + " she's knitting.")
            raw_input("... ")
            show('"Bye sweetie, good luck on your adventures! Don\'t forget to remember: ' + getMotherlyPlattitude() )
            break
        else:
            print("Please input a valid action.")
    # TODO: add more stuff to do in your house


def blacksmith(player):
    if player.getVisits("Main Town Blacksmith", "add") == 1:
        show("You decide to take a look at the quality goods your local blacksmith is selling.")
        show("You walk over to your town's forge and approach the blacksmith, "
             "she's 6'5\" and the strongest one in your town.")
        show('"Hello!" she reaches out to shake your hand and ends up hurting it '
             'slightly.')
        player.takeDamage(1)
    else:
        show("You head over to the blacksmith's place to take a look at some "
             "quality goods.")
    show("You look at the blacksmith's wares, but she doesn't have anything "
         "you need at the moment. You decide to head back into the town.")
    # TODO: blacksmith

def tavern(player):
    if player.getVisits("Main Town Tavern", "add") == 1:
        show("You walk into the old tavern, wanting to visit the old place "
             "once again.")
        show("As you walk in, several patrons of the bar turn around to look "
             "at you.")
        show('"Ah, it\'s you," the bartender says. "Make sure to watch how '
             'much Mtn Dew you have this time!" Several of the bar\'s guests '
             'chuckle jovially.')
    else:
        show("You walk into the old tavern once again, determined to find some "
          "dank shit to do here or something.")
    while True:
        print("You have a look around to see what's up:")
        print("In front of you lies a pretty dope looking 'slot' machine")
        print("You could 'ask' the bartender for some rumors")
        print("It looks like one of the patrons is challenging others to a 'game'")
        print("You could get a room to 'rest' for the night")
        print("Or you could just 'leave'.")
        action = input()
        if action == "slot" or action == "s":
            # Slots(player).slot_machine() TODO: fix this
            # until that gets fixed, run this line instead:
            show("You try your best at the slot machine, but it conveniently results in no net change of dogecoin for you.")
        elif action == "ask" or action == "a":
            show("You walk up to the bartender and ask for some rumors.")
            show("He lets you know that he hasn't heard anything since the last "
                 "time you asked.")
            # TODO: Rumors (random maybe?)
        elif action == "game" or action == "g":
                tavernGame(player)
        elif action == "rest" or action =="r":
            pass # TODO
        elif action == "leave" or action == "l":
            show("You've had enough fun at the tavern for today, and decide to blow this popsicle stand.")
            break
        else:
            print("You need to choose something to do!")
            print("")
    show("You leave the tavern, heading outside to the rest of the town.")


def tavernGame(player):
    # TODO: if you're in the pirates clan this guy respects you more
    show("You saunter up to the gentleman who seems to be looking for "
             "someone willing to play a game with him.")
    show("The old pirate sitting at the table looks up at you and takes a "
         "sip out of his flask.")
    print('"I\'ve been challenging travelers across these lands to the '
         'game of my people for many years. You think you\'ve got what '
         'it takes to beat me?" (y/n)')
    if yesno():
        show('"Hah! Let\'s see how good you really are!')
        show("The pirate cracks his knuckles and offers his hand to you "
             "for a friendly handshake.")
        show("You accept his offer, shaking his hand, when he suddenly "
             "grins at you.")
        show('"Hah, new to the game, are you? I can feel in your hand '
             'what you\'re about to play!"')
        show("You gulp nervously and ready your fist, mentally preparing "
             "yourself for the beginning of the match.")
        yourchoice, opchoice, outcome = RockPaperScissors.RPSGame().game()
        show('"Enough waiting around! Let\'s do this!"')
        while True:
          yourchoice, opchoice, outcome = RockPaperScissors.RPSGame().game()
          show("The world seems to fade away around you as the only thing "
               "you focus on is your own hand and that of your opponent.")
          show("Over the rushing sound in your ears you hear the patrons of "
               "the bar chanting, your fist hitting your open hand.")
          show('"ROCK"')
          show('"PAPER"')
          show('"SCISSORS"')
          show('"SHOOT!"')
          if opchoice == 'rock':
               show("The pirate slams his closed fist down into his open "
                    "palm. He played rock!")
          else:
               print("The pirate opens his hand a split second before slamming "
                    "his fist into his open palm, revealing his true choice: "
                    "%s!" % opchoice)
               raw_input("... ")
          show("The bar erupts in cheers when they see the outcome of your "
               "match.")
          if outcome == 'win':
               print("You look down into your own hand. {0} beats {1}! You "
                    "actually won!").format(yourchoice, opchoice)
               raw_input("... ")
               show("The pirate looks up at you, clearly impressed.")
               show('"Not many can beat me at this game. I think you deserve '
                    'to be in my clan, it houses only the best rock paper '
                    'scissors players in the entire world."')
               player.clantags.append("[Pyr8]")
               show("You have joined The Pirates' Clan! [Pyr8]")
               show("After your rousing game, you head back to the front of the tavern.")
               break
          elif outcome == 'tie':
               print("You look down into your own hand. Both of you played {0}! "
                    "It's a tie!").format(yourchoice)
               raw_input("... ")
               show('"What a match! It looks like we\'re fairly even in skill," the pirate says.')
               show('"Let\'s play again to settle who really is the better player!"')
          else:
               print("You look down into your own hand. {0} beats {1}! He beat "
                    "you!").format(opchoice.title(), yourchoice)
               raw_input("... ")
               show('"Heh heh, well that\'s alright. Not everybody has what '
                    'it takes to play with the best of them. Better luck next time!"')
               show("After your rousing game, you head back to the front of the tavern.")
               break
    else:
        show('"Just as I figured, maybe you can come back when you\'re not '
             'such a fuckin whimp lol')
        show("You're so upset by his unkind words that you don't even want "
             "to be here anymore.")
    print("")

def store(player):
    show("You stride into the sedentary sales store supplementing the "
         "not-so-silent town of %s, where succulent sweets and sundries "
         "are sold. " % player.aspect['town'])
    show("You approach the shopkeeper, an old and wary gentleman with age on "
         "his face and experience in his eyes.")
    show('"What\'ll it be for ya today?"')
    show("You make a point of considering the shopkeeper's wares, but you're "
         "not in the market for anything he's selling at the moment.")
    show("He looks a little irritated that you didn't buy anything as you "
         "head back to the town center, having accomplished nothing at all.")
    # TODO: add the shop