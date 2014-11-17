SummaryTweets
=============

##Authors
Irene Feng

Orestis Lykouropoulos

Patrick Xu

##How to Use
SummaryTweets has been uploaded to the following webpage.
http://www.cs.dartmouth.edu/cgi-bin/cgiwrap/ifeng/summary.cgi

It can also be used by running the bash shell script file run.sh. This runs tf_idf.py using approriate input arguments.
The python file itself can be run with
```python
python tfidf
```
Use the flag "-h" for information about the input arguments.

##Structure
/CorpusFolder- contains the Brown Corpus
/bc3&framework.1.1- corpus of summaries (unused)
/pickl- contains the serialized dictionaries for our corpus. These dictionaries are used for sentence compression and tf-idf
/styles- files for marking up the webpage

