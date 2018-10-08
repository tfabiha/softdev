#Scriptors -- Daniel Gelfand && T Fabiha
#SoftDev1 pd6
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#CREATING PEEPS TABLE
command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"
c.execute(command)

print("\n");

#Opening peeps.csv and reading

print("==============================================================")
print("Printing students, ages, and their ids from the table peeps.\n")

with open("peeps.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['age'], row['id'])
        #Adding onto the command to incorporate names, ages, and ids in CSV file
        command = 'INSERT INTO peeps VALUES '
        command += '( "' + row['name'] + '", '
        command += row['age'] + ', '
        command += row['id'] + ')'
        c.execute(command)

print("==============================================================")
print("\n");

#CREATING COURSES TABLE
command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"
c.execute(command)

print("==========================================================================")
print("Printing courses, grades, and their matching ids from the table courses.\n")

with open("courses.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['code'], row['mark'], row['id'])
        #Adding onto the command to incorporate codes, marks, and ids in CSV file
        command = 'INSERT INTO courses VALUES '
        command += '( "' + row['code'] + '", '
        command += row['mark'] + ', '
        command += row['id'] + ')'
        c.execute(command)

print("==========================================================================")
print("\n");

#==========================================================

db.commit() #save changes
db.close()  #close database
