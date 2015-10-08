import re, collections
def str_frequency(_string):
    wordList = re.findall ('\w+',_string.lower())
    frequency = collections.Counter(wordList).most_common()
    return frequency

if __name__ == "__main__":
    test = "this is a a a a a a a test test"
    print test
    print wordFrequency(test)
