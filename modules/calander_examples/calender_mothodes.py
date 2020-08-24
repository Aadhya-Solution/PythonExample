1. calendar.calendar(year,w=2,l=1,c=6)

Returns a multiline string with a calendar for year year formatted into three columns separated by c spaces. w is the width in characters of each date; each line has length 21*w+18+2*c. l is the number of lines for each week.

2	calendar.firstweekday( )
Returns the current setting for the weekday that starts each week. By default, when calendar is first imported, this is 0, meaning Monday.

3	calendar.isleap(year)
Returns True if year is a leap year; otherwise, False.

4	calendar.leapdays(y1,y2)
Returns the total number of leap days in the years within range(y1,y2).