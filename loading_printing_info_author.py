
from cgitb import text
from certifi import contents
import pywikibot
import re
import pywikibot
import regex as re




ptwiki = pywikibot.Site('wikidata:wikidata', user='Varsha ahirwar from India')
ptwiki_repo = ptwiki.data_repository()

def name(author, pid):
    return author.claims[pid][0].getTarget().labels['en']

def label_of_property(pid):
    property_page = pywikibot.PropertyPage(ptwiki_repo, pid)
    return property_page.labels['en']

def printwikidata(wd_item):
    item_dict = wd_item.get()
    try:
        print('Name: ' + item_dict['labels']['en'])
    except:
        print('No English label!')

    try:
        for claim in item_dict['claims']['P50']:
            name_value = claim.getTarget()
            name_page_info = name_value.get()
            qid=name_value.title()
            print('author:'+ name_page_info['labels']['en'])
            author = pywikibot.ItemPage(ptwiki_repo, qid)
            if author.get():
                
                try:
                    print(f"{label_of_property('P735')}: {name(author, 'P735')}")
                except:
                    print("given name is not present ")
                try:
                    print(f"{label_of_property('P734')}: {name(author, 'P734')}")
                except:
                    print("family name is not present")
    except:
        print("That didn't work!")
    try:
        for claim in item_dict['claims']['P2093']:
            author_string_value = claim.getTarget()
            print(f"{label_of_property('P2093')}: {author_string_value}")
    except:
        print("That didn't work!")
    return 0


page = pywikibot.ItemPage(ptwiki_repo,'Q60101261')
test = printwikidata(page)