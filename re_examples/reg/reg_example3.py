import re
# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'this',
                                     'that'
                                     ]
          ]
text = 'Does this text match the pattern?'
print "list obj:",regexes
for regex in regexes:
	print ">>",regex
	print 'Looking for %s in %s ->' % (regex.pattern, text)
	if regex.search(text):
		print 'found a match!'
	else:
		print 'no match'