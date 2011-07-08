import urllib2
import re

numbers = '63579'

for i in range(400):
  f = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' +numbers)
  s = f.read(6000)
  print s
  numbers = re.search(r'\d+', s).group(0)


