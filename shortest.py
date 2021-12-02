import csv


with open ('2021books.csv', 'r') as csvfile:
    books = csv.reader (csvfile, delimiter = ',')
    next(books)

    titleIndex = 0
    dnfIndex = 4
    daysReadIndex = 12
    rereadIndex = 11 

    shortestTitle = ""
    numDays = 0
    
    shortestList = []
    
    for row in books:
        daysRead = row[daysReadIndex]
        dnf = row[dnfIndex]
        reread = row[rereadIndex]

        # ignore empty string
        if daysRead:
            intDaysRead = int(daysRead)
            
            # if this book took you longer than the previous longest, update the values
            if intDaysRead <= numDays:
                #skip dnf books or reread books (i hope)
                if dnf == 'Yes' or reread == 'Yes': 
                    continue
                numDays = intDaysRead
                shortestTitle = row[titleIndex]
                shortestList.append(shortestTitle)
    print (shortestList)
        