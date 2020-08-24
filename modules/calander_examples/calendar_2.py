import calendar

print calendar.TextCalendar(calendar.MONDAY).formatyear(2015, 1, 1, 1, 3)

'''
$ python calendar_formatyear.py

                   2007

      January               February
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6               1  2  3
 7  8  9 10 11 12 13   4  5  6  7  8  9 10
14 15 16 17 18 19 20  11 12 13 14 15 16 17
21 22 23 24 25 26 27  18 19 20 21 22 23 24
28 29 30 31           25 26 27 28

       March                 April
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
             1  2  3   1  2  3  4  5  6  7
 4  5  6  7  8  9 10   8  9 10 11 12 13 14
11 12 13 14 15 16 17  15 16 17 18 19 20 21
18 19 20 21 22 23 24  22 23 24 25 26 27 28
25 26 27 28 29 30 31  29 30

        May                   June
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
       1  2  3  4  5                  1  2
 6  7  8  9 10 11 12   3  4  5  6  7  8  9
13 14 15 16 17 18 19  10 11 12 13 14 15 16
20 21 22 23 24 25 26  17 18 19 20 21 22 23
27 28 29 30 31        24 25 26 27 28 29 30

        July                 August
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7            1  2  3  4
 8  9 10 11 12 13 14   5  6  7  8  9 10 11
15 16 17 18 19 20 21  12 13 14 15 16 17 18
22 23 24 25 26 27 28  19 20 21 22 23 24 25
29 30 31              26 27 28 29 30 31

     September              October
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
                   1      1  2  3  4  5  6
 2  3  4  5  6  7  8   7  8  9 10 11 12 13
 9 10 11 12 13 14 15  14 15 16 17 18 19 20
16 17 18 19 20 21 22  21 22 23 24 25 26 27
23 24 25 26 27 28 29  28 29 30 31
30
'''