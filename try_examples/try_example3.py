
str1="Shiva"

try:
	print "==>"
	str2=str1+ 2
	print "===",str2
except (TypeError):
	print "Yes erro is comming"
	str2=str1+str(2)
finally:
	print "Name u added :",str2

	