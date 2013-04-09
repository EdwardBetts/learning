def get_page(url) :
	import urllib
	x =  urllib.urlopen(url)
	page = x.read()
	#print page[0:50]
	return get_all_links(page)
	

	
def get_all_links(page) :
	links = []
	end_quote = 0
	while (True) :
		link = page.find('<a href=',end_quote)
		#print "hi get all links"
		#print  link
		if(link!=-1) :
			start_quote = page.find('"', link)
			#print start_quote
			end_quote = page.find('"', start_quote+1)
			#print end_quote
			url = page[start_quote+1:end_quote]
			#print url
			links.append(url)
		else :
			break
	print links
	return links
	
	
	
def union(p,q) :
	for e in q :
		if e not in p :
			p.append(e)

			
			
def web_crawl(seed,max_pages) :
	crawled = []
	tocrawl = get_page(seed)
	while tocrawl :
		url = tocrawl.pop()
		if url not in crawled :
			union(tocrawl,get_page(url))
			crawled.append(url)
			
			if(len(crawled)==max_pages) :
				break
	#print "hi in web_crawl, before printing crawled"
	print crawled
	
#seed = 'http://dj496.wordpress.com/'
seed = 'http://www.garfield.com/sitemap.html'
#seed = ["http://xkcd.com/","www.python.org","http://bbc.co.uk","udacity.com"]
web_crawl(seed,5)
