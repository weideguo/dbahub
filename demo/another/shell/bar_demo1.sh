#!/bin/bash
function Proceess(){
spa=''
i=0
while [ $i -le 100 ]
do
    printf "[%-50s] %d%% \r" "$spa" "$i";
    sleep 0.5
    ((i=i+2))
    spa+='#'
done
echo
}

Proceess
