def get_page(url):
	import urllib
	x=urllib.urlopen(url)
	#x=open(url,'r')
	page=x.read()
	return get_all_links(page)





def union(n,t) :                                          #union of two list in one list 
  a=p+q
  return a                                               #answer-[9,8,9,6,0]


#print links

def get_next_target(page):  
  start_link =page.find('<a href=')
  if start_link == -1:                     #didn't find link
    return None,0
  start_quote = page.find('"', start_link)  
  end_quote= page.find('"' ,start_quote+1) #last quote
  url = page [start_quote+1: end_quote] 
  return url,end_quote


def get_all_links(page) :
	links = []
	while True :
		url,endpos = get_next_target(page)
		if url :
			print url
			page = page[endpos: ]
		else :
			break
	return links                   
 
 

 
#crawling
#variable -tocrawl(pges left to be crawl)
#variable -crawled(stores list of already crawled
def crawl(seed):   #seed page from where crawling begins pg24
	tocrawl=[seed]
	crawled=[]
	while tocrawl:
		page = tocrawl.pop()   #to remove a pg from seed
		if page is not crawled :
			union(tocrawl,get_all_links(get_page(page)))   #pg 35
		crawled.append(page)
	return crawled


print crawl(get_all_links('this is a <a href="http:udacity.com">link!</a> is <a href="test2">link2</a> is <a href="test3">link3</a>'))