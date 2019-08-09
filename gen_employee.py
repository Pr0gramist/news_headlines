'''
    Python Script to generate 10,000 unique employees
        Data stored in employee.txt

        By: Stivan Kitchoukov
'''
import os
import names
import random

#Arrays to be used for random generation
location = ["United States", "United Kingdom", "Canada", "Germany", "Spain", "Bulgaria", "Greece", "China", "Japan", "Brazil", "Russia", "Italy"]
job_role = ["HR", "Recruiter", "Software Engineer", "QA", "Secretary", "Manager", "Support", "Cleaner", "Security"]
department = ["Marketing", "Sales", "IT", "Accounting", "Manufacturing", "Executive", "Shipping"]

#Creating file employee.txt
file = open("employee.txt", "w")
file.write('{"employees":[\n')
print("Generating 10,000 random employees - Please Wait...")

#Loop to create 10,0000 unique employees
for i in range(10000):
    file.write('    {\n')
    file.write('        "ID":"' + str(1000 + i) + '",\n')
    file.write('        "name":"' + names.get_full_name() + '",\n')
    
    rand = random.randint(0,len(location) - 1)
    file.write('        "location":"' + location[rand] + '",\n')
    
    rand = random.randint(0, len(job_role) - 1)
    file.write('        "job role":"' + job_role[rand] + '",\n')
    
    rand = random.randint(0, len(department) - 1)
    file.write('        "department":"' + department[rand] + '"\n')

    if i == 9999:
        file.write('    }\n')
    else:
        file.write('    },\n')

file.write(']}')
file.close()
print("Finished generating 'employee.txt' file.")