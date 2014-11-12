from collections import defaultdict
import argparse
import math
import os
import re
import collections
import nltk

class tfidf:
	def __init__(self, corpusDirectory, tagged):
		self.allCorpora = {} #will be a dictionary pointing to the corpus file, each of which is a dictionary of the all the word counts.
		self.allPoSCorpora = {} 
		self.testWhatPOS = set()
		for filename in os.listdir(corpusDirectory):
			if filename.endswith(".pos"):
				if tagged == False:
					self.wordDictionary(corpusDirectory+str(filename))
				else:
					self.taggedWordDictionary(corpusDirectory+str(filename))
		print self.testWhatPOS


	def wordDictionary(self, filename): #deprecated 
		"""returns the file as a dictionary with word counts"""
		wordCount = defaultdict(int)
		words = open(str(filename)).readlines()
		for line in words:
			"""insert a function to clean up lines"""
			line = line.split()
			for word in line:
				wordCount[word] +=1
		print wordCount
		self.allCorpora[filename] = wordCount #adds the corpus to the corpora dictionary
	
	def taggedWordDictionary(self, filename):
		wordCount = defaultdict(int)
		tagCount = defaultdict(int)
		words = open(str(filename)).readlines()
		for line in words:
			"""insert a function to clean up lines"""
			line = line.split()
			for word in line:
				m = re.match(r"(?P<word>[\w.,!?()-]+)(\/)(?P<tag>[\w.,!?()-]+)", word) 
				if m != None:
					#print m.group('word'), m.group('tag')
					wordCount[m.group('word')] +=1
					tagCount[m.group('tag')] +=1
					self.testWhatPOS.add(m.group('tag'))
		self.allCorpora[filename] = wordCount #adds the corpus to the corpora dictionary
		self.allPoSCorpora[filename] = tagCount #adds the corpus to the corpora dictionary


	def tf_idf(self, inputText):
		"""returns a tf-idf dictionary for each term in inputText"""

		tfidfDict = {}
		#create a word Dictionary for the input text
		inputWordDictionary = defaultdict(int)
		inputText = re.sub('([.,!?()])', r' \1 ', inputText) #regex code to add a space between punctuation
		inputText = inputText.split()
		for word in inputText:
			inputWordDictionary[word] +=1

		# term frequency * log (# files total / # files with term)
		for word in inputText:
			#print "\n",word

			tf = inputWordDictionary[word]
			#print "tf", tf
			numfiles = 0
			for corpus in self.allCorpora:
				if word in self.allCorpora[corpus]:
					numfiles +=1
			if numfiles ==0: #if the word isn't in any of the corpora
				numfiles = .1 #assume it is important -- might change that later: the word is either important or mispelled 
			idf = math.log((len(self.allCorpora)/(numfiles)))

			tfidf = tf * idf
			#print 'tf', tf, "| idf", idf

			tfidfDict[word] = tfidf
		return tfidfDict
	
	def summarize(self, inputText, scores): #not working
		IDScore = {}
		sentences = re.split('(?<=[.!?]) +', inputText)
		for i, j in enumerate(scores):
			print i,j
			occurances = 0
			for counter,sentence in enumerate(sentences):
				occurances = sentence.count(j) #needs to not count words inside of words
			print occurances

		#sentenceScores = sorted(student_tuples, key=lambda student: student[2])
		return summary

	def topSentences(self, inputText, scores):
		"""returns the top Sentences by taking the top 10 percent of words"""
		inputText = re.sub('([.,!?()])', r' \1 ', inputText)
		sentences = re.split('(?<=[.!?-]) +', inputText)
		sentenceList = []

		numWords = int(math.ceil(float(len(scores))/10)) #sets numWords to be the top 10 percent of words
		words = [] #a list of the top words
		for i in range(0, numWords):
			maxWord = max(scores.iterkeys(), key=lambda key: scores[key]) 
			print maxWord
			k= scores.pop(maxWord)
			words.append((maxWord, k)) 
		print words
		print inputText
		#print sorted(words, key=lambda key: words[i])
		for word, val in words:
			for sentence in sentences: 
				wordList = sentence.split()
				if word in wordList and sentence not in sentenceList: #if the word is in the sentence and the sentence is not already in the list
						sentenceList.append(sentence)
		for sentence in sentenceList:
			tokenized = sentence.split()
			tags = nltk.pos_tag(tokenized)
			print tags


		return sentenceList
		#max(stats.iteritems(), key=operator.itemgetter(1))[0]



if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', type=str, help='corpus', required=True)
	parser.add_argument('-text', type=str, help='input file', required=True)
	parser.add_argument('-tagged', type=str, help='boolean for tagged or not', required=False, default=False)
	args = parser.parse_args()

	print "Parsing Corpus..."
	program = tfidf(args.c, args.tagged)
	print "Calculating Score..."
	scores = program.tf_idf(args.text)
	print scores
	#summary = program.summarize(args.text, scores)
	summary = program.topSentences(args.text, scores)
	print summary
