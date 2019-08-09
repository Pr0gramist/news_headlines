'''
    Python Script to generate 3,000 unique news headlines
        Data stored in headlines.txt

        By: Stivan Kitchoukov
'''

import os
import names
import random
import re
from datetime import date
from essential_generators import DocumentGenerator

gen = DocumentGenerator()

language = ["English", "German", "Spanish", "Bulgarian", "Greek", "Chinese", "Japanese", "Brazilian", "Russian", "Italian"]
keyword = ["HR", "Recruiter", "Software Engineer", "QA", "Secretary", "Manager", "Support", "Cleaner", "Security", "Marketing", "Sales", "IT", "Accounting", "Manufacturing", "Executive", "Shipping"]

start_d = date.today().replace(day=1, month=7).toordinal()
end_d = date.today().toordinal()

#Creating file headlines.txt
file = open("headlines.txt", "w")
file.write('{"headlines":[\n')

print("Generating 3,000 random news headlines - Please Wait...")

#Loop to create 3,000 unique News Headlines
for i in range(3000):
    file.write('    {\n')
    
    #Title
    title = gen.sentence()
    title = re.sub('\s', ' ',title)
    title = title.replace('"', '`')
    title = title.replace("\\", "/")
    file.write('        "title":"' + title + '",\n')
    
    #Abstract
    abstract = gen.sentence()
    abstract = re.sub('\s', ' ',abstract)
    abstract = abstract.replace('"', '`')
    abstract = abstract.replace("\\", "/")
    file.write('        "abstract":"' + abstract + '",\n')
    
    #Language
    rand = random.randint(0,len(language) - 1)
    file.write('        "language":"' + language[rand] + '",\n')
    
    #Publication Date
    random_d = date.fromordinal(random.randint(start_d,end_d))
    file.write('        "publication date":"' + str(random_d) + '",\n')
    
    #Author
    file.write('        "author":"' + names.get_full_name() + '",\n')
    
    #Keyword
    rand = random.randint(0, len(keyword) - 1)
    file.write('        "keyword":"' + keyword[rand] + '"\n')

    if i == 2999:
        file.write('    }\n')
    else:
        file.write('    },\n')

file.write(']}')
file.close()
print("Finished Generating 'headlines.txt' file.")