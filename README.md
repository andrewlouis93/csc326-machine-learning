# csc326-machine-learning
# Group 29

# Introduction
Contined is a crawler (crawler.py) which can recursively scrape webpages listed in the (urls.txt) file.
Accompanying this crawler is a frontend interface presented in HTML which can be accessed by running the 
server (server.py) and connecting on localhost at port number 3000. There is a word index and document index
stored in a database.db file using sqlite. Currently this database is not used other than for testing purposes.

#Info on Frontend
- Run `python server.py` in the root directory, and navigate your
web-browser to `localhost:3000` to run the Kanye West powered word counter.
- To update SASS: run this from the `static/scss/` directory to ensure generate and updated style.css: `python -mscss _bootstrap.scss > style.css`

#Main storage of data
Documents = urls 
doc_id = unique integer which represents one Document

Words = string of characters (or numbers) found in a document(s) during the web scraping 
word_id = unique integer which represents one Word


#Main functions of crawler

-crawler class
	The main class of the crawler. Should be initialized as crawler(None, 'urls.txt'). The urls.txt file contains the urls
	that will be scraped.
	
-crawler.crawl()
	The main function of the crawler. This is the first function that should be called in order to build all the various
	caches contained the scarped data. The get_inverted_index() and get_resolved_inverted_index() do not work without calling this 
	function.

-crawler.get_inverted_index()
	Prerequesite: Must have called crawler.crawl(Depth=x) at least once in order to build the mapping_cache which 
				  contains the inverted index.

	Calling this function will return an inverted index stored as a Dict() that contains all the word_ids (keys)
	mapped to the various doc_ids returned in a set()
	
-crawler.get_resolved_inverted_index()
	Prerequesite: Must have called crawler.crawl(Depth=x) at least once in order to build the resolved_inverted_index which 
				  contains the resolved inverted index.
				  
	Calling this function will return the resolved inverted index (cached in mapping_cache) stored as a Dict() that contains all the Words (keys)
	mapped to the various Documents returned in a set() 
	

#Instructions to run
	The way to run and extract the lists from the crawler is very simple
	1)First open the python shell and run the following commands to import the crawler class
		>>>import crawler or import crawler from crawler
	2)Next assign and initialize the crawler
		>>>crawler = crawler.crawler(None,'urls.txt') 
		#note: the urls.txt can be edited by adding more urls in the format found inside (3 sample urls are provided)
	3)Next start crawling (i.e. scraping the web)
		>>>crawler.crawl(depth=1)
		#note: Depth can vary from 1 to 3 but a higher Depth will take much longer (this is a measure of how many pages the crawler will visit recursively)
	4)After the "===Crawler Run Completed===" has been printed the run is complete
	5)Now it is possible to extract further information
		-One can retrieve an inverted index of the word_ids mapping the doc_ids through the follow commands:
		>>>inverted_index=crawler.get_inverted_index()
		-Then print the inverted_index:
		>>>print inverted_index
		-One can also obtain the resolved_inverted_index through similar commands:
		>>>resolved_inverted_index = crawler.get_resolved_inverted_index()
		>>>print resolved_inverted_index

#Instructions to run test
	The current crawler comes with 3 test scripts for quick verification
	1)test_inverted_index
		This will run all the required commands to build the inverted_index and then print the results
		to run this script simply input : execfile("test_inverted_index.py") in the python shell while in the 
		/modules directory (same directory as crawler.py)
	2)test_resolved_inverted_index
		This will run all the required commands to build the resolved_inverted_index and then print the results
		to run this script simply input : execfile("test_resolved_inverted_index.py") in the python shell while in the 
		/modules directory (same directory as crawler.py)
	3)test_crawler_consistency
		This will run 2 crawlers one after the other and then compare the documents stored with the keys 'news', 'finance, and 'email'
		it will then compare how many elements match between the two sets and the length of each of the sets. If the common elements found
		between the two sets are identical to their lengths then we can observe that both sets are identical. The test can be ran with the following 
		command: execfile("test_crawler_consistency.py") in the python shell while in the /modules directory (same directory as crawler.py)
		#Note that for the first test of 'news' there is usually a 1-url discrepency as google assigns a unique id for a certain webpage connection.
		 Therefore, a 1 difference in the common elements and length is still considered a pass
		 


