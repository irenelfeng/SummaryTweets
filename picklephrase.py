import glob 
import pickle
import re
def pickl(filename1):

		outfile1 = open(filename1, 'w')

		pickle.dump(phrase_dict,outfile1, pickle.HIGHEST_PROTOCOL)
		outfile1.close()

		print "Done!"
if __name__=='__main__':
	phrase_dict = {} #maybe dictionary of tuples later
	testPos = set()
	for filename in glob.glob('pickl/ppdb-*'):
		paraphrase = open(filename, 'r')
		for line in paraphrase:
			line = line.split('|||')
			word = line[2].strip() #target e
			otherWord = line[1].strip() #source f
			if len(word) > len(otherWord): #if e > f
				#print word 
				#print otherWord
				#m = re.search('\sp\(e\|f\)=([0-9.]+)', line[3]) #get prob(f|e), probability of shorter given longer.
				#print m.group(1)
				#print line
				#phrase_dict[(word, otherword)] = ###WILL ADD 
				phrase_dict[word] = otherWord
			elif len(otherWord) > len(word): #if f > e
				#m = re.search('\sp\(e\|f\)=([0-9.]+)', line[3]) #get prob(f|e), probability of shorter given longer.
				phrase_dict[otherWord] = word
			testPos.add(line[0])
		paraphrase.close()
	for pos in testPos:
		print pos
	pickl('pickl/allPhrases')
	pickled = open('pickl/allPhrases', 'r')
	phrases = pickle.load(pickled)
	#print phrases