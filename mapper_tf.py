#!/usr/bin/python
import sys, re
import string
from string import digits
#import nltk
#from nltk.corpus import stopwords
#from nltk.stem import *
#stemmer = PorterStemmer()
punctuation = set(string.punctuation)
#removestop = stopwords.words("english")
#s = "string. With. Punctuation?" # Sample string 
#out = s.translate(string.maketrans("",""), string.punctuation)
def clean_data(sth):
	sth.lower()
	sth=''.join(i for i in sth if ord(i)<128)
	sth = ''.join(ch for ch in sth if ch not in punctuation)
	sth=''.join([i for i in sth if not i.isdigit()])
#	sth=' '.join([i for i in sth.split() if i not in removestop])
	return sth

#fham=open(pathname+hamname)
for line in sys.stdin:
    line= clean_data(line)
    line.strip()
    for token in line.split():
		#token=stemmer.stem(token)
		sys.stdout=open("mapoutspam.txt","a")
		if token: print token + '\t1'