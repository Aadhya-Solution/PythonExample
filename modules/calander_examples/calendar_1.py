import calendar

c = calendar.TextCalendar(calendar.MONDAY)
#print ">>",dir(c)

print ">>",c.pryear(2015)
print c.prmonth(2015, 1)
#c.pryear(2015)