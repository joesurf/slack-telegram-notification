from Base import *

LARGE_FONT = ("Arial Bold",40)
COLOUR = "ivory3" # Menu Colour

# Main

def MainMenuPage():

    root = Tk()
    root.geometry("1366x768")
    root.title = "Functions"

    #Images
    m_im = ImageTk.PhotoImage(Image.open(rel_path("member.png")) )
    label1 = Label(root, image = m_im, width =210,height =150)
    label1.place(relx=0.13,rely=0.2)

    b_im = ImageTk.PhotoImage(Image.open(rel_path("book.png")))
    label2 = Label(root, image = b_im, width =210,height =150)
    label2.place(relx=0.43,rely=0.2)

    l_im = ImageTk.PhotoImage(Image.open(rel_path("loan.png")))
    label3 = Label(root, image = l_im, width =210,height =150)
    label3.place(relx=0.73,rely=0.2)

    r_im = ImageTk.PhotoImage(Image.open(rel_path("Reservationimg.png")))
    label3 = Label(root, image = r_im, width =210,height =150)
    label3.place(relx=0.13, rely=0.55)

    f_im = ImageTk.PhotoImage(Image.open(rel_path("fines.png")))
    label4 = Label(root, image = f_im, width =210,height =150)
    label4.place(relx=0.43,rely=0.55)

    re_im = ImageTk.PhotoImage(Image.open(rel_path("report.png")))
    label5 = Label(root, image = re_im, width =210,height =150)
    label5.place(relx=0.73,rely=0.55)

    heading = Label(text = "(ALS)", fg = "black", bg = "ivory3", width = 100, height = 4, font = ("Arial", 30))
    heading.pack()

    #Buttons
    membership = Button(root,text = "Membership",height = 2,font = ("Arial Bold",20),command=sequence(lambda: root.destroy(), MembershipMenuPage))
    membership.place(x= 205, y =320)

    books = Button(root,text = "Books",height = 2,font = ("Arial Bold",20), command=sequence(lambda: root.destroy(), BookMenuPage))
    books.place(x= 645, y = 320)

    loans = Button(root,text = "Loans",height = 2,font = ("Arial Bold",20), command=sequence(lambda: root.destroy(), BookLoanMenuPage))
    loans.place(x= 1055, y = 320)

    reservations = Button(root,text = "Reservations",font = ("Arial Bold",20),height = 2, command=sequence(lambda: root.destroy(), ReservationMenuPage))
    reservations.place(x = 205, y = 590)

    fines = Button(root,text = "Fines",font = ("Arial Bold",20),height = 2, command=sequence(lambda: root.destroy(), FineMenuPage))
    fines.place(x = 645, y = 590)

    reports = Button(root,text = "Reports",font = ("Arial Bold",20), height = 2, command=sequence(lambda: root.destroy(), ReportMenuPage))
    reports.place(x = 1055, y = 590)
            
    root.mainloop()


# Membership

