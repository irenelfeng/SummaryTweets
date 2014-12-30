SummaryTweets
=============

##Authors
Irene Feng, Orestis Lykouropoulos, Patrick Xu

##Overview
SummaryTweets is python-based sentence compression program which primarily uses TF-IDF an phrase substitution to reduce the length of a given text to the desired length. SummaryTweets has a default output length of 140 characters, the length of one Tweet.

We use TF-IDF, or Term Frequency-Inverse Document Frequency, as a way to determine the importance of terms in a sentence, which we then sum within each sentence to build a sentence score. In general, TF-IDF is based upon the idea that, given a large enough sample text, the frequency of a word is inversely related to its importance. Using word counts from a large collection of sample texts, a corpus, we can assign each word a score which reflects its importance. Using these scores, we can determine the importance of a sentence. TF-IDF is not a perfect scoring method but has nonetheless proved quite accurate in our application.

Phrasal substitution is achieved through information from the Paraphrase Database (PPDB). Over 30,000 lexical rules are currently utilized by SummaryTweets, although there exists the possibility of utilizing far more at the trade off of substitution accuracy.

##How to Use
SummaryTweets has been uploaded to the following webpage.

http://www.cs.dartmouth.edu/cgi-bin/cgiwrap/patxu/summary.cgi

It can also be used by running the bash shell script file run.sh. This runs tf_idf.py using approriate input arguments.
The python file itself can be run with
```python
python tfidf
```
Use the flag "-h" for information about the input arguments.

##Structure
/CorpusFolder- contains the Brown Corpus and arpa bigram probabilities

/pickl- contains the serialized dictionaries for our corpus. These dictionaries are used for sentence compression and TF-IDF

/stat_parser- uses the CKY algorithm to return a parse tree of a sentence

/styles- files for marking up the webpage

