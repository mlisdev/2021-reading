#import required modules 
import pandas as pd 

books = pd.read_csv('2021books.csv')
# print(books.columns) 

author_gender = books.Gender 

m = 0 
f = 0 
nb = 0

for gender in author_gender: 
      if gender == 'M': 
            m += 1 

      elif gender == 'F': 
            f += 1

      elif gender == 'NB': 
            nb += 1 

print('Male: ', (m), 
'Female: ', (f), 
'Non-Binary: ', (nb))