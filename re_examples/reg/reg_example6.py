
import re

text = 'ip 10.12.23.45 up ip 12.123.13.34 down abbaaabbbbaaaaa'

pattern = '\d+.\d+.\d+.\d+'
print ">>",re.finditer(pattern, text)
for match in re.finditer(pattern, text):
    print match
    s = match.start()
    e = match.end()
    print 'Found %s==%s at %d:%d' % (match.re.pattern,text[s:e], s, e)