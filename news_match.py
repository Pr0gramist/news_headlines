'''
    API that will match news healines with employees

        Input:
            Publication Date:
        Output:
            File with sorted headlines for the date provided and employees that match each
        Takes in two files
            headlines.txt
            employee.txt
        
'''

import os
import json

#store headlines data into json
with open("headlines.txt") as headlines_file:
    headlines_data = json.load(headlines_file)

#Store employee data into json
with open("employee.txt") as employee_file:
    employee_data = json.load(employee_file)

#Function that returns language based on location
def country_language(location):
    dictionary = {
        "United States": "English",
        "United Kingdom": "English",
        "Canada": "English",
        "Germany": "German",
        "Spain": "Spanish",
        "Bulgaria": "Bulgarian",
        "Greece":"Greek",
        "China": "Chinese",
        "Japan": "Japanese",
        "Brazil": "Brazilian",
        "Russia": "Russian", 
        "Italy": "Italian"
    }
    language = dictionary[str(location)]
    return language

#Function Call that will return all headlines with list of employees based on date
def match_headline2employee(search_d):
    #Create new file to store Headline results
    result = open("result.txt", "w")

    #Loop through headlines and determine matches
    for headline in headlines_data["headlines"]:
        if headline["publication date"] == search_d:
            #print("HEADLINE:" + headline["title"])
            result.write("Headline: " + headline["title"] + "\n")

            for employee in employee_data["employees"]:
                if country_language(employee["location"]) == headline["language"]:
                    if employee["job role"] == headline["keyword"] or employee["department"] == headline["keyword"]:
                        #print("         Employee Name:" + employee["name"])
                        result.write("      Employee: " + employee["ID"] + " --- " + employee["name"] + "\n")

    result.close()
    return True

#List of departments with all headlines that match
def match_dept2headline(search_d):
    #Create new file to store department headlines
    result = open("dept_headlines.txt", "w")

    department = ["Marketing", "Sales", "IT", "Accounting", "Manufacturing", "Executive", "Shipping"]

    if search_d is None:
        for item in department:
            result.write("DEPARTMENT: " + item + "\n")
            for headline in headlines_data["headlines"]:
                if item == headline["keyword"]:
                    result.write("      Headline: " + headline["title"] + "\n")
    else:
        for item in department:
            result.write("DEPARTMENT: " + item + "\n")
            for headline in headlines_data["headlines"]:
                if search_d == headline["publication date"]:
                    if item == headline["keyword"]:
                        result.write("      Headline: " + headline["title"] + "\n")
    result.close()
    

#list of job roles with all headlines that match
def match_job2headline(search_d):
    #Create new file to store department headlines
    result = open("job_headlines.txt", "w")

    job_role = ["HR", "Recruiter", "Software Engineer", "QA", "Secretary", "Manager", "Support", "Cleaner", "Security"]

    if search_d is None:
        for item in job_role:
            result.write("JOB ROLE: " + item + "\n")
            for headline in headlines_data["headlines"]:
                if item == headline["keyword"]:
                    result.write("      Headline: " + headline["title"] + "\n")
    else:
        for item in job_role:
            result.write("JOB ROLE: " + item + "\n")
            for headline in headlines_data["headlines"]:
                if search_d == headline["publication date"]:
                    if item == headline["keyword"]:
                        result.write("      Headline: " + headline["title"] + "\n")
    result.close()

#list of languages and all headlines that match
def match_lang2headline(search_d):
    #Create new file to store department headlines
    result = open("language_headlines.txt", "w")

    language = ["English", "German", "Spanish", "Bulgarian", "Greek", "Chinese", "Japanese", "Brazilian", "Russian", "Italian"]

    if search_d is None:
        for item in language:
            result.write("LANGUAGE: " + item + "\n")
            for headline in headlines_data["headlines"]:
                if item == headline["language"]:
                    result.write("      Headline: " + headline["title"] + "\n")
    else:
        for item in language:
            result.write("LANGUAGE: " + item + "\n")
            for headline in headlines_data["headlines"]:
                if search_d == headline["publication date"]:
                    if item == headline["language"]:
                        result.write("      Headline: " + headline["title"] + "\n")
    result.close()
