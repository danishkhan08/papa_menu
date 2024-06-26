#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Content-type:text/html\r\n\r\n")

import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()


instance_name = form.getvalue('instance_name')
instance_type = form.getvalue('instance_type')
instance_region = form.getvalue('instance_region')





print("<html>")
print("<head>")
print("<title>Instance Description</title>")
print("</head>")
print("<body>")
print("<h1>Instance Description</h1>")
print("<p>Instance Name: {}</p>".format(instance_name))
print("<p>Instance Type: {}</p>".format(instance_type))
print("<p>Instance Region: {}</p>".format(instance_region))
print("</body>")
print("</html>")
