import random
import time
from datetime import datetime
import pygame
from colorama import Fore,Back,Style,init
pygame.init()
#from playsound import playsound
#losesound=r"./lose.wav"
#winsound=r"./vic.wav"
#load player score:

with open("score.txt","r+") as fr:
    load_score=int(fr.read())


#game info and feuture:

#agrasive_num=0
list_player_input=["open","not","yes","no","y","n"]

def app_ver():
    app_ver_checker="0.3.7v"
    print("the version of script is ",app_ver_checker)

def player_score_show():
    print(Fore.CYAN,"--your score now--",load_score)

def play_victory_sound():
    pygame.mixer.init()
    time.sleep(0.3)
    pygame.mixer.music.load(r"./vic.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass

def play_losing_sound():
    pygame.mixer.init()
    time.sleep(0.3)
    pygame.mixer.music.load(r"./lose.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass


#win_sound=playsound(r"win.mp3") couse eror
#lose_sound=playsound(r"lose.mp3")
app_ver()
while True: 
#player input:    

    ask_player=input(" is the door open/not : ").lower()

    if ask_player in list_player_input:# input filter:

        poss_anwser=["open","yes","y"]
        #neg_anwser=["not","no","n"]

        if ask_player in poss_anwser:
            player_poss=True
        else:
            player_poss=False

    else:
        print("Incomprehensible answer,please use ",list_player_input)
        exit(1)

        
#game start:
   
    print(Fore.GREEN+"game start","_"*15)
    print("ai chose...")
    time.sleep(1.5)

#ai chose:
    #bot_choise=["open","not","open","not"]*50

    bot_list_one=["open"]*15

    bot_list_tow=["not"]*16

    new_bot_choise=bot_list_one+bot_list_tow#use extend fun cuse a crush

# ai aggrasive:
    angry_point=0
    random.shuffle(new_bot_choise)# dont store this in varible couse error nontype.
    bot=random.choice(new_bot_choise)
    print("__ai choise__:",bot)

    if bot=="open":

        angry_point=random.randint(1,10)
        print("--angry point :",angry_point)

    else:
        pass

    if angry_point>=5:
        #player_poss=False
        load_score=load_score+7
        
        with open("score.txt","w+") as f:
            f.write(str(load_score))
        time.sleep(0.5)


        print(Fore.LIGHTYELLOW_EX,"---the AI is cheat and kill you :)...,but we add +7 points score in your recorde.")
        play_losing_sound()
        break
    else:
        pass

    if bot=="open" and player_poss==True or bot=="open" and player_poss==False:
        print(Fore.YELLOW+"you skip the mitrex,you win.")
        play_victory_sound()
        load_score=load_score+2
    else:
        print(Fore.RED+"the mitrex controle you,lose.")
        load_score=load_score-1
        play_losing_sound()


#save prog:

    with open("score.txt","w+") as f:
        f.write(str(load_score))
        time.sleep(0.5)

    with open("my_score.txt","a+") as g:
        g.write(f"date:{datetime.now()}\n")
        g.write(f"player score: +{load_score}\n")
        time.sleep(0.3)

#exit game or realoding:
    
    end_game=input("do you want to continu play y/n : ").lower()

    if end_game=="y" or end_game=="yes":
        print("yes sure...")
        player_score_show()
        print(Style.RESET_ALL)#rest font color
        print("--rloead game.")
        time.sleep(1.5)#if you have a eror or problem just + the SEC
        
    else:
        player_score_show()
        print(Fore.GREEN+"game end","_"*15)
        pygame.quit()
        exit(1)

