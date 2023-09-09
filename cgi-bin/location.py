#!/usr/bin/python3

import cgi
import geocoder

print("Content-type: text/html\n\n")
print("<html>")
print("<head>")
print("<title>IP Geolocation</title>")
print("</head>")
print("<body>")

g = geocoder.ip('me')

print("<h2>IP Geolocation</h2>")
print("<p>Your IP address latitude and longitude:</p>")
print("<p>Latitude: {}</p>".format(g.latlng[0]))
print("<p>Longitude: {}</p>".format(g.latlng[1]))

print("</body>")
print("</html>")
#this program is for knowing the location
[root@ip-172-31-3-169 cgi-bin]# cat task.
cat: task.: No such file or directory
[root@ip-172-31-3-169 cgi-bin]# cat test
cat: test: No such file or directory
[root@ip-172-31-3-169 cgi-bin]# cat test.py
#!/usr/bin/python3

import subprocess
import cgi

print("content-type: text/html")
print()

form = cgi.FieldStorage();
cmd = form.getvalue("c");

if "date" in cmd:
        output = subprocess.getoutput("date");
        print(output);
elif "cal" in cmd:
        output = subprocess.getoutput("cal");
        print(output);
else:
        print("i m coming");
  
