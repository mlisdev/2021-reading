#import required modules 
import pandas as pd 

books = pd.read_csv('2021books.csv')
# print(books.columns) 

#save gender column as variable 
author_gender = books.Gender 

#set gender as saved variable and int 
m = 0 
f = 0 
nb = 0
other = 0 

#for look to count each instance of gender type and increment for total count 
for gender in author_gender: 
      if gender == 'M': 
            m += 1 

      elif gender == 'F': 
            f += 1

      elif gender == 'NB': 
            nb += 1 
      
      elif gender == 'other': 
            other += 1

#print results of gender for loop 
# print('Male: ', (m), '\n', 
# 'Female: ', (f), '\n', 
# 'Non-Binary: ', (nb), '\n', 
# 'Not defined: ', (other))

#find book that took the longest to read 
days_read = books['DaysRead'].fillna(0).astype(int) 
title = books.Title
