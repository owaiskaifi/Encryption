import random

#========= word list gen===========

hash_file = 'hash.txt'
wordlist = 'wordlist.txt'


minimum=int(input('Please enter the minimum lenght of any give word to be generated: '))

maximum=int(input('Please enter the maximum lenght of any give word to be generated: '))

wmaximum=int(input('Please enter the max number of words to be generated in the dictionary: '))

alphabet = 'fda0345a77cb7ea8b69490ee39fcecf61fdf0f56960d8177b50d4dd94f353e0a'

xrange=range
file = open(wordlist,"a")
for count in xrange(0,wmaximum) :
	for x in random.sample(alphabet,random.randint(minimum,maximum)) :
		file.write(x)
	file.write("\n")
file.close()
print ( 'DONE!' )

import hashlib, sys
m = hashlib.sha256()
hash = ""
try:     
	hashdocument = open(hash_file,"r")
except IOError:
 	print("Invalid file.")
 	input()
 	sys.exit()
else:     
	hash = hashdocument.readline()
	hash = hash.replace("\n","")

try:
	wordlistfile = open(wordlist,"r")
except IOError:
	print ("Invalid  file.")
	input()
	sys.exit()
else:
	pass
for line in wordlistfile:    
	m = hashlib.sha256()     
	line = line.replace("\n","")
	m.update(line.encode(wordlistfile.encoding))
	word_hash = m.hexdigest()          
	if word_hash==hash:
		print ("Collision! The word corresponding to the given hash is",line ,)
		input()
		sys.exit()
print("The hash given does not correspond to any supplied word in the wordlist.")
input()
sys.exit()