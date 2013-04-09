filea = open("C:/python27/WordsWithUrls.txt",'r',0)


index = {}
def addtoindex(keyword,url) :
    for e in index :
        if e[0] == keyword :
            for u in e[1] :
                if u == url :
                    return
            print url
            index[keyword].append(url)
            return
    index[keyword] = url


def addtoindexb(keyword,url) :
    if keyword in index.keys() :
        l = index[keyword]
        if url in l :
            return
        else :
            print url
            index[keyword].append(url)
            print 'url added'
            return
    index[keyword] = url
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
            print 'start ='
            print start
            if (start!=-1) :
                end = parturl.find('http',start+1)
                print 'end ='
                if end == -1 :
                    end = parturl.find('\n',start)
                print end
                url = parturl[start:end]
                print 'url ='
                print url
                unionb(urllist,url)
            else :
                break 
    return urllist

#read (keyword,url) pair from file
da = filea.read()
length = len(da)
endb = -1
while (True) :
        startb = endb +1
        if startb >= length :
            break
        print startb
        kend = da.find(',',startb+1)
        poskend = kend-1
        ustart = da.find('http',kend)
        endb = da.find('\n',ustart)
        print 'endb ='
        print endb
        if endb != -1 :
                partkey = da[startb:poskend]
                parturl = da[ustart:endb]
                print parturl
        else :
                break
        links = makelist(parturl)
        for link in links :
            print 'key ='
            print partkey
            addtoindexb(partkey,link)


print len(index)
#print index
