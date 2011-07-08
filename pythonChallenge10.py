import itertools

def next_morris(number):
    return ''.join('%s%s' % (len(list(group)), digit)
        for digit, group in itertools.groupby(str(number)))
    
print next_morris(111221)
