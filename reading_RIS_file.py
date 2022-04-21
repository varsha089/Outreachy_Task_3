import pywikibot
import re
import pywikibot
import regex as re


with open('C:\\Users\\91835\\Downloads\\citation-253799173 (1).ris',encoding="utf8") as f:
    article = f.read()
    print(article)

p = re.compile("AU  - (.*)")
print (p.findall(article))