#!/usr/bin/python
import sys, re
import string
from string import digits
#from nltk.corpus import stopwords
#from nltk.stem import *
#stemmer = PorterStemmer()
punctuation = set(string.punctuation)
#removestop = stopwords.words("english")
def clean_data(sth):
	sth.lower()
	sth=''.join(i for i in sth if ord(i)<128)
	sth = ''.join(ch for ch in sth if ch not in punctuation)
	sth=''.join([i for i in sth if not i.isdigit()])
#	sth=' '.join([i for i in sth.split() if i not in removestop])
	return sth

def read_cache(spamfile,hamfile):
	p_dict_spam=dict()
	p_dict_ham =dict()
	fspam=open(spamfile)
	for line in fspam:
		line = line.strip()
		word, p = line.split('\t', 1)
		p_dict_spam[word]= p
		#print p_dict_spam
	fspam.close
	fham=open(hamfile)
	for line in fham:
		line = line.strip()
		word, p = line.split('\t', 1)
		p_dict_ham[word]= p
	fham.close
	p_dict = dict()
	for key in (p_dict_spam.viewkeys() | p_dict_ham.viewkeys()):
		if key in p_dict_spam: 
			p_dict.setdefault(key, []).append(p_dict_spam[key])
		else:
			p_dict.setdefault(key, []).append(1)
		if key in p_dict_ham: 
			p_dict.setdefault(key, []).append(p_dict_ham[key])
		else:
			p_dict.setdefault(key, []).append(1)
		
		
	return p_dict

spamfile="reduceoutdictspam.txt"
hamfile="reduceoutdictham.txt"


#fham=open(pathname+hamname)
p_dict_spam={}
p_dict_ham ={}
p_dict=read_cache(spamfile,hamfile)

	
for line in sys.stdin:
	line= clean_data(line)
	
	for w in line.split():
		w=stemmer.stem(w)
		#print w
		sys.stdout=open("mapoutprobability.txt","a")
		al= p_dict.get(w,['1','1'])
		print w, '\t', al[0],'\t', al[1]
