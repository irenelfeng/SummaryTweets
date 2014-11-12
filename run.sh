#!/bin/bash
#runs the python code with the appropriate parameters

filename=tf_idf.py
flag1=-text
#arg1="Hello Irene, Orestis, and Pat"
#arg1="There's a huge chicken in my living room. Another sentence!"
#arg1="Hi can not make the game. There are three options. I wish to get rid of one."
#arg1="As we begin entering the holiday season, it's great to remember everything we're thankful for! Unfortunately, there a lot of people in the Upper Valley area who are in need of basic necessities, such as warm clothes and food. Dartmouth Christian Union's community service team is raising money for Salvation Army's Star Tree program. Through this program, we'll be able to provide gifts for the families we have adopted. We are also providing an incentive to participate in the fundraiser! We will be raffling off two Dartmouth sweatshirts and and an EBA's pizza at the end of the fundraiser to three lucky winners!!! Although this fundraiser is being run through Christian Union, the Salvation Army's Star Tree does not discriminate towards families on the basis of religion or beliefs. Therefore, we encourage EVERYONE to donate! Your contribution is both meainingful and extremely important. You can find more information on the GOFUNDME page:"
#arg1="There is no limit to the knowledge you can inject into the channel model. For example, some mistakes tend to be extremely common because they appear so often that people don't realize that they're incorrect; the channel model could model this by accounting for the frequency of each error. Certain errors are also particularly frequent. Misspellings, unless they are typos, tend to correspond to the same pronunciations, so one could consult a grapheme-to-phoneme model. Different keyboards give rise to different sorts of typos one could even model the relative frequencies of keyboard configurations. Finally, we'd ideally learn the relative probabilities/costs for each edit from a large corpus of spelling errors, using the the EM algorithm that we'll see next week, rather than relying on messy heuristics. The design of channel models that take into account all such factors is an ongoing research question (and a possible final project topic)."
#arg1="Hi, I can not make the game. There are three options. I wish to get rid of one."
arg1="A summary is a concise description that reflects the essence of a subject. A text, a collection of text documents, or a query answer can be summarized by simple means such as an automatically generated list of the most frequent words or “advanced” by a meaningful natural language description of the subject. In between these two extremes, conceptual summaries encompass selected concepts derived using background knowledge. We address in this paper an approach where conceptual summaries are provided through a conceptualization as given by an ontology.The ontology guiding the summarization can be a simple taxonomy or a generative domain on-tology. A domain ontology can be provided by a preanalysis of a domain corpus and can be usedto condense improved summaries that better reflects the conceptualization of a given domain."
flag2=-c
arg2=./CorpusFolder/
flag3=-tagged
arg3=True
flag4=-textfile
arg4=input.txt

time python $filename $flag1 "$arg1" $flag2 $arg2 $flag3 $arg3 $flag4 $arg4