def MembershipMenuPage():

    root = Tk()
    root.geometry("1366x768")
    root.title("Functions")
    root.resizable(0, 0)

    icon = ImageTk.PhotoImage(Image.open(rel_path('member.png'))) 
    label = Label(root, image = icon, width =400,height =400)
    label.place(relx=0.1,rely=0.3)
  
    heading = Label(text = "Select one of the Options below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    creation = Button(root,text = "1. Creation",height = 2,font = ("Arial Bold",30),command=sequence(lambda: root.destroy(), MembershipCreationPage))
    creation.place(x= 700, y =260)

    t1 = Label(root,text = "Membership Creation",font=("Arial Bold",20))
    t1.place(x = 1000, y=285)

    deletion = Button(root,text = "2. Deletion",height = 2,font = ("Arial Bold",30), command=sequence(lambda: root.destroy(), MembershipDeletionPage))
    deletion.place(x= 700, y = 380)

    t2 = Label(root,text = "Membership Deletion",font=("Arial Bold",20))
    t2.place(x = 1000, y=405)

    update = Button(root,text = "3. Update",height = 2,bg = "Blue",font = ("Arial Bold",30), command=sequence(lambda: root.destroy(), MembershipUpdatePage))
    update.place(x= 700, y = 500)

    t3 = Label(root,text = "Membership Update",font=("Arial Bold",20))
    t3.place(x = 1000, y= 525)

    button = Button(root,text = "Back to Main Menu",font = ("Arial Bold",12),height = 4,width =150, command=sequence(lambda: root.destroy(), MainMenuPage))
    button.place(x = 150, y = 670)
            
    root.mainloop()

def MembershipCreationPage():

    def MembershipCreation():

        def clear():
            MembershipID_entry.delete(0, END)
            Name_entry.delete(0, END)
            PhoneNumber_entry.delete(0, END)
            Faculty_entry.delete(0, END)
            Email_entry.delete(0, END)

        try:
            con = create_db_connection(host, user, password, database)
            cur = con.cursor()
            cur.execute('SELECT MembershipID FROM Member WHERE MembershipID=%s', MembershipID_entry.get())
            row = cur.fetchone()
            if row != None:
                messagebox.showerror('Error!', 'Member already exist; Missing or Incomplete fields.')
            elif (MembershipID_entry.get() == '' or Name_entry.get() == '' or Faculty_entry.get() == '' or PhoneNumber_entry.get() == '' or Email_entry.get() == ''):
                messagebox.showerror('Error!', 'Member already exist; Missing or Incomplete fields.')
            else:
                cur.execute('INSERT INTO Member(MembershipID, Name, PhoneNumber, Faculty, EmailAddress) VALUES (%s, %s, %s, %s, %s)', 
                (MembershipID_entry.get(), Name_entry.get(), PhoneNumber_entry.get(), Faculty_entry.get(), Email_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success!', 'ALS Membership created.')
                clear()
        except Exception as e:
            messagebox.showerror('error!', f'Error due to {e}')

    root = Tk()
    root.geometry("1366x768")
    root.resizable(0, 0)

    bg = PhotoImage(file = rel_path("bookshelf.png"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)

    root.title("MembershipCreation")
    heading = Label(text = "To Create Member, Please Enter Requested Information Below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    MembershipID_text = Label(text = "Membership ID", font = ("Arial", 25), bg = "ivory3")
    Name_text = Label(text = "Name", font = ("Arial", 25), bg = "ivory3")
    Faculty_text = Label(text = "Faculty", font = ("Arial", 25), bg = "ivory3")
    PhoneNumber_text = Label(text = "Phone Number", font = ("Arial", 25), bg = "ivory3")
    Email_text = Label(text = "Email Address", font = ("Arial", 25), bg = "ivory3")

    MembershipID_text.place(x = 60, y = 200)
    Name_text.place(x = 60, y = 280)
    Faculty_text.place(x = 60, y = 360)
    PhoneNumber_text.place(x = 60, y = 440)
    Email_text.place(x = 60, y = 520)

    MembershipID_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    Name_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    Faculty_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    PhoneNumber_entry = Entry(textvariable = IntVar(), bg = "ivory3", bd = 4, width = 100)
    Email_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)

    MembershipID_entry.place(x = 360, y = 200)
    Name_entry.place(x = 360, y = 280)
    Faculty_entry.place(x = 360, y = 360)
    PhoneNumber_entry.place(x = 360, y = 440)
    Email_entry.place(x = 360, y = 520)

    CreateMember = Button(root, text = "Create Member", width = 15, height = 4, font = ("Arial", 25), command = MembershipCreation)
    CreateMember.place(x = 250, y = 600)

    BackToMain = Button(root, text = "Back to Main Menu", width = 15, height = 4, font = ("Arial", 25),command=sequence(lambda: root.destroy(), MembershipMenuPage))
    BackToMain.place(x = 950, y = 600)

    root.mainloop()

def MembershipDeletionPage():

    def MembershipDeletion(id):
        connection = create_db_connection(host, user, password, database)

        # Assumes record is deleted if books have been returned
        q1 = f"""
        SELECT COUNT(*)
        FROM BookLoan
        WHERE MembershipID = '{id}';
        """

        q2 = f"""
        SELECT COUNT(*)
        FROM Reservation
        WHERE MembershipID = '{id}';
        """

        # Assumes record is deleted if no payment due
        q3 = f"""
        SELECT COUNT(*)
        FROM Fine
        WHERE MembershipID = '{id}';
        """

        # Delete ID from all tables via CASCADE
        q4 = f"""
        DELETE FROM Member
        WHERE MembershipID = '{id}';
        """
        success_message = "ALS Membership deleted"
        failure_message = "Member does not exist; Missing or Incomplete fields."

        if read_query(connection, q1)[0][0] == 0 and read_query(connection, q2)[0][0] == 0:
            if read_query(connection, q3)[0][0] == 0:
                execute_query(connection, q4,success_message,failure_message)
            else:
                messagebox.showerror("Error","Fines not paid")
                
        else:
            messagebox.showerror("Error","Books Not Returned")

           

        return
    def MembershipDel():
        MembershipDeletion(MembershipID_entry.get())

    def get(id_):
        connection = create_db_connection(host, user, password, database)
        q1 = f"""
        SELECT *
        FROM Member
        WHERE MembershipID = '{id_}';
        """
        record = read_query1(connection, q1)
        if type(record)!= None:
        
            str = f'\n Membership ID: {id_} \n Member Name： {record[1]} \n Faculty : {record[2]} \n Phone Number : {record[3]} \n Email : {record[4]}'
        
            return str   
        connection.close()

    def getd():
        return get(MembershipID_entry.get())
    def clear():
        MembershipID_entry.delete(0, END)
           
    def MembershipDeleteCheck():
        try:
            con = con = create_db_connection(host, user, password, database)
            cur = con.cursor()
            cur.execute('SELECT * FROM Member WHERE MembershipID=%s',MembershipID_entry.get())
            row = cur.fetchall()
            if len(row) == 0:
                clear()
    
            else:
                comfirm()
        except Exception as e:
            messagebox.showerror('error!', f'Error due to {e}')

    def comfirm():
    
        top = Toplevel(root)
        top.geometry("500x500")
        top.title("Comfirm Details of Deletion")
        Label(top,text = getd(),font =("Arial Bold", 20)).place(x=100,y=80)
        back = Button(top,text = "Back to \n Delete function ",height = 1,bg = "DodgerBlue",font = ("Arial Bold",15),command=sequence(lambda: top.destroy()))
        back.place(relx =0.6,rely=0.6)
        go = Button(top,text = "Delete Member",height = 1,bg = "DodgerBlue",font = ("Arial Bold",15),command = sequence(MembershipDel)) 
        go.place(relx =0.1,rely=0.6)
        
    root = Tk()
    root.geometry("1366x768")

    bg = PhotoImage(file = rel_path("bookshelf.png"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)

    root.title("MembershipDeletion")
    heading = Label(text = "To Delete Member,Please Enter Membership ID:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    MembershipID_text = Label(text = "Membership ID", font = ("Arial", 25), bg = "ivory3")
    MembershipID_text.place(x = 60, y = 350)

    MembershipID_entry = Entry(bg = "ivory3", bd = 4, width = 100)
    MembershipID_entry.place(x = 360, y = 350)

    DeleteMember = Button(root, text = "Delete Member", width = 15, height = 4, font = ("Arial", 25), command=MembershipDeleteCheck)
    DeleteMember.place(x = 250, y = 550)

    BackToMain = Button(root, text = "Back to \n Membership Menu", width = 15, height = 4, font = ("Arial", 25),command=sequence(lambda: root.destroy(), MembershipMenuPage))
    BackToMain.place(x = 900, y = 550)

    root.mainloop()

def MembershipUpdatePage():

    root = Tk()
    root.title = "MembershipUpdate"
    root.geometry("1366x768")

    def next():
        id = entry.get()
        root.destroy()
        MembershipUpdatePage2(id)

    def MembershipUpdateCheck():
        try:
            con = create_db_connection(host, user, password, database)
            cur = con.cursor()
            cur.execute('SELECT * FROM Member WHERE MembershipID=%s',entry.get())
            row = cur.fetchone()
            if row == None:
                messagebox.showerror('Error!', 'Member does not exist')
        
            else:
                next()
        except Exception as e:
            messagebox.showerror('error!', f'Error due to {e}')    


    bg = PhotoImage(file = rel_path("bookshelf.png"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)

    heading = Label(text = "To Update Member,Please Enter Membership ID:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    t1 = Label(text = "Membership ID", font = ("Arial", 25), bg = "ivory3")
    t1.place(x = 60, y = 350)

    entry = Entry(bg = "ivory3", bd = 4, width = 100)
    entry.place(x = 360, y = 350)

    update = Button(root, text = "Update Member", width = 15, height = 4, font = ("Arial", 25), command=MembershipUpdateCheck)
    update.place(x = 250, y = 550)

    back = Button(root, text = "Back to \n Membership Menu", width = 15, height = 4, font = ("Arial", 25),command=sequence(lambda: root.destroy(), MembershipMenuPage))
    back.place(x = 900, y = 550)

    root.mainloop()

def MembershipUpdatePage2(id):

    def clear():
        MembershipID_entry.delete(0, END)
        Name_entry.delete(0, END)
        PhoneNumber_entry.delete(0, END)
        Faculty_entry.delete(0, END)
        Email_entry.delete(0, END)



    def MembershipUpdate():
        try:
            con = create_db_connection(host, user, password, database)
            cur = con.cursor()
            cur.execute('SELECT * FROM Member WHERE MembershipID=%s', MembershipID_entry.get())
            row = cur.fetchone()
            if row == None:
                messagebox.showerror('Error!', 'Member does not exist')
            elif (MembershipID_entry.get() == '' or Name_entry.get() == '' or Faculty_entry.get() == '' or PhoneNumber_entry.get() == '' or Email_entry.get() == ''):
                messagebox.showerror('Error!', 'Member does not exist; Missing or Incomplete fields.')
            else:
                cur.execute('UPDATE Member SET Name= %s, PhoneNumber= %s, Faculty= %s, EmailAddress = %s WHERE MembershipID = %s', 
                (Name_entry.get(), PhoneNumber_entry.get(), Faculty_entry.get(), Email_entry.get(),MembershipID_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success!', 'ALS Membership Updated.')
                clear()


        except Exception as e:
            messagebox.showerror('error!', f'Error due to {e}')
            
    def confirm():
        top = Toplevel(root)
        top.geometry("500x500")
        top.title("Comfirm Details of Member Update")
        Label(top,text = (f'MembershipID = {MembershipID_entry.get()} \n Name= {Name_entry.get()}\n PhoneNumber= {PhoneNumber_entry.get()}\n Faculty= {Faculty_entry.get()} \n EmailAddress = {Email_entry.get()}',
                            ),font = ("Arial Bold", 20)).place(x=100,y=80)
        back = Button(top,text = "Back to \n Update function ",height = 1,bg = "DodgerBlue",font = ("Arial Bold",15), command=sequence(lambda: top.destroy()))
        back.place(relx =0.6,rely=0.6)
        go = Button(top,text = "Confirm Update",height = 1,bg = "DodgerBlue",font = ("Arial Bold",15),command = sequence(MembershipUpdate))
        go.place(relx =0.1,rely=0.6)


    root = Tk()
    root.geometry("1366x768")  
    root.title("MembershipUpdate")

    bg = PhotoImage(file = rel_path("bookshelf.png"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)

    heading = Label(text = "To Update Member, Please Enter Requested Information Below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    MembershipID_text = Label(text = "Membership ID", font = ("Arial", 25), bg = "ivory3")
    Name_text = Label(text = "Name", font = ("Arial", 25), bg = "ivory3")
    Faculty_text = Label(text = "Faculty", font = ("Arial", 25), bg = "ivory3")
    PhoneNumber_text = Label(text = "Phone Number", font = ("Arial", 25), bg = "ivory3")
    Email_text = Label(text = "Email Address", font = ("Arial", 25), bg = "ivory3")

    MembershipID_text.place(x = 60, y = 200)
    Name_text.place(x = 60, y = 280)
    Faculty_text.place(x = 60, y = 360)
    PhoneNumber_text.place(x = 60, y = 440)
    Email_text.place(x = 60, y = 520)

    MembershipID_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    Name_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    Faculty_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    PhoneNumber_entry = Entry(textvariable = IntVar(), bg = "ivory3", bd = 4, width = 100)
    Email_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)

    MembershipID_entry.insert(0, id)

    MembershipID_entry.place(x = 360, y = 200)
    Name_entry.place(x = 360, y = 280)
    Faculty_entry.place(x = 360, y = 360)
    PhoneNumber_entry.place(x = 360, y = 440)
    Email_entry.place(x = 360, y = 520)

    CreateMember = Button(root, text = "Update Member", width = 15, height = 4, font = ("Arial", 25), command=confirm)
    CreateMember.place(x = 250, y = 600)

    BackToMain = Button(root, text = "Back to Main Menu", width = 15, height = 4, font = ("Arial", 25),command=sequence(lambda: root.destroy(), MembershipMenuPage))
    BackToMain.place(x = 950, y = 600)

    root.mainloop()



# Book

def BookMenuPage():

    root = Tk()
    root.geometry("1366x768")
    root.title = "Functions"

    icon = PhotoImage(file = rel_path("book.png"))
    label = Label(root, image = icon, width =400,height =400)
    label.place(relx=0.1,rely=0.3)

    heading = Label(text = "Select one of the Options below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    creation = Button(root,text = "4. Acquisition",height = 2,font = ("Arial Bold",30),command=sequence(lambda: root.destroy(), BookAcquisitionPage))
    creation.place(x= 700, y =260)

    t1 = Label(root,text = "Book Acquisition",font=("Arial Bold",20))
    t1.place(x = 1000, y=285)

    deletion = Button(root,text = "5. Withdrawal",height = 2,font = ("Arial Bold",30), command=sequence(lambda: root.destroy(), BookWithdrawalPage))
    deletion.place(x= 700, y = 460)

    t2 = Label(root,text = "Book Withdrawal",font=("Arial Bold",20))
    t2.place(x = 1000, y=485)

    button = Button(root,text = "Back to Main Menu",font = ("Arial Bold",12),height = 4,width =150, command=sequence(lambda: root.destroy(), MainMenuPage))
    button.place(x = 150, y = 670)
            
    root.mainloop()

def BookAcquisitionPage():

    def BookAcquisition():

        def BookAcquisite(accession, title, isbn, publisher, year, authors):
            connection = create_db_connection(host, user, password, database)

            success_message = 'New Book added in Library.'
            failure_message = 'Book already added; Duplicate, Missing or Incomplete fields.'

            q1 = f"""
            INSERT INTO Book (
                AccessionNO, 
                Year, 
                Title, 
                Publisher, 
                Isbn)
            VALUES ('{accession}', '{year}', '{title}', '{publisher}', '{isbn}');
            """
            execute_query(connection, q1, success_message, failure_message)

            for author in authors.split(","):
                q2 = f"""
                INSERT INTO BookAuthors (
                    Author, 
                    AccessionNO)
                VALUES ('{author}', '{accession}');
                """
                execute_query_no_error(connection, q2)

            connection.close()

            return

        def clear():
            AccessionNo_entry.delete(0, END)
            Year_entry.delete(0, END)
            Title_entry.delete(0, END)
            Publisher_entry.delete(0, END)
            ISBN_entry.delete(0, END)
            Author_entry.delete(0, END)

        try:
            con = create_db_connection(host, user, password, database)
            cur = con.cursor()
            cur.execute('SELECT AccessionNo FROM Book WHERE AccessionNo=%s', AccessionNo_entry)
            row = cur.fetchone()
            if row != None:
                messagebox.showerror('Error!', 'Book already added; Duplicate, Missing or Incomplete fields.')
            elif (AccessionNo_entry.get() == '' or Year_entry.get() == '' or Title_entry.get() == '' or Publisher_entry.get() == '' or ISBN_entry.get() == '' or Author_entry.get() == ''):
                messagebox.showerror('Error!', 'Book already added; Duplicate, Missing or Incomplete fields.')
            else:
                BookAcquisite(AccessionNo_entry.get(), Title_entry.get(), ISBN_entry.get(), Publisher_entry.get(), Year_entry.get(), Author_entry.get())
                clear()
        except Exception as e:
            messagebox.showerror('error!', f'Error due to {e}')

    root = Tk()
    root.geometry("1366x768")

    bg = PhotoImage(file = rel_path("bookshelf.png"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)

    root.title("BookCreation")
    heading = Label(text = "For New Book Acquisition, Please Enter Requested Information Below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    AccessionNo_text = Label(text = "Accession Number", font = ("Arial", 25), bg = "ivory3")
    Year_text = Label(text = "Publication Year", font = ("Arial", 25), bg = "ivory3")
    Title_text = Label(text = "Title", font = ("Arial", 25), bg = "ivory3")
    Publisher_text = Label(text = "Publisher", font = ("Arial", 25), bg = "ivory3")
    ISBN_text = Label(text = "ISBN", font = ("Arial", 25), bg = "ivory3")
    Author_text = Label(text = "Author", font = ("Arial", 25), bg = "ivory3")

    AccessionNo_text.place(x = 60, y = 180)
    Year_text.place(x = 60, y = 250)
    Title_text.place(x = 60, y = 320)
    Publisher_text.place(x = 60, y = 390)
    ISBN_text.place(x = 60, y = 460)
    Author_text.place(x = 60, y = 530)

    AccessionNo_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    Year_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    Title_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    Publisher_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    ISBN_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    Author_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)

    AccessionNo_entry.place(x = 360, y = 180)
    Year_entry.place(x = 360, y = 250)
    Title_entry.place(x = 360, y = 320)
    Publisher_entry.place(x = 360, y = 390)
    ISBN_entry.place(x = 360, y = 460)
    Author_entry.place(x = 360, y = 530)

    AddNewBook = Button(root, text = "Add New Book", width = 15, height = 4, font = ("Arial", 25), command = BookAcquisition)
    AddNewBook.place(x = 250, y = 600)

    BackToBooksMenu = Button(root, text = "Back to Books Menu", width = 15, height = 4, font = ("Arial", 25), command=sequence(lambda: root.destroy(), BookMenuPage))
    BackToBooksMenu.place(x = 950, y = 600)

    root.mainloop()

def BookWithdrawalPage(): 

    def BookWithdrawal():

        def getd():

            def get(accession):
                connection = create_db_connection(host, user, password, database)
                q1 = f"""
                SELECT *
                FROM Book
                WHERE AccessionNo = '{accession}';
                """
                q2 = f"""
                SELECT GROUP_CONCAT(BookAuthors.Author SEPARATOR', ') as "Authors"
                FROM BookAuthors
                WHERE AccessionNo = '{accession}';
                """
                
                record = read_query1(connection, q1)
                if record != None:
                    str = f'Accession Number : {record[0]} \n Year: {record[1]} \n Title: {record[2]} \n Publisher: {record[3]} \n ISBN: {record[4]}'
                    author = read_query(connection,q2)
                    str += f'\n Authors : {author[0][0]}'
                    return str
                else:
                    entry.delete(0, END)
                
                connection.close()

            return get(entry.get())

        def withdraw():

            def clear():
                entry.delete(0, END)

            def BookWithdrawal_(accession):
                connection = create_db_connection(host, user, password, database)

                #Check if borrowed
                q1 = f"""
                SELECT COUNT(*)
                FROM BookLoan
                WHERE AccessionNo = '{accession}';
                """

                #Check if reserved
                q2 = f"""
                SELECT COUNT(*)
                FROM Reservation
                WHERE AccessionNO = '{accession}';
                """

                #to withdrawal
                q3 = f"""
                DELETE FROM Book
                WHERE AccessionNO = '{accession}';
                """

                q4 = f"""
                SELECT * FROM Book
                WHERE AccessionNO = '{accession}';
                """

                success_message = "Book Withdrawed"
                failure_message = "Cannot withdraw book"

                if read_query1(connection, q4) == None:
                    clear()
                
                if read_query(connection, q1)[0][0] == 0:
                    if read_query(connection, q2)[0][0] == 0:
                        execute_query(connection, q3,success_message,failure_message)
                    else:
                        messagebox.showinfo("Error","Book is currently Reserved")
                else:
                    messagebox.showinfo("Error","Book is currently on Loan")
                
                connection.close()

                return     

            return BookWithdrawal_(entry.get())

        a=StringVar().set(getd())
        top = Toplevel(root)
        top.geometry("500x500")
        top.title("Comfirm Details of Loan")
        Label(top,text = getd(),font =("Arial Bold", 20)).place(x=100,y=80)
        back = Button(top,text = "Back to \n Withdraw function ",height = 1,bg = "DodgerBlue",font = ("Arial Bold",15), command=lambda: top.destroy())
        back.place(relx =0.6,rely=0.6)
        go = Button(top,text = "Withdraw Book",height = 1,bg = "DodgerBlue",font = ("Arial Bold",15),command =sequence(lambda: top.destroy(), withdraw))
        go.place(relx =0.1,rely=0.6)

    root = Tk()
    root.geometry("1366x768")

    bg = PhotoImage(file = rel_path("bookshelf.png"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)

    root.title("MembershipDeletion")
    l1 = Label(text = "To Remove Outdated Books From System, Please Enter Required Information Below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    l1.pack()

    t1 = Label(text = "Accession Number", font = ("Arial", 25), bg = "ivory3")
    t1.place(x = 60, y = 350)

    entry = Entry(bg = "ivory3", bd = 4, width = 100)
    entry.place(x = 360, y = 350)

    withdraw = Button(root, text = "Withdraw Book", width = 15, height = 4, font = ("Arial", 25), command=BookWithdrawal)
    withdraw.place(x = 250, y = 550)

    back = Button(root, text = "Back to Books Menu", width = 15, height = 4, font = ("Arial", 25),command=sequence(lambda: root.destroy(), BookMenuPage))
    back.place(x = 900, y = 550)

    root.mainloop()

# Book Loan

def BookLoanMenuPage():

    root = Tk()
    root.geometry("1366x768")
    root.title = "Functions"

    icon = PhotoImage(file = rel_path("loan.png"))
    label = Label(root, image = icon, width =400,height =400)
    label.place(relx=0.1,rely=0.3)

    heading = Label(text = "Select one of the Options below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    creation = Button(root,text = "6. Borrow",height = 2,font = ("Arial Bold",30),command=sequence(lambda: root.destroy(), BookBorrowingPage))
    creation.place(x= 700, y =260)

    t1 = Label(root,text = "Book Borrowing",font=("Arial Bold",20))
    t1.place(x = 1000, y=285)

    deletion = Button(root,text = "7. Return",height = 2,font = ("Arial Bold",30), command=sequence(lambda: root.destroy(), BookReturnPage))
    deletion.place(x= 700, y = 460)

    t2 = Label(root,text = "Book Returning",font=("Arial Bold",20))
    t2.place(x = 1000, y=485)

    button = Button(root,text = "Back to Main Menu",font = ("Arial Bold",12),height = 4,width =150, command=sequence(lambda: root.destroy(), MainMenuPage))
    button.place(x = 150, y = 670)
            
    root.mainloop()

def BookBorrowingPage():

    def get(accession,id_):
        connection = create_db_connection(host, user, password, database)
        q1 = f"""
        SELECT *
        FROM Book
        WHERE AccessionNo = '{accession}';
        """
        q2 = f"""
        SELECT *
        FROM Member
        WHERE MembershipID = '{id_}';
        """
        
        record = read_query1(connection, q1)
        if record != None:
            str = f'Accession Number : {record[0]} \n Title: {record[2]} '
            record = read_query1(connection,q2)
            str += f'\n Borrow Date : {date.today()} \n Due Date : {date.today() + timedelta(days =14)}'
            str += f'\n Membership ID: {id_} \n Member Name： {record[1]}'
            
            return str
        
        connection.close()

    def getd():
        return get(entry2.get(),entry1.get())


    def BookBorrowing(acc, id):
        connection = create_db_connection(host, user, password, database)

        #Check if book loaned
        q1 = f"""
        SELECT COUNT(*)
        FROM BookLoan
        WHERE AccessionNO = '{acc}';
        """

        #If loaned
        q11 = f"""
        SELECT *
        FROM BookLoan
        WHERE AccessionNO = '{acc}';
        """

        #Check if member load quota exceed
        q2 = f"""
        SELECT COUNT(*)
        FROM BookLoan
        WHERE MembershipID = '{id}';
        """

        #Check if member has outstanding fines
        q3 = f"""
        SELECT COUNT(*)
        FROM fine
        WHERE MembershipID = '{id}';
        """

        #Check for all reservations
        q4 = f"""SELECT MembershipID
        FROM Reservation
        WHERE AccessionNO = '{acc}';
        """

        #DELETE RESERVATION
        q41 = f"""
        DELETE FROM Reservation
        WHERE AccessionNO = '{acc}';
        """

        #Borrow successfully
        q5 = f"""INSERT INTO BOOKLOAN
        VALUES("{acc}", "{id}",curdate(),NULL,date_add(CURDATE(), INTERVAL 14 DAY))
        """
        success_message = "Book Borrowed Successful"
        failure_message = "Book does not exist"

        if read_query(connection, q1)[0][0] == 0:
            if read_query(connection, q2)[0][0] < 2:
                if read_query(connection, q3)[0][0] == 0:
                    if len(read_query(connection, q4)) == 0:
                        execute_query(connection, q5,success_message,failure_message)
                    else:
                        if id in map(lambda x: x[0], read_query(connection, q4)):
                            execute_query(connection, q5,success_message,failure_message)
                            execute_query(connection, q41,success_message,failure_message)
                        else:
                            messagebox.showinfo("Book in reservation for other member.")
                else:
                    messagebox.showinfo("Error!","Member has outstanding fines.")
            else:
                messagebox.showinfo("Error","Member loan quota exceeded.")
        else:
            loandate = read_query(connection, q11)[0][4]
            messagebox.showinfo("Error",f"Book currently on Loan until {loandate}.")

        connection.close()

        return
            
    def comfirm():
        
        top = Toplevel(root)
        top.geometry("500x500")
        top.title("Comfirm Details of Loan")
        Label(top,text = getd()
            ,font =("Arial Bold", 20)).place(x=100,y=80)
        back = Button(top,text = "Back to \n Loan function ",height = 1,bg = "DodgerBlue",font = ("Arial Bold",15), command=lambda: top.destroy())
        back.place(relx =0.6,rely=0.6)
        go = Button(top,text = "Borrow Book",height = 1,bg = "DodgerBlue",font = ("Arial Bold",15),command = sequence(borrow))
        go.place(relx =0.1,rely=0.6)

    def borrow():
        BookBorrowing(entry2.get(),entry1.get())

    root = Tk()
    root.geometry("1366x768")

    bg = PhotoImage(file = rel_path("bookshelf.png"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)

    root.title("BookBorrowing")
    l1 = Label(text = "To Borrow a Book, Please Enter Information Below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    l1.pack()

    t1 = Label(text = "Membership ID", font = ("Arial", 25), bg = "ivory3")
    t1.place(x = 60, y = 250)

    t2 = Label(text = "Accession Number", font = ("Arial", 25), bg = "ivory3")
    t2.place(x = 60, y = 350)

    entry1 = Entry(bg = "ivory3", bd = 4, width = 100)
    entry1.place(x = 360, y = 250)

    entry2 = Entry(bg = "ivory3", bd = 4, width = 100)
    entry2.place(x = 360, y = 350)

    withdraw = Button(root, text = "Borrow Book", width = 15, height = 4, font = ("Arial", 25), command=comfirm)
    withdraw.place(x = 250, y = 550)

    back = Button(root, text = "Back to Loans Menu", width = 15, height = 4, font = ("Arial", 25),command=sequence(lambda: root.destroy(), BookLoanMenuPage))
    back.place(x = 900, y = 550)

    root.mainloop()

def BookReturnPage():

    def BookReturn():
        connection = create_db_connection(host, user, password, database)
        acc = entry2.get()
        
        dated = entry1.get()
        y = int(dated.split(",")[0])
        m = int(dated.split(",")[1])
        d = int(dated.split(",")[2])
        rd = datetime.date(y,m,d)
        #get member id
        q0 = f"""
        SELECT * FROM BookLoan
        WHERE AccessionNO = '{acc}';
        """
        id = read_query(connection,q0)[0][1]


        
        #update the return date in bookloan
        q1 = f"""
        UPDATE BookLoan
        SET 
            ReturnDate = '{rd}'
        WHERE AccessionNO = '{acc}';
        """

        execute_query_no_error(connection, q1)

        

        #Check if member has outstanding fines
        q2 = f"""
        SELECT *
        FROM fine
        WHERE MembershipID = '{id}';
        """


        #DELETE BORROWING RECORD
        q3 = f"""
        DELETE FROM BookLoan
        WHERE AccessionNO = '{acc}';
        """

        #Check if get fined
        
        duedate = read_query(connection, q0)[0][4]

        returndate = rd

        days = (returndate-duedate).days

        
        

        if days > 0:
            if len(read_query(connection, q2)) == 0:
                q5 = f"""
                INSERT INTO Fine 
                VALUES ('{id}', NULL, '{days}')
                """
                execute_query_no_error(connection, q5)
                print("new fine created")
            else:
                #cumulative fines
                total = read_query(connection, q2)[0][2]+days
                q6 = f"""
                UPDATE Fine
                SET
                    Payment_due = '{total}'
                WHERE
                    MembershipID = '{id}';
                """
                execute_query_no_error(connection, q6)
                print("new fine cumulated")
            messagebox.showinfo(title='Error', 
                                message = "Book returned successfully but has fine")
            execute_query_no_error(connection, q3)
        else:
            
        
        
            execute_query_no_error(connection, q3)
            messagebox.showinfo(title='successful',message='Book returned')


        connection.close()
        return

    def confirm():
        connection = create_db_connection(host, user, password, database)
        if len(entry1.get()) == 0:
            messagebox.showinfo(title = 'Error!',message = "Please enter full information.")
            return
        if len(entry2.get()) == 0:
            messagebox.showinfo(title = 'Error!',message = "Please enter full information.")    
            return
        acc = entry2.get()
        date = entry1.get()
        y = int(date.split(",")[0])
        m = int(date.split(",")[1])
        d = int(date.split(",")[2])
        rd = datetime.date(y,m,d)

        #get member id
        q0 = f"""
        SELECT * FROM BookLoan
        WHERE AccessionNO = '{acc}';
        """

        if len(read_query(connection, q0)) == 0:
            messagebox.showinfo(title = "Error", message = "Book is not loaned")
            return
        else:
            id = read_query(connection, q0)[0][1]

        #get Book Title
        q1 = f"""
        SELECT Title FROM book
        WHERE AccessionNO = '{acc}';
        """
        title = read_query(connection,q1)[0][0]


        #get member name
        q2 = f"""
        SELECT Name FROM member
        WHERE MembershipID = '{id}';
        """
        name = read_query(connection,q2)[0][0]

        duedate = read_query(connection, q0)[0][4]

        returndate = rd

        fines = (returndate-duedate).days
        if fines<0:
            fines = 0

        top = Toplevel(root)
        top.geometry("500x500")
        top.title('Confirm Return Details To Be Correct')
        t1 = Label(top,font =("Arial Bold", 15),text=f'Accession Number: {acc} \n Book Title: {title} \n Membership ID: {id} \n Member Name: {name} \n Return Date: {date} \n Fine: ${fines}')
        t1.place(x=5,y = 40)

        b = Button(top, text = 'confirm return', height = 1,bg = "DodgerBlue",font = ("Arial Bold",15),command=sequence(lambda: top.destroy(), BookReturn))
        b.place(relx = 0.1,rely=0.8)

        back = Button(top,text = "Back to \n Return function ",height = 1,bg = "DodgerBlue",font = ("Arial Bold",15), command = top.destroy)
        back.place(relx =0.5,rely=0.8)
        return

    root = Tk()
    root.geometry("1366x768")

    bg = PhotoImage(file = rel_path("bookshelf.png"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)

    root.title("BookBorrowing")
    l1 = Label(text = "To Return a Book, Please Enter Information Below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    l1.pack()

    t1 = Label(text = "Return Date", font = ("Arial", 25), bg = "ivory3")
    t1.place(x = 60, y = 250)

    t2 = Label(text = "Accession Number", font = ("Arial", 25), bg = "ivory3")
    t2.place(x = 60, y = 350)

    entry1 = Entry(bg = "ivory3", bd = 4, width = 100)
    entry1.place(x = 360, y = 250)

    entry2 = Entry(bg = "ivory3", bd = 4, width = 100)
    entry2.place(x = 360, y = 350)

    withdraw = Button(root, text = "Return Book", width = 15, height = 4, font = ("Arial", 25), command=confirm)
    withdraw.place(x = 250, y = 550)

    back = Button(root, text = "Back to Loans Menu", width = 15, height = 4, font = ("Arial", 25),command=sequence(lambda: root.destroy(), BookLoanMenuPage))
    back.place(x = 900, y = 550)

    root.mainloop()


# Reservation

def ReservationMenuPage():

    root = Tk()
    root.geometry("1366x768")
    root.title = "Functions"

    icon = PhotoImage(file = rel_path("Reservationimg.png"))
    label = Label(root, image = icon, width =400,height =400)
    label.place(relx=0.1,rely=0.3)

    heading = Label(text = "Select one of the Options below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    creation = Button(root,text = "8. Reserve a Book",height = 2,font = ("Arial Bold",30),command=sequence(lambda: root.destroy(), BookReservationPage))
    creation.place(x= 600, y =260)

    t1 = Label(root,text = "Book Reservation",font=("Arial Bold",20))
    t1.place(x = 1000, y=285)

    deletion = Button(root,text = "9. Cancel Reservation",height = 2,font = ("Arial Bold",30), command=sequence(lambda: root.destroy(), BookCancelReservationPage))
    deletion.place(x= 600, y = 460)

    t2 = Label(root,text = "Reservation Cancellation",font=("Arial Bold",20))
    t2.place(x = 1000, y=485)

    button = Button(root,text = "Back to Main Menu",font = ("Arial Bold",12),height = 4,width =150, command=sequence(lambda: root.destroy(), MainMenuPage))
    button.place(x = 150, y = 670)
            
    root.mainloop()

def BookReservationPage():

    def clear():
        AccessionNo_entry.delete(0, END)
        MembershipID_entry.delete(0, END)
        ReserveDate_entry.delete(0, END)


    def confirm():

        def getd():

            def get(AccNo, MID, RD):
                connection = create_db_connection(host, user, password, database)

                #Book title
                q1 = f"""
                SELECT *
                FROM Book
                WHERE AccessionNo = '{AccNo}';
                """
                #Member Name
                q2 = f"""
                SELECT *
                FROM Member
                WHERE MembershipID = '{MID}';
                """
                record = read_query1(connection, q1)
                member = read_query1(connection, q2)
                if (type(record)!= None and type(member) != None):
                    str = f'Accession Number : {AccNo} \n Book Title: {record[2]} \n Membership ID: {MID} \n Member Name: {member[1]} \n Reserve Date: {RD}'
                    return str
                
                connection.close()

            return get(AccessionNo_entry.get(), MembershipID_entry.get(), ReserveDate_entry.get())


        def Reserve():
            dated = ReserveDate_entry.get()
            y = int(dated.split(",")[0])
            m = int(dated.split(",")[1])

 
            d = int(dated.split(",")[2])
            rd = datetime.date(y,m,d)


            def BookReserve(acc, id, reservedate):
                connection = create_db_connection(host, user, password, database)

                #Check if book loaned
                q1 = f"""
                SELECT COUNT(*)
                FROM BookLoan
                WHERE AccessionNO = '{acc}';
                """

                #Check if member reservation quota exceed
                q2 = f"""
                SELECT COUNT(*)
                FROM Reservation
                WHERE MembershipID = '{id}';
                """

                #Check if member has outstanding fines
                q3 = f"""
                SELECT *
                FROM Fine
                WHERE MembershipID = '{id}';
                """

                #Create reservation
                q4 = f"""INSERT INTO Reservation
                VALUES("{id}", "{acc}","{reservedate}")
                """

                success = "Book successfully reserved"
                failure = "Error"


                if read_query(connection, q1)[0][0] != 0:
                    if read_query(connection, q2)[0][0] < 2:
                        if len(read_query(connection, q3)) == 0:
                            execute_query(connection, q4,success,failure)
                            
                        else:
                            fine = read_query(connection, q3)[0][2]
                            messagebox.showerror('Error!', f"Member has outstandind fines of {fine}")
                    else:
                        messagebox.showerror('Error!', "Member currently has 2 Books on Reservation")
                else:
                    messagebox.showinfo("Message","Book can be loaned")
                       

                connection.close()
                return 

            return BookReserve(AccessionNo_entry.get(), MembershipID_entry.get(), rd)



        top = Toplevel(root)
        top.geometry("500x500")
        top.title("Comfirm Reservation Details To Be Correct")
        Label(top,text = getd(),font =("Arial Bold", 20)).place(x=100,y=80)
        back = Button(top,text = "Back to \n Reserve function ",height = 1,bg = "DodgerBlue",font = ("Arial Bold",15), command=lambda: top.destroy())
        back.place(relx =0.6,rely=0.6)
        go = Button(top,text = "Confirm Reservation",height = 1,bg = "DodgerBlue",font = ("Arial Bold",15),command =sequence(Reserve))
        go.place(relx =0.1,rely=0.6)




    root = Tk()
    root.geometry("1366x768")
    bg = PhotoImage(file = rel_path("bookshelf.png"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)


    root.title("BookReservation")
    heading = Label(text = "To Reserve a Book, Please Enter Requested Information Below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    AccessionNo_text = Label(text = "Accession Number", font = ("Arial", 25), bg = "ivory3")
    MembershipID_text = Label(text = "Membership ID", font = ("Arial", 25), bg = "ivory3")
    ReserveDate_text = Label(text = "Reserve Date", font = ("Arial", 25), bg = "ivory3")

    AccessionNo_text.place(x = 60, y = 200)
    MembershipID_text.place(x = 60, y = 300)
    ReserveDate_text.place(x = 60, y = 400)

    AccessionNo_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    MembershipID_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    ReserveDate_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)

    AccessionNo_entry.place(x = 360, y = 200)
    MembershipID_entry.place(x = 360, y = 300)
    ReserveDate_entry.place(x = 360, y = 400)

    ReserveBook = Button(root, text = "Reserve Book", width = 15, height = 4, font = ("Arial", 25), command = confirm)
    ReserveBook.place(x = 250, y = 600)



    BackToReservationsMenu = Button(root, text = "Back to Reservations Menu", width = 20, height = 4, font = ("Arial", 25), command = sequence(lambda: root.destroy(), ReservationMenuPage))
    BackToReservationsMenu.place(x = 950, y = 600)

    root.mainloop()

def BookCancelReservationPage():

    def confirm():

        def clear():
            AccessionNo_entry.delete(0, END)
            MembershipID_entry.delete(0, END)
            CancelDate_entry.delete(0, END)

        def ReserveCancel(acc, id, canceldate):#what is canceldate for, not needed here
            connection = create_db_connection(host, user, password, database)


            #Check if reservation exist
            q1 = f"""
            SELECT COUNT(*)
            FROM Reservation
            WHERE MembershipID = '{id}' AND AccessionNO = '{acc}';
            """

            #cancel reservation
            q2 = f"""
            DELETE FROM Reservation
            WHERE MembershipID = '{id}' AND AccessionNO = '{acc}';
            """
            success = "Reservation Cancelled"
            failure = "error"

            if read_query(connection, q1)[0][0] == 0:
                print("Member has no such reservation")
                messagebox.showerror('Error!', "Member has no such reservation")
            else:
                execute_query(connection, q2,success,failure)
               


            connection.close()
            return

        def CancelReservation():
            dated = CancelDate_entry.get()
            y = int(dated.split(",")[0])
            m = int(dated.split(",")[1])
  
 
            d = int(dated.split(",")[2])
            rd = datetime.date(y,m,d)

            ReserveCancel(
                AccessionNo_entry.get(), MembershipID_entry.get(), rd
            )

                
        def Cancel():
            return CancelReservation()

        def get(AccNo, MID, CD):
            connection = create_db_connection(host, user, password, database)

            #Book title
            q1 = f"""
            SELECT *
            FROM Book
            WHERE AccessionNo = '{AccNo}';
            """
            #Member Name
            q2 = f"""
            SELECT *
            FROM Member
            WHERE MembershipID = '{MID}';
            """
            record = read_query1(connection, q1)
            member = read_query1(connection, q2)
            if (type(record)!= None and type(member) != None):
                str = f'Accession Number : {AccNo} \n Book Title: {record[2]} \n Membership ID: {MID} \n Member Name: {member[1]} \n Cancellation Date: {CD}'
                return str
            
            connection.close()

        def getd():
            return get(AccessionNo_entry.get(), MembershipID_entry.get(), CancelDate_entry.get())


        top = Toplevel(root)
        top.geometry("500x500")
        top.title("Cancel Reservation Details To Be Correct")
        Label(top,text = getd(),font =("Arial Bold", 20)).place(x=100,y=80)
        back = Button(top,text = "Back to \n Cancel Reservation function ",height = 1,bg = "DodgerBlue",font = ("Arial Bold",15), command=top.destroy)
        back.place(relx =0.6,rely=0.6)
        go = Button(top,text = "Cancel Reservation",height = 1,bg = "DodgerBlue",font = ("Arial Bold",15),command = sequence(lambda: top.destroy(), Cancel))
        go.place(relx =0.1,rely=0.6)

    root = Tk()
    root.geometry("1366x768")
    bg = PhotoImage(file = rel_path("bookshelf.png"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)

    root.title("cancelReservation")
    heading = Label(text = "To Cancel a Reservation, Please Enter Requested Information Below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    AccessionNo_text = Label(text = "Accession Number", font = ("Arial", 25), bg = "ivory3")
    MembershipID_text = Label(text = "Membership ID", font = ("Arial", 25), bg = "ivory3")
    CancelDate_text = Label(text = "Cancel Date", font = ("Arial", 25), bg = "ivory3")

    AccessionNo_text.place(x = 60, y = 200)
    MembershipID_text.place(x = 60, y = 300)
    CancelDate_text.place(x = 60, y = 400)

    AccessionNo_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    MembershipID_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    CancelDate_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)

    AccessionNo_entry.place(x = 360, y = 200)
    MembershipID_entry.place(x = 360, y = 300)
    CancelDate_entry.place(x = 360, y = 400)

    CancelReserv = Button(root, text = "Cancel Reservation", width = 15, height = 4, font = ("Arial", 25), command = confirm)
    CancelReserv.place(x = 250, y = 600)

    BackToReservationsMenu = Button(root, text = "Back to Reservations Menu", width = 20, height = 4, font = ("Arial", 25), command = sequence(lambda: root.destroy(), ReservationMenuPage))
    BackToReservationsMenu.place(x = 950, y = 600)

    root.mainloop()


# Fine

def FineMenuPage():

    root = Tk()
    root.geometry("1366x768")
    root.title = "Functions"

    icon = PhotoImage(file = rel_path("fines.png"))
    label = Label(root, image = icon, width =400,height =400)
    label.place(relx=0.1,rely=0.3)

    heading = Label(text = "Select one of the Options below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    creation = Button(root,text = "10. Payment",height = 2,font = ("Arial Bold",30),command=sequence(lambda: root.destroy(), FinePaymentPage))
    creation.place(x= 700, y =260)

    t1 = Label(root,text = "Fine Payment",font=("Arial Bold",20))
    t1.place(x = 1000, y=285)

    button = Button(root,text = "Back to Main Menu",font = ("Arial Bold",12),height = 4,width =150, command=sequence(lambda: root.destroy(), MainMenuPage))
    button.place(x = 150, y = 670)
            
    root.mainloop()

def FinePaymentPage():

    def FinePayment():
        connection = create_db_connection(host, user, password, database)
        id = MembershipID_entry.get()
        date = PaymentDate_entry.get()
        y = int(date.split(",")[0])
        m = int(date.split(",")[1])
        d = int(date.split(",")[2])
        paydate = datetime.date(y,m,d)
        amount = int(PaymentAmount_entry.get())

        #Check if member has fine
        q1 = f"""
        SELECT *
        FROM fine
        WHERE MembershipID = '{id}';
        """


        q2 = f"""
        UPDATE Fine
        SET
            Payment_date = '{paydate}'
        WHERE
            MembershipID = '{id}';
        """

        q3 = f"""
        DELETE FROM Fine
        WHERE MembershipID = '{id}';
        """

        

        if len(read_query(connection, q1)) == 0:
            messagebox.showinfo(title = 'Error!',message = "Member has no fine.")
        else:
            if read_query(connection, q1)[0][2] != amount:
                messagebox.showinfo(title = 'Error!',message = "Incorrect fine payment amount")
            else:
                execute_query_no_error(connection, q2)
                execute_query_no_error(connection, q3)
                messagebox.showinfo(title="Successful", message="Fine payed")
                

        connection.close()
        return

    def confirm():
        connection = create_db_connection(host, user, password, database)
        if len(MembershipID_entry.get()) == 0:
            messagebox.showinfo(title = 'Error!',message = "Please enter full information.")
            return
        if len(PaymentDate_entry.get()) == 0:
            messagebox.showinfo(title = 'Error!',message = "Please enter full information.")    
            return
        if len(PaymentAmount_entry.get()) == 0:
            messagebox.showinfo(title = 'Error!',message = "Please enter full information.")
            return
        ID = MembershipID_entry.get()
        dated = PaymentDate_entry.get()
        y = int(dated.split(",")[0])
        m = int(dated.split(",")[1])
        d = int(dated.split(",")[2])
        rd = datetime.date(y,m,d)
        fines = 0

                #get payment due
        q0 = f"""
        SELECT *
        FROM fine
        WHERE MembershipID = '{ID}';
        """
        if len(read_query(connection, q0)) != 0:
            fines = read_query(connection, q0)[0][2]

        
        top = Toplevel(root)
        top.geometry("500x500")
        top.title('Please Confirm Details \n to Be Correct')
        t1=Label(top,font =("Arial Bold", 15),text=f'Payment Due: \n${fines}')
        t1.place(x=5,y = 40)
        t2=Label(top,font =("Arial Bold", 15),text=f'Member ID: \n{ID}')
        t2.place(x=250,y = 40)
        t3=Label(top,font =("Arial Bold", 15),text=f'Payment Date: \n{rd}')
        t3.place(x=250,y = 100)
        t4=Label(top,font =("Arial Bold", 15),text=f'Exact Fee Only')
        t4.place(x=5,y = 100)

        b = Button(top, text = 'Confirm Payment', height = 2,bg = "DodgerBlue",font = ("Arial Bold",15),command=FinePayment)
        b.place(relx = 0.1,rely=0.8)

        back = Button(top,text = "Back to \n Payment function ",height = 2,bg = "DodgerBlue",font = ("Arial Bold",15), command = top.destroy)
        back.place(relx =0.5,rely=0.8)
        
        return

    root = Tk()
    root.geometry("1366x768")
    bg = PhotoImage(file = rel_path("bookshelf.png"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)

    root.title("FinePayment")
    heading = Label(text = "To Pay a Fine, Please Enter Information Below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    MembershipID_text = Label(text = "Membership ID", font = ("Arial", 25), bg = "ivory3")
    PaymentDate_text = Label(text = "Payment Date", font = ("Arial", 25), bg = "ivory3")
    PaymentAmount_text = Label(text = "Payment Amount", font = ("Arial", 25), bg = "ivory3")

    MembershipID_text.place(x = 60, y = 200)
    PaymentDate_text.place(x = 60, y = 300)
    PaymentAmount_text.place(x = 60, y = 400)

    MembershipID_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    PaymentDate_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    PaymentAmount_entry = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)

    MembershipID_entry.place(x = 360, y = 200)
    PaymentDate_entry.place(x = 360, y = 300)
    PaymentAmount_entry.place(x = 360, y = 400)

    CancelReserv = Button(root, text = "Pay Fine", width = 15, height = 2, font = ("Arial", 25), command = confirm)
    CancelReserv.place(x = 250, y = 550)

    BackToReservationsMenu = Button(root, text = "Back to Fines Menu", width = 20, height = 2, font = ("Arial", 25), command = sequence(lambda: root.destroy(), FineMenuPage))
    BackToReservationsMenu.place(x = 750, y = 550)

    root.mainloop()


# Report

def ReportMenuPage():

    BUTTON_FONT = ("Arial Bold",30)
    TEXT_FONT = ("Arial Bold",20)

    
    root = Tk()
    root.geometry("1366x768")
    root.title = "Functions"

    icon = PhotoImage(file = rel_path("report.png")) 
    label = Label(root, image = icon, width =400,height =400)
    label.place(relx=0.05,rely=0.25)

    heading = Label(text = "Select one of the Options below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    # Button: Book Search
    button1 = Button(root, text="11. Book Search ", height=2, font = ("Arial Bold",30), command=sequence(lambda: root.destroy(), BookSearchPage))
    button1.place(relx= 0.39,rely=0.23)

    button1_info = Label(root,text = "Search for a book",font=("Arial Bold",20))
    button1_info.place(relx = 0.7, rely= 0.26)

    # Button: Books on Loan
    button2 = Button(root, text="12. Book on Loan", height=2, font = ("Arial Bold",30), command=sequence(lambda: root.destroy(), BookLoanReportPage))
    button2.place(relx= 0.39,rely=0.35)

    button2_info = Label(root,text = "Display all books on loan",font=("Arial Bold",20))
    button2_info.place(relx = 0.7, rely= 0.38)

    # Button: Books on Reservation
    button3 = Button(root, text = "13. Book on Reservation ",height = 2, font = ("Arial Bold",30), command=sequence(lambda: root.destroy(), BookReservationReportPage))
    button3.place(relx= 0.39,rely=0.47)

    button3_info = Label(root,text = "Display books reserved",font=("Arial Bold",20))
    button3_info.place(relx = 0.7, rely= 0.5)

    # Button: Outstanding Fines
    button4 = Button(root, text = "14. Outstanding Fines ",height = 2,font = BUTTON_FONT, command=sequence(lambda: root.destroy(), BookFinesReportPage))
    button4.place(relx= 0.39,rely=0.59)

    button4_info = Label(root,text = "Display oustanding fines",font=TEXT_FONT)
    button4_info.place(relx = 0.7, rely= 0.62)

    # Button: Books on Loan to Member
    button5 = Button(root,text = "15. Book on Loan to Member",height = 2,font = BUTTON_FONT, command=sequence(lambda: root.destroy(), BookLoanMemberSearchPage))
    button5.place(relx= 0.39,rely=0.71)

    button5_info = Label(root,text = "Display books on loan to you",font=TEXT_FONT)
    button5_info.place(relx = 0.76,rely= 0.74)

    # Bottom Frame / Button
    bottom_frame_button = Button(root, text = "Back to Main Menu ", font = ("Arial Bold",12), height = 4, width = 150, command=sequence(lambda: root.destroy(), MainMenuPage))
    bottom_frame_button.place(x = 150, y = 670)

    root.mainloop()

def BookSearchPage():

    def Search():
        connection = create_db_connection(host, user, password, database)
        title = entryNum.get()
        Authors= entrydate.get()
        ISBN = entryamt.get()
        pb = entrypb.get()
        py = entrypy.get()
        record = []
        acc="nno"


        q0 = f"""
        SELECT p.*, h.Author
        FROM book p
        INNER JOIN
        bookauthors h ON p.AccessionNO = h.AccessionNo
        WHERE p.Title LIKE '%{title}%';
        """

        q1 = f"""
        SELECT p.*, h.Author
        FROM bookauthors h
        INNER JOIN
        book p ON h.AccessionNO = p.AccessionNo
        WHERE h.AccessionNO IN (SELECT AccessionNO FROM bookauthors WHERE author LIKE '%{Authors}%');
        """


        q2 = f"""
        SELECT p.*, h.Author
        FROM book p
        INNER JOIN
        bookauthors h ON p.AccessionNO = h.AccessionNo
        WHERE p.ISBN = '{ISBN}';
        """

        q3 = f"""
        SELECT p.*, h.Author
        FROM book p
        INNER JOIN
        bookauthors h ON p.AccessionNO = h.AccessionNo
        WHERE p.Publisher LIKE '%{pb}%';
        """

        q4 = f"""
        SELECT p.*, h.Author
        FROM book p
        INNER JOIN
        bookauthors h ON p.AccessionNO = h.AccessionNo
        WHERE p.Year  = '{py}';
        """
        
        if len(title) != 0:
            if read_query(connection, q0) == None:
                messagebox.showinfo(title = "Error!",message = 'No Result ! \n Wrong information')
            if len(read_query(connection, q0)) != 0 :
                for b in read_query(connection, q0):
                    if b[0] in record:
                        ind = record.index(b[0])+5
                        aa = b[5]
                        record[ind] += f', {aa}'
                    else:
                        record += b


        if len(Authors) != 0:
            if read_query(connection, q1) == None:
                messagebox.showinfo(title = "Error!",message = 'No Result ! \n Wrong information')
            if len(read_query(connection, q1)) != 0:
              for b in read_query(connection, q1):
                    if b[0] in record:
                        ind = record.index(b[0])+5
                        aa = b[5]
                        record[ind] += f', {aa}'
                    else:
                        record += b

        if len(ISBN) != 0:
            if read_query(connection, q2) == None:
                messagebox.showinfo(title = "Error!",message = 'No Result ! \n Wrong information')
            if len(read_query(connection, q2)) != 0 :
                for b in read_query(connection, q2):
                    if b[0] in record:
                        ind = record.index(b[0])+5
                        aa = b[5]
                        record[ind] += f', {aa}'
                    else:
                        record += b

        if len(pb) != 0:
            if read_query(connection, q3) == None:
                messagebox.showinfo(title = "Error!",message = 'No Result ! \n Wrong information')
                return 
            if len(read_query(connection, q3)) != 0 :
                for b in read_query(connection, q3):
                    if b[0] in record:
                        ind = record.index(b[0])+5
                        aa = b[5]
                        record[ind] += f', {aa}'
                    else:
                        record += b
            
        if len(py) != 0:
            if read_query(connection, q4) == None:
                messagebox.showinfo(title = "Error!",message = 'No Result ! \n Wrong information')
            if len(read_query(connection, q4)) != 0 :
                for b in read_query(connection, q4):
                    if b[0] in record:
                        ind = record.index(b[0])+5
                        aa = b[5]
                        record[ind] += f', {aa}'
                    else:
                        record += b
    
        top = Toplevel(root)
        top.geometry("900x800")
        top.title('Book Search Results')
        att = ['Accession Number', 'Year',  'Title', 'Publisher', 'ISBN', 'Authors']
        att+=record
        bl = iter(att)
        #rl = iter(record)
        columns = 6
        rows=int(len(record)/6)
        for r in range(rows+1):
            for c in range(columns):
                cell = Text(top, width=20,height=2)
                cell.grid(row=r,column=c)
                cell.insert("end",bl.__next__())

        button1 = Button(top, text="Back to Search Function", command=top.destroy)
        button1.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor='n')    
        return
    
    root = Tk()
    root.geometry("1366x768")
    bg = PhotoImage(file = rel_path("bookshelf.png"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)

    root.title("BookSearch")
    heading = Label(text = "Search based on one of the categories below:", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    labelNum = Label(text = "Title", font = ("Arial", 25), bg = "ivory3")
    labeldate = Label(text = "Authors", font = ("Arial", 25), bg = "ivory3")
    labelamt = Label(text = "ISBN", font = ("Arial", 25), bg = "ivory3")
    labelpb = Label(text = "Publisher", font = ("Arial", 25), bg = "ivory3")
    labelpy = Label(text = "Publication Year", font = ("Arial", 25), bg = "ivory3")

    labelNum.place(x = 60, y = 180)
    labeldate.place(x = 60, y = 250)
    labelamt.place(x = 60, y = 320)
    labelpb.place(x = 60, y = 390)
    labelpy.place(x = 60, y = 460)

    entryNum = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    entrydate = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    entryamt = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    entrypb = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)
    entrypy = Entry(textvariable = StringVar(), bg = "ivory3", bd = 4, width = 100)

    entryNum.place(x = 360, y = 180)
    entrydate.place(x = 360, y = 250)
    entryamt.place(x = 360, y = 320)
    entrypb.place(x = 360, y = 390)
    entrypy.place(x = 360, y = 460)

    button1 = Button(root, text = "Search Book", width = 15, height = 4, font = ("Arial", 25), command = Search)
    button1.place(x = 250, y = 600)

    button2 = Button(root, text = "Back to \n Reports Menu", width = 15, height = 4, font = ("Arial", 25), command=sequence(lambda: root.destroy(), ReportMenuPage))
    button2.place(x = 950, y = 600)

    root.mainloop()

def BookSearchResultsPage():

    root = Tk()
    root.title = "Functions"
    root.geometry("1366x768")

    label = Label(root, text="Book Search Results", font=LARGE_FONT)
    label.pack(pady=10,padx=10)

    button1 = Button(root, text="Back to Reports Menu", command=sequence(lambda: root.destroy(), ReportMenuPage))
    button1.pack()

    root.mainloop()

def BookLoanReportPage():

    def BookLoanReport():
    
        q1 = f"""
        SELECT Book.AccessionNO, Book.Title, GROUP_CONCAT(BookAuthors.Author SEPARATOR', ') as "Authors", Book.ISBN, Book.Publisher, Book.Year
        FROM BookAuthors
        LEFT JOIN Book
        ON Book.AccessionNO = BookAuthors.AccessionNO
        LEFT JOIN BookLoan
        ON Book.AccessionNO = BookLoan.AccessionNO
        WHERE Book.AccessionNO IN (SELECT AccessionNO FROM BookLoan)
        GROUP BY AccessionNO
        ORDER BY AccessionNO;
        """

        connection = create_db_connection(host, user, password, database)
        raw_data = read_query(connection, q1)
        list_data = output_to_list(raw_data)
        connection.close()

        return list_data

    root = Tk()
    root.title = "Functions"
    root.geometry("1366x768")

    REPORT_COLOUR = '#F9F7F7'
    TABLE_COLOUR = '#112D4E'
    FRAME_FONT = ("Arial Bold",40)
    TABLE_ODDROW_COLOUR = "#3F72AF"
    TABLE_EVENROW_COLOUR = "#DBE2EF"

    TABLE_COLUMNS = ("c1", "c2", "c3", "c4", "c5", "c6")
    COLUMNS_HEADER = (("Accession Number", 150), ("Title", 200), ("Authors", 300), ("ISBN", 150), ("Publisher", 150), ("Year", 50))
    

    main_frame = Frame(root, bg=REPORT_COLOUR, bd=5)
    main_frame.place(relx=0.5, rely=0.05, relwidth=0.85, relheight=0.85, anchor='n')

    main_frame_label = Label(main_frame, text="Books on Loan Report", font=FRAME_FONT, bg=REPORT_COLOUR)
    main_frame_label.place(relx=0.5, rely=0, relwidth=1, relheight=0.2, anchor='n')

    table_frame = Frame(main_frame, bg=TABLE_COLOUR, bd=5)
    table_frame.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.5, anchor='n')

    style = ttk.Style()
    style.configure("Treeview", rowheight=40, background=TABLE_COLOUR)

    tree = ttk.Treeview(table_frame, column=TABLE_COLUMNS, show='headings', height=5)
    for index, (text, width) in enumerate(COLUMNS_HEADER):
        tree.column(f"# {index+1}", anchor=CENTER, width=width)
        tree.heading(f"# {index+1}", text=text)

    odd = True
    for row in BookLoanReport():
        if odd:
            tree.insert('', 'end', values=row, tags=('oddrow',))
            odd = False
        else:
            tree.insert('', 'end', values=row, tags=('evenrow',))
            odd = True

    tree.tag_configure('oddrow', background=TABLE_ODDROW_COLOUR)
    tree.tag_configure('evenrow', background=TABLE_EVENROW_COLOUR)

    tree.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    button1 = Button(main_frame, text="Back to Reports Menu", command=sequence(lambda: root.destroy(), ReportMenuPage))
    button1.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor='n')

    root.mainloop()

def BookReservationReportPage():

    def BookReservationReport():

        q1 = f"""
        SELECT Book.AccessionNO, Book.Title, Member.MembershipID, Member.Name
        FROM Reservation
        LEFT JOIN Book
        ON Reservation.AccessionNO = Book.AccessionNO
        LEFT JOIN Member
        ON Reservation.MembershipID = Member.MembershipID
        WHERE Book.AccessionNO IN (SELECT AccessionNO FROM Reservation);
        """

        connection = create_db_connection(host, user, password, database)
        raw_data = read_query(connection, q1)
        list_data = output_to_list(raw_data)
        connection.close()

        return list_data

    root = Tk()
    root.title = "Functions"
    root.geometry("1366x768")

    REPORT_COLOUR = '#F9F7F7'
    TABLE_COLOUR = '#112D4E'
    FRAME_FONT = ("Arial Bold",40)
    TABLE_ODDROW_COLOUR = "#3F72AF"
    TABLE_EVENROW_COLOUR = "#DBE2EF"

    TABLE_COLUMNS = ("c1", "c2", "c3", "c4")
    COLUMNS_HEADER = (("Accession Number", 150), ("Title", 200), ("Membership ID", 50), ("Name", 200))
    

    main_frame = Frame(root, bg=REPORT_COLOUR, bd=5)
    main_frame.place(relx=0.5, rely=0.05, relwidth=1, relheight=0.85, anchor='n')

    main_frame_label = Label(main_frame, text="Books on Reservation Report", font=FRAME_FONT, bg=REPORT_COLOUR)
    main_frame_label.place(relx=0.5, rely=0, relwidth=0.8, relheight=0.2, anchor='n')

    table_frame = Frame(main_frame, bg=TABLE_COLOUR, bd=5)
    table_frame.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.5, anchor='n')

    style = ttk.Style()
    style.configure("Treeview", rowheight=40, background=TABLE_COLOUR)

    tree = ttk.Treeview(table_frame, column=TABLE_COLUMNS, show='headings', height=5)
    for index, (text, width) in enumerate(COLUMNS_HEADER):
        tree.column(f"# {index+1}", anchor=CENTER, width=width)
        tree.heading(f"# {index+1}", text=text)

    odd = True
    for row in BookReservationReport():
        if odd:
            tree.insert('', 'end', values=row, tags=('oddrow',))
            odd = False
        else:
            tree.insert('', 'end', values=row, tags=('evenrow',))
            odd = True

    tree.tag_configure('oddrow', background=TABLE_ODDROW_COLOUR)
    tree.tag_configure('evenrow', background=TABLE_EVENROW_COLOUR)

    tree.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    button1 = Button(main_frame, text="Back to Reports Menu", command=sequence(lambda: root.destroy(), ReportMenuPage))
    button1.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor='n')

    root.mainloop()

def BookFinesReportPage():

    def BookFineReport():
 
        q1 = f"""
        SELECT Member.MembershipID, Member.Name, Member.Faculty, Member.PhoneNumber, Member.EmailAddress
        FROM Fine
        LEFT JOIN Member
        ON Fine.MembershipID = Member.MembershipID
        WHERE Member.MembershipID IN (SELECT MembershipID FROM Fine);
        """

        connection = create_db_connection(host, user, password, database)
        raw_data = read_query(connection, q1)
        list_data = output_to_list(raw_data)
        connection.close()

        return list_data

    root = Tk()
    root.title = "Functions"
    root.geometry("1366x768")

    REPORT_COLOUR = '#F9F7F7'
    TABLE_COLOUR = '#112D4E'
    FRAME_FONT = ("Arial Bold",40)
    TABLE_ODDROW_COLOUR = "#3F72AF"
    TABLE_EVENROW_COLOUR = "#DBE2EF"

    TABLE_COLUMNS = ("c1", "c2", "c3", "c4", "c5")
    COLUMNS_HEADER = (("Membership ID", 100), ("Name", 200), ("Faculty", 100), ("Phone Number", 100), ("Email Address", 200))
    

    main_frame = Frame(root, bg=REPORT_COLOUR, bd=5)
    main_frame.place(relx=0.5, rely=0.05, relwidth=0.85, relheight=0.85, anchor='n')

    main_frame_label = Label(main_frame, text="Members With Outstanding Fines", font=FRAME_FONT, bg=REPORT_COLOUR)
    main_frame_label.place(relx=0.5, rely=0, relwidth=1, relheight=0.2, anchor='n')

    table_frame = Frame(main_frame, bg=TABLE_COLOUR, bd=5)
    table_frame.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.5, anchor='n')

    style = ttk.Style()
    style.configure("Treeview", rowheight=40, background=TABLE_COLOUR)

    tree = ttk.Treeview(table_frame, column=TABLE_COLUMNS, show='headings', height=5)
    for index, (text, width) in enumerate(COLUMNS_HEADER):
        tree.column(f"# {index+1}", anchor=CENTER, width=width)
        tree.heading(f"# {index+1}", text=text)

    odd = True
    for row in BookFineReport():
        if odd:
            tree.insert('', 'end', values=row, tags=('oddrow',))
            odd = False
        else:
            tree.insert('', 'end', values=row, tags=('evenrow',))
            odd = True

    tree.tag_configure('oddrow', background=TABLE_ODDROW_COLOUR)
    tree.tag_configure('evenrow', background=TABLE_EVENROW_COLOUR)

    tree.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    button1 = Button(main_frame, text="Back to Reports Menu", command=sequence(lambda: root.destroy(), ReportMenuPage))
    button1.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor='n')

    root.mainloop()

def BookLoanMemberSearchPage():

    root = Tk()
    root.title = "Functions"
    root.geometry("1366x768")

    FRAME_COLOUR = '#80c1ff'
    FRAME_LABEL_COLOUR = "Light Cyan"
    BUTTON_COLOUR = 'DodgerBlue'

    FRAME_FONT = ("Arial Bold",40)
    BUTTON_FONT = ("Arial Bold", 20)
    TEXT_COLOUR = ("Light Blue")
    TEXT_FONT = ("Verdana", 20)

    bg = PhotoImage(file = rel_path("bookshelf.png"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)


    heading = Label(text = "Books on Loan to Member", fg = "black", bg = "ivory3", width = 500, height = 5, font = ("Arial", 25))
    heading.pack()

    MembershipID_text = Label(text = "Membership ID", font = ("Arial", 25), bg = "ivory3")
    MembershipID_text.place(x = 60, y = 350)

    MembershipID_entry = Entry(bg = "ivory3", bd = 4, width = 100)
    MembershipID_entry.place(x = 360, y = 350)

    def activate():
        id = MembershipID_entry.get()
        root.destroy()
        BookLoanMemberReportPage(id)

    DeleteMember = Button(root, text = "Search Member", width = 15, height = 4, font = ("Arial", 25), command=activate)
    DeleteMember.place(x = 250, y = 550)

    BackToMain = Button(root, text = "Back to \n Reports Menu", width = 15, height = 4, font = ("Arial", 25),command=sequence(lambda: root.destroy(), ReportMenuPage))
    BackToMain.place(x = 900, y = 550)

    root.mainloop()

def BookLoanMemberReportPage(id): 

    def BookLoanMemberReport(id):
 
        q1 = f"""
        SELECT Book.AccessionNO, Book.Title, GROUP_CONCAT(BookAuthors.Author SEPARATOR', ') as "Authors", Book.ISBN, Book.Publisher, Book.Year
        FROM BookAuthors
        LEFT JOIN Book
        ON Book.AccessionNO = BookAuthors.AccessionNO
        LEFT JOIN BookLoan
        ON Book.AccessionNO = BookLoan.AccessionNO
        WHERE BookLoan.MembershipID = '{id}'
        GROUP BY AccessionNO
        ORDER BY AccessionNO;
        """

        connection = create_db_connection(host, user, password, database)
        raw_data = read_query(connection, q1)
        list_data = output_to_list(raw_data)
        connection.close()

        return list_data

    root = Tk()
    root.title = "Functions"
    root.geometry("1366x768")

    REPORT_COLOUR = '#F9F7F7'
    TABLE_COLOUR = '#112D4E'
    FRAME_FONT = ("Arial Bold",40)
    TABLE_ODDROW_COLOUR = "#3F72AF"
    TABLE_EVENROW_COLOUR = "#DBE2EF"

    TABLE_COLUMNS = ("c1", "c2", "c3", "c4", "c5", "c6")
    COLUMNS_HEADER = (("Accession Number", 150), ("Title", 200), ("Authors", 300), ("ISBN", 150), ("Publisher", 150), ("Year", 50))
    
    main_frame = Frame(root, bg=REPORT_COLOUR, bd=5)
    main_frame.place(relx=0.5, rely=0.05, relwidth=0.85, relheight=0.85, anchor='n')

    main_frame_label = Label(main_frame, text="Books on Loan to Member", font=FRAME_FONT, bg=REPORT_COLOUR)
    main_frame_label.place(relx=0.5, rely=0, relwidth=1, relheight=0.2, anchor='n')

    table_frame = Frame(main_frame, bg=TABLE_COLOUR, bd=5)
    table_frame.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.5, anchor='n')

    style = ttk.Style()
    style.configure("Treeview", rowheight=40, background=TABLE_COLOUR)

    tree = ttk.Treeview(table_frame, column=TABLE_COLUMNS, show='headings', height=5)
    for index, (text, width) in enumerate(COLUMNS_HEADER):
        tree.column(f"# {index+1}", anchor=CENTER, width=width)
        tree.heading(f"# {index+1}", text=text)

    odd = True
    for row in BookLoanMemberReport(id):
        if odd:
            tree.insert('', 'end', values=row, tags=('oddrow',))
            odd = False
        else:
            tree.insert('', 'end', values=row, tags=('evenrow',))
            odd = True

    tree.tag_configure('oddrow', background=TABLE_ODDROW_COLOUR)
    tree.tag_configure('evenrow', background=TABLE_EVENROW_COLOUR)

    tree.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')


    button1 = Button(main_frame, text="Back to Reports Menu", command=sequence(lambda: root.destroy(), ReportMenuPage))
    button1.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor='n')

    root.mainloop()


