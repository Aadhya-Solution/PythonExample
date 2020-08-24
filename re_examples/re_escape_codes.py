from re_test_patterns import test_patterns

test_patterns('This is a prime #1 example!',
              [ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ])

				
'''
$ python re_escape_codes.py


          11111111112222222
012345678901234567890123456
This is a prime #1 example!

Matching "\d+"
  17 : 17 = "1"

Matching "\D+"
   0 : 16 = "This is a prime #"
  18 : 26 = " example!"

Matching "\s+"
   4 :  4 = " "
   7 :  7 = " "
   9 :  9 = " "
  15 : 15 = " "
  18 : 18 = " "

Matching "\S+"
   0 :  3 = "This"
   5 :  6 = "is"
   8 :  8 = "a"
  10 : 14 = "prime"
  16 : 17 = "#1"
  19 : 26 = "example!"

Matching "\w+"
   0 :  3 = "This"
   5 :  6 = "is"
   8 :  8 = "a"
  10 : 14 = "prime"
  17 : 17 = "1"
  19 : 25 = "example"

Matching "\W+"
   4 :  4 = " "
   7 :  7 = " "
   9 :  9 = " "
  15 : 16 = " #"
  18 : 18 = " "
  26 : 26 = "!"
'''
