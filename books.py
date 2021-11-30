#import required modules 
import csv 
import statistics as stats
import pandas as pd 

#print first row to check header names 
# with open('2021books.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = ',')
#     list_of_column_names = []

#     for row in csv_reader:
#         list_of_column_names.append(row)
#         break 

# print("List of column names : ",
#       list_of_column_names[0])

# bookinfo = open('2021books.csv', 'r')

#set columns as variables for easy retrieval 
# TITLE = 0 
# AUTHOR = 1
# DATE_STARTED = 2
# DATE_FINISHED = 3
# DNF = 4 
# RATING = 5
# AUTHOR_GENDER = 6 
# GENRES = 7 
# PAGE_COUNT = 8 
# FORMAT = 9 
# SOURCE = 10 
# REREAD = 11 
# DAYS_READ = 12 
# PPD = 13 

books = pd.read_csv('2021books.csv')

#check csv data 
# print(books)

#print length 
print("Number of lines present:-", 
      len(books))

