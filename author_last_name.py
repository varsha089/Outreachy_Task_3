import urllib.request
import pywikibot
import re
import pywikibot


with open('C:\\Users\\91835\\Downloads\\citation-253799173 (1).ris',encoding="utf8") as f:
    article = f.read()

p = re.compile("AU  - (.*)")
print (p.findall(article))

 
with open('C:\\Users\\91835\\Downloads\\citation-253799173 (1).ris',encoding="utf8") as fh:
     for line in fh:
        match = re.search(r', (\S+)', line)
        if match: 
            author_last_name = match.group(0)
            print('last name: {}'.format(author_last_name))
