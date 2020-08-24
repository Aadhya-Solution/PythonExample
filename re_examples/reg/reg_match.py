import re

patterns = [ 'this', 'Does' ]
text = 'Does this text match the pattern?'

for pattern in patterns:
    print 'Looking for "%s" in "%s" ->' % (pattern, text)

    if re.match(pattern,  text):
        print 'found a match!'
    else:
        print 'no match'