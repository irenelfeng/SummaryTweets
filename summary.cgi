#!/usr/bin/python

"""TEST CGI""" 

import cgitb; cgitb.enable()
import tf_idf
import cgi

print "Content-type: text/html"
print 
print "<html><head>"
print "<title>Web Interface Summary Tweets"
print "</title>"
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"styles/layout.css\">"
print "<style>"
print ".box{height: 550px; float: left; border: 1px solid #cdcdcd; padding: 10px;}"
print "</style>"
print "</head><body style=\"padding: 20px;\">"

print "<h1><center>Summary Tweets</center></h1>"

form = cgi.FieldStorage()

textbox = form.getvalue("textbox", "")
#textfile = form["textfile"]
#if "textfile" in form:
	#textfile = form["textfile"] 
	#textfile = form.getvalue("textfile")

print "<div class=\"box\" style=\"width:40%;\"><h1>Enter your input text</h1><p>"
print "<form action=\"summary.cgi\" method=\"post\">" #action is the name of the page?? 
print "<textarea rows=\"25\" cols=\"70\" name=\"textbox\">"
print cgi.escape(textbox)+"</textarea><p>"
#print "<h2>Or Upload a file: <input type=\"file\" name=\"textfile\"/></h2>"
#print "*.txt files only<p>"

print "<input type=\"submit\" value=\"Submit\"></form><p>"
print "</div>"

program = tf_idf.tfidf("CorpusFolder/")
#print textfile
#if textfile.file:
	#text = textfile.file.read()
	#print text
	#textbox = text #sets textbox to whatever is uploaded 

textbox = textbox.lower()

print "<div class=\"box\" style=\"width: 55%; margin-left: 5px;\">"
print "<h3>Results</h3>"
scores = program.tf_idf(textbox)
#summary = program.topSentences(args.text, scores)
summary2 = program.total_sent_score(textbox, scores,5)
#print summary
print summary2
print "</div>"
print "<div style=\"clear: both;\"></div>"
print "</body></html>"
