from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
import urllib

url = 'http://en.wikipedia.org/wiki/Disha'
x =  urllib.urlopen(url)
content = x.read()

class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text


def main():
    text =content
    print(dehtml(text))


if __name__ == '__main__':
    main()



#tokenizer n nesting of list




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


