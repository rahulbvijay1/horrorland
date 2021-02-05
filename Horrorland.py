
                                                            # HORRORLAND ! 
                                                     

  # Game Introduction:
  

# This is a text-based game wherein a player is brought into a haunted castle called Horrorland, located near southern coast of Honolulu, Hawaii.
# The game is meant for adults only (18+) and contains moderate violence.

# The castle contains a Black room.

# The aim of this game is to find an ancient green glass box that contains a precious 90 carat diamond ring
# which is believed to have belonged to a Roman emperor, Romeo Caesar, dated back 7th century BC.
# Known to have reached at the castle under mysterious circumstances,
# this ring is needed to be retained back to government who will then display at a museum. It is valued at around $ 2.0 million.


  # Game Contents:

# As simple as it appears to be, the game is loaded with a series of exciting stages,
# that challenges the player to move forward in quest to finding the box.
# There are 3 characters involved in this game.

# 1) Lucifer, the friendly ghost and player's companion.
# 2) Hell Raiser, Lucifer's unfriendly brother, who is trying to eliminate the player.
# 3) Kijo, the witch who demands smartest answers to the riddles.


# Faetures of Lucifer and Hell Raiser:


# Lucifer's Strengths:

# i)   Able to travel through walls
# ii)  Survives in sunlight
# iii) Create loud high pitched noises to battle demons

# Lucifer's Weaknesses:

# i)   Reacts badly to Salt
# ii)  Avoids Electromagnetic radiations
# iii) Avoids his brother's Demonic Knife


# Hell Raiser's Strengths:


# i)   Strong in dark conditions
# ii)  Able to vanish himself
# iii) Throw fireballs from mouth


# Hell Raiser's Weaknesses:

# i)   Repels from sunlight
# ii)  Avoids high pitched noises
# iii) Gets weak by hearing the word, "Christo"
# iv)  Reacts badly to Salt


#-----------------------------------------------------------

                                                                  # THE GAME BEGINS!

                                                                

# Introduction


import random # using 'random' module to access another builtin library of python that provides features to print random numbers, strings, lists, etc. 

import sys # using 'sys' module for python to interact with the player's computer

import time # using time module to return number of seconds passed during program's execution.


time.sleep(2) # Using time delays from time module to print the output on console.In this case, 2 in brackets represents 2 seconds.



print("\n\n\n\t\t *** Welcome to the HORROR LAND! ***\n") # Greeting the player 

time.sleep(2)
    
askpermission = input("### Do you want to play this scary game? Please type yes or no. ### \n\n") # Asking player if he really wishes to play the game.


## If interested to play, enter the name and age of the player, else close the game.


if askpermission.lower() == "yes": # Condition created if player replies yes to play the game.
    
    print("\t \n ** To begin with, you will first need to write your name. ** \n\n")
    
    name = input("\t ->>> What is your name? " "")
    
    print(f"\n Welcome, {name.title()}! In order for us to fully confirm your identity, please provide your age in the box below. Note: You must be over 18. \n\n")
    
    age = int(input("\t ->>> Write your age here: " ""))
    
        
    ## If younger than 18 years, stop!
    

    if age > 18:

        print("\n Thank you for your details. Lets play! \n\n")

        print("\n\t\t\t\t *_*_THE GAME BEGINS_*_*") 

    else: # If the age given by user less than 18, perform following execution

        print("Sorry! You must be over 18 years to play the game :(")

        sys.exit()

elif askpermission.lower() == "no": # If player does not wish to play the game, exit.

    print("\nThank you! You can now exit the window.")

    sys.exit() # Exit the game
    




                                                    ## Begin the Game... ##

    
    
    
time.sleep(3) # delay the output for 3 seconds

entercastle = f"\n\n\n\t\t You have now entered the castle! \n"

castlediagram = f" \t\t     || \n  \t\t  ## ## ## \n \t\t # || || || # \n\n" # Textual Diagram representing the Castle

print(entercastle)

print(castlediagram)

time.sleep(3)

# Entering the Black room and story continues...

print("You see a Black door room and enter inside. You meet Lucifer who is standing at front to greet you....")

time.sleep(3)

# You meet friendly ghost, Lucifer

