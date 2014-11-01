from collections import defaultdict
import argparse
import math
import os

class tfidf:
	def __init__(self, corpusDirectory):
		self.allCorpora = {} #will be a dictionary pointing to the corpus file, each of which is a dictionary of the all the word counts.
		for filename in os.listdir(corpusDirectory):
			if filename.endswith(".txt"):
				self.wordDictionary(corpusDirectory+str(filename))

	def wordDictionary(self, filename):
		"""returns the file as a dictionary with word counts"""
		wordCount = defaultdict(int)
		words = open(str(filename)).readlines()
		for line in words:
			line = line.split()
			for word in line:
				wordCount[word] +=1
		print wordCount
		self.allCorpora[filename] = wordCount #adds the corpus to the corpora dictionary

	def tf_idf(self, inputText):
		"""returns a tf-idf dictionary for each term in inputText"""

		tfidfDict = {}
		#create a word Dictionary for the input text
		inputWordDictionary = defaultdict(int)
		inputText = inputText.split()
		for word in inputText:
			inputWordDictionary[word] +=1

		# term frequency * log (# files total / # files with term)
		for word in inputText:
			print word

			tf = inputWordDictionary[word]
			print tf
			numfiles = 0
			for corpus in self.allCorpora:
				if word in self.allCorpora[corpus]:
					numfiles +=1
			idf = math.log((len(self.allCorpora)/(numfiles)))
			print len(self.allCorpora)/numfiles
			tfidf = tf * idf

			tfidfDict[word] = tfidf
		return tfidfDict

if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', type=str, help='', required=True)
	parser.add_argument('-text', type=str, help='', required=True)
	args = parser.parse_args()

	program = tfidf(args.c)
	scores = program.tf_idf(args.text)
	print scores

