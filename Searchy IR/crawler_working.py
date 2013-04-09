
#extract html content for given url
def get_page(url) :
        import urllib2
        try :
                x =  urllib2.urlopen(url)
                page = x.read()
                #print page[0:50]
                return get_all_links(page)
        except :
                return get_all_links('')
	

	
#extract all hyperlinks from the extracted html content
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
        
	

#union of two lists, i.e., two arguments, both lists 
def union(p,q) :
        for e in q :
                if e not in p :
                        p.append(e)



#union of a list and a string, i.e., two argumetns, one list and one string
def unionb(p,q) :
        flag = 0
        for e in p :
                if e == q :
                        flag =1
        if flag == 0 :
                p.append(q)
                        


outfilea = open("C:/python27/crawled.txt", "a+",0)
crawled = []

#merge existing crawled links from txt file to the list
da = outfilea.read()
print da
endb = 0
while (True) :
        starta = da.find('http',endb)
        print starta
        if(starta!=-1) :
                endb = da.find('\n',starta+1)
                print endb
                k = da[starta:endb]
                unionb(crawled,k)

        else :
                break
print crawled
#print 'out'



#crawl the seed list			
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

        #write new links from the list to the txt file 
        try :
                
                j = outfilea.read()
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


        #write to txt file for seed list
        outfileb = open("C:/python27/tocrawl.txt", "a+",0)			
        print >>outfileb,tocrawl
        print len(tocrawl)
        outfileb.close()
        
        #print tocrawl
        
	
#seed = 'http://dj496.wordpress.com/'
seed = 'http://mit.edu/site/?ref=mithomepage'
#seed = 'http://en.wikipedia.org/wiki/Disha'
#seed = ["http://xkcd.com/","udacity.com","http://bbc.co.uk"]
#for k in seed :
        #web_crawl(k,5)
web_crawl(seed,5)
