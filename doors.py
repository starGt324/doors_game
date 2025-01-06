from playsound import playsound
bit_one=1
bit_tow=0
#win_sound=playsound(r"win.mp3") couse eror
#lose_sound=playsound(r"lose.mp3")
ask_player=input(" is the door open/not : ")
ask_player.lower()
if ask_player=="open" or ask_player=="OPEN"  or ask_player=="not" or ask_player=="NOT":

    pass
else:
    print("you have 2 anwser open or not to go for next step.")
    exit()

import random
import time
print("game start_______")
print()
print("ai chose...")
print()
time.sleep(2.5)

bot_choise=("open","not")

bot=random.choice(bot_choise)
print("_ai choise_:",bot)
print()

if bot=="open" and ask_player=="open":
    print("you skip the mitrex.")
    print("you win.")
    playsound("win.mp3")

    
elif bot=="not" and ask_player=="not":
    print("the mitrex controle you.")
    playsound("lose.mp3")


elif bot=="not" and ask_player=="open":
    print("the mitrex controle you.")
    playsound("lose.mp3")

    
elif bot=="open" and ask_player=="not":
    print("you skip the mitrex.")
    print("you win.")
    playsound("win.mp3")

else:
    print("god help you.")
print()
print("game end______")



