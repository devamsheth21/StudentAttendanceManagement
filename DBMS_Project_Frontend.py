#!/usr/bin/env python
# coding: utf-8

# In[38]:


import sys
from tkinter import *
import tkinter.messagebox

sys.path.append("../DBMS_project")

import DBMS_Project_Backend
class student :
    
    def __init__(self,root) :
        self.root = root
        self.root.title("Student Attendance Management System")
        self.root.geometry("1350x75000+0+0")
        self.root.config(bg = "cadet blue")
        
        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Courseid = StringVar()
        Attendance = StringVar()
        Emailid =StringVar()
        Classid = StringVar()
        #||=====================================================||
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Database", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        
        def cleardata():
            self.txtclid.delete(0,END)
            self.txtcoid.delete(0,END)
            self.txtStdID.delete(0,END)
            self.txtfnaid.delete(0,END)
            self.txtsnaid.delete(0,END)
            self.txteid.delete(0,END)
            self.txtAtt.delete(0,END)
            
        def addData():
            if(len(Classid.get())!=0):
                DBMS_Project_Backend.addStdRec(Classid.get(), Courseid.get(), StdID.get(), Firstname.get(), Surname.get(), Emailid.get(), Attendance.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(Classid.get(), Courseid.get(), StdID.get(), Firstname.get(), Surname.get(), Emailid.get(), Attendance.get()))
        
        def DisplayData():
            studentlist.delete(0,END)
            for row in DBMS_Project_Backend.viewDate():
                studentlist.insert(END,row,str(""))
            
        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)
            
            self.txtclid.delete(0,END)
            self.txtclid.insert(END,sd[0])
            self.txtcoid.delete(0,END)
            self.txtcoid.insert(END,sd[1])
            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,sd[2])
            self.txtfnaid.delete(0,END)
            self.txtfnaid.insert(END,sd[3])
            self.txtsnaid.delete(0,END)
            self.txtsnaid.insert(END,sd[4])
            self.txteid.delete(0,END)
            self.txteid.insert(END,sd[5])
            self.txtAtt.delete(0,END)
            self.txtAtt.insert(END,sd[6])
        
        def DeleteData():
            if(len(Classid.get())!=0):
                DBMS_Project_Backend.deleteRec(sd[0])
                cleardata()
                DisplayData()
        
        #def stdrec():
        #    studentlist.delete(0,END)
        #    for row in DBMS_Project_Backend.studentrecord():
        #        studentlist.insert(END,row,str(""))
        
        #def classrec():
        #    studentlist.delete(0,END)
        #    for row in DBMS_Project_Backend.classrecord():
        #        studentlist.insert(END,row,str(""))
        
        def searchDatabase():
            studentlist.delete(0,END)
            for row in DBMS_Project_Backend.searchData(Classid.get(), Courseid.get(), StdID.get(), Firstname.get(), Surname.get(), Emailid.get(), Attendance.get()):
                studentlist.insert(END,row,str(""))
                
        def update():
            if(len(StdID.get())!=0):
                DBMS_Project_Backend.deleteRec(sd[0])
            if(len(StdID.get())!=0):
                DBMS_Project_Backend.addStdRec(Classid.get(), Courseid.get(), StdID.get(), Firstname.get(), Surname.get(), Emailid.get(), Attendance.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(Classid.get(), Courseid.get(), StdID.get(), Firstname.get(), Surname.get(), Emailid.get(), Attendance.get()))
            
        #||=====================================================||
        MainFrame = Frame(self.root,bg="cadet blue")
        MainFrame.grid()
        
        TitFrame = Frame(MainFrame,bd=2,width=1250,height=70,padx=10,pady=10,bg="Ghost White", relief= RIDGE)
        TitFrame.pack(side=TOP)
        
        self.lblTit =Label(TitFrame, font=('arial', 20, 'bold'),text="Student Attendance Management System", bg="Ghost White")
        self.lblTit.grid(sticky=W)
        
        ButtonFrame = Frame(MainFrame,bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief= RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,relief= RIDGE, bg="cadet blue")
        DataFrame.pack(side=BOTTOM)
        
        DataFrameLEFT = LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,relief= RIDGE,bg="Ghost White",
                               font=('arial',20,'bold'),text="Student Info\n")
        DataFrameLEFT.pack(side=LEFT)
        
        DataFrameRIGHT = LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=3,relief= RIDGE,bg="Ghost White",
                               font=('arial',20,'bold'),text="Student Details\n")
        DataFrameRIGHT.pack(side=RIGHT)
              #||=====================================================||
        
        self.lblclid = Label(DataFrameLEFT,font=('arial',20,'bold'),text="ClassID:",padx=2,pady=3,bg="Ghost White")
        self.lblclid.grid(row=0,column=0,sticky=W)
        self.txtclid = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Classid,width=33)
        self.txtclid.grid(row=0,column=1)
        
        self.lblcoid = Label(DataFrameLEFT,font=('arial',20,'bold'),text="CourseID:",padx=2,pady=3,bg="Ghost White")
        self.lblcoid.grid(row=1,column=0,sticky=W)
        self.txtcoid = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Courseid,width=33)
        self.txtcoid.grid(row=1,column=1)
        
        self.lblStdID = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Roll No.:",padx=2,pady=3,bg="Ghost White")
        self.lblStdID.grid(row=2,column=0,sticky=W)
        self.txtStdID = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=StdID,width=33)
        self.txtStdID.grid(row=2,column=1)
        
        self.lblfnaid = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Firstname:",padx=2,pady=3,bg="Ghost White")
        self.lblfnaid.grid(row=3,column=0,sticky=W)
        self.txtfnaid = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Firstname,width=33)
        self.txtfnaid.grid(row=3,column=1)
        
        self.lblsnaid = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Lastname:",padx=2,pady=3,bg="Ghost White")
        self.lblsnaid.grid(row=4,column=0,sticky=W)
        self.txtsnaid = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Surname,width=33)
        self.txtsnaid.grid(row=4,column=1)
     
        self.lbleid = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Email ID:",padx=2,pady=3,bg="Ghost White")
        self.lbleid.grid(row=5,column=0,sticky=W)
        self.txteid = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Emailid,width=33)
        self.txteid.grid(row=5,column=1)

        self.lblAtt = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Attendance:",padx=2,pady=3,bg="Ghost White")
        self.lblAtt.grid(row=6,column=0,sticky=W)
        self.txtAtt = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Attendance,width=33)
        self.txtAtt.grid(row=6,column=1)
              #||=====================================================||
        
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')
        
        studentlist = Listbox(DataFrameRIGHT,width=41,height=16,font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command= studentlist.yview)
        
        #||=====================================================||
        
        self.btnAddDate = Button(ButtonFrame, text = "Add New",font = ('arial',20,'bold'),height =1,width =8,bd=4, command=addData)
        self.btnAddDate.grid(row=0,column=0)
        
        self.btnDisplay = Button(ButtonFrame, text = "Display",font = ('arial',20,'bold'),height =1,width =8,bd=4, command=DisplayData)
        self.btnDisplay.grid(row=0,column=1)
        
        self.btnClear = Button(ButtonFrame, text = "Clear",font = ('arial',20,'bold'),height =1,width =8,bd=4, command=cleardata)
        self.btnClear.grid(row=0,column=2)
        
        self.btnDelete = Button(ButtonFrame, text = "Delete",font = ('arial',20,'bold'),height =1,width =8,bd=4, command=DeleteData)
        self.btnDelete.grid(row=0,column=3)
        
        self.btnSearch = Button(ButtonFrame, text = "Search",font = ('arial',20,'bold'),height =1,width =8,bd=4, command=searchDatabase)
        self.btnSearch.grid(row=0,column=4)
        
        self.btnUpdate = Button(ButtonFrame, text = "Update",font = ('arial',20,'bold'),height =1,width =8,bd=4, command=update)
        self.btnUpdate.grid(row=0,column=5)
        
        self.btnClassr = Button(ButtonFrame, text = "Exit",font = ('arial',20,'bold'),height =1,width =10,bd=4, command=iExit)
        self.btnClassr.grid(row=0,column=6)
        
if __name__ == '__main__' :
        
        root= Tk()
        application = student(root)
        root.mainloop()


# In[ ]:





# In[ ]:




