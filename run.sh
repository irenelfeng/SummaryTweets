#!/bin/bash
#runs the python code with the appropriate parameters

filename=tf_idf.py
flag1=-text
arg1="Hello Irene , Orestis , and Pat"
flag2=-c
arg2=./CorpusFolder/
flag3=-tagged
arg3=True

time python $filename $flag1 "$arg1" $flag2 $arg2 $flag3 $arg3
