import crawler
crawler = crawler.crawler(None,'urls.txt')
crawler.crawl(depth=1)
print "====Printing resolved inverted index===="
print crawler.get_resolved_inverted_index()