print(f"\n\n Lucifer - 'Hello {name.title()}! I am Lucifer, the castle's friendly ghost and your companion'.")

lucifer_question= input("\n\n Lucifer - 'There must be a strong reason for you to end up at a place like this! What are you looking for?': ")

print(f"\n\n Lucifer - 'Alright! Now I know, I have seen many people come before you to retain the {lucifer_question.title()}, \n\t    but couldn't due to their lack of smartness.'")

time.sleep(2)


# Lucifer takes player to the mysterious cupboard that is on the left corner of the room.

print(f"\n\n Lucifer - '{name.title()}, please follow me to reach the wooden cupboard that stands across the left corner of this room.'")

# The cupboard inside had a magical piece of red paper. This paper had a printed riddle...
# ... the player had to write the answer onto that paper.
# ..... if the answer was correct, this paper would then levitate and throw itself onto a direction, indicating the box's whereabouts.


time.sleep(3)

# Creating function for Cupboard


print(f"\n\n Lucifer - '{name.title()}, please open the cupboard and try to grab the red paper and read what is printed on it.'")

def cupboard_details(answeryes, answerfire): # Two parameters - answeryes and asnwerfire
    

               # The below line is a docstring explaining this function's activities.

    """This function is created for player's interaction with cupboard and store the answer of riddle"""
    
    
    opencupboard = input("\nTo open the cupboard, type yes: ") # User input to open the cupboard

    if opencupboard.lower() == answeryes: # Comparing if input given by user above matches the argument "yes" given below.

        print("\nSolve this riddle if you want to reach the box:")

        time.sleep(2)

        # Printing the riddle found from Red paper.
    
        riddle = print("\n I am not alive, \n but I grow; I don't have lungs, \n but I need air; I don't have a mouth, \n but water kills me. What am I?")

        riddle_answer = input("\nYour answer: ")

        # Create condition to check correct answer of riddle given by player:

        if riddle_answer.lower() == answerfire: # Comparing the riddle answer with argument given below that is assigned in this function

            print(f"\n\n{answerfire.title()} is correct.") # If player's answer is correct, print by acknowledging.

            time.sleep(3)

            print(f"\n Lucifer -  'Good job, {name.title()}! Let us wait for the paper to levitate and watch which direction does it fall at.'")

            time.sleep(5)

            print("\n\n Paper falls on North side of the room...")
            
            time.sleep(3)

            print(f"\n Lucifer - '{name.title()}, I think we are getting closer to the box! Lets check to north if we could find something.'")


        else:   # If player enters wrong answer on the paper, restart the game from beginning.

            print("Sorry, you gave wrong answer! You will have to restart the game :(")

            sys.exit()

cupboard_details('yes','fire') # Assigning Arguments - yes and fire, for the above parameters, respectively.



# Hell Raiser's entry in the game!


time.sleep(4)

# \n used to create new line in output on console.

print("\nWhile you and Lucifer try to find clues for box, his demonic brother, Hell Raiser appears in the room...") 

time.sleep(3)

# Usng f strings: to insert value of variable into strings. For example, in below line, {name.title()} corresponds to name of player that was first written at beginning of game.

print(f"\n\n Lucifer - 'Aww ohh! {name.title()}, its my brother again! I gotta protect you from him, he's a ruthless devil trying to kill you.'")

time.sleep(4)

print(f"\n\n Hell Raiser - 'Hey Lucifer, you better move out of my way! I am thirsty for human blood right now and gonna kill this \n\t\tpiece of flesh.'")

time.sleep(4)

print(f"\n\n Lucifer - 'Raiser, you cannot do this to my companion. Humans are friendly beings. You cannot hurt them for no reason!'")

time.sleep(3)

print("\nThe devil chases you......")

time.sleep(3)

print(f"\n\n Lucifer - '{name.title()}, stay behind my back, I will create a special shield for you to protect from Hell Raiser.'")


time.sleep(3)

# Creating INPUT statement to enable Lucifer's Shield

shield = input("\nType 'shield' to activate Lucifer's sheild: ")


# Create a condition for player's input - if written SHEILD, perform rest of the execution


