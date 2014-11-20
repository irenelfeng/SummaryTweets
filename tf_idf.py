from collections import defaultdict, Counter
import argparse
import math
import os
import re
import collections
import pickle
import sys
import string
import parse_compress #code to parse sentences and delete based on 

class tfidf:
	def __init__(self):
		"""reads corpus files and adds it to all_corpora"""
		all_corpora = open('pickl/allCorpora')
		#all_pos_corpora = open('pickl/allPosCorpora')

		all_phrases = open('pickl/allPhrases')

		self.all_corpora = pickle.load(all_corpora) #will be a dictionary pointing to the corpus file, each of which is a dictionary of the all the word counts.
		#self.all_pos_corpora = pickle.load(all_pos_corpora)
		self.all_phrases = pickle.load(all_phrases)

		all_corpora.close()
		#all_pos_corpora.close()
		all_phrases.close()

		#store url, if any
		self.url = ''

	def has_url(self):
		return self.url != ''
	
	def get_input_text(self, filename):
		"""returns the text within a file for summarizing"""
		try:
			my_file = open(filename, 'r')
			text = ''
			for line in my_file:
				text = text + line
			return text
		except IOError:
			print 'ERROR: Invalid filename'
			return False

	def read_input_text(self, input_text):
		"""preprocesses the input_text. removes and stores the url, and also fixes any ascii character bugs"""
		#first search for a url, store it and remove it from the input text
		m = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[~$-_@.&#+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', input_text) #we are assuming only 1 url per input - makes sense in the context of twitter
		if m: #if there is a url
			self.url = str(m.group(0))
			#print self.url
			input_text = input_text.replace(self.url, '')
		tree_tags = parse_compress.tag(input_text) #maybe move somewhere else in the end

		###for orestis for ascii characters

		return input_text

	def tf_idf(self, input_text):
		"""returns a tf-idf dictionary for each term in input_text"""

		tfidf_dict = {}
		#create a word Dictionary for the input text
		input_word_dictionary = defaultdict(int)
		# input_text = re.sub('([.,!?()])', r' \1 ', input_text) #regex code to add a space between punctuation
		input_text = input_text.split()
		for w in input_text:
			word = w.strip("'.,!?;:'*()")
			input_word_dictionary[string.lower(word)] +=1

		# term frequency * log (# files total / # files with term)
		for w in input_text:
			#print "\n",word
			word = w.strip("'.,!?;:'*()")

			tf = input_word_dictionary[string.lower(word)]
			#print "tf", tf

			num_files = 0
			for corpus in self.all_corpora:
				if word in self.all_corpora[corpus]:
					num_files +=1
			if num_files ==0: #if the word isn't in any of the corpora
				num_files = .1 #assume it is important
			idf = math.log((len(self.all_corpora)/(num_files)))

			tfidf = tf * idf
			#print 'tf', tf, "| idf", idf

			tfidf_dict[string.lower(word)] = tfidf
		return tfidf_dict

	# def top_sentences(self, input_text, scores):
	# 	"""returns the top Sentences by taking the top 10 percent of words"""
	# 	input_text = re.sub('([.,!?()])', r' \1 ', input_text)
	# 	sentences = re.split('(?<=[.!?-]) +', input_text)
	# 	sentence_list = []

	# 	#delete any urls (urls are still stored for later)
	# 	if self.has_url(): input_text = input_text.replace(' '+self.url, '')

	# 	num_words = int(math.ceil(float(len(scores))/10)) #sets num_words to be the top 10 percent of words
	# 	words = [] #a list of the top words
	# 	for i in range(0, num_words):
	# 		max_word = max(scores.iterkeys(), key=lambda key: scores[key]) 
	# 		# print max_word
	# 		k= scores.pop(max_word)
	# 		words.append((max_word, k)) 

	# 	#print sorted(words, key=lambda key: words[i])
	# 	for word, val in words:
	# 		for sentence in sentences: 
	# 			wordList = sentence.split()
	# 			if word in wordList and sentence not in sentence_list: #if the word is in the sentence and the sentence is not already in the list
	# 					sentence_list.append(sentence)
	# 	# for sentence in sentence_list:
	# 	# 	tokenized = sentence.split()
	# 	# 	tags = nltk.pos_tag(tokenized)
	# 		#print tags

	# 	return sentence_list
		#max(stats.iteritems(), key=operator.itemgetter(1))[0]

	def total_sent_score(self, input_text, scores):
		"""Compute the total tf-idf score of a sentence by summing the scores of each word in each sentence"""
		# input_text = re.sub('([.,!?()])', r' \1 ', input_text) #I took these two lines from top_sentences

		#print "\nThe input text is:\n", input_text, "\n"

		sentences = re.split('(?<=[.!?-]) +', input_text)

		#top_sentences = Counter()
		top_sentences = []

		for index, sentence in enumerate(sentences):
			words = sentence.split()
			total_score = 0.0
			num_words = 0.0
			word_list = []
			if len(sentence) > 1: #to avoid single punctuation marks or one-word sentences.
				for word in words:
					num_words += 1
					score = scores[string.lower(word.strip("'.,!?;:'*()"))]
					total_score += score
					word_list.append((word, score))

				#if num_words != 0: top_sentences[sentence] = (total_score / num_words, index)
				#if num_words != 0: top_sentences.append((sentence, total_score / num_words, index))
				if num_words != 0: top_sentences.append((word_list, total_score / num_words, index))
				# top_sentences[sentence] = total_score

		"""returns all the sentences with a score and index"""
		#print top_sentences
		return top_sentences 
		#return top_sentences.most_common(num_sentences)

		
	def delete_phrases(self, sentences_in_lists, input_text, scores):

		"""deletes words and (like total_sent_score) returns sentences with score and index"""
		#sentences_in_lists = parse_compress.drop_phrases(sentences_in_lists)
		#print "before: {0}".format(sentences_in_lists)
		parse_compress.simple_drop(sentences_in_lists, input_text, scores)
		#print "after: {0}".format(sentences_in_lists)


	def compress_sentences(self, sentences_in_lists, out_length):
		"""compresses and returns the sentences within our desired length"""
		sentences = []
		
		"""compression"""
		for sent_list in sentences_in_lists:
			max_changes = len(sent_list[0])/2 #the greatest number of changes we want to make
			bigrams = []
			first = ('', 0)
			second = ('', 0)
			for index, word in enumerate(sent_list[0]):
				first = second
				second = word
				if first[0] == '': continue# or second[0] == '.': continue
				bigrams.append((first[0] + ' ' + second[0], first[1]+second[1], index))
			bigrams.sort(key = lambda x:x[1])
			changes = 0
			new_sent = []
			for bigram in bigrams:
				if changes > max_changes: break
				if self.all_phrases.has_key(bigram[0]):
					#print 'changing', bigram[0], '>>>', self.all_phrases[bigram[0]]
					bigram = (self.all_phrases[bigram[0]], bigram[1], bigram[2])

			seen = [] #list of indices of bigrams changed

			for bigram in bigrams:
				if changes > max_changes: break
				if bigram[0] in self.all_phrases:
					#print 'changing', bigram[0], '>>>', self.all_phrases[bigram[0]]
					bigram = (self.all_phrases[bigram[0]], bigram[1], bigram[2])
					seen.append(bigram[2]) #remember that this bigram was changed
					changes += 1
				new_sent.append(bigram)

			new_sent.sort(key = lambda x:x[2])
			#print new_sent
			sentence = ''
			for ind,i in enumerate(new_sent):
				if i[2]-1 in seen and not i[2] in seen: continue
				word = i[0].split()
				sentence += word[0]
				if ind < len(new_sent):
					sentence += ' '
			try:	
				sentence += new_sent[len(new_sent)-1][0].split()[1]
			except IndexError:
				sentence += ''

			sentences.append((sentence, sent_list[1], sent_list[2]))

		"""ordering, printing to correct length"""
		output = []
		total_length = 0
		sentences.sort(key = lambda x:x[1], reverse = True)

		for sentence in sentences:
			#print sentence
			length = len(sentence[0]) + 1 #+1 for space before sentences
			if total_length + length > out_length:
				continue
			total_length += length

			"""insert sentences in the correct order"""
			counter = 0
			for i in range(len(output)): 
				if output[i][2] < sentence[2]:
					counter += 1
			output.insert(counter, sentence)

		"""create the output string"""
		out_string = ''
		for i in output:
			out_string += i[0] + ' '
		out_string +=self.url

		return out_string

if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-text', type=str, help='input text', required=False)
	parser.add_argument('-textfile', type=str, help='boolean if given input file', required=False)
	parser.add_argument('-length', type=str, help='length of final compression', required=False, default=134) #140 for twitter, -6 for #CS73 hashtag+space
	args = parser.parse_args()

	if args.text is None and args.textfile is None:
		print "Either command line text or a text file is required!"
		sys.exit() 

	print "Parsing Corpus..."
	program = tfidf()
	if args.textfile != None:
		print 'Opening Input Text File...'
		text = program.get_input_text(args.textfile)
		args.text = text
		if text == False:
			sys.exit() 
	print "Calculating Score..."

	# args.text = args.text.lower() #added to make lowercase

	processed_text = program.read_input_text(args.text)
	scores = program.tf_idf(processed_text)
	# print scores
	# print'\n'

	#summary = program.top_sentences(args.text, scores)
	summary2 = program.total_sent_score(processed_text, scores)
	program.delete_phrases(summary2, processed_text, scores)
	#print summary
	#print summary2
	if program.has_url(): length = args.length - 23 #-23 for link+space(twitter condenses all links to max 22 characters)
	else: length = args.length
	print length
	output = program.compress_sentences(summary2, length)

	print "url:"
	print program.url
	print 'The output text is:'
	print output
