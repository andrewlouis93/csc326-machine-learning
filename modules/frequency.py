import re, collections, operator

def str_frequency(_string):
    wordList = re.findall ('\w+',_string.lower())
    frequency = collections.Counter(wordList).most_common()
    return frequency

def cache_update(_string, _cache):
    wordList = re.findall ('\w+',_string.lower())
    for word in wordList:
        if word in _cache:
            _cache[word] += 1
        else:
            _cache[word] = 1
    return _cache

def top_twenty(_cache):
    return sorted(_cache.iteritems(), key=operator.itemgetter(1), reverse=True)[:20]

if __name__ == "__main__":
    test = "this is a a a a a a a test test"
    print test
    print wordFrequency(test)
