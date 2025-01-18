#!/bin/bash
echo "do you want install Program operating requirements y/n :"
read anwser

if [[ $anwser == "y" ]]; then
    sleep 3
    echo "the process start"
    sleep 2
    command="pip install pygame"
    command_colo="pip install colorama==0.4.6"
    $command
    echo "waiting lib to install."
    sleep 47
    $command_colo
    sleep 3
    echo "all lib is steup for you."
    sleep 2
else
    echo "The process has been stopped."
    sleep 4

fi