from stat_parser import Parser
import re
import nltk
import numpy
import pickle

nouns = ['NN','NNS','NNP','NNPS']
adverbs = ['RB','RBR','RBS']
adjs = ['JJ','JJR','JJS']
nodrop = ['not','never']

class compressor:
	
	def __init__(self):
		"""dictionaries loaded"""
		all_phrases = open('pickl/allPhrasesProb')
		#bigram_dic = open('pickl/bigramDic')
		#unigram_dic= open('pickl/unigramDic')
		self.all_phrases = pickle.load(all_phrases)
		#self.bigram_dic = pickle.load(bigram_dic)
		#self.unigram_dic = pickle.load(unigram_dic)
		all_phrases.close()
		#bigram_dic.close()
		#unigram_dic.close()


	def simple_drop(self, sentences, text, scores):
		"""drops adjs and adverbs based on tf-idf scores and location"""
		score = numpy.percentile([scores.values()], 75) #threshold for deleting words - upper quartile
		#print score
		for sentence in sentences:
			tokenized = [i[0] for i in sentence[0]] #just gets word in the sentence

			POS = nltk.pos_tag(tokenized)
			#print POS
			for i, word_tuple in enumerate(sentence[0]):
				#print "word: {0}, POS {1}".format(word_tuple, POS[i][1])
				if POS[i][1] in adjs: #if adj
					#if the word coming after the adjective is a noun and the adj is not important by tf_idf, delete it
					if i < len(sentence[0])-1 and POS[i+1][1] in nouns and word_tuple[1]<= score and word_tuple[0] not in nodrop:
						sentence[0].remove(word_tuple)
						del POS[i]
						#print "removed {0}".format(word_tuple)
				elif POS[i][1] in adverbs:
					if word_tuple[1]<=score and word_tuple[0] not in nodrop:
						sentence[0].remove(word_tuple)
						del POS[i]
						#print "removed {0}".format(word_tuple)
		return sentences

	def get_dictionary_paraphrase(self, unigram): 
		"""gets best phrase"""
		#r_punc and l_punc just to keep syntax
		r_punc = ''
		l_punc = ''
		if unigram.rstrip(".'.,!?;:'*)]") != unigram: #if there exists a punctuation on the right
			r_punc = unigram[-1]
		if unigram.lstrip(".'.,!?;:'*([") != unigram: #if there exists a punctuation on the left
			l_punc = unigram[-1]

		unigram_uniform = unigram.strip(".'.,!?;:'*()[]").lower()
		for poss_paraphrase in self.all_phrases[unigram_uniform]:
			prob_p = self.all_phrases[unigram_uniform][poss_paraphrase]
			print "{0} changes to {1} with prob {2}".format(unigram, poss_paraphrase, prob_p)

		#new_unigram = self.all_phrases[unigram.strip(".'.,!?;:'*()[]").lower()] #gets the unigram from dictionary

		#if unigram[0].lower() != unigram[0]: #check if capitalized
			#new_unigram = new_unigram.capitalize() #then also capitalize the new unigram
		#new_unigram = l_punc + new_unigram + r_punc
		return unigram

	def compress_sentences(self, sentences_in_lists):
		sentences = []

		"""unigram compression"""
		for sent_list in sentences_in_lists:
			max_changes = len(sent_list[0])/2 #the greatest number of changes we want to make in each sentence
			unigrams = []
			changes = 0
			new_sent = []
			#for index, word in enumerate(sent_list[0]):
				#if word[0] == '': continue
				#unigrams.append((word[0], word[1], index)) #Probably don't need index OLD CODE
			#unigrams.sort(key = lambda x:x[1]) #sort based on score
			#
			# for sentence in sent_list[0]:
			# 	print sentence
			for index, unigram in enumerate(sent_list[0]):
			#if changes > max_changes: break
				unigram_uniform = unigram[0].strip(".'.,!?;:'*()[]").lower() #stripped and lowercased to check in the dictionary
				if unigram_uniform in self.all_phrases:
					#print "changing:", unigram[0], ">>>", self.get_dictionary_paraphrase(unigram[0])
					if index != 0: prev_word = sent_list[0][index-1][0]
					else: prev_word = ''
					if index != len(sent_list[0])-1: sent_list[0][index-1][0]
					else: next_word = '' 
					unigram = (self.get_dictionary_paraphrase(unigram[0]), unigram[1])
					changes += 1
				new_sent.append(unigram)

			#new_sent.sort(key = lambda x:x[2])
			sentence = ''
			for ind,i in enumerate(new_sent):
				word = i[0]
				sentence += word
				if ind < len(new_sent):
					sentence += ' '

			sentences.append((sentence, sent_list[1], sent_list[2]))

		return sentences

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


