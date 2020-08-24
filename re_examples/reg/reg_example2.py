import re

pattern = 'this'
text = 'Does this text match the this pattern?'

ma = re.search(pattern, text)

s = ma.start()
e = ma.end()

print "Found %s in %s from %d to %d (%s)" % \
    (ma.re.pattern, ma.string, s, e, text[s:e])
