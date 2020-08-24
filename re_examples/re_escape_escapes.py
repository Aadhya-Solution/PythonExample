from re_test_patterns import test_patterns

test_patterns(r'\d+ \D+ \s+ \S+ \w+ \W+',
              [ r'\\d\+',
                r'\\D\+',
                r'\\s\+',
                r'\\S\+',
                r'\\w\+',
                r'\\W\+',
                ])

'''
$ python re_escape_escapes.py


          1111111111222
01234567890123456789012
\d+ \D+ \s+ \S+ \w+ \W+

Matching "\\d\+"
   0 :  2 = "\d+"

Matching "\\D\+"
   4 :  6 = "\D+"

Matching "\\s\+"
   8 : 10 = "\s+"

Matching "\\S\+"
  12 : 14 = "\S+"

Matching "\\w\+"
  16 : 18 = "\w+"

Matching "\\W\+"
  20 : 22 = "\W+"
'''