if shield.lower() == "shield": # Condition created if written "SHIELD"

    print("\n\nLucifer is now shielding you...")

    print("\n\nTo further produce supernatural powers from Lucifer, he needs your help!")

    supernatural = input("\n\nType 'power' to activate supernatural skills from Lucifer: ")
    

    # Similarly, creating a condition, if written Power, perform following activities.

    if supernatural.lower() == "power": # Condition created if written "POWER"

        print(f"\n\n Lucifer - 'Thanks, {name.title()}, lets see how long I am able to control him!'")

        time.sleep(3)

        print("\n\nHell Raiser now trying to cause damage to electronics - television, microwave, resulting in electromagnetic radiation,\nmaking Lucifer weaker...")


        print(f"\n\n Lucifer - '{name.title()}, try to hide behind cupboard, as long as your away from his sight, your safe. Let me regain my energy \n\t    for next 15 seconds.'")

        
        hide = input("\nType 'hide'to hide behind cupboard: ")

        if hide.lower() == "hide": # Condition created if written "HIDE".

            print(f"\n\nHell Raiser trying to find you...\n\nHe screams out - 'You cannot escape from me, {name.title()}!!!'...\n\nLucifer still gaining his energy!")
            
            time.sleep(15)

            print(f"\n\n Lucifer - 'Hey {name.title()}!, I'm back, hold on there while I showup mirror on his face to cast sunlight!'")

            mirror = input("\nType 'mirror' to cast sunlight on devil's face: ")

            if mirror.lower() == "mirror": # Same Logic

                print("\n\n Lucifer - 'Awesome!! He is getting weaker and falling down!'")

                time.sleep(4)

                print("\nThe devil is now finding himself to immerse into dark areas... \n\nYou and Lucifer head towards North...")

                time.sleep(4)

                print("\nBoth of you are figuring out the room to fetch some clues for the box...")
                
                time.sleep(4)
                
                print("\nRoom includes a king size bed, a sofa, dining table, a bar stool, some classic paintings on north side and a water jug...")

                time.sleep(2)
                
                print("\nAnxious Lucifer later decides to apply his magical skills to travel through other side of north wall...")

                print("\n\nOn reaching other side, he sees a graveyard and a gatekeeper walking around...")

                time.sleep(3)

                print("\nLucifer and you enter the yard. You meet the gatekeeper and explain your situation...")

                time.sleep(2)

                print("\nThe gatekeeper warns you both to keep out of that area and go back to castle, and gave a piece of advice...")

                time.sleep(2)

                print("\n Gatekeeper - 'Your direction is wrong, I suggest you to think deeper once you reach back to castle.'")
                
                print("\n\nStruggling to get further clues from graveyard, you both come back to castle...")
                print("\n\nAfter pondering upon gatekeeper's words, you and Lucifer begin to find something special to reach the box.")

                time.sleep(6)

                print("\n\nBy now, Hell Raiser had already vanished.\n\nAfter spending considerable amount of time on inspecting the room, your foot slips accidentally and sit on bar stool.")
                time.sleep(2)

                print("\n\nThe stool had secret electric button attached to it's bottom to detonate the right wall of the room, which got pressed upon your \ncontact.")
                print("\n\nThis causes the right wall to break!!!")

                time.sleep(3)
                
                print("\n BOOM!!! The Wall Breaks! You now witness a secret staircase, leading all the way up to another room - BLUE ROOM!")


                print("\n\t\t\t***STAIRCASE***") # While \n used for new line, \t is used to create tab or indentation on print the statements.


                # The next line represents representation of staircase, assigned with variable "staircase" 
                
                staircase = "\n\t\t\t\t\t    _____ ***BLUE ROOM***    \n\t\t\t\t\t  _|\n\t\t\t\t        _|\n\t\t\t\t      _|\n\t\t\t            _|\n\t\t\t\t  _|\n\t     **BLACK ROOM** _____|"

                print(staircase) # print the staircase.
              
                time.sleep(5)

                print(f"\n\n\t Lucifer - '{name.title()}! what a discovery! I believe we better head upstairs to the BLUE ROOM! Let's go!!!")

                time.sleep(3)

                print("\n\tThe HELL RAISER reappears !!!")

                time.sleep(3)

                print(f"\n\t Hell Raiser - 'I am gonna crush you to DARK HELL and eat you, {name.title()}!'")

                time.sleep(3)

                

