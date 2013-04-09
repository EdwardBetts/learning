def get_page(url) :
    import urllib2
    x = urllib2.urlopen(url)
    page = x.read()
    coded = unicode(page,'utf8')
    return coded




#union of a list and a string, i.e., two argumetns, one list and one string
def unionb(p,q) :
        flag = 0
        for e in p :
                if e == q :
                        flag =1
        if flag == 0 :
                p.append(q)



filea = open("C:/python27/crawled.txt", "r",0)
crawleda = []

#merge existing crawled links from txt file to the list
da = filea.read()
endb = 0
while (True) :
        starta = da.find('http',endb)
        if(starta!=-1) :
                endb = da.find('\n',starta+1)
                k = da[starta:endb]
                unionb(crawleda,k)

        else :
                break
print "length from file = "
print len(crawleda)
#print 'out'
filea.close()




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



wordsa = []    
fileb = open("C:/python27/words.txt", "r",0)
db = fileb.read()
l = len(db)
#print l
endbb = 0
while (True) :
        startaa = endbb+1
        #print startaa
        endbb = db.find('\n',startaa)
        #print endbb
        if endbb != -1 :
                kbb = db[startaa:endbb]
                unionb(wordsa,kbb)
        else :
                break
fileb.close()
print len(wordsa)


stopwords = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among', 'an', 'and',
             'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear',
             'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has', 'have',
             'he', 'her', 'hers', 'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just',
             'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor', 'not',
             'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says', 'she',
             'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they',
             'this', 'tis', 'to', 'too', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which',
             'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your']


k = crawleda[23]
words = []
if k in crawleda :
    content = get_page(k)
    processed = stripHTMLTags(content)
    print 'len processed = '
    print len(processed)
    w = processed.split()
    for k in w :
        if k not in stopwords:
            unionb(words,k)
    print 'len words = '
    print len(words)
    print words[34]

fileb = open("C:/python27/words.txt", "a",0)
try :
        for kb in words :
                if kb not in wordsa :
                        fileb.write(kb)
                        fileb.write('\n')
except :
        print 'exception'


