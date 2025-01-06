#!/bin/bash
echo "do you want install Program operating requirements y/n :"
read anwser

if [[ $anwser == "y" ]]; then
    sleep 3
    echo "the process start"
    sleep 2
    command="pip install playsound"
    $command
else
    echo "The process has been stopped."

fi