# CASE 1: HELL RAISER KILLS PLAYER -


def hellraiser_kills_player():

                                    # The below docstring explains the use of this function.

    """ This function created for player to engage fight with the Devil. This will be used to ultimately kill the player """
    

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

            print("\n\t***CHRISTO***")

            print(f"\n\nHell Raiser - 'Ahhh will you just stop it!!!? Those words are no more frightening to me. \n\t       I am not gonna leave you now!!!'")
           
            time.sleep(3)

            print("\n\tYou are screaming CRISTO, whilt Lucifer keeps splashing water...")

            time.sleep(3)
            
            print("\n You find salt saucer on dining table...")
            
            time.sleep(3)

            print("\nLucifer tells you to throw salt on devil's eyes...")

            salt = input("Type 'salt' to rub on devil: ")

            if salt.lower() == "salt":
                
                print("\n\n Hell Raiser - 'You bloody maniac! How dare you rub salt on me!...'")
                
            time.sleep(3)    

            print("\nUnfortunately this time, the devil has garnered extreme resilience and agility...")

            time.sleep(2)

            print("\nThe Hell Raiser grabs you by his tough hands...\n and throws his demonic knife on Lucifer's chest, killing him on the spot.")

            time.sleep(5)

            print("\nYou fought hard with Lucifer, but the devil drags you down to hell and finally eliminates you!")

            time.sleep(1)

            print("\n\n\t\t     Game Over !!! \n\n\t\tBetter luck next time!")

            sys.exit()
            

# CASE 2: HELL RAISER SMASHED BY PLAYER -
            

