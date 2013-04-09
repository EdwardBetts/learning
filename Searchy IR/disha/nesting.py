

#tokenizer n nesting of list

url = 'http://en.wikipedia.org/wiki/Disha'


def get_page(url) :
	import urllib
	x =  urllib.urlopen(url)
	content = x.read()
	print content[0:50]
	return tokenizer(content,url)

#tokens=['udacity']
#urls=['http://udacity.com']
#index=[tokens,[urls]]

index=[]


def nesting(content,url):
    words = content.split()
    print len(words)
    for t in words:            #user keyword 
        for a in index:       # checking elelments of index  
            if a != t:        #IF TOKEN IS IN INDEX
                #for u in index[1]:  #index url
                 #   if u != url:  #checking  url,url found
                  #      index[1].append(url)# token is present ,url not ,url is added

            #else:
                index.append(t,[url])
    return index
                            
                            
print get_page(url)   

