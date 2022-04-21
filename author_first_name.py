import pywikibot
import re
import pywikibot
import regex as re

with open('C:\\Users\\91835\\Downloads\\citation-253799173 (1).ris',encoding="utf8") as fh:
     for line in fh:
        match = re.search(r'(.*?), \w*?', line)
        if match: 
            author_first_name = match.group(0)
            print('first name: {}'.format(author_first_name))