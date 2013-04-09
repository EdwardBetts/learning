#take all links in a list
#links = get_all_links(get_page('http://www.udacity.com/cs101x/index.html')

def get_next_target(page):  
  start_link =page.find('<a href=')
  if start_link == -1:                     #didn't find link
    return None,0
  start_quote = page.find('"', start_link)  
  end_quote= page.find('"' , start_quote+1) #last quote
  url = page [start_quote+1: end_quote] 
  return url,end_quote

 
def get_all_the_links(page) :
	links = []
	while True :
		url,endpos = get_next_target(page)
		if url :
			links.append(url)
			page = page[endpos: ]
		else :
			break
	return links
 
print get_all_the_links('this is a <a href="http:udacity.com">link!</a> is <a href="test2">link2</a>')   #test string
 
 
#variable -tocrawl(pges left to be crawl)
#variable -crawled(stores list of already crawled pages)