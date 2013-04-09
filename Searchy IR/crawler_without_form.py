def get_page(url) :
        import urllib2
        try :
                x =  urllib2.urlopen(url)
                page = x.read()
                #print page[0:50]
                return get_all_links(page)
        except :
                return get_all_links('')
	

	
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
        
        return links
        
	
	
def union(p,q) :
        for e in q :
                if e not in p :
                        p.append(e)
                

outfilea = open("C:/python27/crawled.txt", "a+")
outfileb = open("C:/python27/tocrawl.txt", "a+")			
			
def web_crawl(seed,max_pages) :
        crawled = []
        tocrawl = [seed]
        while tocrawl :
                url = tocrawl.pop()
                if url[:4]=='http':
                        if url not in crawled :
                                union(tocrawl,get_page(url))
                                crawled.append(url)
                        
                        if(len(crawled)==max_pages) :
                                break

        #print "hi in web_crawl, before printing crawled"
        
        #print >>outfilea,crawled
        try :
                j = outfilea.read()
                print "j =" + j[:50]
                for k in crawled :
                        
                        m = j.find(k)
                        print m
                        if m == -1 :
                                outfilea.write(k)
                                print k
                                outfilea.write('\n')
                print crawled
        except :
                print 'no new links'
        
        
        print >>outfileb,tocrawl
        print len(tocrawl)
        
        #print tocrawl
        
	
#seed = 'http://dj496.wordpress.com/'
#seed = 'http://mit.edu/site/?ref=mithomepage'
#seed = 'http://en.wikipedia.org/wiki/Disha'
seed = ["http://xkcd.com/","www.python.org","udacity.com","http://bbc.co.uk"]
for k in seed :
        web_crawl(k,5)
#web_crawl(seed,5)
