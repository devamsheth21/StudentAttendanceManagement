#!/usr/bin/env python
# coding: utf-8


import sqlite3

#datafile = 'student2.db'
#datadir = 'C:\\Users\\ASUS\\'
db = 'student2.db'

def studentData() :
    con=sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(("CREATE TABLE student2(id INTEGER PRIMARY KEY, Classid INTEGER, Courseid text, StdID text, Firstname text, Surname text, Emailid text, Attendance text)")
    con.commit()
    con.close()
    
def addStdRec(Classid, Courseid, StdID, Firstname, Surname, Emailid, Attendance):
    con=sqlite3.connect(db)
    cur =con.cursor()
    cur.execute("INSERT INTO student2 VALUES (NULL,?,?,?,?,?,?,?)",(Classid,Courseid,StdID,Firstname,Surname,Emailid,Attendance))
    con.commit()
    con.close()
    
def viewDate():
    con=sqlite3.connect(db)
    cur =con.cursor()
    cur.execute("SELECT * FROM student2")
    records = cur.fetchall()
    con.close
    return records

def deleteRec(id):
    con=sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("DELETE FROM student2 WHERE id=?", (id,))
    con.commit()
    con.close()
    
def searchData(Classid="", Courseid="", StdID="", Firstname="",Surname="", Emailid="", Attendance=""):
    con=sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT * FROM student2 WHERE Classid=? OR Courseid=? OR StdID=? OR Firstname=? OR Surname=? OR Emailid=? OR Attendance=?", (Classid, Courseid, StdID, Firstname, Surname, Emailid, Attendance))
    records = cur.fetchall()
    con.close()
    return records

def dataUpdate(id,Classid="", Courseid="", StdID="", Firstname="", Surname="", Emailid="", Attendance=""):
    con=sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("UPDATE student2 SET Classid=?, Courseid=?, StdID=?, Firstname=?, Surname=?, Emailid=?, Attendance=?",(Classid, Courseid, StdID, Firstname, Surname, Emailid, Attendance))
    con.commit()
    con.close()

studentData()



