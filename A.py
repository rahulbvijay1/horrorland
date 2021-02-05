

#print("\n\t\t\t***STAIRCASE***")

#staircase = "\n\t\t\t\t\t    _____ ***BLUE ROOM***    \n\t\t\t\t\t  _|\n\t\t\t\t        _|\n\t\t\t\t      _|\n\t\t\t            _|\n\t\t\t\t  _|\n\t     **BLACK ROOM** _____|"

#print(staircase)


# CASE 1: HELL RAISER KILLS PLAYER -

          
import time

import random

import sys

def hellraiser_kills_player():

    #name = "rahul"

    print("\nThe Hell Raiser pulls you back on the floor...\n\nLucifer trying to splash Holy water from jug kept on dining table...")

    time.sleep(3)

    print("\nYou are battling hard with devil to save your life...")

    time.sleep(3)
    print("\nLucifer tries to splash water on devil's face!")
    
    time.sleep(2)
          
    holywater = input("\n\nType 'splash' to splash holy water: ")

    if holywater.lower() == "splash":

        print("\nLucifer splashes water on devil...\n\nHowever the Hell Raiser has become ultra strong this time and does not repel to water...")

        time.sleep(2)

        print("\n\nIt's time to use your tactics; Cry out 'CHRISTO'!")

        time.sleep(3)

        christo = input("\nType 'christo' to retaliate against Hell raiser: ")

        if christo.lower() == "christo":

            print("\n\t*** CHRISTO***")

            print(f"\nHell Raiser - 'Ahhh will you just stooppp it!!!? Those words are no more frightening to me. \nI am not gonna leave you now!!!'")

            time.sleep(3)

            print("\n\tYou are screaming CRISTO, whilt Lucifer keeps splashing water...")

            time.sleep(3)

            print("\n Unfortunately, the devil has garnered extreme resilience and agility...")

            time.sleep(2)

            print("\nHell Raiser - 'One last cry from your mouth and your dead!'...")

            time.sleep(3)

            print("\nThe Hell Raiser grabs you by his tough hands...\n and throws his demonic knife on Lucifer's chest, killing him on the spot.")

            time.sleep(5)

            print("You fought hard with Lucifer, but the devil drags you down to hell and finally eliminates you!")

            time.sleep(1)

            print("Game Over !!! \n Better luck next time!")

            sys.exit()
            

# CASE 2: HELL RAISER SMASHED BY PLAYER -
            

