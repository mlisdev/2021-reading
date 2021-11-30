import csv

with open ('2021books.csv', 'r') as csvfile:
    books = csv.reader (csvfile, delimiter = ',')
    next(books)

    titleIndex = 0
    daysReadIndex = 12

    longestReadBookTitle = ""
    numDays = 0
    
    for row in books:
        # skip the header
        # if row[titleIndex] == "Title":
        #     continue
        # get the string value of days read
        daysRead = row[daysReadIndex]
        
        # ignore empty string
        if daysRead:
            intDaysRead = int (daysRead)
            
            # if this book took you longer than the previous longest, update the values
            if intDaysRead > numDays:
                numDays = intDaysRead
                longestReadBookTitle = row[titleIndex]
    print ("The book I spent the most time on was %s; it took me %d days." % (longestReadBookTitle, numDays))
        