from re_test_patterns import test_patterns

test_patterns('This is some text -- with punctuation.',
              [ '[a-z]+',      # sequences of lower case letters
                '[A-Z]+',      # sequences of upper case letters
                '[a-zA-Z]+',   # sequences of lower or upper case letters
                '[A-Z][a-z]+', # one upper case letter followed by lower case letters
                ])

				
'''
$ python re_charset_ranges.py


          1111111111222222222233333333
01234567890123456789012345678901234567
This is some text -- with punctuation.

Matching "[a-z]+"
   1 :  3 = "his"
   5 :  6 = "is"
   8 : 11 = "some"
  13 : 16 = "text"
  21 : 24 = "with"
  26 : 36 = "punctuation"

Matching "[A-Z]+"
   0 :  0 = "T"

Matching "[a-zA-Z]+"
   0 :  3 = "This"
   5 :  6 = "is"
   8 : 11 = "some"
  13 : 16 = "text"
  21 : 24 = "with"
  26 : 36 = "punctuation"

Matching "[A-Z][a-z]+"
   0 :  3 = "This"
 '''