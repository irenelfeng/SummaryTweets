#!/bin/bash
#runs the python code with the appropriate parameters

filename=tf_idf.py
flag1=-text
#arg1="Hello Irene, Orestis, and Pat"
#arg1="There's a huge chicken in my living room. Another sentence!"
#arg1="Hi, I can not make the game. There are three options. I wish to get rid of one."
#arg1="A summary is a concise description that reflects the essence of a subject. A text, a collection of text documents, or a query answer can be summarized by simple means such as an automatically generated list of the most frequent words or “advanced” by a meaningful natural language description of the subject. In between these two extremes, conceptual summaries encompass selected concepts derived using background knowledge. We address in this paper an approach where conceptual summaries are provided through a conceptualization as given by an ontology.The ontology guiding the summarization can be a simple taxonomy or a generative domain on-tology. A domain ontology can be provided by a preanalysis of a domain corpus and can be usedto condense improved summaries that better reflects the conceptualization of a given domain."
arg1="However, this is just extraction. Abstraction seems a lot more complicated but a lot better in the task of summarizing. We want to do more than pyteaser which just takes the top 5 sentences - and our code right now basically just does pyteaser-like extraction. We did meet our milestone!"
flag2=-c
arg2=./CorpusFolder/
flag3=-tagged
arg3=True
flag4=-textfile
arg4=input.txt

time python $filename $flag1 "$arg1" $flag2 $arg2 $flag3 $arg3 $flag4 $arg4
