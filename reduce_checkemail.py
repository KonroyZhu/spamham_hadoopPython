#!/usr/bin/env python

from operator import itemgetter
import sys,math

spam_sum=0
ham_sum=0


spamProb=0.5
hamProb=0.5
# input comes from STDIN
for line in sys.stdin:
	line = line.strip()
	word, spam, ham = line.split('\t')
	spam = float(spam)
	ham = float(ham)

	spam_sum+=math.log10((spam*spamProb)/(ham*spamProb+spam*hamProb))
	ham_sum+=math.log10((ham*spamProb)/(ham*spamProb+spam*hamProb))

if spam_sum > ham_sum:
	print '%s\t%s' % ("Email Type", "Spam email")
else:
	print '%s\t%s' % ("Email Type", "Ham email")
