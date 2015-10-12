import crawler
crawler = crawler.crawler(None,'urls.txt')
crawler.crawl(depth=1)
print "====Printing inverted index===="
print crawler.get_inverted_index()
