#!C:/Python27/python.exe -u

print "content-type: text/html\n"



import cgi
import cgitb; cgitb.enable()

form=cgi.FieldStorage()



def get_page(url) :
        import urllib2
        x =  urllib2.urlopen(url)
        page = x.read()
        #print page[0:50]
        return get_all_links(page)
	

	
def get_all_links(page) :
	links = []
	end_quote = 0
	while (True) :
		link = page.find('<a href=',end_quote)
		#print "hi get all links"
		#print>>outfile,link
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
                if url[:4]=='http':
                        if url not in crawled :
                                union(tocrawl,get_page(url))
                                crawled.append(url)
                        
                        if(len(crawled)==max_pages) :
                                break
        #print "hi in web_crawl, before printing crawled"
        outfile = open("C:/xampp/htdocs/a.html", "w")
        print >>outfile,"<p> crawled"
        print >>outfile,len(crawled)
        
        #print tocrawl
print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=http://localhost/a.html">'
	
#seed = 'http://dj496.wordpress.com/'
#seed = 'http://mit.edu/site/?ref=mithomepage'
#seed = 'https://en.wikipedia.org/wiki/Disha'
#seed = ["http://xkcd.com/","www.python.org","http://bbc.co.uk","udacity.com"]
web_crawl(form['seed'].value,form['max_pages'].value)
