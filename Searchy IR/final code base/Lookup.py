#!C:/Python27/python.exe -u

print "content-type: text/html\n"



import cgi
import cgitb; cgitb.enable()
import pickle

form=cgi.FieldStorage()

infile = open('c:/python27/index.pkl','r')
index = {}
index = pickle.load(infile)


out = []



def lookup(index,keyword) :
  result = []
  if keyword in index.keys() :
    result = index[keyword]
    
  return result


outfile = open('c:/xampp/htdocs/a.html',"w")

def writefile(out)  :
  if out == None :
    outfile.write('No Results')
    return
  for item in out :
    outfile.write('<a href ="' + item + '">'+item+'</a>')
    #outfile.write('<a href ="' + item + '" </a>')
    outfile.write('<br>')
    
  outfile.close()
  


 
print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=http://localhost/a.html">'
#searchterm = 'twitter'
searchterm = form['box'].value
out = lookup(index,searchterm)
writefile(out)
