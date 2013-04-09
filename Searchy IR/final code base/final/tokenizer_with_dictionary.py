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


stopwords = ['am', 'ii', 'iii', 'per', 'po', 're', 'a', 'about', 'above', 'across', 'after', 'afterwards',
             'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always',
             'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anyhow', 'anyone',
             'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at', 'back', 'be', 'became', 'because',
             'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside',
             'besides', 'between', 'beyond', 'bill', 'both', 'bottom', 'but', 'by', 'can', 'cannot', 'cant', 'con',
             'could', 'couldnt', 'cry', 'describe', 'detail', 'do', 'done', 'down', 'due', 'during', 'each', 'eg',
             'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 'even', 'ever', 'every', 'everyone',
             'everything', 'everywhere', 'except', 'few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first', 'five',
             'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give',
             'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon',
             'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed',
             'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'made',
             'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much',
             'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody',
             'none',             'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once',
             'one', 'only', 'onto', 'or','other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own',
             'per', 'perhaps', 'please', 'pre','put', 'rather', 're', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems',
             'serious', 'several', 'she', 'should','show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 'somehow',
             'someone', 'something', 'sometime','sometimes', 'somewhere', 'still', 'such', 'take', 'ten', 'than', 'that', 'the',
             'their', 'them', 'themselves','then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon',
             'these', 'they', 'thick', 'thin', 'third', 'this', 'those', 'though', 'three', 'through', 'throughout',
             'thru', 'thus', 'to', 'together', 'too', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under',
             'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what', 'whatever', 'when', 'whence',
             'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether',
             'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within',
             'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves', 'able', 'dear', 'did', 'does',
             'got', 'just', 'let', 'like', 'likely', 'said', 'say', 'says', 'tis', 'twas', 'wants']



def makehash(keyword,url) :
    if keyword in d :
        d[keyword].append(url)
    else :
        d[keyword] = url


url = crawleda[50]
d = {}

if url in crawleda :
    words = []
    content = get_page(url)
    processed = stripHTMLTags(content)
    print 'len processed = '
    print len(processed)
    w = processed.split()
    for kw in w :
        if kw not in stopwords:
            unionb(words,kw)
    for kw in words :
        makehash(kw,url)
    print 'len words = '
    print len(words)
    #print words[34]

fileb = open("C:/python27/words.txt", "a",0)
try :
        for kb in words :
                if kb not in wordsa :
                        fileb.write(kb)
                        fileb.write('\n')
except :
        print 'exception'

print 'length of d ='
print len(d)

filec = open("C:/python27/keys.txt", "a",0)
try :
        for entry in d.keys() :
            filec.write(entry)
            filec.write(' , ')
            filec.write(d[entry])
            filec.write('\n')
except :
        print 'exception'


