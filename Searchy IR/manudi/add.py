#!C:/Python27/python.exe -u

print "content-type: text/html\n"

import cgi
import cgitb; cgitb.enable()

form=cgi.FieldStorage()
outfile = open("C:/xampp/htdocs/a.html", "w")
if (form.has_key("UserName")):

	print >>outfile,"<p>Hi,", form["UserName"].value,  ". How are you?"
else:
	print >>outfile,"error"
print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=http://localhost/a.html">'
