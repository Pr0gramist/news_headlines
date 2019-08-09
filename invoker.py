'''
    Python Script to call API
        Input: Publication Date (yyyy-mm-dd)
    By: Stivan Kitchoukov
'''

import datetime
import news_match as newsAPI
print("######################################################################")
print("Welcome to News Headline matching service!")
print("Please use dates between 2019-06-01 and 2019-08-07 for results.")
print("######################################################################")
print("Please enter a publication date in format yyyy-mm-dd:")
search_d = input()

try:
    datetime.datetime.strptime(search_d, "%Y-%m-%d")
except ValueError:
    raise ValueError("Incorrect format for date. Format should be YYYY-MM-DD")

print("Getting your headlines ready...")
if newsAPI.match_headline2employee(search_d):
    print("Headlines have been created. Please see result.txt")
else:
    print("Failed to match headlines with employees.")
