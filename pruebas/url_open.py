import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
   print(html[:1000].decode('utf-8')+' ...')
   print("\nURL:", response.geturl())
   print("\ninfo:",response.info())
