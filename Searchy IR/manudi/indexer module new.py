url='http://mit.edu/site/?ref=mithomepage'
import urllib2

#content = unicode(urllib2.urlopen(url).read(),'utf8')
index = {}

def addo(url):
    content = unicode(urllib2.urlopen(url).read(),'utf8')
 #   
    add_page_to_index(index,url,content)
    


def add_page_to_index(index,url,content) :
    
    
    words = content.split()
    for word in words :
        add_to_index(index,word,url)
    print "add page to index"


def add_to_index(index,word,url) :
    index = {}
    if word in index :
        index[word].append(url)
    else:
        index[word] = [url]
    print index
    print "add to index"



addo(url)




