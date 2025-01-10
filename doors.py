import random
import time
import pygame
pygame.init()
#from playsound import playsound
#losesound=r"./lose.wav"
#winsound=r"./vic.wav"

#load player score:
with open("score.txt","r+") as fr:
    load_score=int(fr.read())


#game info and feuture:
def app_ver():
    app_ver_checker="0.2"
    print("the version of script is ",app_ver_checker)

def player_score_show():
    print("--your score now--",load_score)

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

while True: 
#player input:  
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
        load_score=load_score+1
        #playsound(r"./win.mp3")
        #playsound(winsound)
        play_victory_sound()
        
    elif bot=="not" and ask_player=="not":
        print("the mitrex controle you.")
        play_losing_sound()
        #playsound(r"./lose.mp3")
        #playsound(losesound)

    elif bot=="not" and ask_player=="open":
        print("the mitrex controle you.")
        play_losing_sound()
        #playsound(r"./lose.mp3")
        #playsound(losesound)
        
        
    elif bot=="open" and ask_player=="not":
        print("you skip the mitrex.")
        print("you win.")
        load_score=load_score+1
        play_victory_sound()
        #playsound(r"./win.mp3")
        #playsound(winsound)

    else:
        print("god help you.")
        print()


#save prog:

    with open("score.txt","w+") as f:
        f.write(str(load_score))
        time.sleep(0.5)

#exit game or realoding:
    
    end_game=input("do you want to continu play y/n : ").lower()

    if end_game=="y" or end_game=="yes":
        print("yes sure...")
        player_score_show()
        print()
        print("--rloead game.")
        
        time.sleep(2)
        
    else:
        player_score_show()
        print("game end______")
        pygame.quit()
        exit(1)

