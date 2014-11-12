#!/bin/bash
#runs the python code with the appropriate parameters

filename=tf_idf.py
flag1=-text
#arg1="Hello Irene, Orestis, and Pat"
#arg1="There's a huge chicken in my living room. Another sentence!"
#arg1="Hi can not make the game. There are three options. I wish to get rid of one."
arg1="However, this is just extraction. Abstraction seems a lot more complicated but a lot better in the task of summarizing. We want to do more than pyteaser which just takes the top 5 sentences - and our code right now basically just does pyteaser-like extraction. We did meet our milestone!"
flag2=-c
arg2=./CorpusFolder/
flag3=-tagged
arg3=True

time python $filename $flag1 "$arg1" $flag2 $arg2 $flag3 $arg3
