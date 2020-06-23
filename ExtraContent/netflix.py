import os

import csv



csvpath = os.path.join("..","Resources" , "netflix_ratings.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    video = input("What movie would you like to watch? ")
#print(csvreader)
    
    for row in csvreader:
        if video == row[0]:
            print(f"{video} is rated {row[1]} with a user rating of {row[5]}")
            break
        #else:
           # print("Sorry, that movie is not available")


#if video in csvreader:
    #print(f"{video} is in the library.")

