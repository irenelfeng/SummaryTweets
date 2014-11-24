#!/bin/bash
#runs the python code with the appropriate parameters

filename=tf_idf.py
flag1=-text

#arg1="We are elders of the Maasai from Tanzania, one of Africa's oldest tribes. The government has just announced that it plans to kick thousands of our families off our lands so that wealthy tourists can use them to shoot lions and leopards. The evictions are to begin immediately. Last year, when word first leaked about this plan, almost one million Avaaz members rallied to our aid."
#arg1="Dashing through the snow. In a one horse open sleigh. O'er the fields we go. Laughing all the way. Bells on bob tails ring. Making spirits bright. Oh what fun it is to laugh and sing. A sleighing song tonight."
#arg1="As we begin entering the holiday season, it's great to remember everything we're thankful for ! I am thankful for you and a yellow banana. Unfortunately, there a lot of people in the Upper Valley area who are in need of basic necessities, such as warm clothes and food. Dartmouth Christian Union's community service team is raising money for Salvation Army's Star Tree program. Through this program, we'll be able to provide gifts for the families we have adopted. We are also providing an incentive to participate in the fundraiser! We will be raffling off two Dartmouth sweatshirts and and an EBA's pizza at the end of the fundraiser to three lucky winners!!! Although this fundraiser is being run through Christian Union, the Salvation Army's Star Tree does not discriminate towards families on the basis of religion or beliefs. Therefore, we encourage EVERYONE to donate! Your contribution is both meainingful and extremely important. You can find more information on the GOFUNDME page:"
#arg1="Dashing through the snow. In a one horse open sleigh.https://docs.google.com/~presentation/d/1a-okr8-1LtHh6FhSxzz59AxnLXbtXf6nTQ2oKgAYH5w/edit#slide=id.p O'er the fields we go. Laughing all the way. Bells on bob tails ring. Making spirits bright. Oh what fun it is to laugh and sing. A sleighing song tonight."
#arg1="As we begin entering the holiday season, it's great to remember everything we're thankful for! Unfortunately, there a lot of people in the Upper Valley area who are in need of basic necessities, such as warm clothes and food. Dartmouth Christian Union's community service team is raising money for Salvation Army's Star Tree program. Through this program, we'll be able to provide gifts for the families we have adopted. We are also providing an incentive to participate in the fundraiser! We will be raffling off two Dartmouth sweatshirts and and an EBA's pizza at the end of the fundraiser to three lucky winners!!! Although this fundraiser is being run through Christian Union, the Salvation Army's Star Tree does not discriminate towards families on the basis of religion or beliefs. Therefore, we encourage EVERYONE to donate! Your contribution is both meainingful and extremely important. You can find more information on the GOFUNDME page:"
#arg1="There is no limit to the knowledge you can inject into the channel model. For example, some mistakes tend to be extremely common because they appear so often that people don't realize that they're incorrect; the channel model could model this by accounting for the frequency of each error. Certain errors are also particularly frequent. Misspellings, unless they are typos, tend to correspond to the same pronunciations, so one could consult a grapheme-to-phoneme model. Different keyboards give rise to different sorts of typos one could even model the relative frequencies of keyboard configurations. Finally, we'd ideally learn the relative probabilities/costs for each edit from a large corpus of spelling errors, using the the EM algorithm that we'll see next week, rather than relying on messy heuristics. The design of channel models that take into account all such factors is an ongoing research question (and a possible final project topic)."
#arg1="A summary is a concise description that reflects the essence of a subject. A text, a collection of text documents, or a query answer can be summarized by simple means such as an automatically generated list of the most frequent words or \"advanced\" by a meaningful natural language description of the subject. In between these two extremes, conceptual summaries encompass selected concepts derived using background knowledge. We address in this paper http://www.cs.dartmouth.edu/cgi-bin/cgiwrap/ifeng/summary.cgi an approach where conceptual summaries are provided through a conceptualization as given by an ontology.The ontology guiding the summarization can be a simple taxonomy or a generative domain on-tology. A domain ontology can be provided by a preanalysis of a domain corpus and can be usedto condense improved summaries that better reflects the conceptualization of a given domain."
#arg1="http://www.cnn.com/2014/11/24/politics/defense-secretary-hagel-to-step-down/index.html?hpt=hp_t1"
arg1="http://money.cnn.com/2014/11/24/investing/digital-ally-ferguson/index.html?iid=A_MKT_News"
#arg1="https://secure.avaaz.org/en/stand_with_the_maasai_2014a/?rc=fb&pv=50"
#arg1="The move, White House officials told the Times, was meant to acknowledge that the new national security threats facing the nation — most notably the rise of the Islamic State in Iraq and Syria — call for a different kind of leadership in the Defense Department."
#arg1="The Neukom DALI lab http://dali.dartmouth.edu focuses on social justice and social entrepreneurship projects.  We also work on clever, fun projects that push the envelope of design and technology, if we believe it has a meaningful real-world application. We work with engineers and doctors to build communication systems and interfaces for new medical devices and non-profits to display large data sets effectively.  We are designing and creating a line of high end digital fashion and robots that can be used for urban planning."
#arg1="We are elders of the Maasai from Tanzania, one of Africa's oldest tribes. The government has just announced that it plans to kick thousands of our families off our lands so that wealthy tourists can use them to shoot lions and leopards. The evictions are to begin immediately. https://secure.avaaz.org/en/stand_with_the_maasai_2014a/?rc=fb&pv=50 Last year, when word first leaked about this plan, almost one million Avaaz members rallied to our aid. Your attention and the storm it created forced the government to deny the plan, and set them back months. But the President has waited for international attention to die down, and now he's revived his plan to take our land. We need your help again, urgently. President Kikwete may not care about us, but he has shown he'll respond to global media and public pressure -- to all of you! We may only have hours. Please stand with us to protect our land, our people and our world's most majestic animals and tell everyone, before it is too late. This is our last hope."
#arg1="If you are unsure why you lost points on a homework or exam problem, or feel that the grader made a mistake, you must act before the resolution deadline for that homework - exam. The resolution deadline for a homework is the submission deadline of the next homework. The resolution deadlines for Midterm 1, Midterm 2, and Homework 8 are 11:59pm on Oct 16, Nov 13, and Nov 18 respectively. Before the resolution deadline you must first contact the relevant grader(s) and try to resolve the matter with them."
#arg1="We will begin with an overview of mathematical notation and the basic concepts of sets, functions, and relations. We will then study logic, proof techniques, combinatorics (counting), probability, and the beginnings of graph theory. By the end of this course, you will have become familiar with a number of discrete structures that are used throughout computer science."
#flag4=-textfile
#arg4=input.txt

flag2=-c
arg2=./CorpusFolder/
flag3=-tagged
arg3=True


time python $filename $flag1 "$arg1" #$flag4 $arg4
