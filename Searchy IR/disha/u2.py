# to print first url in a web page
#page ='<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="http://www.xkcd.com">'
#start_link =page.find('<a href=>')
#start_quote = page.find('"', start_link)  
#end_quote= page.find('"' ,start_quote+1) #last quote
#url = page [start_quote+1: end_quote] 
#print url

#page= page[end_quote:]         #for second url
#start_link =page.find('<a href=>')
#start_quote = page.find('"', start_link)  
#end_quote= page.find('"' ,start_quote+1) #last quote
#url = page [start_quote+1: end_quote] 
#print url


#procedure to find first link
def get_next_target(page):  
  start_link =page.find('<a href=')
  start_quote = page.find('"', start_link)  
  end_quote= page.find('"' ,start_quote+1) #last quote
  url = page [start_quote+1: end_quote] 
  return url,end_quote
print get_next_target('this is a <a href="http:udacity.com">link!</a>')  # answer- ('http:udacity.com',35)
url,endpos = get_next_target('this is a <a href="http:udacity.com">link!</a>')
print url    #answer-http:udacity.com


#if 
def get_next_target(page):  
  start_link =page.find('<a href=')
  if start_link == -1:  #diin't find link
    return None,0
  start_quote = page.find('"', start_link)  
  end_quote= page.find('"' ,start_quote+1) #last quote
  url = page [start_quote+1: end_quote] 
  return url,end_quote
url,endpos = get_next_target('no good') 
if url:
 print "here"    #answer-not here
else:
  print "not here"


  

def get_next_target(page):  
  start_link =page.find('<a href=')
  if start_link == -1:                     #didn't find link
    return None,0
  start_quote = page.find('"', start_link)  
  end_quote= page.find('"' ,start_quote+1) #last quote
  url = page [start_quote+1: end_quote] 
  return url,end_quote

def print_all_links(page) :
	while True :
		url,endpos = get_next_target(page)
		if url :
			print url
			page = page[endpos: ]
		else :
			break
print_all_links('this is a <a href="http:udacity.com">link!</a> is <a href="test2">link2</a> is <a href="test3">link3</a>')   #test string
 
 
 
 
 
 
 
 
 
 


