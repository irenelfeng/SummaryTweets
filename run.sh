#!/bin/bash
#runs the python code with the appropriate parameters

filename=tf_idf.py
flag1=-text
arg1="Hello Irene, Orestis, and Pat"
flag2=-c
arg2=./CorpusFolder/brown/ca/

python $filename $flag1 "$arg1" $flag2 $arg2
