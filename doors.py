import os
import random
import time
from playsound import playsound
losesound=r"lose.wav"
winsound=r"vic.wav"
load_score=int


def app_ver():
    app_ver_checker="0.2"
    print("the version of script is ",app_ver_checker)
#win_sound=playsound(r"win.mp3") couse eror
#lose_sound=playsound(r"lose.mp3")


while True:
   
    ask_player=input(" is the door open/not : ")
    ask_player.lower()
    if ask_player=="open" or ask_player=="OPEN"  or ask_player=="not" or ask_player=="NOT":

        pass
    else:
        print("you have 2 anwser open or not to go for next step.")
        exit(1)

    
    #game start:

    print("game start_______")
    print()
    print("ai chose...")
    print()
    time.sleep(1.5)
    #ai chose:

    bot_choise=("open","not")

    bot=random.choice(bot_choise)
    print("_ai choise_:",bot)
    print()

    if bot=="open" and ask_player=="open":
        print("you skip the mitrex.")
        print("you win.")
        #playsound(r"./win.mp3")
        playsound(winsound)
        break
        
    elif bot=="not" and ask_player=="not":
        print("the mitrex controle you.")
        #playsound(r"./lose.mp3")
        playsound(losesound)

    elif bot=="not" and ask_player=="open":
        print("the mitrex controle you.")
        #playsound(r"./lose.mp3")
        playsound(losesound)
        
        
    elif bot=="open" and ask_player=="not":
        print("you skip the mitrex.")
        print("you win.")
        #playsound(r"./win.mp3")
        playsound(winsound)

    else:
        print("god help you.")
        print()
    
    load_score=load_score+1

#save prog:

    with open("score.txt","w") as f:
        
        f.write(str(load_score))
        #f.write(f"player score:{int(score)}")
        time.sleep(0.5)

#exit game or realoding:
  
    end_game=input("do you want to continu play y/n : ").lower()

    if end_game=="y" or end_game=="yes":
        print("yes sure...")
        print()
        print("--rloead game.")
        time.sleep(2)
    else:
        print("game end______")
        exit(1)

