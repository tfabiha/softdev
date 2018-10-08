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
command = "CREATE TABLE peeps_avg(average REAL , id INTEGER)"
c.execute(command)

command = "SELECT id from peeps"
ppl_ids = c.execute(command).fetchall()

print("\n")
print("=============================================")

print("Printing name, id and average of each student\n")

for each in ppl_ids:
    i = each[0]

    command = "SELECT name FROM peeps WHERE id = " + str(i)
    name = c.execute(command).fetchone()[0]

    command = "SELECT mark FROM courses WHERE id = " + str(i)
    grades = c.execute(command).fetchall()

    summ = 0
    for num in grades:
        summ += num[0]
    avg = summ/len(grades)

    command = "INSERT INTO peeps_avg VALUES({0}, {1})".format(avg, i)
    c.execute(command)

    '''
    print("\n")
    print(name)
    print(each[0])
    print(grades)
    print(avg)
    '''

    print('({}, {}, {})'.format(name, i, avg))

print("=============================================")

#==========================================================

db.commit() #save changes
db.close()  #close database
