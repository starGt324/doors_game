#!/bin/bash
echo "do you want install Program operating requirements y/s :"
read anwser
command="pip install playsound"
if [[ $anwser=="y" ]]; then
    sleep 3
    echo "the process start"
    sleep 1
    $command
else
    echo "The process has been stopped."
    exit 
fi