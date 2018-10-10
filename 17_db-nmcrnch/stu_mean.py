#T Fabiha
#SoftDev1 pd6
#Average
#2018-10-09

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

#CREATING PEEPS TABLE
command = "CREATE TABLE peeps_avg(average REAL , id INTEGER)" #creates table peeps_avg
c.execute(command)

command = "SELECT id from peeps"
ppl_ids = c.execute(command).fetchall() #finds list of all the ids

print("\n")
print("=============================================")

print("Printing name, id and average of each student\n")

for each in ppl_ids:
    i = each[0] #saves the id

    command = "SELECT name FROM peeps WHERE id = " + str(i)
    name = c.execute(command).fetchone()[0] #saves the name associated with the id

    command = "SELECT mark FROM courses WHERE id = " + str(i)
    grades = c.execute(command).fetchall() #saves a lit of the grades associated with the id

    #finds the average of each student's grades
    summ = 0
    for num in grades:
        summ += num[0]
    avg = summ/len(grades) #saves average

    command = "INSERT INTO peeps_avg VALUES({0}, {1})".format(avg, i) #adds to table peeps_avg
    c.execute(command)

    '''
    print("\n")
    print(name)
    print(each[0])
    print(grades)
    print(avg)
    '''

    print('({}, {}, {})'.format(name, i, avg)) #prints out: (name, id, average)

print("=============================================")

#==========================================================

db.commit() #save changes
db.close()  #close database
