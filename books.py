#import required modules 
import csv 

with open('2021books.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    list_of_column_names = []

    for row in csv_reader:
        list_of_column_names.append(row)
        break 

print("List of column names : ",
      list_of_column_names[0])

