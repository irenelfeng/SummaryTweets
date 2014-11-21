from stat_parser import Parser
import re
import nltk
import numpy

nouns = ['NN','NNS','NNP','NNPS']
adverbs = ['RB','RBR','RBS']
adjs = ['JJ','JJR','JJS']
nodrop = ['not','never']

def tag(text):
	parser = Parser()
	#print "done with initializing parser"
	sentences = re.split('(?<=[.!?-]) +', text)
	# tree = parser.parse(text)
	# for subtree in tree.subtrees():
	# 	print subtree
	# 	print "parent = {0}".format(subtree.parent())
	# return tree


def drop_phrases(sentences, text):
	"""reads in sentences and drops certain parts of speech based on their tf-idf score"""
	parser = Parser()

def simple_drop(sentences, text, scores):
	"""more simple"""
	score = numpy.percentile([scores.values()], 75) #threshold for deleting words - upper quartile
	#print score

	for sentence in sentences:
		tokenized = [i[0] for i in sentence[0]] #just gets word in the sentence
		POS = nltk.pos_tag(tokenized)
		#print POS
		for i, word_tuple in enumerate(sentence[0]):
			if POS[i][1] in adjs: #if adj
				#if the word coming after the adjective is a noun and the adj is not important by tf_idf, delete it
				if i < len(sentence[0])-1 and POS[i+1][1] in nouns and word_tuple[1]<= score and word_tuple[0] not in nodrop:
					sentence[0].remove(word_tuple)
					print "removed {0}".format(word_tuple)
			elif POS[i][1] in adverbs:
				if word_tuple[1]<=score and word_tuple[0] not in nodrop:
					sentence[0].remove(word_tuple)
					print "removed {0}".format(word_tuple)
	return sentences


