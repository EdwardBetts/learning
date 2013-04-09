#!C:/Python27/python.exe -u

print "content-type: text/html\n"



import cgi
import cgitb; cgitb.enable()

form=cgi.FieldStorage()




infile = open('c:/python27/indexer.txt','rb',0)

d = {}
def get_pair(line):
  key, sep, value = line.strip().partition(" ")
  
  #print str(key)
  #print value
  return str(key), value



def search(key1) :
    outfilea = open('c:/xampp/htdocs/a.html',"w")
    with open("c:/python27/indexer.txt") as fd:    
      d = dict(get_pair(line) for line in fd)
    with open("c:/python27/indexer.txt") as fd:
      
      for line in fd :
        key, sep, value = line.strip().partition(" ")
        print str(key)
        print value
        if key1 not in str(key) :
          print >>outfilea,'<p>none is retrieved'
          break
        else:
          
          print >>outfilea,'<p>retreived url is <a href ="' + value + '"></a>'
            
          print >>outfilea,'<p>key is <a href ="',key1,'"></a>'
          break
      
        
          
    
print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=http://localhost/a.html">'


with open("c:/python27/indexer.txt") as fd:    
      d = dict(get_pair(line) for line in fd)
    

#search('Products/en/products/online-business-optimisatio')
search(form['box'].value)
