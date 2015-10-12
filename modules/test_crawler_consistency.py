'''Tests the consistency of resolved inverted index created by comparing the
    resolved inverted indexes from two different crawl() runs close together'''
import crawler
print "====Running first crawl===="
crawler_t = crawler.crawler(None,'urls.txt')
crawler_t.crawl(depth=1)
word_id_cache_first_run = crawler_t.get_word_id_cache()
resolved_inverted_index_first_run = crawler_t.get_resolved_inverted_index()
print "====Running second crawl===="
crawler2 = crawler.crawler(None,'urls.txt')
crawler2.crawl(depth=1)
word_id_cache_second_run = crawler2.get_word_id_cache()
resolved_inverted_index_second_run = crawler2.get_resolved_inverted_index()
print "====Starting comparisons===="
print "\n\n\n"
print "====Comparing documents listed with word 'news' ==== "
print "First run:", sorted(resolved_inverted_index_first_run["news"])
print "-----------------------------"
print "Second run:", sorted(resolved_inverted_index_second_run["news"])
print "\n number of common elements found in second and first run:", len(resolved_inverted_index_first_run["news"].intersection(resolved_inverted_index_second_run["news"]))
print "\n Length of first set()=", len(resolved_inverted_index_first_run["news"])
print "\n Length of second set()=", len(resolved_inverted_index_second_run["news"])
print "\n\n\n"
print "====Comparing documents listed with word 'finance' ==== "
print "First run:", sorted(resolved_inverted_index_first_run["finance"])
print "-----------------------------"
print "Second run:", sorted(resolved_inverted_index_second_run["finance"])
print "\n number of common elements found in second and first run:", len(resolved_inverted_index_first_run["finance"].intersection(resolved_inverted_index_second_run["finance"]))
print "\n Length of first set()=", len(resolved_inverted_index_first_run["finance"])
print "\n Length of second set()=", len(resolved_inverted_index_second_run["finance"])
print "\n\n\n"
print "====Comparing documents listed with word 'email' ==== "
print "First run:", sorted(resolved_inverted_index_first_run["email"])
print "-----------------------------"
print "Second run:", sorted(resolved_inverted_index_second_run["email"])
print "\n number of common elements found in second and first run:", len(resolved_inverted_index_first_run["email"].intersection(resolved_inverted_index_second_run["email"]))
print "\n Length of first set()=", len(resolved_inverted_index_first_run["email"])
print "\n Length of second set()=", len(resolved_inverted_index_second_run["email"])
print "\n====END OF TEST===="


