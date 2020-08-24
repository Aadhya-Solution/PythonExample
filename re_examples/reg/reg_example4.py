import re

text = '10/02/1980  kdahfskjafd jhLFK 12/03/2016'

pat = '\d+/\d+/\d+'
print  re.findall(pat, text)
for match in re.findall(pat, text):
    print 'Found "%s"' % match