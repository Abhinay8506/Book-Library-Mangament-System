import mysql.connector as sql
import datetime
import sys

def addbook():
    conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
    mycursor=conn.cursor()
    bno=int(input("Enter Book no"))
    bname= input("Enter the Book name")
    Auth= input("Enter the Author name")
    pub=input("Enter the publisher")
    qty=int(input("Enter the quantity"))
    cat=input("Enter the cateogry")
    try:
        query="insert into book values(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(query,(bno,bname,Auth,pub,qty,cat))
        print("Data inserted successfully")
        conn.commit()
        conn.close()
    except sql.IntegrityError:
        print("Book No exists")
        print("Enter new book no")
        
def displayB():
    conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
    mycursor=conn.cursor()
    query="select * from book"
    mycursor.execute(query)
    data = mycursor.fetchall()
    for row in data:
        print("Bookcode :", row[0])
        print("Book Name :", row[1])
        print("Author :", row[2])
        print("Publisher :", row[3])
        print("Quantuty:", row[4])
        print("Cateogry :", row[5])
        print("*************************************")
    conn.close()

def searchB():
    conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
    mycursor=conn.cursor()
    ch=input("Enter Book No or Book Name")
    if ch.isdigit():
        x=int(ch)
        y="bno"
    else:
        x=ch
        y="bname"
    query= "select * from book where " + y + " =%s"
    mycursor.execute(query,(x,))
    data=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No record found")
    else:
        for row in data:
            print()
            print("Bookcode :", row[0])
            print("Book Name :", row[1])
            print("Author :", row[2])
            print("Publisher :", row[3])
            print("Quantuty:", row[4])
            print("Cateogry :", row[5])
            print("*************************************")
            
    conn.close()


def delB():
    conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
    mycursor=conn.cursor()
    ch=input("Enter Book No or Book Name")
    if ch.isdigit():
        x=int(ch)
        y="bno"
    else:
        x=ch
        y="bname"
    query= "select * from book where " + y + " =%s"
    mycursor.execute(query,(x,))
    count=mycursor.rowcount
    conn.close()
    if count==0:
        print("No record to delete")
    elif count>1:
        print("Multiple books are found. Enter the book no of the book you want to delete")
        searchB()
        delb()
    else:
        conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
        mycursor=conn.cursor()
        query="delete from book where "+y+" =%s"
        mycursor.execute(query,(x,))
        conn.commit()
        conn.close()
        print("Data deleted successfully")
        
def addM():
    conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
    mycursor=conn.cursor()
    mno=int(input("Enter Member no."))
    name= input("Enter the Member name")
    phno=int(input("Enter the Phone no"))
    #date=input("Enter the Date of joining in YYYYMMDD format")
    try:
        query="insert into member values(%s,%s,%s)"
        mycursor.execute(query,(mno,name,phno))
        print("Data inserted successfully")
        conn.commit()
        conn.close()
    except sql.IntegrityError:
        print("Member No. exists")
        print("Enter new Member no.")


def displayM():
    conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
    mycursor=conn.cursor()
    query="select * from member"
    mycursor.execute(query)
    data = mycursor.fetchall()
    for row in data:
        print("Membership code :", row[0])
        print("Name :", row[1])
        print("Phone No :", row[2])
        print("*************************************")
    conn.close()

def searchM():
    conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
    mycursor=conn.cursor()
    ch=input("Enter Membership No")
    query= "select m.mno,m.mname,m.phoneno,b.bno,b.bname, i.idate, i.rdate from book b, issue i, member m where b.bno=i.bno and m.mno=i.mno and m.mno=%s"
    mycursor.execute(query,(ch,))
    data=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No record found")
    else:
        print("Membership code :", data[0][0])
        print("Name :", data[0][1])
        print("Phone No :", data[0][2])
        print("Details of Book Issued")
        for row in data:
            print()
            print("Book no issued: ",row[3])
            print("Book name issued: ",row[4])
            print("Date of Issue:",row[5])
            print("Return Date: ", row[6])
            print("*************************************")
            
    conn.close()
def delM():
    try:
        conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
        mycursor=conn.cursor()
        ch=int(input("Enter Member No"))
        query= "select * from member where mno =%s"
        mycursor.execute(query,(ch,))
        count=mycursor.rowcount
        conn.close()
        if count==0:
            print("No record to delete")
        else:
            conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
            mycursor=conn.cursor()
            query="delete from member where mno =%s"
            mycursor.execute(query,(ch,))
            conn.commit()
            conn.close()
            print("Data deleted successfully")
    except sql.errors.IntegrityError:
        print("Cannot delete member as books are issued to the members")

