import itertools

def next_morris(number):
    return ''.join('%s%s' % (len(list(group)), digit)
        for digit, group in itertools.groupby(str(number)))

def morris_generator(numResults, start=1):
    num = start
    for i in range(0,numResults):
        yield int(num)
        num = int(next_morris(num))
        
#generate the first 31 numbers in the morris sequence
#since arrays start indexing at 0
#print the length of each one to avoid giant output
#the last number is the answer
for i in morris_generator(31):  
    print len(str(i))
    
#fun trick: python pythonChallenge10.py | nl to see "index   length" in terminal
#next clue: 5808
    
