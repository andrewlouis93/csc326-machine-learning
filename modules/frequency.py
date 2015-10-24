"""
frequency.py
- Holds helper functions relevant to CSC326 Lab #1
"""
import re, collections, operator

# Returns a tuple list that contains
# the most common words in an input string and their
# corresponding counts
def str_frequency(_string):
    wordList = re.findall ('\w+',_string.lower())
    frequency = collections.Counter(wordList).most_common()
    return frequency

# Updates a cache dictionary
# to account for words in a query string.
# Maintains their counts

# TODO: Use str_frequency(_string) results
# to update the cache instead of recomputing.
def cache_update(_string, _cache):
    wordList = re.findall ('\w+',_string.lower())
    for word in wordList:
        _cache[word] = (_cache[word]+1) if (word in _cache) else 1
    return _cache

# Keeps a list of users and their last 10 recently searched words.
def users_cache_update(_string, _cache, _email):
    # Initialize if user dne in hash yet
    if (_email not in _cache):
        _cache[_email] = []

    wordList = re.findall('\w+',_string.lower())

    # maintain a list, but preserve order
    seen = set()
    seen_add = seen.add
    wordList = [ x for x in wordList if not (x in seen or seen_add(x))]

    # push word to stack
    push = lambda email, word: (_cache[email].insert(0,word))
    # if word exists in last 10 recently searched words
    # pluck it, and reposition at the beginning of the stack
    pushHead = lambda email, word: (_cache[email].remove(word), push(email, word))
    # push or pushHead to stack after checking if it already exists.
    for word in wordList:
        if (word in _cache[_email]):
            _cache[_email].remove(word)
            _cache[_email].insert(0,word)
        else:
            _cache[_email].insert(0,word)
    # [ pushHead(_email, word) if (word in _cache[_email]) else push(_email, word) for word in wordList ]

    # for a2: return only last 10 searches
    _cache[_email] = _cache[_email][0:10]
    return _cache

# Returns a tuple of the top 20 most relevant
# results from the cache.
def top_twenty(_cache):
    return sorted(_cache.iteritems(), key=operator.itemgetter(1), reverse=True)[:20]

if __name__ == "__main__":
    # TODO: Add tests for cache_update, top_twenty, users_cache_update here
    test = "this is a a a a a a a test test"
    print test
    print str_frequency(test)
