import re

def test_patterns(text, patterns=[]):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Show the character positions and input text
    print "===>",text

    # Look for each pattern in the text and print the results
    for pattern in patterns:
        print
        print 'Matching "%s"' % pattern
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            print '  %2d : %2d = "%s"' % \
                (s, e-1, text[s:e])
    return
print "======>",__name__
if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa', ['ab'])
	
	
'''
output:
$ python re_test_patterns.py


          11111
012345678901234
abbaaabbbbaaaaa

Matching "ab"
   0 :  1 = "ab"
   5 :  6 = "ab"
   
'''