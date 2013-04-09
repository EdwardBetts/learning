#startlink <a href=tags < url> is known as link

#search string.find(target string)
pythogoras = 'There is geometry in the humming of the string'
print pythogoras.find('string')    #ans-40,position
print pythogoras[40:]             #ans-String
print pythogoras.find('T')     #Ans-0
print pythogoras.find('hi')    #answ=-1,not present


# to find first url in a web page
#page = content of a web
start_link =page.find('<a href=>')
start_quote = page.find('"', start_link)  
end_quote= page.find('"' ,start_quote+1) #last quote
url = page [start_quote+1: end_quote]  #string selection between start to end


