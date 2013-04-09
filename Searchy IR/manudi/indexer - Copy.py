seed = 'http://mit.edu/site/?ref=mithomepage'
#url='http://mit.edu/site/?ref=mithomepage'
import urllib2

html=unicode(urllib2.urlopen(seed).read(), 'utf8')

def get_page(url) :
	import urllib2
	page=  unicode(urllib2.urlopen(url).read(),'utf8')
	#page = x.read()
	print "get page"
	return page
	#return get_all_links(page)
	

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
	print "get all links"
	return links
	


def crawl_web(seed):
                tocrawl = [seed]
                crawled = []
                index = {}              
                while tocrawl:
                        page = tocrawl.pop()
                        if page not in crawled:
                                
                                content = get_page(page)
                                if page[:4]=='http':
                                        u=page
                                
                                filter_all(u,page)
                                html=unicode(urllib2.urlopen(seed).read(), 'utf8')
                                #r=stripHTMLTags(html)
                                k =stripHTMLTags (html)
                                key= k.split()
                                add_page_to_index(index, page, content,key)
                                union(tocrawl, get_all_links(content))
                                crawled.append(page)
                print "crawl web"    
                return index



def add_page_to_index(index, url, content,key):
        words = content.split()
        for word in words:
                if key==url:
                        add_to_index(index, word, url)
        print "add page to index"    


def add_to_index(index, keyword, url):
        if keyword in index:
                index[keyword].append(url) 
        else:
# not found, add new keyword to index
                index[keyword] = [url]
        print"add to index"

def stripHTMLTags (html):
  """
    Strip HTML tags from any string and transfrom special entities
  """
  import re
  text = html
 
  # apply rules in given order!
  rules = [
    { r'>\s+' : u'>'},                  # remove spaces after a tag opens or closes
    { r'\s+' : u' '},                   # replace consecutive spaces
    { r'\s*<br\s*/?>\s*' : u'\n'},      # newline after a <br>
    { r'</(div)\s*>\s*' : u'\n'},       # newline after </p> and </div> and <h1/>...
    { r'</(p|h\d)\s*>\s*' : u'\n\n'},   # newline after </p> and </div> and <h1/>...
    { r'<head>.*<\s*(/head|body)[^>]*>' : u'' },     # remove <head> to </head>
    { r'<a\s+href="([^"]+)"[^>]*>.*</a>' : r'\1' },  # show links instead of texts
    { r'[ \t]*<[^<]*?/?>' : u'' },            # remove remaining tags
    { r'^\s+' : u'' }                   # remove spaces at the beginning
  ]
 
  for rule in rules:
    for (k,v) in rule.items():
      regex = re.compile (k)
      text  = regex.sub (v, text)
 
  # replace special strings
  special = {
    '&nbsp;' : ' ', '&amp;' : '&', '&quot;' : '"',
    '&lt;'   : '<', '&gt;'  : '>'
  }
 
  for (k,v) in special.items():
    text = text.replace (k, v)
      
 
  return text
            



    
def union(a,b):
        for e in b:
                if e not in a:
                        a.append(e)
        print "union"   


#def filter_all(page):
#       list=[".html"]
#        for words in list:
#                if words[-5:]=='.html':
#                        content=get_page(page)
#        print "filtered"

def filter_all(u,page):
       # for words in list:
        import urlparse
       
       
        if page[:4]!='http':
                        urlparse.urljoin(u,page)
        print "filtered"
        
                

crawl_web(seed)
