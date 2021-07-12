#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import cgi, os, view
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
  {listStr}
  </ol>
  <a href="create.py">create</a>
  <form action="process_create.py" method="post">
  <p><input type="text" name="title" Placeholder="title"></p>
  <p><textarea row="4" name="description" Placeholder="description"></textarea></p>
  <p><input type="submit"></p>
  </form>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getList()))
