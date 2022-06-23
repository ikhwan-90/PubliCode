#!/bin/bash

#Count files in directory and Initialize running number
countFiles=$(find -name "files*" | wc -l)

for (( i=$(( countFiles + 1 )); i<=$(( countFiles + 25 )); i++ ))
do
	touch files${i}.txt	#create the files with the numbers
done
#Exit and save the script after this comment
