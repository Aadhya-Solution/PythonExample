from re_test_patterns import test_patterns

test_patterns('abbaaabbbbaaaaa',
              [ 'ab*',     # a followed by zero or more b
                'ab+',     # a followed by one or more b
                'ab?',     # a followed by zero or one b
                'ab{3}',   # a followed by three b
                'ab{2,3}', # a followed by two to three b
                ])

				

'''
$ python re_repetition.py


          11111
012345678901234
abbaaabbbbaaaaa

Matching "ab*"
   0 :  2 = "abb"
   3 :  3 = "a"
   4 :  4 = "a"
   5 :  9 = "abbbb"
  10 : 10 = "a"
  11 : 11 = "a"
  12 : 12 = "a"
  13 : 13 = "a"
  14 : 14 = "a"

Matching "ab+"
   0 :  2 = "abb"
   5 :  9 = "abbbb"

Matching "ab?"
   0 :  1 = "ab"
   3 :  3 = "a"
   4 :  4 = "a"
   5 :  6 = "ab"
  10 : 10 = "a"
  11 : 11 = "a"
  12 : 12 = "a"
  13 : 13 = "a"
  14 : 14 = "a"

Matching "ab{3}"
   5 :  8 = "abbb"

Matching "ab{2,3}"
   0 :  2 = "abb"
   5 :  8 = "abbb"
   '''
   