def hellraiser_weak():

    """This function is created to for player to outperform the devil.

       This will be used to lead the player win the game after passing through some challenges."""

    print("\n\nThe Hell Raiser pulls you back on the floor...\n\nLucifer trying to splash Holy water from jug kept on dining table...")

    time.sleep(3)

    print("\n\nYou are battling hard with devil to save your life...")

    time.sleep(3)
    
    print("\n\nLucifer tries to splash water on devil's face!")
    
    time.sleep(2)
          
    holywater = input("\n\nType 'splash' to splash holy water: ")

    if holywater.lower() == "splash": # Create condition and compare if input from player matches the word, "SPLASH"

        print("\n\nLucifer splashes water on devil...\n\n Hell Raiser - 'Lucifer, stop it! You are getting crazy, don't splash me,, I can't survive!'")

        time.sleep(2)

        print("\n\nHell Raiser now utilises his next skill - Fireballs!")
        time.sleep(3)

        print("\n\n Hell Raiser - 'If you really want to make this uglier, take this!!!' \n\n\n  ***FIREBALLS*** ***FIREBALLS*** ***FIREBALLS***")

        time.sleep(2)

        print("\n\nHelp Lucifer activate his double shield")

        shield = input("\nType 'shield' to enable: ")

        if shield == "shield": #Comparing player's response with "SHIELD"

            print(f"\n\n Lucifer - '{name.title()}, speak out CHRISTO, it will make him weak!'")

            christo = input("\nType 'christo' to retaliate against Hell Raiser: ")

            if christo.lower() == "christo":

                print(f"\n Lucifer - 'Great, {name.title()}!, I will now emitt High Frequency noises on him...'")

                time.sleep(2)

                high_noise = input("\nType 'high' to activate Lucifer's noise: ")

                if high_noise.lower() == "high": # Comparing player's response with HIGH.
                    
                    print("\n\n Hell Raiser - 'Aaahhh! Stop this please! Lucifer, this is exhaustive...stop this noise! I am shaking and getting incapacitated!'")

                    time.sleep(3)

                    print("\nDevil's health deteriorates, he avoids further impact from Lucifer and vanishes again...")

                    time.sleep(3)

                    # After Lucifer emits the noise, devil diappears. The player and Lucifer then heading to Blue room.
                    

                    print("\nYou and Lucifer finally climb upstairs towards Blue Room.")
                    

                    print("\n\t\t\t***STAIRCASE***")

                    time.sleep(3)

                    staircase = "\n\t\t\t\t\t    _____ ***BLUE ROOM***    \n\t\t\t\t\t  _|\n\t\t\t\t        _|\n\t\t\t\t      _|\n\t\t\t            _|\n\t\t\t\t  _|\n\t     **BLACK ROOM** _____|"

                    print(staircase)

                    time.sleep(3)

                    # On reaching the Blue room, they face another challenge to solve a riddle to enter the room.

                    print("\n\nNow that you have reached Blue Room, there is a catch! \nYou will have to solve riddle written on sticky note hung on doorknob.")

                    time.sleep(3)

                    print("\n\nSolve the riddle given below: ")

                    # Creating blueroom_riddle variable to display the riddle question and get input from player

                    blueroom_riddle = input("\n\n\tWhat Demands an Answer, But Ask no Questions?: ")

                    if blueroom_riddle == "telephone": # Checking if player enters "telephone" as the answer

                        print(f"\n\n{blueroom_riddle.title()} is correct! You have now entered the room.")
                        

                        ## If written TELEPHONE, they enter room and witness the Ancient Green Glass Box.
                        

                        print("\n\nAs you and Lucifer enter room, you are amazed to see the Ancient Green Glass Box resting on a chair.")

                        # Creating a variable to represent the box.

                        ancient_box = "\n\n\t\t\t       ***GREEN BOX*** \n\t\t\t\t ___________\n\t\t\t\t|           |\n\t\t\t\t|           |\n\t\t\t\t|___________|"

                        # Create a variable to represent floor.
                            
                        floor = "\n\t\t\t\t------------- \n\t\t\t\t    FLOOR \n\t\t\t\t-------------"

                        # Print both.

                        print(ancient_box)

                        print(floor)

                        time.sleep(3)

                        ## The player meets the witch, Kijo, who demands to answer her 3 questions from the player to retain the box and win the game.
                        
                        print("\nAlthough the box is at front of you, you encounter a witch, named Kijo.")
                        
                        time.sleep(5)

                        # Kijo welcoming the player.

                        print(f"\n\n Kijo - 'Welcome to the Blue room, {name.title()}! You proved to be a valiant human to reach this far.\n\n\tHowever, you will have to answer 3 of my questions to get to the box.'")

                        time.sleep(5)

                        # Kijo's conditions for each riddle...
                        
                        print("\n\nKijo will ask you three riddles... \n\nYou have 3 attempts to answer first riddle, 2 for second, and only 1 for the third.\n\nEach correct answer will bring you 3 steps closer to the box.")

                        time.sleep(5)

                            
                        print("\n\nBe mindful that failure to give correct answer at any stage will force you to get locked out of room forever. \n\nYou will not get the box and the game will be over.")

                        time.sleep(5)

                        # Creating input statement for player to answer the questions

                        yes = input("\nType yes if ready to answer: ")

                        if yes.lower() == "yes":

                            ## First riddle:

                            print(f"\nKijo - 'Okay, {name.title()}!, here is your first question:'")

                            guessestaken = 0 # Number of guesses taken by player is stored here.

                            # Create the variable to print the first question

                            firstriddle = print("\nI Am Heavy And Hard To Pick Up, But Backwards I Am Not. What Am I?")
                            
                            

                            while guessestaken < 3:  # Create While loop - the condition states that unless the player gives write answer to question,
                                                     # offer 3 attempts
                            

                                print("\nGive Your Answer\n")
                                
                                answer = str(input()) # The variable created for player's input. This input stores player's answer and convert into string.

                                guessestaken = guessestaken + 1 # Instruct the system to update the guesses taken by the player.
                                

                                # Creating conditional statements for player's answer.

                                if answer.lower() == "ton":

                                    # If he answers "TON", then print the below statement.

                                    print(f"\n\n{answer.title()} is correct! You move 3 steps closer to box. Solve next question.")

                                    time.sleep(3)

                                    # After successfully completing first question, head on to second question:
                                    

                                    ## Second riddle:

                                    # Kijo appreciating the player:

                                    print(f"\n\n Kijo - 'Well done, {name.title()}! Here is your next question:'")

                                    nextguess = 0 # Number of guesses taken by player for the second question's answer

                                    # Print the second question:

                                    secondriddle = print("\nWhat work of writing can one never finish?")
                                    

                                    while nextguess < 2: # Creating While loop for second question, this time with 2 attempts.

                                        print("\nGive Your Answer\n")

                                        secondanswer = str(input()) # Create input for second answer

                                        nextguess = nextguess + 1 # Update the guesses

                                        # Create Conditional Statements for Second Question:
                                        

                                        if secondanswer.lower() == "autobiography": # If player's answer is "AUTOBIOGRAPHY', execute following:
                                            
                                            print(f"\n\n{secondanswer.title()} is correct! You move 3 steps more closer to box. Solve last question.")

                                            time.sleep(3)

                                            # If successful, then head on to last question:

                                            ## Third riddle:

                                            print(f"\n\n Kijo - 'Great, {name.title()}! Solve the final question to retain the box:'")

                                            finalguess = 0 # Number of guesses taken by player for final question's answer

                                            # end = '' used to continue printing the next lines of strings together in console.

                                            print("\n\n\t\t CAN YOU OPEN THIS LOCK ?", end='')
                                            print(" \n\n\n\t\t 206: Two digits are right but both are in the wrong place", end='')
                                            print(" \n\n\t\t 738: All Digits are wrong", end='')
                                            print(" \n\n\t\t 380: One digit is right but in the wrong place",end='')
                                            print(" \n\n\t\t 682: One digit is right and in its place", end='')
                                            print(" \n\n\t\t 614: One digit is right but in the wrong place", end='')

                                            while finalguess < 1: # Create While loop with only 1 attempt...

                                                print("\nGive Your Answer\n")

                                                finalanswer = str(input())

                                                finalguess = finalguess + 1

                                                if finalanswer.lower() == "042": # Check and Compare player's answer with "042".
                                                    

                                                    print(f"\n\n{finalanswer.title()} is absolutely correct!")
                                                    
                                                    time.sleep(3)
                                                    
                                                    print(f"\n\n  Kijo - 'Congratulations, {name.capital()}!!! You finally were able to retain the box!!! \n\n\t\t***YOU WIN :)***")

                                                    sys.exit() # Exit the game.

                                                    

                                            if finalanswer.lower() != "042": # Creating Conditions if player's answer for third question does not match "042"

                                                # Print following statements and end the game.
                                                        
                                                print("\nSorry, you did not give the correct answer :(")

                                                time.sleep(3)

                                                print("\nYou are locked out of room! \n\nGave Over!")

                                                sys.exit()

                                         

                                    if secondanswer.lower() != "autobiography": # Creating similar Condition for Second Question, if player's answer does not match "AUTOBIOGRAPHY"

                                        # Print the following and end the game.
                                            
                                        print("\nSorry, you did not give the correct answer :(")

                                        time.sleep(3)
   
                                        print("\nYou are locked out of room! \n\nGame Over!")

                                        sys.exit()
                                    

                            if answer.lower() != "ton": # Finally, creating the Condition for First Question if player's answer not matched with "TON"

                                # Print the following statements and end the game
                                
                                print("\nSorry, you did not give the correct answer :(")

                                time.sleep(3)

                                print("\nYou are locked out of room! \n\nGame Over!")

                                sys.exit()
                                
                    else: # If to open Blue room, the player writes answer other than "TELEPHONE", restart the game.

                        print("You gave wrong answer, sorry but you will have to restart the game :(")

                        sys.exit()
                                

cases = [hellraiser_kills_player, hellraiser_weak] # Creating a list with variable name "cases", and nesting the above two functions.

case = random.choice(cases)()

# The random module's random.choice() function returns random element from non-empty sequence.
# The element is enclosed in brackets; in this case, it is "cases".
# So, random.choice(cases) will randomly select one of the elements(functions from (cases) list) and then execute them.

# In other words, one of the execution will take place:

#                        player will definitely be killed (hellraiser_kills_player);

#                        or will have chance to win the game (hellraiser_weak).

print(case)


# End of code, thank you!


        
                

                      

                   
    
                

                    
                      
                
                

                

            












    


