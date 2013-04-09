import pickle

output = open('C:/python27/index.pkl', 'a')
inputf = open('C:/python27/index.pkl', 'r')

d = pickle.load(inputf)

filea = open("C:/python27/WordsWithUrls.txt",'r',0)
index = {}

def addtoindexb(keyword,url) :
    if keyword in index.keys() :
        l = index[keyword]
        if url in l :
            return
        else :
            #print url
            l.append(url)
            print 'url added'
            return
    index[keyword] = [url]
    print 'pair added'


#union of a list and a string, i.e., two argumetns, one list and one string
def unionb(p,q) :
        flag = 0
        for e in p :
                if e == q :
                        flag =1
        if flag == 0 :
                p.append(q)


# convert string to list (for urls retrieved from file)
def makelist(parturl) :
    urllist = []
    end = 0
    while (True) :
            start = parturl.find('http',end)
            #print 'start ='
            #print start
            if (start!=-1) :
                end = parturl.find('http',start+1)
                #print 'end ='
                if end == -1 :
                    end = parturl.find('\n',start)
                #print end
                url = parturl[start:end]
                #print 'url ='
                #print url
                unionb(urllist,url)
            else :
                break 
    return urllist

#read (keyword,url) pair from file
da = filea.read()
length = len(da)
print 'reading new'
endb = -1
while (True) :
        startb = endb +1
        if startb >= length :
            break
        #print startb
        kend = da.find(',',startb+1)
        poskend = kend-1
        ustart = da.find('http',kend)
        endb = da.find('\n',ustart)
        #print 'endb ='
        #print endb
        if endb != -1 :
                partkey = da[startb:poskend]
                parturl = da[ustart:endb]
                print parturl
        else :
                break
        links = makelist(parturl)
        for link in links :
            #print 'key ='
            #print partkey
            addtoindexb(partkey,link)

print 'new = '
print len(index)
#print index

print 'created ='
print len(index)

for entry in d :
    if entry in index :
        del index[entry]

print 'unique ='
print len(index)

#pickle.dump(index,open('C:/python27/index3.txt','w'))
pickle.dump(index,output)

    


    