def hellraiser_weak():

    #name = "rahul"

    print("\nThe Hell Raiser pulls you back on the floor...\n\nLucifer trying to splash Holy water from jug kept on dining table...")

    time.sleep(3)

    print("\nYou are battling hard with devil to save your life...")

    time.sleep(3)
    
    print("\nLucifer tries to splash water on devil's face!")
    
    time.sleep(2)
          
    holywater = input("\n\nType 'splash' to splash holy water: ")

    if holywater.lower() == "splash":

        print("Lucifer splashes water on devil...\n Hell Raiser - 'Lucifer, stop it! You are getting crazy, dont't splash me,, I can't survive!'")

        time.sleep(2)

        print("\n Hell Raiser now utilises his next skill - Fireballs!")
        time.sleep(3)

        print("\nHell Raiser - 'If you really want to make this uglier, take this!!!' \n\n***FIREBALLS*** ***FIREBALLS*** ***FIREBALLS***")

        time.sleep(2)

        print("\nHelp Lucifer activate his double shield")

        shield = input("Type 'shield' to enable: ")

        if shield == "shield":

            print(f"\nLucifer - '{name.title()}, speak out CHRISTO, it will make him weak!'")

            christo = input("Type 'christo' to retaliate against Hell Raiser: ")

            if christo.lower() == "christo":

                print(f"\nLucifer - 'Great, {name.title()}!, I will now emitt high frequency noises for him...'")

                time.sleep(2)

                high_noise = input("Type 'high' to activate Lucifer's noise: ")

                if high_noise.lower() == "high":

                    print("\n\nHell Raiser - 'Aaahhh! Stop this please!!!!\nLucifer, this is exhaustive...stop this noise! I am shaking and getting incapacitated!'")

                    time.sleep(3)

                    print("\n Devil's health deteriorates, he avoids further impact from Lucifer and vanishes again...")

                    time.sleep(3)

                    print("\nYou and Lucifer finally climb upstairs towards Blue Room.")

                    print("\n\t\t\t***STAIRCASE***")

                    time.sleep(3)

                    staircase = "\n\t\t\t\t\t    _____ ***BLUE ROOM***    \n\t\t\t\t\t  _|\n\t\t\t\t        _|\n\t\t\t\t      _|\n\t\t\t            _|\n\t\t\t\t  _|\n\t     **BLACK ROOM** _____|"

                    print(staircase)

                    time.sleep(3)

                    print("\nNow that you have reached Blue Room, there is a catch! \nYou will have to solve riddle written on sticky note hung on doorknob.")

                    time.sleep(3)

                    print("\nSolve the riddle given below: ")

                    blueroom_riddle = input("What Demands an Answer, But Ask no Questions?: ")

                    if blueroom_riddle == "telephone":

                        print(f"\n{blueroom_riddle.title()} is correct! You have now entered the room.")

                        print("\nAs you and Lucifer enter room, you are amazed to see the Ancient Green Glass Box resting on a chair.")

                        time.sleep(3)

                        print("Although the box is at front of you, you encounter a witch, named Kijo.")
                        
                        time.sleep(5)

                        print(f"\n\nKijo - 'Welcome to the Blue room! You proved to be a valiant human to reach this far.\n\n\tHowever, you will have to answer 3 of my questions to get to the box.'")

                        time.sleep(5)
                        
                        print("\n\nKijo will ask you three riddles... \n\nYou have 3 attempts to answer first riddle, 2 for second, and only 1 for the third.\n\nEach correct answer will bring you 3 steps closer to the box.")

                        time.sleep(5)    
                            
                        print("\nBe mindful that failure to give correct answer at any stage will force you to get locked out of room forever. \n\nYou will not get to box and game will be over.")

                        time.sleep(5)

                        

                        yes = input("Type yes if ready to play: ")

                        if yes.lower() == "yes":

                            ## First riddle

                            print(f"\nKijo - 'Okay, {name.title()}!, here is your first question:'")

                            guessestaken = 0

                            firstriddle = print("\nI Am Heavy And Hard To Pick Up, But Backwards I Am Not. What Am I?")

                            while guessestaken < 3:

                                print("\nGive Your Answer\n")
                                
                                answer = str(input())

                                guessestaken = guessestaken + 1

                                if answer.lower() == "ton":

                                    print(f"\n{answer.title()} is correct! You move 3 steps closer to box. Solve next question.")

                                    time.sleep(3)

                                    ## Second riddle

                                    print(f"\nKijo - 'Well done, {name.title()}! Here is your next question:'")

                                    nextguess = 0

                                    secondriddle = print("\nWhat work of writing can one never finish?")

                                    while nextguess < 2:

                                        print("\nGive Your Answer\n")

                                        secondanswer = str(input())

                                        nextguess = nextguess + 1

                                        if secondanswer.lower() == "autobiography":
                                            
                                            print(f"\n{secondanswer.title()} is correct! You move 3 steps more closer to box. Solve last question.")

                                            time.sleep(3)

                                            ## Third riddle

                                            print(f"\nKijo - 'Great, {name.title()}! Solve the final question to retain the box:'")

                                            finalguess = 0

                                            print("\n\n\t\t CAN YOU OPEN THIS LOCK ?", end='')
                                            print(" \n\n\n\t\t 206: Two digits are right but both are in the wrong place", end='')
                                            print(" \n\n\t\t 738: All Digits are wrong", end='')
                                            print(" \n\n\t\t 380: One digit is right but in the wrong place",end='')
                                            print(" \n\n\t\t 682: One digit is right and in its place", end='')
                                            print(" \n\n\t\t 614: One digit is right but in the wrong place", end='')

                                            while finalguess < 1:

                                                print("\nGive Your Answer\n")

                                                finalanswer = str(input())

                                                finalguess = finalguess + 1

                                                if finalanswer.lower() == "042":

                                                    print(f"\n{finalanswer.title()} is absolutely correct!")
                                                    
                                                    time.sleep(3)
                                                    
                                                    print(f"\nKijo - 'Congratulations, {name.title()}!!! You finally were able to retain the box!!! \n\n\t\t***YOU WIN :)***")

                                                    sys.exit()

                                            if finalanswer.lower() != "042":

                                                print("\nSorry, you did not give the correct answer :(")

                                                time.sleep(3)

                                                print("\nYou are locked out of room! \n\nGave Over!")

                                                sys.exit()

                                         

                                    if secondanswer.lower() != "autobiography":

                                        print("\nSorry, you did not give the correct answer :(")

                                        time.sleep(3)
   
                                        print("\nYou are locked out of room! \n\nGame Over!")

                                        sys.exit()
                                    

                            if answer.lower() != "ton":

                                print("\nSorry, you did not give the correct answer :(")

                                time.sleep(3)

                                print("\nYou are locked out of room! \n\nGame Over!")

                                sys.exit()                               

cases = [hellraiser_kills_player, hellraiser_weak]

case = random.choice(cases)()         

print(case)

      