def updateM():
    conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
    mycursor=conn.cursor()
    ch=int(input("Enter Member No"))
    query= "select * from member where mno =%s"
    mycursor.execute(query,(ch,))
    count=mycursor.rowcount
    conn.close()
    if count==0:
        print("No record to update")
    else:
        x=int(input("Enter 1. to update name and 2. to update phoneno "))
        if x==1:
            y=input("Enter the new name")
            query="update member set mname=%s where mno = %s"
            
        elif ch==2:
            y=int(input("Enter number"))
            query="update member set phoneno=%s where mno = %s"
        
            
        conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
        mycursor=conn.cursor()
        mycursor.execute(query,(y,ch))
        conn.commit()
        conn.close()
        print("Data Updated Successfully")
def issueB():
    try:
        conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
        mycursor=conn.cursor()
        bno=int(input("Enter Book no"))
        mno=int(input("Enter Membership no."))
        idate=datetime.date.today()
        conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
        mycursor=conn.cursor()
        query="insert into issue(bno,mno,idate) values(%s,%s,%s)"
        mycursor.execute(query,(bno,mno,idate))
        conn.commit()
        conn.close()
        print("Book issued")
    except sql.errors.IntegrityError:
        print("Check book no or membership  no.")

def returnB():
    try:
        conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
        mycursor=conn.cursor()
        mno=int(input("Enter Membership no."))
        bno=int(input("Enter Book no"))
        rdate=datetime.date.today()
        query="update issue set rdate = %s where mno=%s and bno=%s"
        mycursor.execute(query,(rdate,mno,bno))
        conn.commit()
        conn.close()
        print("Book returned. Database updated")
    except sql.errors.IntegrityError:
        print("Check book no or membership  no.")

def displayI():
    conn=sql.connect(host="localhost", user="root", password="root1234", database="library")
    mycursor=conn.cursor()
    query= "select m.mno,m.mname,m.phoneno,b.bno,b.bname, i.idate, i.rdate from book b, issue i, member m where b.bno=i.bno and m.mno=i.mno and i.rdate IS NULL"
    mycursor.execute(query)
    data=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No record found")
    else:
        for row in data:
            print("Membership code :", row[0])
            print("Name :", row[1])
            print("Phone No :", row[2])
            print("Details of Book Issued")
            print()
            print("Book no issued: ",row[3])
            print("Book name issued: ",row[4])
            print("Date of Issue:",row[5])
            print("Return Date: ", row[6])
            print("*************************************")
            
    conn.close()
    
def issue():
    while  True:
        print("1. Issue Book")
        print("2. Return Book")
        print("3. Display Issued Books")
        print("4. Back to Main Menu")
        ch=int(input("Enter your choice"))
        if ch==1:
            issueB()
        elif ch==2:
            returnB()
        elif ch==3:
            displayI()
        elif ch==4:
            menu()
        else:
            print("Wrong Choice. Enter your choice again")

    
        
def member():
    while True:
        print("1. Add Member")
        print("2. Display Member")
        print("3. Search a Member")
        print("4. Delete a Member")
        print("5. Update details")
        print("6. Back to Main Menu")
        ch = int(input("Enter your choice"))
        if ch==1:
            addM()
        elif ch==2:
            displayM()
        elif ch==3:
            searchM()
        elif ch==4:
            delM()
        elif ch==5:
            updateM()
        elif ch==6:
            menu()
        else:
            print("Wrong Choice. Enter your choice again")





def book():
    while True:
        print("1. Add Book")
        print("2. Display Book")
        print("3. Search a Book")
        print("4. Delete a Book")
        print("5. Back to Main Menu")
        ch = int(input("Enter your choice"))
        if ch==1:
            addbook()
        elif ch==2:
            displayB()
        elif ch==3:
            searchB()
        elif ch==4:
            delB()
        elif ch==5:
            menu()
        else:
            print("Wrong Choice. Enter your choice again")



def menu():
    while True:
        print("*****LIBRARY MANAGEMENT SYSTEM*****")
        print("1. Book")
        print("2. Member")
        print("3. Issue/Return")
        print("4. Exit")
        ch=int(input("Enter your choice"))
        if ch==1:
            book()
        elif ch==2:
            member()
        elif ch==3:
            issue()
        elif ch==4:
            sys.exit()
        else:
            print("Wrong choice. Enter your choice again")

 

menu()
