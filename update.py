#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import cgi, os, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    description = sanitizer.sanitize(description)
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
  <form action="process_update.py" method="post">
  <p><input type="hidden" name="pageId" value="{form_default_title}"</p>
  <p><input type="text" name="title" Placeholder="title" value="{form_default_title}"></p>
  <p><textarea row="4" name="description" Placeholder="description">{form_default_description}</textarea></p>
  <p><input type="submit"></p>
  </form>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getList(), form_default_title=pageId, form_default_description=description))
