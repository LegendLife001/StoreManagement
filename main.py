#=======================================================    Imports & Import Handlings  ========================================================================
print("loading...")
import sys, os, webbrowser, datetime, random, warnings
# from warnings import WarningMessage
from tkinter import *   #using tkinter to make a graphic interface
from tkinter import font
import tkinter.messagebox
from tkinter import ttk
import glob
import _thread
def check_net(*args, **kwargs):    # to check if the system has internet connection
    import requests
    try:
        request = requests.get("https://www.google.com", timeout=3)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False
try:
    import tkcalendar
except:
    try:
        if check_net():       # if internet is working then install the library else prompt to get internet connection
            os.system('cmd /c "python -m pip install tkcalendar"')
            import tkcalendar
        else:
            if tkinter.messagebox.showerror("Network Error", "Python tkcalendar module is missing, which this program will download automatically.\nBut Kindly make sure that you have PROPER INTERNET CONNECTION for that to happen."):
                sys.exit(0)
    except:      # the error occurs then maybe the pip command is old.
        os.system('cmd /c "python -m pip install --upgrade pip')
        if check_net():       # if internet is working then install the library else prompt to get internet connection
            os.system('cmd /c "python -m pip install tkcalendar"')
            import tkcalendar
        else:
            if tkinter.messagebox.showerror("Network Error", "Python tkcalendar module is missing, which this program will download automatically.\nBut Kindly make sure that you have PROPER INTERNET CONNECTION for that to happen."):
                sys.exit(0)
#mysql importing and handling
try:
    import mysql.connector as sql
except:
    if check_net():
        # mysql installing from buildin setup or web, if not exists
        if tkinter.messagebox.askyesno("Error", "MySQL is not installed\nYou need to install MySQL\nWould you like to run MySQL installer?"):
            try:
                os.system(r".\additionals\mysql.msi")
            except:
                if tkinter.messagebox.askyesno("Query", "Sry, application N.A.\nDo you want to continue installing from web? \nKindly start program after installing mysql."):
                    webbrowser.open(r"https://dev.mysql.com/downloads/file/?id=508935")
            sys.exit(0)
        else:
            if tkinter.messagebox.askyesno("Query", "Do you want to continue installing from web? \nKindly start program after installing mysql."):
                webbrowser.open(r"https://dev.mysql.com/downloads/file/?id=508935")
            sys.exit(0)
    else:
        if tkinter.messagebox.showerror("Network Error", "Mysql.connector module is missing, which this program will download automatically.\nBut Kindly make sure that you have PROPER INTERNET CONNECTION for that to happen."):
            sys.exit(0)
print("imported")

#=======================================================  Login Window  ======================================================================================

#checking if the working table matches the ideal format
def check_table(*args, **kwargs):
    tables=[]
    ideal= ['id', 'product_name', 'stock', 'cp', 'sp', 'totalcp', 'totalsp', 'assumed_profit', 'vender', 'date', 'time']
    try:
        con= sql.connect(user=uname, passwd=pwd, database=dbName)
        cc= con.cursor()
    except:
        return "DB ERROR"
    try:
        cc.execute("desc inventory;")
    except:
        return "TABLE ERROR"
    for i in cc:
        tables.append(i[0].lower())
    if tables==ideal:
        return True
    else:
        return False
#default value
try:
    with open(r".\additionals\default_values.txt") as f:
        ah= f.read().split(",")
        pre_user= ah[0]
        pre_pwd=ah[1]
        pre_db=ah[2]
except:
    if tkinter.messagebox.askyesno("File Not Found Error", "the 'default_values.txt' file\nin the addtionals folder is Not Found!\nDo you want to continue without defaults?"):
        pre_user, pre_pwd, pre_db= "","",""
        pass
    else:
        tkinter.messagebox.showinfo("Info", "Kindly download latest version from github\nhttps://github.com/LegendLife001/StoreManagement.git")
#definition 
def main(entry, *args, **kwargs):     #first entry with database deatails; getting all details by user by entry widget
    #texts in the entry window
    title= Label(entry, text="Welcome to Store Manager by Raja", font=("Stylish",21, "bold"), bg="beige", fg="#EE8262")
    title.place(x=30, y=10)
    head_l= Label(entry, text="Enter Login Details", font=("Comic Sans", 22, "bold"), fg="#20bebe", bg="beige")
    head_l.place(x=130, y=60)
    uname_l = Label(entry, text="Enter User Name ", font=("Comic Sans MS", 14, "bold"), bg="beige")
    uname_l.place(x=0, y=120)
    pwd_l = Label(entry, text="Enter Root Password ", font=("Comic Sans MS", 14, "bold"), bg="beige")
    pwd_l.place(x=0, y=170)
    db_l = Label(entry, text="Enter Database Name ", font=("Comic Sans MS", 14, "bold"), bg="beige")
    db_l.place(x=0, y=220)
    table_l = Label(entry, text="You will be working on inventory table", font=("Comic Sans MS", 14, "bold"), bg="beige")
    table_l.place(x=0, y=270)
    info_l = Label(entry, text="(Hover for more info, )")
    sign_canvas= Canvas(entry, width=150, height=60, bg="beige", borderwidth=0)
    sign_canvas.place(x=385,y=440)
    try:
        sign_img= PhotoImage(file=".\\additionals\\sign.png")
        sign_canvas.create_image((0,0), image=sign_img, anchor='nw')
        entry.one = sign_img
    except:
        pass
    # create instance of Balloon
    global uname_e    #making the entries global to use in other functions
    uname_e= Entry(entry, width=25, font=("Comic Sans MS", 14, "bold"), borderwidth=3)
    uname_e.place(x=230, y=120)
    uname_e.insert(END, pre_user)   #pre-inserting wanted details
    
    global pwd_e
    pwd_e= Entry(entry, width=25, font=("Comic Sans MS", 14, "bold"), show="*", borderwidth=3)
    pwd_e.place(x=230, y=170)
    pwd_e.insert(END, pre_pwd)
    pwd_e.focus()
    global db_e
    db_e= Entry(entry, width=25, font=("Comic Sans MS", 14, "bold"), borderwidth=3)
    db_e.place(x=230, y=220)
    db_e.insert(END, pre_db)   
    global table_e
    table_e= "inventory"
    def func_default(*args, **kwargs):
        head_l.config(text="Enter Login Details")
        canvas_default.destroy() 
        btn_default.config(text="Set default values", command=fun_default)
    def fun_default(*args, **kwargs):
        global canvas_default
        canvas_default= Canvas(entry, width=550, height=270, bg="#00A6A6")
        head_l.config(text="Set Defaults")
        canvas_default.place(x=0, y=110)
        btn_default.config(text="Cancel", command=func_default)
        l1= Label(canvas_default, text="Default User", font=("Comic Sans MS", 14, "bold"), bg="#00A6A6").place(x=10,y=20 )
        l2= Label(canvas_default, text="Default Password", font=("Comic Sans MS", 14, "bold"), bg="#00A6A6").place(x=10, y=80)
        l3= Label(canvas_default, text="Default Database", font=("Comic Sans MS", 14, "bold"), bg="#00A6A6").place(x=10, y=140)
        e1= Entry(canvas_default, width=23, font=("ariel", 15, "bold"), borderwidth=2)
        e1.place(x=200, y=20)
        e1.focus()
        e2= Entry(canvas_default, width=23, font=("ariel", 15, "bold"), borderwidth=2)
        e2.place(x=200, y=80)
        e3= Entry(canvas_default, width=23, font=("ariel", 15, "bold"), borderwidth=2)
        e3.place(x=200, y=140)
        def dooit(*args, **kwargs):
            if tkinter.messagebox.askyesno("Confirmation", "Are you sure you want to\nchange the default valeus"):
                try:
                    with open(r".\additionals\default_values.txt", "w+") as f:
                        f.write(e1.get()+","+e2.get()+","+e3.get())
                        f.seek(0)
                        ahh= f.read().split(',')
                        uname_e.delete(0, END)
                        pwd_e.delete(0, END)
                        db_e.delete(0, END)
                        uname_e.insert(END, ahh[0])
                        pwd_e.insert(END, ahh[1]) 
                        db_e.insert(END, ahh[2])
                        func_default()
                except:
                    tkinter.messagebox.showerror("File Not Found Error", "the 'default_values.txt' in the addtionals folder is missing!")

        btn_set=Button(canvas_default, text="SET", font=("ariel", 15, "bold"), width=10, bg="darkorange", command=dooit)
        btn_set.place(x=330, y=200)

    btn_default= Button(entry, text="Set deafult values", width=20, bg="darkorange",font=("arial 12 bold"), cursor="hand2", command=fun_default, activebackground="OrangeRed3")
    btn_default.place(x=20, y=445) 

    def else_load(*args, **kwargs):
        #1.create a new database and table with the provided name
        def create_fun(*args, **kwargs):
            def createe(*args, **kwargs):
                eee= db_e.get()
                try:
                    conn= sql.connect(host="localhost", user=uname_e.get() , passwd=pwd_e.get())
                    c=conn.cursor()
                    c.execute(f"CREATE DATABASE {eee};")
                except sql.errors.DatabaseError:
                    tkinter.messagebox.showerror("DBName Error", "Database with same name already exists, enter a different name!")
                    return
                except:
                    tkinter.messagebox.showerror("DBName Error", "enter a different name!")
                    return
                c.execute(f"USE {eee}")
                c.execute(f"CREATE TABLE inventory (ID INT PRIMARY KEY auto_increment, Product_Name VARCHAR(100) NOT NULL, stock INT NOT NULL, cp INT NOT NULL, sp INT NOT NULL, totalcp INT, totalsp INT, assumed_profit INT, Vender VARCHAR(100), date Varchar(12), time Varchar(12));")
                conn.commit()
                global uname
                uname= user
                global pwd
                pwd= pwdd
                global dbName
                dbName= eee  #getting the database to work on
                global TableName
                TableName= "inventory"   #getting the name of the table wanted in the db
                tkinter.messagebox.showinfo("Success", "You have successfully created the database & Table!!!")
                entry.destroy()
            deff.destroy()
            btn_load.place_forget()
            btn_default.place_forget()
            entry.title("STORE MANAGEMENT-RAJA.create_database")
            db_e.delete(0, END)
            db_e.focus()
            btnn.config(command=createe, text="Create Database")
            btnn.bind("<Return>", createe)
            
        #2.To load database from a local path
        def load_fun(*args, **kwargs):
            entry.geometry("550x500+160+15")
            entry.title("STORE MANAGEMENT-RAJA.load_database")
            deff.destroy()
            #creating frame to overlay on the entry window to get new data
            fr= Frame(entry, height=620, width=550, bg="beige")
            fr.grid(row=0, column=0)
            #placing wanted widget on the frame
            title= Label(fr, text="Welcome to Store Manager by Raja", font=("Comic Sans", 22, "bold"), bg="beige", fg="#EE8262")
            title.place(x=30, y=10)
            head_l= Label(fr, text="LOAD DATABASE", font=("Comic Sans", 22, "bold"), fg="#20bebe", bg="beige")
            head_l.place(x=175, y=60)
            uname_l = Label(fr, text="Enter User Name ", font=("Comic Sans MS", 14, "bold"), bg="beige")
            uname_l.place(x=0, y=120)
            pwd_l = Label(fr, text="Enter Root Password ", font=("Comic Sans MS", 14, "bold"), bg="beige")
            pwd_l.place(x=0, y=170)
            db_l = Label(fr, text="Enter Database Name ", font=("Comic Sans MS", 14, "bold"), bg="beige")
            db_l.place(x=0, y=220)
            dbpath_l= Label(fr, text="Enter Database Path ", font=("Comic Sans MS", 14, "bold"), bg="beige")
            dbpath_l.place(x=0, y=270)
            dbpath_l2= Label(fr, text="(with extension)", font=("Comic Sans MS",11, "bold"), bg="beige")
            dbpath_l2.place(x=0, y=300)
            dbsaved_l= Label(fr, text="Or Select database", font=("Comic Sans MS",14, "bold"), bg="beige")
            dbsaved_l.place(x=0,y=330)
            uname1_e= Entry(fr, width=25, font=("Comic Sans MS", 14, "bold"), borderwidth=3)
            uname1_e.place(x=230, y=120)
            uname1_e.insert(END, pre_user)
            pwd1_e= Entry(fr, width=25, font=("Comic Sans MS", 14, "bold"), show="*", borderwidth=3)
            pwd1_e.place(x=230, y=170)
            pwd1_e.insert(END, pre_pwd)
            db1_e= Entry(fr, width=25, font=("Comic Sans MS", 14, "bold"), borderwidth=3)
            db1_e.place(x=230, y=220)
            dbpath_e= Entry(fr, width=35, font=("Arial", 12, "bold"), borderwidth=3)
            dbpath_e.place(x=220, y=280)
            #for selecting db
            aa=glob.glob(r".\database\*")
            var=[]
            for i in aa:
                var.append(i[11:])
            def callback_(sel, *args, **kwargs):
                dbpath_e.delete(0, END)
                dbpath_e.insert(END, ".\database"+f"\{sel}")
            value_inside = StringVar(fr)
            value_inside.set("Select a database")
            me= tkinter.OptionMenu(fr, value_inside, *var, command=callback_)
            me.place(x=230, y=310)
            me.config(bg="#EE6363")
            db1_e.focus()
            table1_e= "inventory"           
            def loadd(*args, **kwargs):     #sql query for loading data
                conn= sql.connect(user=uname1_e.get() , passwd=pwd1_e.get())
                try: 
                    query= open(dbpath_e.get()).read()
                    print(dbpath_e.get())
                except:
                    tkinter.messagebox.showerror("Error", "Path not found!")
                    return
                try:
                    c=conn.cursor()
                except:
                    tkinter.messagebox.showerror("Connection Error", "Cant connect to mysql")
                    return
                db1=db1_e.get()
                try:
                    print(db1)
                    c.execute(f"CREATE DATABASE {db1};")
                    c.execute(f"use {db1};")
                except:
                    tkinter.messagebox.showerror("Name Error", "Database name already exists\nKindly enter proper name")
                    c.execute(f"drop database {db1}")
                    return
                c.execute(query)
                global uname
                uname= uname1_e.get()
                global pwd
                pwd= pwd1_e.get()
                global dbName
                dbName= db1_e.get()
                global TableName
                TableName= table1_e
                #checking format
                a= check_table()
                if a==True:
                    pass
                else:
                    tkinter.messagebox.showerror("Error", "Inventory format doesnt match!\nKindly select proper formatted database\nor create new")
                    conn= sql.connect(user=uname , passwd=pwd)
                    cur= conn.cursor()
                    cur.execute(f"drop database {dbName};")
                    return
                tkinter.messagebox.showinfo("Success", "Successfully loaded the database")
                entry.destroy()
                
            load_me= Button(fr, text="LOAD Database", width=25, height=2, bg="#20bebe",font=("arial 12 bold"), cursor="hand2", command=loadd)
            load_me.place(x=270, y=370)
            def close(*args, **kwargs):
                root1.destroy()
                sys.exit(0)
            close= Button(fr, text="Close", bg="brown", command=close, font=("arial 15 bold"), cursor="hand2").place(x=450, y=440)  
        
        user= uname_e.get()
        pwdd= pwd_e.get() 
        #window for choosing between option 1 & 2, i.e.create or load
        global deff
        deff=Toplevel()
        deff.focus()
        entry.eval(f'tk::PlaceWindow {str(deff)} center')  #placing the window at the center of screen
        try:
            deff.wm_iconbitmap(r".\additionals\icon.ico")  
        except:
            pass
        deff.config(bg="beige")
        deff.title("Load Database")
        deff.geometry("350x230")
        deff.resizable(False, False)
        inf= Label(deff, text="Database Does Not Exist \nIf you dont have a database you can,\nCreate a new database \nor Load from pre-saved databases",bg="beige" ,font=("Arial", 14, "bold"))
        inf.place(x=0, y=22)
        btn_createdb= Button(deff, text="Create", width=13, height=2, bg="#20bebe",font=("arial 10 bold"), cursor="hand2", command=create_fun)
        btn_createdb.place(x=60, y=130)
        btn_loaddb= Button(deff, text="Load", width=13, height=2, bg="#20bebe",font=("arial 10 bold"), cursor="hand2", command=load_fun)
        btn_loaddb.place(x=200, y=130)
        btn_loaddb= Button(deff, text="Close", width=12, bg="brown",font=("arial 10 bold"), cursor="hand2", command=lambda *args, **kwargs: deff.destroy())
        btn_loaddb.place(x=225, y=190)
        deff.mainloop()
    
    def run(*args, **kwargs):    #running the entered details at backend to open or create the neeedful
        try:
            conn= sql.connect(host="localhost", user=uname_e.get() , passwd=pwd_e.get())
            c= conn.cursor()
            q1= "show databases;"
            c.execute(q1)
            list=[]    #storing names of all the databases available in the device
            for i in c:
                list.append(i[0])
        except:
            tkinter.messagebox.showerror("Error", "MySQL Error\nYou might have entered wrong entries, Kindly review and start again.")
            return
        #checking if the database exists
        if db_e.get() in list:      #if yes then just storing the data in variables to use it
            global uname
            uname= uname_e.get()
            global pwd
            pwd= pwd_e.get()
            global dbName
            dbName= db_e.get()  #getting the database to work on
            global TableName
            TableName= table_e   #getting the name of the table wanted in the db
            a= check_table()
            if a==True:
                entry.destroy()
            elif a=="DB ERROR":
                tkinter.messagebox.showerror("Error", "Database Error\nEnter existing database")
                return
            elif a=="TABLE ERROR":
                tkinter.messagebox.showerror("Error", "Wrong Table")
                return
            else:
                tkinter.messagebox.showerror("Error", "Inventory format doesnt match!")
                return
        else:     #if db not exists then giving user 2 options to make the db
            else_load()
    def focusme(*args,**kwargs):
        btnn.focus()
    uname_e.bind("<Return>",  focusme)
    pwd_e.bind("<Return>",  focusme)
    db_e.bind("<Return>",  focusme)
    def close(*args, **kwargs):
        root1.destroy()
        sys.exit(0)      
    btnn= Button(entry, text="ENTER", width=25, height=2, bg="#20bebe",font=("arial 12 bold"), cursor="hand2", command=run, borderwidth=4,activebackground="OrangeRed3")
    btnn.place(x=270, y=326)    
    btn_load= Button(entry, text="Load Database", width=20, height=2, bg="silver",font=("arial 10 bold"), cursor="hand2", command=else_load, activebackground="OrangeRed3")
    btn_load.place(x=60, y=331)   
    # btnn.focus()
    btnn.bind("<Return>", run)
    close= Button(entry, text="Close", bg="brown", command=close, width=10, font=("arial 15 bold"), cursor="hand2").place(x=400, y=400)

#ENTRY WINDOW    
entry=Tk()
entry.title("STORE MANAGEMENT-RAJA.enter")  #putting title name of window
try:
    entry.wm_iconbitmap(r".\additionals\icon.ico")      #title icon
except:
    pass
entry.geometry("550x500+160+15")            #size of window in pixels
entry.configure(background="beige")       
entry.resizable(False, False)        #making the window Non-extendable 

def on_closing(*args, **kwargs):   #CLOSING the window by X button on title bar 
    if tkinter.messagebox.askokcancel("Close Tabs", "Are you sure to close the main window?"):
        root1.destroy()
        sys.exit(0)
entry.protocol("WM_DELETE_WINDOW", on_closing)   #closing window by X button on title bar
def welcome(*args, **kwargs):
    print("\n```Welcome to Raja Store Management System```\n\t\tHave fun:)")
#_thread.start_new_thread(welcome,())
ent=main(entry)
entry.mainloop()

#======================================================MAIN WINDOW=================================================================
#creating workspace frames and functionalities for each workspace in functions (accessed using buttons)

#getting all the ids to make the id for the next stock addition item
def get_ids(*args, **kwargs):
    conn= sql.connect(host="localhost", user=uname, passwd=pwd, database=dbName)
    c=conn.cursor()
    c.execute(f"select ID from {TableName} order by id;")
    global ids_list
    ids_list=[]
    x= c.fetchall()
    if x!=[]:
        for i in x:
            ids_list.append(i[0])  
    else:
        ids_list.append(0)
    global ids_len
    ids_len= int(len(ids_list))
get_ids()

def stock_addition(*args, **kwargs):     #stock addition section to add data in the db
    try:
        left.pack_forget()
    except:
        pass
    try:
        can_mod.place_forget()
    except:
        pass
    #button plaining
    headbtn1.config(bg="#88BDBC", cursor="arrow", command=passs, state="disabled")
    headbtn2.config(bg="#FFC58B", cursor="hand2", command=stock_modify, state="normal")
    headbtn0.config(bg="#FFC58B", cursor="hand2", command=bill_btn, state="normal")
    #class for the section
    class Stock_addition:           #running Stock_addition class when stock_addition button is called
        def __init__(self, root,*args, **kwargs):
            root1.title("STORE MANAGEMENT-RAJA.Addition")
            try:
                self.conn= sql.connect(host="localhost", user=uname, passwd=pwd, database=dbName)
            except:
                tkinter.messagebox.showerror("Error", "Kindly enter correct details")
            canvas= Frame(root, width=765, height=600, bg="#88BDBC")
            canvas.place(x=0, y=83)
            global can_add
            can_add= canvas
            self.master=canvas     #making the window in self
            master= self.master
            dt_1= Label(master, text="Date\t     Time", font=('Courier', 13, 'bold'), bg="#88BDBC").place(x=10,y=500)
            def clock(*args, **kwargs):
                try:
                    now = datetime.datetime.now()
                    dt= now.strftime("%Y-%m-%d | %H:%M:%S")
                    dt_2.config(text=dt)
                    dt_2.after(1000, clock)
                except:
                    return
            dt_2= Label(master, text="", font=('Courier', 13, 'bold'), bg="#88BDBC")
            dt_2.place(x=10,y=525)
            clock()
            def back(*args, **kwargs):
                root1.title("STORE MANAGEMENT-RAJA.Billing")
                root1.geometry("1260x645")
                center(root1) 
                master.destroy()
                left.pack(side=LEFT)
                headbtn1.config(bg="#FFC58B", cursor="hand2", command=stock_addition, state="normal")
                headbtn2.config(cursor="hand2")
                headbtn0.config(bg="#88BDBC", cursor="arrow", command= passs, state="disabled")
                right.pack(side=RIGHT) 
                try:
                    btn.destroy()
                except:
                    pass
            def close(*args, **kwargs):
                closer()
                root1.destroy()
                sys.exit(0)
            btn_close= Button(master, text="CLOSE", padx=20, pady=10, command=close, bg="brown", cursor="hand2")
            btn_close.place(x=580, y=500)
            btn_back= Button(master, text="Back", padx=20, pady=10, command=back, bg="brown", cursor="hand2")
            btn_back.place(x=480, y=500)
            self.heading= Label(master, text="Add to the database", font=("arial 40 bold"), fg="darkblue", bg="#88BDBC").place(x=90, y=0)
            #checking if there is any id left
            self.notcon=0
            self.break_id=0
            get_ids()
            self.check_id()
            if self.break_id!=0:
                #labels for the window
                self.ID_l= Label(master, text='Product ID will be {}'.format(self.break_id), font=("arial 15 bold"), fg="tomato", bg="#88BDBC")
                self.ID_l.place(x=100,y=80)
            else:
                #labels for the window
                self.ID_l= Label(master, text='Product ID will be {}'.format(int(ids_list[-1])+1), font=("arial 15 bold"), fg="tomato", bg="#88BDBC")
                self.ID_l.place(x=100,y=80)
            global ID_l
            ID_l= self.ID_l
            self.name_l= Label(master, text='Enter Product Name ', font=("arial 19 bold"), bg="#88BDBC").place(x=10,y=130)
            self.stock_l= Label(master, text='Enter stocks ', font=("arial 19 bold"), bg="#88BDBC").place(x=10,y=180)
            self.cp_l= Label(master, text='Enter Cost Price ', font=("arial 19 bold"), bg="#88BDBC").place(x=10,y=230)
            self.sp_l= Label(master, text='Enter Selling Price ', font=("arial 19 bold"), bg="#88BDBC").place(x=10,y=280)
            self.vendor_l= Label(master, text='Enter Vendor Name ', font=("arial 19 bold"), bg="#88BDBC").place(x=10,y=330)
            #entries for all labels
            self.name_e= Entry(master, width=30, font=("arial 19 bold"), bg="#F0F8FF", borderwidth=4)
            self.name_e.place(x=270, y=130)
            self.name_e.focus()
            def focus(*args, **kwargs):
                self.stock_e.focus()
            self.name_e.bind("<Return>", focus)
            self.stock_e= Entry(master, width=30, font=("arial 19 bold"), bg="#F0F8FF", borderwidth=3)
            self.stock_e.place(x=270, y=180)
            self.cp_e= Entry(master, width=30, font=("arial 19 bold"), bg="#F0F8FF", borderwidth=3)
            self.cp_e.place(x=270, y=230)
            self.sp_e= Entry(master, width=30, font=("arial 19 bold"), bg="#F0F8FF", borderwidth=3)
            self.sp_e.place(x=270, y=280)
            self.vendor_e= Entry(master, width=30, font=("arial 19 bold"), bg="#F0F8FF", borderwidth=3)
            self.vendor_e.place(x=270, y=330)    
            self.stock_e.bind("<Return>", lambda *args, **kwargs: self.cp_e.focus())
            self.cp_e.bind("<Return>", lambda *args, **kwargs: self.sp_e.focus())
            self.sp_e.bind("<Return>", lambda *args, **kwargs: self.vendor_e.focus())
            #button to add the data
            self.btn_add= Button(master, text="Add to databse", width=23, height=2, bg="#20bebe",font=("arial 13 bold"), cursor="hand2", command= self.get_items)
            self.btn_add.place(x=430, y=390)
            self.vendor_e.bind("<Return>", lambda *args, **kwargs: self.btn_add.focus())
            self.btn_add.bind("<Return>", self.get_items)
            self.btn_clear= Button(master, text="Clear all", width=16, height=2, bg="lightgreen", font=("arial 10 bold"), cursor="hand2", command=self.clear)
            self.btn_clear.place(x=270, y=390)
            global check_meid
            check_meid= self.check_id()
        def check_id(self, *args, **kwargs):
            cc=[]
            if ids_len!=0:
                for i in range(1, int(ids_list[-1])+1):
                    cc.append(i)
            else:
                self.notcon=0
                self.break_id=0
                return 
            for x in range(len(cc)):
                try:
                    if ids_list[x]!=cc[x]:
                        self.break_id=cc[x]
                        self.notcon=0
                        break
                    else:
                        self.notcon=1
                        self.break_id=0
                except:
                    pass        
        
        def clear(self, *args, **kwargs):    #to clear the entry fields
            self.name_e.delete(0, END)
            self.stock_e.delete(0, END)
            self.cp_e.delete(0, END)
            self.sp_e.delete(0, END)
            self.vendor_e.delete(0, END)
        
        def get_items(self, *args, **kwargs):
            try:
                #getting entries
                self.name= self.name_e.get()
                self.stock= self.stock_e.get()
                self.cp= self.cp_e.get()
                self.sp= self.sp_e.get()
                self.vendor= self.vendor_e.get()
                #dynamic entries
                self.totalcp= int(self.cp) * int(self.stock)
                self.totalsp= int(self.sp) * int(self.stock)
                self.assumed_profit= int(self.totalsp - self.totalcp)
            except:
                if self.name=='' or self.stock=='' or self.cp=='' or self.sp=='' or self.vendor=="":
                #tkinter.messagebox.showerror("Error", "Please fill all entries!!!")
                    tkinter.messagebox.showerror("Error", "Kindly fill all entries")
                elif self.stock.isdigit()==False or self.cp.isdigit()==False or self.sp.isdigit()==False: 
                    tkinter.messagebox.showerror("Error", "stock, cp, sp must be a number")
                return
            
            if self.stock.isdigit() and self.cp.isdigit() and self.sp.isdigit(): 
                if self.notcon!=0:
                    cur=self.conn.cursor()
                    cur.execute(f"select Product_Name from {TableName};")
                    namess=[]
                    for i in cur:
                        namess.append(i[0].lower())
                    if self.name.lower() not in namess:
                        date=datetime.datetime.now().strftime("%d.%m.%Y")
                        time=datetime.datetime.now().strftime("%H:%M:%S")
                        query= "INSERT INTO {} (id, Product_Name, stock, cp, sp, totalcp, totalsp, assumed_profit, Vender, date, time) VALUES ({},'{}',{},{},{},{},{},{},'{}','{}','{}');".format(TableName,ids_list[-1]+1, self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, date, time)
                        cur.execute(query)
                        self.conn.commit()
                        tkinter.messagebox.showinfo("Success", "You have successfully added one item to the database!!!") 
                        get_ids()
                        self.ID_l.configure(text='Product ID will be {}'.format(ids_list[-1]+1))
                        self.clear()
                        self.name_e.focus()
                    else:
                        if tkinter.messagebox.askyesno("Error", f"{self.name} already exists!\nDo you want to add stock data with old details?"):
                            cur.execute(f"select id, stock, totalcp, totalsp, assumed_profit from {TableName} where Product_Name='{self.name}';")
                            a=cur.fetchall()[0]
                            id, quan,tcp, tsp, profit = a[0], a[1], a[2], a[3], a[4]
                            nquan= int(quan)+ int(self.stock)
                            ntcp= int(tcp)+self.totalcp
                            ntsp= int(tsp)+self.totalsp
                            nprofit= int(profit)+self.assumed_profit
                            cur.execute(f"update {TableName} SET stock={nquan}, totalcp={ntcp}, totalsp={ntsp}, assumed_profit={nprofit} where id={id};")
                            self.conn.commit()
                            self.clear()
                            self.name_e.focus()
                else:
                    cur=self.conn.cursor()
                    cur.execute(f"select Product_Name from {TableName};")
                    namess=[]
                    for i in cur:
                        namess.append(i[0].lower())
                    if self.name.lower() not in namess:
                        date=datetime.datetime.now().strftime("%d.%m.%Y")
                        time=datetime.datetime.now().strftime("%H:%M:%S")
                        query= "INSERT INTO {} (id, Product_Name, stock, cp, sp, totalcp, totalsp, assumed_profit, Vender, date, time) VALUES ({},'{}',{},{},{},{},{},{},'{}','{}','{}');".format(TableName,self.break_id, self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, date, time)
                        cur.execute(query)
                        self.conn.commit()
                        tkinter.messagebox.showinfo("Success", "You have successfully added one item to the database!!!") 
                        get_ids()
                        self.check_id()
                        if self.notcon!=0:
                            self.ID_l.configure(text='Product ID will be {}'.format(ids_list[-1]+1))
                            self.clear()
                        else:
                            self.ID_l.configure(text='Product ID will be {}'.format(self.break_id ))
                            self.clear()
                        self.name_e.focus()
                    else:
                        if tkinter.messagebox.askyesno("Error", f"{self.name} already exists!\nDo you want to add stock data with old details?"):
                            cur.execute(f"select id, stock, totalcp, totalsp, assumed_profit from {TableName} where Product_Name='{self.name}';")
                            a=cur.fetchall()[0]
                            id, quan,tcp, tsp, profit = a[0], a[1], a[2], a[3], a[4]
                            nquan= int(quan)+ int(self.stock)
                            ntcp= int(tcp)+self.totalcp
                            ntsp= int(tsp)+self.totalsp
                            nprofit= int(profit)+self.assumed_profit
                            cur.execute(f"update {TableName} SET stock={nquan}, totalcp={ntcp}, totalsp={ntsp}, assumed_profit={nprofit} where id={id};")
                            self.conn.commit()
                            self.clear()
                            self.name_e.focus()   
    b= Stock_addition(root1)

def stock_modify(*args, **kwargs):     #stock modification section to modify data in the db
    #clearing background canvases and frames for fresh space for this frame
    try:
        left.pack_forget()
    except:
        pass
    try:
        can_add.place_forget()
    except:
        pass
    #button plaining
    headbtn2.config(bg="#88BDBC", cursor="arrow", command=passs, state="disabled")
    headbtn1.config(bg="#FFC58B", cursor="hand2", command=stock_addition, state="normal")
    headbtn0.config(bg="#FFC58B", cursor="hand2", command=bill_btn, state="normal")
    
    class Stock_modify:                  #running Stock_Modify class when stock_modify button is called
        def __init__(self, root,*args, **kwargs):
            root1.title("STORE MANAGEMENT-RAJA.Modification")
            self.conn= sql.connect(host="localhost", user=uname, passwd=pwd, database=dbName)
            canvas= Frame(root, width=765, height=600, bg="#88BDBC")
            canvas.place(x=0, y=80)
            global can_mod
            can_mod= canvas
            self.master=canvas     #making the window in self
            master= self.master
            def close(*args, **kwargs):
                closer()
                root1.destroy()
                sys.exit(0)
            def back(*args, **kwargs):
                root1.geometry("1260x645")
                center(root1) 
                root1.title("STORE MANAGEMENT-RAJA.Billing")
                master.destroy()
                left.pack(side=LEFT)
                headbtn2.config(bg="#FFC58B", cursor="hand2", command=stock_modify, state="normal")
                headbtn1.config(cursor="hand2")
                headbtn0.config(bg="#88BDBC", cursor="arrow", command= passs, state="disabled")
                right.pack(side=RIGHT) 
                try:
                    btn.destroy()
                except:
                    pass
            btn1= Button(master, text="CLOSE", padx=20, pady=10, command=close, bg="brown", cursor="hand2")
            btn1.place(x=610, y=515)
            btn_back= Button(master, text="Back", padx=20, pady=10, command=back, bg="brown", cursor="hand2")
            btn_back.place(x=520, y=515)
            
            self.heading= Label(master, text="Modify database", font=("arial 40 bold"), fg="darkblue", bg="#88BDBC").place(x=180, y=0)
            #labels for the window
            self.searchl= Label(master, text="Select Product ID", font=("arial 19 bold"), bg="#88BDBC").place(x=22,y=80)

            self.name_l= Label(master, text='Product Name ', font=("arial 19 bold"), bg="#88BDBC").place(x=22,y=200)
            self.stock_l= Label(master, text='stocks ', font=("arial 19 bold"), bg="#88BDBC").place(x=22,y=250)
            self.cp_l= Label(master, text='Cost Price ', font=("arial 19 bold"), bg="#88BDBC").place(x=22,y=300)
            self.sp_l= Label(master, text='Selling Price ', font=("arial 19 bold"), bg="#88BDBC").place(x=22,y=350)
            self.vendor_l= Label(master, text='Vendor Name ', font=("arial 19 bold"), bg="#88BDBC").place(x=22,y=400)

            val=[]
            c= self.conn.cursor()
            c.execute("select id, Product_Name from inventory order by id")
            for i in c.fetchall():
                val.append(str(i[0])+": "+str(i[1]))
            #dropdown menu for viewing and selecting items
            global callme_modify
            def callme_modify(*args, **kwargs):
                selection=self.mc.get()
                if selection.isdigit():
                    self.searche=int(selection)
                    self.value.set('')
                    self.search()
                elif ":" in selection:
                    ind=selection.index(":")
                    sel= int(selection[:ind])
                    self.searche=int(sel)
                    self.value.set('')
                    self.search()
                else:
                    tkinter.messagebox.showerror("Error", "Invalid Entry")
            self.value = StringVar(master)
            self.mc= tkinter.ttk.Combobox(master, textvariable=self.value, values=val)
            self.mc.place(x=250, y=80)
            self.mc.bind("<<ComboboxSelected>>", callme_modify)
            self.mc.configure(width=22)
            self.mc.config(height=25)
            self.mc.config(font=("arial", 15, "bold"))
            self.mc.bind("<Return>", callme_modify)
            self.mc.focus()
            self.searche=0
            global modify_combovalue
            modify_combovalue=self.value

            #entries for all labels
            self.name_e= Entry(master, width=33, font=("arial 19 bold"), bg="#F0F8FF", borderwidth=3)
            self.name_e.place(x=210, y=200)  
            self.name_e.bind("<Control-Return>",  self.modify_items)   
            self.stock_e= Entry(master, width=33, font=("arial 19 bold"), bg="#F0F8FF", borderwidth=3)
            self.stock_e.place(x=210, y=250)
            self.stock_e.bind("<Control-Return>",  self.modify_items)   
            self.cp_e= Entry(master, width=33, font=("arial 19 bold"), bg="#F0F8FF", borderwidth=3)
            self.cp_e.place(x=210, y=300)
            self.cp_e.bind("<Control-Return>",  self.modify_items)   
            self.sp_e= Entry(master, width=33, font=("arial 19 bold"), bg="#F0F8FF", borderwidth=3)
            self.sp_e.place(x=210, y=350)
            self.sp_e.bind("<Control-Return>",  self.modify_items)   
            self.vendor_e= Entry(master, width=33, font=("arial 19 bold"), bg="#F0F8FF", borderwidth=3)
            self.vendor_e.place(x=210, y=400)    
            self.vendor_e.bind("<Control-Return>",  self.modify_items)   
            #button to add the data
            self.btn_search= Button(master, text="Search", width=20, height=2, bg="#20bebe", font=("arial 10 bold"), cursor="hand2",command=self.search)
            self.btn_search.place(x=505, y=120)
            self.btn_add= Button(master, text="Modify databse", width=25, height=2, bg="#20bebe",font=("arial 12 bold"), cursor="hand2", command= self.modify_items)
            self.btn_add.place(x=420, y=450)
            self.btn_clear= Button(master, text="Clear all", width=24, height=2, bg="lightgreen", font=("arial 10 bold"), cursor="hand2", command=self.clear)
            self.btn_clear.place(x=210, y=450)
            self.textt= Label(master, text="", font=("arial 19 bold"), bg="#88BDBC", fg="green")

        def clear(self, *args, **kwargs):
            self.name_e.delete(0, END)
            self.stock_e.delete(0, END)
            self.cp_e.delete(0, END)
            self.sp_e.delete(0, END)
            self.vendor_e.delete(0, END)  
            self.textt.place_forget()
            self.mc.focus()
        
        def search(self, *args, **kwargs):
            try:
                qq= "SELECT ID from {}".format(TableName)
                cur= self.conn.cursor()
                cur.execute(qq)
                lii=[]
                for i in cur:
                    lii.append(i[0])
                if self.searche=="":
                    tkinter.messagebox.showerror("Error", "Kindly enter product ID")
                    self.clear()
                elif self.searche in lii:
                    def prr(*args, **kwargs):
                        self.textt.place(x=120,y=150)
                        self.textt.config(text="Product ID: {}".format(self.searche))
                        self.idd= int(self.searche)
                        
                        query= "SELECT * FROM {} WHERE ID={}".format(TableName, self.idd)
                        cur=self.conn.cursor()
                        cur.execute(query)
                        for i in cur:
                            
                            self.a=i[1]
                            self.name_e.insert(END,self.a)
                            self.b= i[2]
                            self.stock_e.insert(END,self.b)
                            self.c=i[3]
                            self.cp_e.insert(END, self.c)
                            self.d=i[4]
                            self.sp_e.insert(END, self.d)
                            self.a1= i[5]
                            self.a2= i[6]
                            self.a3= i[7]
                            self.e=i[8]
                            self.vendor_e.insert(END, self.e)
                    if self.name_e.get()=="":
                        prr()
                    else:
                        self.clear()
                        prr()
                else:
                    tkinter.messagebox.showerror("Error!!!", "Product ID not present in database \nYou can add the product from the stock addition section.")
                    self.clear()
                    self.textt.place_forget()
                    # self.searche.delete(0, END)
                    # self.searche.focus()
            except ValueError:
                tkinter.messagebox.showerror("Error", "Enter valid ID")

        def modify_items(self, *args, **kwargs):
            try:
                #getting entries
                self.name= self.name_e.get()
                self.stock= self.stock_e.get()
                self.cp= self.cp_e.get()
                self.sp= self.sp_e.get()
                self.vendor= self.vendor_e.get()
                #dynamic entries
                self.totalcp= int(self.cp) * int(self.stock)
                self.totalsp= int(self.sp) * int(self.stock)
                self.assumed_profit= int(self.totalsp - self.totalcp)
            except:
                if self.name=='' or self.stock=='' or self.cp=='' or self.sp=='':
                    tkinter.messagebox.showerror("Error", "Please fill all entries!!!")
            #updating entries in sql if it is not empty
            if self.name!='' or self.stock!='' or self.cp!='' or self.sp!='':
                cur=self.conn.cursor()
                if self.a!=self.name:
                    query="UPDATE {} SET Product_name='{}' WHERE ID={}".format(TableName,self.name, self.idd)
                    cur.execute(query)
                    self.conn.commit()
                if self.b!=self.stock:
                    query="UPDATE {} SET stock={} WHERE ID={}".format(TableName,self.stock, self.idd)
                    cur.execute(query)
                    self.conn.commit()
                if self.c!=self.cp:
                    query="UPDATE {} SET cp={} WHERE ID={}".format(TableName, self.cp, self.idd)
                    cur.execute(query)
                    self.conn.commit()
                if self.d!=self.sp:
                    query="UPDATE {} SET sp={} WHERE ID={}".format(TableName, self.sp, self.idd)
                    cur.execute(query)
                    self.conn.commit()
                if self.a1!=self.totalcp:
                    query="UPDATE {} SET totalcp={} WHERE ID={} ".format(TableName, self.totalcp, self.idd)
                    cur.execute(query)
                    self.conn.commit()
                if self.a2!=self.totalsp:
                    query="UPDATE {} SET totalsp={} WHERE ID={} ".format(TableName, self.totalsp, self.idd)
                    cur.execute(query)
                    self.conn.commit()
                if self.a3!=self.assumed_profit:
                    query="UPDATE {} SET assumed_profit={} WHERE ID={}".format(TableName, self.assumed_profit, self.idd)
                    cur.execute(query)
                    self.conn.commit()
                if self.e!=self.vendor:
                    query="UPDATE {} SET Vender='{}' WHERE ID={} ".format(TableName, self.vendor, self.idd)
                    cur.execute(query)
                    self.conn.commit()
                tkinter.messagebox.showinfo("Success", "You have successfully modified one item to the database!!!")
                self.clear()
                self.textt.place_forget()
                #if called from stock review then entering to stock review
                try:
                    if 1 in xyzz:
                        stock_review()
                        xyzz.clear()
                except:
                    pass
    b= Stock_modify(root1)


def stock_review(*args, **kwargs):     #inside the stock addition section
    class Stock_review:                #running Stock_review class when stock_review button is called
        def __init__(self, root,*args, **kwargs):
            root1.title("STORE MANAGEMENT-RAJA.Stock_Review")
            self.conn= sql.connect(host="localhost", user=uname, passwd=pwd, database=dbName)
            root1.geometry("1100x650")
            center(root1)
            canvas= Frame(root, width=1100, height=650, bg="#88BDBC")
            canvas.place(x=0, y=0)
            self.master=canvas     #making the window in self
            master= self.master
            dt_1= Label(master, text="Date\t     Time", font=('Courier', 13, 'bold'), bg="#88BDBC").place(x=10,y=560)
            def clock(*args, **kwargs):            #running live date and time in the window
                try:
                    now = datetime.datetime.now()
                    dt= now.strftime("%Y-%m-%d | %H:%M:%S")
                    dt_2.config(text=dt)
                    dt_2.after(1000, clock)
                except:
                    return
            dt_2= Label(master, text="", font=('Courier', 13, 'bold'), bg="#88BDBC")
            dt_2.place(x=10,y=585)
            clock()

            c= self.conn.cursor()
            c.execute(f"use {dbName};")
            c.execute(f"select * from {TableName};")
            self.rows= []
            for x in c:
                self.rows.append(x)
            scrollbar= Scrollbar(master)
            scrollbar.place(x=1043, y=72, height=475)
            style = ttk.Style(master)
            style.theme_use('clam')
            self.trees= ttk.Treeview(master, selectmode="browse")
            self.profit= Label(master, text="", font=('ariel', 20, 'bold'), fg="darkred",bg="#88BDBC")
            self.profit.place(x=280, y=570)
            self.trees.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command= self.trees.yview)
            def close(*args, **kwargs):
                closer()
                root1.destroy()
                sys.exit(0)
            def back(*args, **kwargs):
                root1.title("STORE MANAGEMENT-RAJA.Billing")
                style = ttk.Style(root1)
                style.theme_use("classic")
                style.configure("Treeview", background="silver", fieldbackground="#55BDCA", foreground="black")
                style.map("Treeview", background=[('selected', 'aliceblue')])
                root1.geometry("1260x645")
                center(root1)
                right.pack(side=RIGHT) 
                try:
                    btn.destroy()
                except:
                    pass
                master.destroy() 
                bill_btn()
            btn1= Button(master, text="CLOSE", padx=20, pady=10, command=close, bg="brown", cursor="hand2")
            btn1.place(x=940, y=600)
            btn_back= Button(master, text="Back", padx=20, pady=10, command=back, bg="brown", cursor="hand2")
            btn_back.place(x=850, y=600)
            self.count=0
            self.setup()
            #function for sorting the table data
            def callback(selection, *args, **kwargs):
                if selection=="By Date":
                    sortbyoptions.place_forget()
                    ll1.config(text="Sort By Date")
                    dump_btn.place_forget()
                    now = datetime.datetime.now()
                    y= int(now.strftime("%Y"))
                    m= int(now.strftime("%m"))
                    d= int(now.strftime("%d"))
                    cal= tkcalendar.Calendar(master, selectmode="day", year=y, day=d, month=m)
                    cal.place(x=190, y=10)
                    def calp(*args, **kwargs):
                        cal.place(x=190, y=10)
                        btt2.config(text="Hide Calendar")
                        btt2.config(command=calf)
                    def calf(*args, **kwargs):
                        cal.place_forget()
                        btt2.config(text="Show Calendar")
                        btt2.config(command= calp)
                    def btt_fun(*args, **kwargs):
                        self.ll.place_forget()
                        cal.config(date_pattern='dd.MM.yyyy')
                        date=cal.get_date()
                        self.trees.delete(*self.trees.get_children())
                        c.execute(f"select * from {TableName} WHERE date='{date}'")
                        data=c.fetchall()
                        self.count=0
                        if data!=[]:
                            for i in data:
                                self.trees.insert(parent='', index='end', iid=self.count, text="", values=(f"{i[0]}",f"{i[1]}",f"{i[2]}", f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}", f"{i[7]}", f"{i[8]}", f"{i[9]}", f"{i[10]}"))
                                self.count+=1
                        else:
                            self.ll.config(text=f"No Data Found on {date}")
                            self.ll.place(x=400, y=300)
                        pro=[]
                        for i in self.trees.get_children():
                            pro.append(int(self.trees.item(i)['values'][7]))
                        self.profit.config(text=f"Total Assumed Profit= Rs.{sum(pro)}/-")
                    def callcan(*args, **kwargs):
                        self.trees.delete(*self.trees.get_children())
                        self.setup()
                        btt.destroy()
                        btt2.destroy()
                        cal.destroy()
                        btt3.destroy()
                        ll1.config(text="Sort By")
                        sortbyoptions.place(x=120, y=15)
                        dump_btn.place(x=930, y=10)
                        self.ll.place_forget()
                        self.count=0
                        value_inside.set("Select an option")
                    btt= Button(master, text="Sort", font=('ariel', 17, 'bold'), bg="lightgreen", command=btt_fun)
                    btt.place(x=480,y=10 )
                    btt2= Button(master, text="Hide Calendar",font=('ariel', 17, 'bold'), bg="lightgreen", command=calf)
                    btt2.place(x=600, y=10)
                    btt3= Button(master, text="Cancel Sort",font=('ariel', 17, 'bold'), bg="lightgreen", command=callcan)
                    btt3.place(x=820, y=10)

                elif selection=="By Month":
                    sortbyoptions.place_forget()
                    ll1.config(text="Sort By Month")
                    dump_btn.place_forget()
                    def callme(*args, **kwargs):
                        self.ll.place_forget()
                        sel= me.get()
                        try:
                            m=realm[val.index(sel.title())]
                        except ValueError:
                            return
                        self.trees.delete(*self.trees.get_children())
                        c.execute(f"select * from {TableName} where date like '%.{m}.{s.get()}'")
                        data = c.fetchall()
                        self.count=0
                        if data!=[] and data!=None:
                            for i in data:
                                self.trees.insert(parent='', index='end', iid=self.count, text="", values=(f"{i[0]}",f"{i[1]}",f"{i[2]}", f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}", f"{i[7]}", f"{i[8]}", f"{i[9]}", f"{i[10]}"))
                                self.count+=1
                        else:
                            nd=sel+" "+s.get()
                            self.ll.config(text=f"No Data Found for {nd}")
                            self.ll.place(x=300, y=300)
                        #updating total assumed profit
                        pro=[]
                        for i in self.trees.get_children():
                            pro.append(int(self.trees.item(i)['values'][7]))
                        self.profit.config(text=f"Total Assumed Profit= Rs.{sum(pro)}/-")
                        
                    value_in = StringVar(master)
                    val=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                    realm=['01','02','03','04', '05', '06', '07', '08', '09', '10', '11', '12']
                    me= tkinter.ttk.Combobox(master, textvariable=value_in, values=val, state='readonly')
                    me.place(x=210, y=20)
                    value_in.set("select month")
                    me.bind("<<ComboboxSelected>>", callme)
                    me.configure(width=20)
                    me.config(height=25)
                    me.config(font=("arial", 17, "bold"))
                    me.bind("<Return>", callme)
                    me.focus()
                    val_s= IntVar()
                    s= Spinbox(master, from_=2018, to=2025, textvariable=val_s, width=9, font=("Ariel", 15, "bold"))
                    s.place(x=530, y=20)
                    val_s.set("2021")
                    s.bind("<Return>", callme)
                    def callcanc(*args, **kwargs):
                        self.trees.delete(*self.trees.get_children())
                        value_inside.set("Select an option")
                        self.setup()
                        me.destroy()
                        s.destroy()
                        btc.destroy()
                        bts.destroy()
                        self.ll.place_forget()
                        self.count=0
                        pro=[]
                        for i in self.trees.get_children():
                            pro.append(int(self.trees.item(i)['values'][7]))
                        self.profit.config(text=f"Total Assumed Profit= Rs.{sum(pro)}/-")
                        ll1.config(text="Sort By")
                        sortbyoptions.place(x=120, y=15)
                        dump_btn.place(x=930, y=10)
                    bts= Button(master, text="SORT",font=('ariel', 17, 'bold'), bg="lightgreen", command=callme)
                    bts.place(x=700, y=10)
                    btc= Button(master, text="Cancel Sort",font=('ariel', 17, 'bold'), bg="lightgreen", command=callcanc)
                    btc.place(x=840, y=10)

                elif selection=="By Year":
                    sortbyoptions.place_forget()
                    ll1.config(text="Sort By Year")
                    dump_btn.place_forget()
                    def callme(*args, **kwargs):
                        self.ll.place_forget()
                        sel=s.get()
                        self.trees.delete(*self.trees.get_children())
                        c.execute(f"select * from {TableName} where date like '%{sel}'")
                        data = c.fetchall()                        
                        if data!=[] and data!=None:
                            for i in data:
                                self.trees.insert(parent='', index='end', iid=self.count, text="", values=(f"{i[0]}",f"{i[1]}",f"{i[2]}", f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}", f"{i[7]}", f"{i[8]}", f"{i[9]}", f"{i[10]}"))
                                self.count+=1
                        else:
                            self.ll.config(text=f"No Data Found for {sel}")
                            self.ll.place(x=300, y=300)
                        self.count=0
                        #updating total assumed profit
                        pro=[]
                        for i in self.trees.get_children():
                            pro.append(int(self.trees.item(i)['values'][7]))
                        self.profit.config(text=f"Total Assumed Profit= Rs.{sum(pro)}/-")
                        
                    val_s= IntVar()
                    s= Spinbox(master, from_=2018, to=2025, textvariable=val_s, width=9, font=("Ariel", 15, "bold"))
                    s.place(x=210, y=20)
                    s.bind("<Return>", callme)
                    val_s.set("2021")
                    s.focus()
                    def callcanc(*args, **kwargs):
                        self.trees.delete(*self.trees.get_children())
                        value_inside.set("Select an option")
                        self.setup()
                        s.destroy()
                        btc.destroy()
                        bts.destroy()
                        self.ll.place_forget()
                        self.count=0
                        pro=[]
                        for i in self.trees.get_children():
                            pro.append(int(self.trees.item(i)['values'][7]))
                        self.profit.config(text=f"Total Assumed Profit= Rs.{sum(pro)}/-")
                        ll1.config(text="Sort By")
                        sortbyoptions.place(x=120, y=15)
                        dump_btn.place(x=930, y=10)
                    bts= Button(master, text="SORT",font=('ariel', 17, 'bold'), bg="lightgreen", command=callme)
                    bts.place(x=400, y=10)
                    btc= Button(master, text="Cancel Sort",font=('ariel', 17, 'bold'), bg="lightgreen", command=callcanc)
                    btc.place(x=540, y=10)

                elif selection=="By Vender":
                    sortbyoptions.place_forget()
                    c.execute(f"select Vender from {TableName}")
                    ll1.config(text="Sort By Vender")
                    dump_btn.place_forget()
                    val=[]
                    for x in c:
                        if x[0] not in val:
                            val.append(x[0])
                    def callme(*args, **kwargs):
                        self.ll.place_forget()
                        sel= me.get().lower()
                        self.trees.delete(*self.trees.get_children())
                        c.execute(f"select * from {TableName} WHERE Vender='{sel}'")
                        data=c.fetchall()
                        self.count=0
                        if data!=[]:
                            for i in data:
                                self.trees.insert(parent='', index='end', iid=self.count, text="", values=(f"{i[0]}",f"{i[1]}",f"{i[2]}", f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}", f"{i[7]}", f"{i[8]}", f"{i[9]}", f"{i[10]}"))
                                self.count+=1
                        else:
                            self.ll.config(text=f"No Data Found for {sel}")
                            self.ll.place(x=400, y=300)
                        
                        pro=[]
                        for i in self.trees.get_children():
                            pro.append(int(self.trees.item(i)['values'][7]))
                        self.profit.config(text=f"Total Assumed Profit= Rs.{sum(pro)}/-")
                    def callcanc(*args, **kwargs):
                        self.trees.delete(*self.trees.get_children())
                        value_inside.set("Select an option")
                        self.setup()
                        me.destroy()
                        btc.destroy()
                        self.ll.place_forget()
                        self.count=0
                        pro=[]
                        for i in self.trees.get_children():
                            pro.append(int(self.trees.item(i)['values'][7]))
                        self.profit.config(text=f"Total Assumed Profit= Rs.{sum(pro)}/-")
                        ll1.config(text="Sort By")
                        sortbyoptions.place(x=120, y=15)
                        dump_btn.place(x=930, y=10)
                    value_in = StringVar(master)
                    me= tkinter.ttk.Combobox(master, textvariable=value_in, values=val)
                    me.place(x=280, y=10)
                    me.bind("<<ComboboxSelected>>", callme)
                    me.configure(width=20)
                    me.config(height=25)
                    me.config(font=("arial", 17, "bold"))
                    me.bind("<Return>", callme)
                    btc= Button(master, text="Cancel Sort",font=('ariel', 17, 'bold'), bg="lightgreen", command=callcanc)
                    btc.place(x=620, y=10)

            #sorting table data by 4 ways
            var=["By Date","By Month", "By Year", "By Vender"]
            value_inside = StringVar(master)
            value_inside.set("Select an option")
            ll1= Label(master, text="Sort By", font=('ariel', 17, 'bold'), bg="#88BDBC")
            ll1.place(x=20, y=15)
            self.ll= Label(master, text="", font=('ariel', 25, 'bold'), fg="red",bg="#88BDBC")
            sortbyoptions= tkinter.OptionMenu(master, value_inside, *var, command=callback)
            sortbyoptions.config(bg="lightgreen")
            sortbyoptions.place(x=120, y=15)
            #product deleting
            self.delete_btn= Button(master, text="Delete Product",font=('ariel', 14, 'bold'), bg="lightgreen", command=self.delete)
            self.delete_btn.place(x=890, y=550)

            #saving database in external folder
            def dumpme(*args, **kwargs):
                def cannn(*args, **kwargs):
                    dump_canvas.destroy()
                    e1.destroy()
                    dump_btn.config(text="Export Database", command=dumpme)
                dump_btn.config(text="Cancel", command= cannn)
                dump_canvas= Canvas(master, width=330, height=150, bg="#88B04B")
                dump_canvas.place(x=750, y=65)
                l1= Label(dump_canvas, text="Enter file name", font=('ariel', 15, 'bold'), bg="#88B04B")
                l1.place(x=10, y=10)
                e1= Entry(dump_canvas, width=25, font=('ariel', 15))
                e1.place(x=10, y=50)
                e1.focus()
                def dump(*args, **kwargs):
                    if " " not in e1.get():
                        try:
                            pathn=os.path.abspath(os.getcwd())
                            tkinter.messagebox.showinfo("Enter Pwd", "Go to the terminal and enter your mysql password to save it")
                            os.chdir("C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin")
                            os.system(f"mysqldump.exe -u root -p{pwd} store > {pathn}\\database\\{e1.get()}.sql")
                            tkinter.messagebox.showinfo("Success", "Successfully saved database\nin the database folder")
                            cannn()
                        except:
                            tkinter.messagebox.showerror("Error", "Can't locate mysqldump")
                            cannn()
                    else:
                        tkinter.messagebox.showerror("Error", "Invalid File Name\nFile name cannot have white spaces")
                        cannn()
                def thread_dump(*args, **kwargs):
                    _thread.start_new_thread(dump,())
                    
                b1= Button(dump_canvas, text="Save", font=('ariel', 17, 'bold'), bg="orange", command=thread_dump)
                b1.place(x=200,y=90)
            dump_btn= Button(master, text="Export Database", bg="orange",font=('ariel', 12), command=dumpme)
            dump_btn.place(x=930, y=10)

            # creating button for modifying selected item
            def modifyme(*args, **kwargs):
                x=self.trees.selection()
                xyzz.append(1)
                if x!=():
                    id= int(self.trees.item(x[0])["values"][0])
                    back()
                    stock_modify()
                    modify_combovalue.set(id)
                    callme_modify()
            self.modify_btn= Button(master, text="M\no\nd\ni\nf\ny",font=('ariel', 13, 'bold'), bg="lightgreen", command=modifyme)
            self.modify_btn.place(x=1060, y=418)

        def delete(self, *args, **kwargs):
            x=self.trees.selection()
            if x!=():
                if tkinter.messagebox.askyesno("Delete Forever", "Are you sure?\nThis is delete the product if forever"):
                    index=x[0]      
                    prof = int(self.trees.item(index)["values"][7])
                    id= int(self.trees.item(index)["values"][0])
                    c= self.conn.cursor()
                    c.execute(f"delete from {TableName} where id={id};")
                    self.conn.commit()
                    self.trees.delete(index)
                    new_profit=sum(self.pro)-prof
                    self.profit.config(text=f"Total Assumed Profit= Rs.{new_profit}/-")
                    # resetting the profit value
                    get_ids()
                    pro=[]
                    for i in self.trees.get_children():
                        pro.append(int(self.trees.item(i)['values'][7]))
                    self.profit.config(text=f"Total Assumed Profit= Rs.{sum(pro)}/-")
        
        def setup(self, *args, **kwargs):
            #create columns
            self.trees['columns']= ("ID", "name", "stock", "cp", "sp", "tcp", "tsp","profit", "vendor", "date", "time")
            #format colummn
            self.trees.column("#0", width=0, stretch=NO)
            self.trees.column("ID", anchor=W, width=10)
            self.trees.column("name", anchor=W, width=200)
            self.trees.column("stock", anchor=CENTER, width=90)
            self.trees.column("cp", anchor=CENTER, width=90)
            self.trees.column("sp", anchor=CENTER, width=90)
            self.trees.column("tcp", anchor=CENTER, width=90)
            self.trees.column("tsp", anchor=CENTER, width=90)
            self.trees.column("profit", anchor=CENTER, width=90)
            self.trees.column("vendor", anchor=CENTER, width=90)
            self.trees.column("date", anchor=CENTER, width=90)
            self.trees.column("time", anchor=CENTER, width=90)
            #create headings
            self.trees.heading("#0", text="")
            self.trees.heading("ID", text="ID", anchor=W)
            self.trees.heading("name", text="Product Name", anchor=W)
            self.trees.heading("stock", text="Quantity", anchor=CENTER)
            self.trees.heading("cp", text="Cost Price", anchor=CENTER)
            self.trees.heading("sp", text="Selling Price", anchor=CENTER)
            self.trees.heading("tcp", text="Total CP", anchor=CENTER)
            self.trees.heading("tsp", text="Total SP", anchor=CENTER)
            self.trees.heading("profit", text="Profit", anchor=CENTER)
            self.trees.heading("vendor", text="Vendor", anchor=CENTER)
            self.trees.heading("date", text="Date", anchor=CENTER)
            self.trees.heading("time", text="Time", anchor=CENTER)
            for i in self.rows:
                self.trees.insert(parent='', index='end', iid=self.count, text="", values=(f"{i[0]}",f"{i[1]}",f"{i[2]}", f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}", f"{i[7]}", f"{i[8]}", f"{i[9]}", f"{i[10]}"))
                self.count+=1
            style = ttk.Style(self.master)
            style.theme_use("clam")
            children= self.trees.get_children()
            style.configure("Treeview", background="lightblue", fieldbackground="#88BDBC", foreground="red")
            style.map("Treeview", background=[('selected', "green")])
            self.trees.place(x=20, y=70, height=480)
            self.pro=[]
            for i in children:
                self.pro.append(int(self.trees.item(i)['values'][7]))
            self.profit.config(text=f"Total Assumed Profit= Rs.{sum(self.pro)}/-")
    Stock_review(root1)


def sold_item_review(*args, **kwargs):      #inside the stock review section
    class Sold_item_review:                 #running Sold_item_review class when sold_item_review button is called
        def __init__(self, root,*args, **kwargs):
            root1.title("STORE MANAGEMENT-RAJA.Sold_Item_Review")
            self.conn= sql.connect(host="localhost", user=uname, passwd=pwd, database=dbName)
            root1.geometry("900x620")
            center(root1)
            canvas= Frame(root, width=900, height=620, bg="#88BDBC")
            canvas.place(x=0, y=0)
            self.master=canvas     #making the window in self
            master= self.master

            dt_1= Label(master, text="Date\t     Time", font=('Courier', 13, 'bold'), bg="#88BDBC").place(x=10,y=560)
            def clock(*args, **kwargs):         #running the live date and time in the window
                try:
                    now = datetime.datetime.now()
                    dt= now.strftime("%Y-%m-%d | %H:%M:%S")
                    dt_2.config(text=dt)
                    dt_2.after(1000, clock)
                except:
                    return
            dt_2= Label(master, text="", font=('Courier', 13, 'bold'), bg="#88BDBC")
            dt_2.place(x=10,y=585)
            clock()
            def close(*args, **kwargs):
                closer()
                root1.destroy()
                sys.exit(0)
            def back(*args, **kwargs):
                root1.title("STORE MANAGEMENT-RAJA.Billing")
                style = ttk.Style(root1)
                style.theme_use("classic")
                style.configure("Treeview", background="silver", fieldbackground="#55BDCA", foreground="black")
                style.map("Treeview", background=[('selected', 'aliceblue')])
                root1.geometry("1260x645") 
                center(root1)
                right.pack(side=RIGHT) 
                try:
                    btn.destroy()
                except:
                    pass
                master.destroy()
            btn1= Button(master, text="CLOSE", padx=20, pady=10, command=close, bg="brown", cursor="hand2")
            btn1.place(x=790, y=560)
            btn_back= Button(master, text="Back", padx=20, pady=10, command=back, bg="brown", cursor="hand2")
            btn_back.place(x=700, y=560)

            c= self.conn.cursor()
            c.execute(f"use {dbName};")
            c.execute(f"select * from transactions;")
            self.rows= []
            for x in c:
                self.rows.append(x)
            scrollbar= Scrollbar(master)
            scrollbar.place(x=723, y=75, height=470)
            style = ttk.Style(root1)
            style.theme_use('clam')
            self.trees= ttk.Treeview(master, selectmode="browse")
            self.trees.config(yscrollcommand=scrollbar.set)
            self.profitt= Label(master, text="", font=('ariel', 19, 'bold'), fg="darkred",bg="#88BDBC")
            self.profitt.place(x=245, y=570)
            scrollbar.config(command= self.trees.yview)
            self.count=0
            self.setup()
            #showing bill functions
            def hide_bill(*args, **kwargs):
                txt.destroy()
                root1.geometry("900x620+160+5")
                center(root1)
                canvas.config(width=900, height=620)
                btn_showbill.config(text="Show Bill", command=show_bill)
            def show_bill(*args, **kwargs):
                selc= self.trees.selection()
                if selc!=():
                    root1.geometry("1200x620+20+5")
                    center(root1)
                    canvas.config(width=1200, height=620)
                    global txt
                    txt= Text(master, width=53, height=27)
                    txt.place(x=750, y=50)
                    invoiceid=self.trees.item(int(selc[0]))["values"][7]
                    date=self.trees.item(int(selc[0]))["values"][5]
                    time=self.trees.item(int(selc[0]))["values"][6]
                    invoicedate=date[6:]+"-"+date[3:5]+"-"+date[:2]
                    dr=f".\\additionals\\Invoices\\{invoicedate}\\{invoiceid}.rtf"
                    def open_bill(*args, **kwargs):
                        try:
                            def inside(*args, **kwargs):
                                os.system(dr)
                            _thread.start_new_thread(inside,())
                        except:
                            tkinter.messagebox.showerror("Error", "Operation is not working")
                    open_btn= Button(master, text="Open Original Bill File", font=('ariel', 17, 'bold'), bg="lightgreen", command=open_bill)
                    open_btn.place(x=900, y=500)
                    try:
                        f= open(dr, "r")
                        read=f.readlines()
                        file=[]
                        for i in range(9, len(read)):
                            file.append(read[i][3:])
                        f.close()
                    except:
                        hide_bill()
                        tkinter.messagebox.showinfo("Error", "Bill Not Found!")
                        return
                    file.insert(-7, "\n")
                    txt.insert(END,"\t\tRaja Store Management\n")
                    txt.insert(END, "\t\t   Roorkee-India\n")
                    txt.insert(END, "\t\t phone-xxxxxxxxx\n")
                    txt.insert(END, "\t\t\tInvoice\n\n")
                    txt.insert(END, f"Date:{date}\t\t\t\tTime-{time}")
                    txt.insert(END, '''
================================================
Sno. Product Name			    Qty	Amount
================================================\n''')
                    for i in file:
                        txt.insert(END, i)
                    btn_showbill.config(text="Hide Bill", command= hide_bill)
            #showing bill
            btn_showbill= Button(master, text="Show Bill",font=('ariel', 17, 'bold'), bg="lightgreen", command= show_bill)
            btn_showbill.place(x=745, y=500)
            
            def fun_sortdate(*args, **kwargs):
                sortdate.place_forget()
                sortmonth.place_forget()
                sortyear.place_forget()
                now = datetime.datetime.now()
                y= int(now.strftime("%Y"))
                m= int(now.strftime("%m"))
                d= int(now.strftime("%d"))
                cal= tkcalendar.Calendar(master, selectmode="day", year=y, day=d, month=m)
                cal.place(x=30, y=10)
                def calp(*args, **kwargs):
                    cal.place(x=30, y=10)
                    btt2.config(text="Hide Calendar")
                    btt2.config(command=calf)
                def calf(*args, **kwargs):
                    cal.place_forget()
                    btt2.config(text="Show Calendar")
                    btt2.config(command= calp)
                def btt_fun(*args, **kwargs):
                    self.ll.place_forget()
                    cal.config(date_pattern='dd.MM.yyyy')
                    date=cal.get_date()
                    self.trees.delete(*self.trees.get_children())
                    c.execute(f"select * from transactions WHERE date='{date}'")
                    data=c.fetchall()
                    self.count=0
                    if data!=[]:
                        for i in data:
                            self.trees.insert(parent='', index='end', iid=self.count, text="", values=(f"{i[0]}",f"{i[1]}",f"{i[2]}", f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}", f"{i[7]}"))
                            self.count+=1
                    else:
                        self.ll.config(text=f"No Data Found on {date}")
                        self.ll.place(x=185, y=300)
                    pro=[]
                    check=[]
                    for i in self.trees.get_children():
                        inid= int(self.trees.item(i)['values'][7])
                        if inid not in check:
                            check.append(inid)
                            pro.append(int(self.trees.item(i)['values'][4]))
                    self.profitt.config(text=f"Total Earned Profit= Rs.{sum(pro)}/-")
                def callcan(*args, **kwargs):
                    self.trees.delete(*self.trees.get_children())
                    self.setup()
                    btt.destroy()
                    btt2.destroy()
                    cal.destroy()
                    btt3.destroy()
                    self.ll.place_forget()
                    sortdate.place(x=30, y=20)
                    sortmonth.place(x=230, y=20)
                    sortyear.place(x=430, y=20)
                    pro=[]
                    check=[]
                    for i in self.trees.get_children():
                        inid= int(self.trees.item(i)['values'][7])
                        if inid not in check:
                            check.append(inid)
                            pro.append(int(self.trees.item(i)['values'][4]))
                    self.profitt.config(text=f"Total Earned Profit= Rs.{sum(pro)}/-")
                    self.count=0
                btt= Button(master, text="Sort", font=('ariel', 17, 'bold'), bg="lightgreen", command=btt_fun)
                btt.place(x=300,y=10)
                btt2= Button(master, text="Hide Calendar",font=('ariel', 17, 'bold'), bg="lightgreen", command=calf)
                btt2.place(x=420, y=10)
                btt3= Button(master, text="Cancel Sort",font=('ariel', 17, 'bold'), bg="lightgreen", command=callcan)
                btt3.place(x=630, y=10)
            
            def fun_sortmonth(*args, **kwargs):
                sortdate.place_forget()
                sortmonth.place_forget()
                sortyear.place_forget()
                def callme(*args, **kwargs):
                    self.ll.place_forget()
                    sel= me.get()
                    try:
                        m=realm[val.index(sel.title())]
                    except ValueError:
                        return
                    self.trees.delete(*self.trees.get_children())    #deleting old data
                    c.execute(f"select * from transactions where date like '%.{m}.{s.get()}'")
                    data = c.fetchall()
                    self.count=0
                    if data!=[] and data!=None:    #for inserting new sorted data
                        for i in data:
                            self.trees.insert(parent='', index='end', iid=self.count, text="", values=(f"{i[0]}",f"{i[1]}",f"{i[2]}", f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}", f"{i[7]}"))
                            self.count+=1
                    else:
                        nd=sel+" "+s.get()
                        self.ll.config(text=f"No Data Found for {nd}")
                        self.ll.place(x=100, y=300)
                    #updating the total earned profit
                    pro=[]
                    check=[]
                    for i in self.trees.get_children():
                        inid= int(self.trees.item(i)['values'][7])
                        if inid not in check:
                            check.append(inid)
                            pro.append(int(self.trees.item(i)['values'][4]))
                    self.profitt.config(text=f"Total Earned Profit= Rs.{sum(pro)}/-")
                    
                value_in = StringVar(master)
                val=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                realm=['01','02','03','04', '05', '06', '07', '08', '09', '10', '11', '12']
                me= tkinter.ttk.Combobox(master, textvariable=value_in, values=val, state='readonly')
                me.place(x=40, y=20)
                me.bind("<<ComboboxSelected>>", callme)
                me.configure(width=20)
                me.config(height=25)
                me.config(font=("arial", 17, "bold"))
                me.bind("<Return>", callme)
                me.focus()
                val_s= IntVar()
                s= Spinbox(master, from_=2018, to=2025, textvariable=val_s, width=9, font=("Ariel", 15, "bold"))
                s.place(x=350, y=20)
                val_s.set("2022")
                def callcanc(*args, **kwargs):
                    self.trees.delete(*self.trees.get_children())
                    self.setup()
                    me.destroy()
                    s.destroy()
                    btc.destroy()
                    bts.destroy()
                    self.ll.place_forget()
                    self.count=0
                    pro=[]
                    check=[]
                    for i in self.trees.get_children():
                        inid= int(self.trees.item(i)['values'][7])
                        if inid not in check:
                            check.append(inid)
                            pro.append(int(self.trees.item(i)['values'][4]))
                    self.profitt.config(text=f"Total Earned Profit= Rs.{sum(pro)}/-")
                    sortdate.place(x=30, y=20)
                    sortmonth.place(x=230, y=20)
                    sortyear.place(x=430, y=20)
                bts= Button(master, text="SORT",font=('ariel', 17, 'bold'), bg="lightgreen", command=callme)
                bts.place(x=520, y=10)
                btc= Button(master, text="Cancel Sort",font=('ariel', 17, 'bold'), bg="lightgreen", command=callcanc)
                btc.place(x=660, y=10)

            def fun_sortyear(*args, **kwargs):
                sortdate.place_forget()
                sortmonth.place_forget()
                sortyear.place_forget()
                def callme(*args, **kwargs):
                    self.ll.place_forget()
                    sel=s.get()
                    self.trees.delete(*self.trees.get_children())
                    c.execute(f"select * from transactions where date like '%{sel}'")
                    data = c.fetchall()
                    self.count=0
                    if data!=[] and data!=None:
                        for i in data:
                            self.trees.insert(parent='', index='end', iid=self.count, text="", values=(f"{i[0]}",f"{i[1]}",f"{i[2]}", f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}", f"{i[7]}"))
                            self.count+=1
                    else:
                        self.ll.config(text=f"No Data Found for {sel}")
                        self.ll.place(x=100, y=300)
                    #updating total earned profit for the new sorted 
                    pro=[]
                    check=[]
                    for i in self.trees.get_children():
                        inid= int(self.trees.item(i)['values'][7])
                        if inid not in check:
                            check.append(inid)
                            pro.append(int(self.trees.item(i)['values'][4]))
                    self.profitt.config(text=f"Total Earned Profit= Rs.{sum(pro)}/-")
                    
                val_s= IntVar()
                s= Spinbox(master, from_=2018, to=2025, textvariable=val_s, width=9, font=("Ariel", 15, "bold"))
                s.place(x=60, y=20)
                s.bind("<Return>", callme)
                val_s.set("2021")
                s.focus()
                def callcanc(*args, **kwargs):
                    self.trees.delete(*self.trees.get_children())
                    self.setup()
                    s.destroy()
                    btc.destroy()
                    bts.destroy()
                    self.ll.place_forget()
                    self.count=0
                    pro=[]
                    check=[]
                    for i in self.trees.get_children():
                        inid= int(self.trees.item(i)['values'][7])
                        if inid not in check:
                            check.append(inid)
                            pro.append(int(self.trees.item(i)['values'][4]))
                    self.profitt.config(text=f"Total Earned Profit= Rs.{sum(pro)}/-")
                    sortdate.place(x=30, y=20)
                    sortmonth.place(x=230, y=20)
                    sortyear.place(x=430, y=20)
                bts= Button(master, text="SORT",font=('ariel', 17, 'bold'), bg="lightgreen", command=callme)
                bts.place(x=250, y=10)
                btc= Button(master, text="Cancel Sort",font=('ariel', 17, 'bold'), bg="lightgreen", command=callcanc)
                btc.place(x=390, y=10)

            sortdate= Button(master, text="Sort by Date",width=15, bg="lightgreen", font=("arial 13 bold"), cursor="hand2", command=fun_sortdate )
            sortdate.place(x=30, y=20)
            sortmonth= Button(master, text="Sort by Month",width=15, bg="lightgreen", font=("arial 13 bold"), cursor="hand2", command=fun_sortmonth )
            sortmonth.place(x=230, y=20)
            sortyear= Button(master, text="Sort by Year",width=15, bg="lightgreen", font=("arial 13 bold"), cursor="hand2", command=fun_sortyear )
            sortyear.place(x=430, y=20)
            self.ll= Label(master, text="", font=('ariel', 25, 'bold'), fg="red",bg="#88BDBC")
            pro=[]
            check=[]
            for i in self.trees.get_children():
                inid= int(self.trees.item(i)['values'][7])
                if inid not in check:
                    check.append(inid)
                    pro.append(int(self.trees.item(i)['values'][4]))
            self.profitt.config(text=f"Total Earned Profit= Rs.{sum(pro)}/-")

        def setup(self, *args, **kwargs):
            #create columns
            self.trees['columns']= ("ID", "name", "quan", "amount","BillProfit", "date", "time", "invoice")
            #format colummn
            self.trees.column("#0", width=0, stretch=NO)
            self.trees.column("ID", anchor=W, width=10)
            self.trees.column("name", anchor=W, width=170)
            self.trees.column("quan", anchor=CENTER, width=75)
            self.trees.column("amount", anchor=CENTER, width=105)
            self.trees.column("BillProfit", anchor=CENTER, width=90)
            self.trees.column("date", anchor=CENTER, width=80)
            self.trees.column("time", anchor=CENTER, width=80)
            self.trees.column("invoice", anchor=CENTER, width=90)

            self.trees.heading("#0", text="")
            self.trees.heading("ID", text="ID", anchor=W)
            self.trees.heading("name", text="Product Name", anchor=W)
            self.trees.heading("quan", text="Quantity", anchor=CENTER)
            self.trees.heading("amount", text="Recieved Amount", anchor=CENTER)
            self.trees.heading("BillProfit", text="Bill Profit", anchor=CENTER)
            self.trees.heading("date", text="Date", anchor=CENTER)
            self.trees.heading("time", text="Time", anchor=CENTER)
            self.trees.heading("invoice", text="Invoice ID", anchor=CENTER)
 
            for i in self.rows:
                self.trees.insert(parent='', index='end', iid=self.count, text="", values=(f"{i[0]}",f"{i[1]}",f"{i[2]}", f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}",f"{i[7]}"))
                self.count+=1
            style = ttk.Style(self.master)
            style.theme_use("clam")
            style.configure("Treeview", background="lightblue", fieldbackground="#88BDBC", foreground="red")
            style.map("Treeview", background=[('selected', "green")])
            self.trees.place(x=20, y=70, height=480)
    Sold_item_review(root1)


#starting with the main billing window
prodid, prodname, prodstock, prodprice, prodquan, prodcp=[],[],[],[],[],[]
class Billing:
    def __init__(self,root1,left, right, *args, **kwargs):
        self.conn= sql.connect(host="localhost", user=uname , passwd=pwd)
        c=self.conn.cursor()
        c.execute(f"use {dbName}")
        # getting all tables
        c.execute("show tables;")
        tbs=[]
        for i in c.fetchall(): 
            tbs.append(i[0])
        if "transactions" not in tbs:
            c.execute("Create table transactions(ID INT , Product_Name VARCHAR(100),Quantity INT,Received_Amount INT, bill_profit INT, date VARCHAR(12), time VARCHAR(12), invoice INT(10));")
            self.conn.commit()
        else:
            c.execute("desc transactions;")
            desc=[]
            for i in c.fetchall():
                desc.append(i[0])
            ideal=["ID", "Product_Name", "Quantity", "Received_Amount", "bill_profit", "date", "time", "invoice"]
            if ideal==desc:
                pass
            else:
                tkinter.messagebox.showerror("Format Error", "Your transaction table format is wrong\You have to drop it and create correct one.")
                tkinter.messagebox.showinfo("Confirmation", "This will delete your current data in transactions.")
                c.execute("drop table transactions;")
                c.execute("Create table transactions(ID INT , Product_Name VARCHAR(100),Quantity INT,Received_Amount INT, bill_profit INT, date VARCHAR(12), time VARCHAR(12), invoice INT(10));")
                self.conn.commit()
        self.root1= root1
        self.left=left
        self.right=right
        
        dt_1= Label(self.right, text="Date\t     Time", font=('Courier', 13, 'bold'), bg="#55BDCA")
        dt_1.place(x=240,y=10)
        def clock(*args, **kwargs):
            try:
                now = datetime.datetime.now()
                dt= now.strftime("%Y-%m-%d | %H:%M:%S")
                dt_2.config(text=dt)
                dt_2.after(1000, clock)
            except:
                return
        dt_2= Label(self.right, text="", font=('Courier', 13, 'bold'), bg="#55BDCA")
        dt_2.place(x=240,y=35)
        clock()
        headl= Label(self.left, text= "RAJA Store Management" ,  font=("arial 30 bold"), bg="#88BDBC", fg="darkblue")
        headl.place(x=10, y=90)
        headb= Label(self.left, text= "Billing" ,  font=("arial 28 bold"), bg="#88BDBC", fg="#B40505")
        headb.place(x=175, y=136)
        self.id= Label(self.left, text= "Select Product ID" ,  font=("arial 20 bold"), bg="#88BDBC")
        self.id.place(x=10, y=200)
        #selecting id from dropmenu  
        global val
        val=[]      
        def callme(*args, **kwargs):
            selection=self.me.get()
            if selection.isdigit():
                self.id_e=int(selection)
                self.searchid()
            elif ":" in selection:
                ind=selection.index(":")
                sel= int(selection[:ind])
                self.id_e=int(sel)
                #value_inside.set(sel)
                self.searchid()
            else:
                tkinter.messagebox.showerror("Error", "Invalid Entry")
        global val_fun
        def val_fun(*args, **kwargs):
            val.clear()
            conn= sql.connect(host="localhost", user=uname , passwd=pwd, database=dbName)
            c= conn.cursor()
            c.execute("select id, Product_Name from inventory order by id")
            for i in c.fetchall():
                val.append(str(i[0])+": "+str(i[1]))
            
            #dropdown menu for viewing items
            self.value_inside = StringVar(self.left)
            self.me= tkinter.ttk.Combobox(self.left, textvariable=self.value_inside, values=val)
            self.me.place(x=245, y=200)
            self.me.bind("<<ComboboxSelected>>", callme)
            self.me.configure(width=20)
            self.me.config(height=25)
            self.me.config(font=("arial", 17, "bold"))
            self.me.bind("<Return>", callme)
            self.me.focus()
            global bill_combobox
            bill_combobox= self.me
        val_fun()
        self.id_btn= Button(self.left, text="Search", width=20, height=2, bg="#20bebe", font=("arial 10 bold"), cursor="hand2", command=callme)
        self.id_btn.place(x=540, y=200)
        headr= Label(self.right, text= "Cart" , font=("arial 30 bold"), bg="#55BDCA", fg="yellow")
        headr.place(x=10, y=10)
                    
        self.pn= Label(self.left, text= "", font=("arial 17 bold"),fg="#FF7D40", bg="#88BDBC")
        self.pn.place(x=10, y=290)
        self.pv= Label(self.left, text= "", font=("arial 17 bold"),fg="#FF7D40", bg="#88BDBC")
        self.pv.place(x=500, y=290)
        self.pp= Label(self.left, text= "", font=("arial 17 bold"),fg="#FF7D40", bg="#88BDBC")
        self.pp.place(x=10, y=330)
        self.pq= Label(self.left, text= "", font=("arial 17 bold"),fg="#FF7D40", bg="#88BDBC")
        self.pq.place(x=10, y=370) 
        
        self.tc_r= Label(self.right, text="Total Cost:", font=("arial 25 bold"), bg="#55BDCA", fg="yellow")
        self.tc_r.place(x=130, y=600)
        self.rc= Label(self.right, text="", font=("arial 25 bold"), bg="#55BDCA", fg="yellow")
        self.rc.place(x=325, y=600)
        self.total=[]
        self.total_t=0
        def close_cart(*args, **kwargs):
            self.right.pack_forget()
            root1.geometry("800x642")
            center(root1)
            def show_cart(*args, **kwargs):
                btn.destroy()
                root1.geometry("1260x645")
                center(root1)
                self.right.pack(side=RIGHT)
            global btn
            btn= Button(root1, text="S\nH\nO\nW\n \nC\nA\nR\nT", height=24, font=("Ariel", 17), bg="#55BDCA", cursor="hand2", command=show_cart)
            btn.place(x=760, y=0)
        self.bac= Button(self.right, text="X", bg="#55BDCA",borderwidth=0, cursor="hand2",font=("ariel",25), fg="red", command=close_cart)
        self.bac.place(x=455, y=0)
        self.remove= Button(self.right, text="Remove Items",height=2, bg="#BCEE68", font=("arial 10 bold"), cursor="hand2", command=self.removeitem)
        self.remove.place(y=550, x=360)
        self.clear_cart= Button(self.right, text="Clear Cart",height=2, bg="#BCEE68", font=("arial 10 bold"), cursor="hand2", command=self.clear_cart)
        self.clear_cart.place(y=550, x=10)
        
        self.treeframe= Frame(self.right, width=500, height=470, bg='#55BDCA')
        self.treeframe.place(x=5, y=75)
        scrollbar= Scrollbar(self.treeframe)
        scrollbar.place(x=450, y=20, height=445)
        style = ttk.Style(self.treeframe)
        style.theme_use('classic') 
        #Treeview for showing cart items
        self.tree= ttk.Treeview(self.treeframe)
        style = ttk.Style(self.right)
        self.tree.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command= self.tree.yview)
        # set ttk theme to "clam" which support the fieldbackground option
        style.theme_use("classic")
        style.configure("Treeview", background="silver", fieldbackground="#55BDCA", foreground="black")
        style.map("Treeview", background=[('selected', 'aliceblue')])
        #create columns
        self.tree['columns']= ("Name", "Quan", "Price")
        #format colummn
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("Name", anchor=W, width=265, minwidth=180)
        self.tree.column("Quan", anchor=CENTER, width=90, minwidth=75)
        self.tree.column("Price", anchor=CENTER, width=90, minwidth=75)
        #create headings
        self.tree.heading("#0", text="")
        self.tree.heading("Name", text="Product Name", anchor=W)
        self.tree.heading("Quan", text="Quantity", anchor=CENTER)
        self.tree.heading("Price", text="Total Price", anchor=CENTER)
        self.tree.place(x=0, y=0, height=480)
        self.count=0
        self.x=0  
        self.bill= Button(self.left, text="Generate Bill",width=45, font=("arial", 18, "bold"), cursor="hand2", bg="#B40505",fg="white", command=self.gbill)
        self.bill.place(x=20, y=580)
        #for removing
        self.namee= []
        self.tpp=[]
        #CLOSE BUTTON  
        global closer
        def closer(*args, **kwargs):     # to clear the cart items if exists(so that stock is correct)
            for i in range(len(prodid)):
                self.detuptst(i)
        def close(*args, **kwargs):
            closer()
            root1.destroy()
            sys.exit(0)
        self.main_close_btn= Button(self.left, text="C\nL\nO\nS\nE", bg="brown", font=("arial 12 bold"), cursor="hand2", command=close)
        self.main_close_btn.place(x=0, y=460)
        self.main_close_btn.lift()
        def on_closing2(*args, **kwargs):   #CLOSING the window by X button on title bar 
            if tkinter.messagebox.askokcancel("Close Tabs", "Are you sure to close the main window?"):
                closer()
                root1.destroy()
                sys.exit(0)
        root1.protocol("WM_DELETE_WINDOW", on_closing2)   #closing window by X button on title bar
        #for updating stock in cart
        self.uptstock=0

    def searchid(self, *args, **kwargs):
        #getting all ids
        conn= sql.connect(host="localhost", user=uname , passwd=pwd, database=dbName)
        cur=conn.cursor()
        cur.execute("select id from {};".format(TableName))
        self.idss=[]
        for i in cur.fetchall(): 
            self.idss.append(i[0])
        try:
            if int(self.id_e) in self.idss:
                try:
                    self.showinfo.destroy()
                except:
                    pass
                self.showinfo= Canvas(self.left, width=760, bg="#88BDBC",bd=0, highlightthickness=0, relief='ridge')
                self.showinfo.place(x=0, y=244)
                self.main_close_btn.lift()
                def fun_cancel(*args, **kwargs):
                    btn_cancel.destroy()
                    self.showinfo.destroy()
                    self.value_inside.set("")
                    self.me.focus()
                global btn_cancel
                btn_cancel= Button(left, text="Cancel Item", bg="brown",width=15, font=("arial 12 bold"), cursor="hand2", command= fun_cancel)
                btn_cancel.place(x=500, y=485)
                btn_cancel.lift()
                # global
                self.pn= Label(self.showinfo, text= "", font=("arial 17 bold"),fg="darkorange", bg="#88BDBC")
                self.pn.place(x=10, y=40)
                self.pv= Label(self.showinfo, text= "", font=("arial 17 bold"),fg="darkorange", bg="#88BDBC")
                self.pv.place(x=500, y=40)
                self.pp= Label(self.showinfo, text= "", font=("arial 17 bold"),fg="darkorange", bg="#88BDBC")
                self.pp.place(x=10, y=80)
                self.pq= Label(self.showinfo, text= "", font=("arial 17 bold"),fg="darkorange", bg="#88BDBC")
                self.pq.place(x=10, y=120)
                q1= "select Product_Name, stock, sp, vender, cp from inventory where id={};".format(self.id_e)
                cur.execute(q1)
                for i in cur:
                    self.get_name= i[0]
                    self.get_stock= i[1]
                    self.get_price= i[2]
                    self.get_vender=i[3]
                    self.get_cp= i[4]
                    self.pid= Label(self.showinfo, text= "Product ID {}".format(self.id_e), font=("arial 17 bold"),fg="#3A00DE",bg="#88BDBC")
                    self.pid.place(x=10, y=10)
                    self.pn.configure(text="Product Name: {}".format(i[0]))
                    self.pv.configure(text= "(By {})".format(i[3]))
                    self.pp.configure(text=r"Selling Price: Rs.{} /- ".format(i[2]))
                    self.pq.configure(text="Available Quantity: {}".format(i[1]))
                self.quan= Label(self.showinfo, text= "Enter Quantity " ,  font=("arial 20 bold"), bg="#88BDBC").place(x=130, y=175)
                val_cart= IntVar()
                self.quan_e= Spinbox(self.showinfo, from_=1, to=1000, textvariable=val_cart, width=9, font=("Comic Sans", 17, "bold"))
                self.quan_e.place(x=340, y=175)
                val_cart.set("1")
                self.quan_e.bind("<Return>", self.cart)
                self.quan_e.bind("<Escape>", fun_cancel)
                self.quan_e.focus()
                # self.quan_e= Entry(self.showinfo, width=22 ,  font=("arial 20 bold"), borderwidth=3)
                # self.quan_e.bind("<Return>", self.cart)
                # self.quan_e.bind("<Escape>", fun_cancel)
                # self.quan_e.place(x=230, y=175)
                self.atc_btn= Button(self.showinfo, text="Add to Cart", width=19, font=("arial 10 bold"), height=2, bg="#20bebe",cursor='hand2', command=self.cart)
                self.atc_btn.place(x=500, y=175)
            else:
                tkinter.messagebox.showerror("Error","ID does NOT exist!")
        except ValueError:
            tkinter.messagebox.showerror("Error", "Please enter a valid id")
            root1.lift()

    def cart(self, *args,**kwargs):
        try:
            if self.get_stock< int(self.quan_e.get()) or int(self.quan_e.get())==0:
                tkinter.messagebox.showerror("Error", "Entered quantity not available")
                self.quan_e.delete(0, END)                
            else:
                prodid.append(self.id_e)
                prodname.append(self.get_name)
                prodstock.append(self.get_stock)
                prodprice.append(self.get_price)
                prodquan.append(int(self.quan_e.get()))
                prodcp.append(self.get_cp)
                self.tprice= prodquan[self.x]*prodprice[self.x]
                self.total.append(self.tprice)
                self.total_t+= self.tprice
                self.tree.insert(parent='', index='end', iid=self.count, text="", values=(f"{prodname[self.x]}",f"{self.quan_e.get()}",f"{self.tprice}"))
                self.rc.configure(text=f"₹{sum(self.total)}/-")
                self.count+=1
                self.x+=1
                self.showinfo.destroy()
                btn_cancel.destroy()
                self.value_inside.set("")
                self.me.focus()
                newstock= prodstock[self.uptstock] -prodquan[self.uptstock]
                c=self.conn.cursor()
                c.execute(f"update {TableName} set stock={newstock} where id={prodid[self.uptstock]};")
                self.conn.commit()
                self.uptstock+=1
        except ValueError:
            tkinter.messagebox.showerror("Error", "Enter valid quantity")

    def gbill(self, *args,**kwargs):
        if len(prodquan)==0:
            tkinter.messagebox.showerror("Error","No item added") 
            return
        else:
            def submit_fun(*args, **kwargs):
                #generating bill
                now = datetime.datetime.now()
                date= now.strftime("%Y-%m-%d")
                dr="./additionals/Invoices/" + str(date)
                #Bill Template
                indate= now.strftime("%d.%m.%Y")
                intime= now.strftime("%H:%M:%S")
                com= "\t\t\t\tRaja Store Management\n"
                add="\t\t\t\t   Roorkee-India\n"
                ph= "\t\t\t\t  phone-xxxxxxxxx\n"
                inn= "\t\t\t\t\tInvoice\n\n"
                datee=f"\t\t   Date:{indate}\t\t\t   Time-{intime}\n"
                div="\t\t   ================================================\n"
                header="\t\t    Sno. Product Name\t\t\t Qty\tAmount\n"
                final= com+add+ph+inn+datee+div+header+div
                if not os.path.exists(dr):
                    os.makedirs(dr)
                #getting invoice if from a text and updating it for future everytime
                def randomno(*args, **kwargs):
                    id= random.randint(1111, 9999)
                    return id
                try:
                    f= open(r".\additionals\inid.txt",'r+')
                    randomid= f.read()
                    f.truncate(0)
                    f.seek(0)
                    f.write(str(int(randomid)+1))
                    f.close()
                except:
                    randomid= randomno()
                while True:
                    try:
                        filename= str(dr) + "\\" + str(randomid)+".rtf"
                        break
                    except:
                        randomid= randomno()
                file=open(filename, "w")
                file.write(final)
                sn=1
                for i in range(len(prodname)):
                    file.write("\t\t\t" + str(sn)+"  "+ str(prodname[i]+ "                     ")[:26]+" "+ str(prodquan[i])+"\t"+ str(prodprice[i]*prodquan[i])+"\n") 
                    sn+=1
                file.write("\n")
                file.write("\t\t\t\t\t\t\tItems: {}".format(sum(prodquan))+"\n")
                file.write("\t\t\t\t\t\t\tTotal:Rs. {}/-".format(total)+"\n")
                file.write("\t\t\t\t\t\t\tDiscount: Rs.{}".format(total-total_atm)+"\n")
                file.write("\t\t\t\t\t\t   Grand Total:Rs. {}/-".format(total_atm)+"\n\n")
                file.write("\t\t\t\tThank You Visit Again!!!")
                file.close()
                
                #mysql database handlings
                if len(prodquan)!=0:
                    c=self.conn.cursor()
                    for i in range(len(prodstock)):
                        newstock= prodstock[i]-prodquan[i]
                        tcp= int(prodcp[i] * newstock)
                        tsp= int(prodprice[i] * newstock)
                        asp= tsp-tcp
                        c.execute(f"UPDATE {TableName} SET totalcp={tcp}, totalsp={tsp}, assumed_profit={asp} where ID={prodid[i]};")
                        self.conn.commit()
                        #adding cart data to transaction table
                        tp= (total-sum(prodcp)) - (total-total_atm)
                        print(total)
                        print(total_atm)
                        print(prodcp)
                        date=datetime.datetime.now().strftime("%d.%m.%Y")
                        time=datetime.datetime.now().strftime("%H:%M:%S")
                        c.execute(f"INSERT INTO transactions values({prodid[i]},'{prodname[i]}', {prodquan[i]}, {self.total[i]},{tp},'{date}','{time}', {int(randomid)});")
                        self.conn.commit()
                    #printing billing
                    self.tree.delete(*self.tree.get_children())
                    self.x=0
                    self.count= 0
                    self.rc.configure(text=f"")
                    prodname.clear()
                    prodid.clear()
                    prodprice.clear()
                    prodquan.clear()
                    prodstock.clear()
                    prodcp.clear()
                    self.total.clear()
                    top.destroy()
                    if tkinter.messagebox.askyesno("Print Bill", "Successfully updated and created bill\nDo you want to print the bill?"):
                        os.startfile(filename, "print")
                else:
                    tkinter.messagebox.showerror("Error","No item added")            
                self.me.focus()

            # showing discount and cashing details on a toplevel
            total= sum(self.total)
            top= Toplevel(root1)
            center(top)
            top.geometry("550x300")
            top.config(bg="#55BDCA")
            top.resizable(False, False)
            top_l1= Label(top, text= "Select Discount Option", font=("arial 20 bold"), bg="#55BDCA", fg="yellow")
            top_l1.place(x=10, y=10)
            def topp(sel, *args, **kwargs):
                top_option.place_forget()
                top_l1.place_forget()
                #main discount stucture
                def discount(*args, **kwargs):
                    def back2(*args, **kwargs):
                        top_e1.delete(0, END)
                        top_e1.focus()
                        top_tatm1.place_forget()
                        top_tatm2.place_forget()
                        top_tatm3.place_forget()
                        top_tatm4.place_forget()
                        s.place_forget()
                        top_lx.place_forget()
                        top_lx1.place_forget()
                        top_lx2.place_forget()
                        top_ex1.place_forget()
                        top_btn1x.place_forget()
                        top_btn1.place(x=300,y=50)
                        backbtn.config(command=back1)
                    backbtn.config(command=back2)
                    global total_atm
                    total_atm=0
                    if op=="per":
                        try:
                            if int(top_e1.get())>100 or int(top_e1.get())<0:
                                tkinter.messagebox.showerror("ValueError", "Enter a Percentage betn. 0-100")
                                backbtn.config(command=back1)
                                top.lift()
                                return
                        except:
                            return
                            
                        try:
                            total_atm= total- int((int(top_e1.get())/100)*total)
                        except:
                            tkinter.messagebox.showerror("Value Error", "Only +ve Interger allowed")
                            backbtn.config(command=back1)
                            top.lift()
                            return
                    elif op=="price":
                        try:
                            if int(top_e1.get())>total or int(top_e1.get())<0:
                                tkinter.messagebox.showerror("ValueError", f"Enter a price discount betn. 0-{total}")
                                backbtn.config(command=back1)
                                top.lift()
                                return
                        except:
                            return
                        try:
                            total_atm= total- (int(top_e1.get()))
                        except:
                            tkinter.messagebox.showerror("Value Error", "Only +ve Interger allowed")
                            backbtn.config(command=back1)
                            top.lift()
                            return
                    top_btn1.place_forget()   
                    top_tatm1= Label(top, text= "Fixed Total Amount:", font=("arial 19 bold"), bg="#55BDCA", fg="yellow")
                    top_tatm1.place(x=10, y=60)
                    top_tatm2= Label(top, text=f"Rs.{total}/-", font=("arial 19 bold"), bg="#55BDCA", fg="red")
                    top_tatm2.place(x=255, y=60)
                    top_tatm3= Label(top, text= "New Total Amount:", font=("arial 18 bold"), bg="#55BDCA", fg="yellow")
                    top_tatm3.place(x=10, y=100)
                    top_tatm4= Label(top, text=f"Rs.{total_atm}/-", font=("arial 18 bold"), bg="#55BDCA", fg="red")
                    top_tatm4.place(x=255, y=100)
                    s= Label(top, text='\n|\n|\n|\n|\n|\n|', bg="#55BDCA")
                    s.place(x=385, y=42)
                    top_lx= Label(top, text= "You Saved", font=("arial 15 bold"), bg="#55BDCA", fg="yellow")
                    top_lx.place(x=400, y=60)
                    top_lx1= Label(top, text= f"Rs.{total-total_atm}/-", font=("arial 15 bold"), bg="#55BDCA", fg="darkorange")
                    top_lx1.place(x=410, y=90)
                    top_lx2= Label(top, text= "Received Amount", font=("arial 14 bold"), bg="#55BDCA", fg="yellow")
                    top_lx2.place(x=10, y=160)
                    
                    def calculate_change(*args, **kwargs):
                        try:    
                            rm= int(top_ex1.get())
                        except ValueError:
                            return
                        if rm<total_atm:
                            tkinter.messagebox.showerror("Error", f"Received Amount is low\nNeed Rs.{total_atm-int(top_ex1.get())} more to complete transaction!")
                            top.lift()
                            return
                        def back3(*args, **kwargs):
                            top_lx2.config(font=("arial 14 bold"))
                            try:
                                top_lxc1.place_forget()
                            except:
                                pass
                            top_lxc2.place_forget()
                            top_lxc3.place_forget()
                            top_open.place_forget()
                            top_btn1x.place(x=380,y=156)
                            top_ex1.place(x=185, y=160)
                            top_ex1.delete(0, END)
                            top_ex1.focus()
                            backbtn.config(command=back2)
                        backbtn.config(command=back3)   
                        
                        top_lx2.config(font=("arial 17 bold"))
                        top_ex1.place_forget()
                        top_btn1x.place_forget()
                        top_lxc1= Label(top, text= f"Rs.{rm}/-", font=("arial 17 bold"), bg="#55BDCA", fg="darkorange")
                        top_lxc1.place(x=215, y=160)
                        top_lxc2= Label(top, text= "Change Amount", font=("arial 17 bold"), bg="#55BDCA", fg="yellow")
                        top_lxc2.place(x=10, y=200)
                        top_lxc3= Label(top, text= f"Rs.{rm-total_atm}/-", font=("arial 17 bold"), bg="#55BDCA", fg="darkorange")
                        top_lxc3.place(x=205, y=200)
                        def open_cashcounter(*args, **kwargs):
                            def back4(*args, **kwargs):
                                top_open.config(bg="orange", command= open_cashcounter, cursor="hand2")
                                top_submit.config(bg="grey", cursor="arrow", command= passs)
                                backbtn.config(command=back3)
                            backbtn.config(command=back4)
                            top_open.config(bg="grey", command= passs, cursor="arrow")
                            top_submit.config(state="normal",bg="#B40505", fg="white", cursor="hand2", command= submit_fun)
                            # rest cash counter can be made open from here

                        top_open= Button(top, text="Open\nCash Counter", bg="orange", font=("Comic Sans", 12, "bold"), cursor="hand2", command=open_cashcounter) 
                        top_open.place(x=364,y=168)
                        
                    top_ex1= Entry(top, width=16 ,  font=("arial 15 bold"), borderwidth=3)
                    top_ex1.place(x=185, y=160)
                    top_ex1.bind("<Return>", calculate_change)
                    top_ex1.focus()
                    top_btn1x= Button(top, text="Calculate", width=20, height=2, bg="#20bebe", font=("arial 8 bold"), cursor="hand2", command= calculate_change) 
                    top_btn1x.place(x=380,y=156)
                op=""
                if sel=="By Percentage":
                    #to undo an operation and go back once
                    def back1(*args, **kwargs):
                        backbtn.place_forget()
                        top_dis.place_forget()
                        top_dis1.place_forget()
                        top_e1.place_forget()
                        top_submit.place_forget()
                        top_btn1.place_forget()
                        value_top.set("Select an Option")
                        top_option.focus()
                        top_option.place(x=330, y=10)
                        top_l1.place(x=10, y=10)
                    try:
                        self.img_bill= PhotoImage(file=".\\additionals\\backkk.png")
                        backbtn= Button(top, image=self.img_bill, bg="#55BDCA", activebackground="#55BDCA", cursor="hand2", borderwidth=0, command=back1)
                        backbtn.place(x=480, y=5)
                    except:
                        backbtn= Button(top, text="<---", bg="#55BDCA", activebackground="#55BDCA", cursor="hand2", borderwidth=0, command=back1, font=("Comic Sans" ,18,"bold"))
                        backbtn.place(x=480, y=5)
                    top_dis= Label(top, text= "Total Discount", font=("arial 19 bold"), bg="#55BDCA", fg="yellow")
                    top_dis.place(x=10, y=10)
                    top_dis1= Label(top, text= "%", font=("arial 19 bold"), bg="#55BDCA", fg="black")
                    top_dis1.place(x=420, y=10)
                    op="per"
                    top_e1= Entry(top, width=19 ,  font=("arial 15 bold"), borderwidth=3)
                    top_e1.place(x=200, y=10)
                    top_e1.bind("<Return>", discount)
                    top_e1.focus()
                    top_btn1= Button(top, text="Generate Total", width=20, height=2, bg="#20bebe", font=("arial 10 bold"), cursor="hand2", command= discount) 
                    top_btn1.place(x=300,y=50)
                    top_submit= Button(top, text="SUBMIT BILL", width=60, height=2, bg="grey", font=("arial 11 bold"), state="disabled") 
                    top_submit.place(x=0,y=250)
                elif sel=="By Specific Price":
                    #to undo an operation and go back once
                    def back1(*args, **kwargs):
                        backbtn.place_forget()
                        top_dis.place_forget()
                        top_dis1.place_forget()
                        top_e1.place_forget()
                        top_submit.place_forget()
                        top_btn1.place_forget()
                        value_top.set("Select an Option")
                        top_option.focus()
                        top_option.place(x=330, y=10)
                        top_l1.place(x=10, y=10)
                    try:
                        self.img_bill= PhotoImage(file=".\\additionals\\backkk.png")
                        backbtn= Button(top, image=self.img_bill, bg="#55BDCA", activebackground="#55BDCA", cursor="hand2", borderwidth=0, command=back1)
                        backbtn.place(x=480, y=5)
                    except:
                        backbtn= Button(top, text="<--", bg="#55BDCA", activebackground="#55BDCA", cursor="hand2", borderwidth=0, command=back1, font=("Comic Sans" ,14,"bold"))
                        backbtn.place(x=480, y=5)
                    top_dis= Label(top, text= "Total Discount", font=("arial 19 bold"), bg="#55BDCA", fg="yellow")
                    top_dis.place(x=10, y=10)
                    top_dis1= Label(top, text= "₹", font=("arial 19 bold"), bg="#55BDCA", fg="black")
                    top_dis1.place(x=420, y=10)
                    op="price"
                    top_e1= Entry(top, width=19 ,  font=("arial 15 bold"), borderwidth=3)
                    top_e1.place(x=200, y=10)
                    top_e1.bind("<Return>", discount)
                    top_e1.focus()
                    top_btn1= Button(top, text="Generate Total", width=20, height=2, bg="#20bebe", font=("arial 10 bold"), cursor="hand2", command= discount) 
                    top_btn1.place(x=300,y=50)
                    top_submit= Button(top, text="SUBMIT BILL", width=60, height=2, bg="grey", font=("arial 11 bold"), state="disabled") 
                    top_submit.place(x=0,y=250)
                elif sel=="No Discount":
                    def back1(*args, **kwargs):
                        backbtn.place_forget()
                        top_disd.place_forget()
                        top_disd1.place_forget()
                        top_ld1.place_forget()
                        top_ed1.place_forget()
                        top_btn1d.place_forget()
                        top_submitd.place_forget()
                        value_top.set("Select an Option")
                        top_option.focus()
                        top_option.place(x=330, y=10)
                        top_l1.place(x=10, y=10)
                    try:
                        self.img_bill= PhotoImage(file=".\\additionals\\backkk.png")
                        backbtn= Button(top, image=self.img_bill, bg="#55BDCA", activebackground="#55BDCA", cursor="hand2", borderwidth=0, command=back1)
                        backbtn.place(x=480, y=5)
                    except:
                        backbtn= Button(top, text="<--", bg="#55BDCA", activebackground="#55BDCA", cursor="hand2", borderwidth=0, command=back1, font=("Comic Sans" ,14,"bold"))
                        backbtn.place(x=480, y=5)
                    top_disd= Label(top, text= "Total Amount: ", font=("arial 19 bold"), bg="#55BDCA", fg="yellow")
                    top_disd.place(x=10, y=10)
                    top_disd1= Label(top, text= f"₹{total}/-", font=("arial 19 bold"), bg="#55BDCA", fg="black")
                    top_disd1.place(x=220, y=10)
                    def rev_atm(*args, **kwargs):
                        val=int(top_ed1.get())
                        if val<total:
                            tkinter.messagebox.showerror("ValueError", f"Amount is less\nYou have to receive atleast Rs.{total}")
                            top.lift()
                            return
                        else:
                            def back2(*args, **kwargs):
                                top_disd2.place_forget()
                                top_ld2.place_forget()
                                top_disd3.place_forget()
                                top_opend.place_forget()
                                top_ed1.delete(0, END)
                                top_ed1.place(x=20, y=120)
                                top_btn1d.place(x=270,y=120)
                                backbtn.config(command=back1)
                            backbtn.config(command=back2)
                            top_ed1.place_forget()
                            top_btn1d.place_forget()
                            top_disd2= Label(top, text= f"₹{val}/", font=("arial 19 bold"), bg="#55BDCA", fg="black")
                            top_disd2.place(x=250, y=70)
                            top_ld2= Label(top, text= "Change Amount:", font=("arial 19 bold"), bg="#55BDCA", fg="yellow")
                            top_ld2.place(x=10, y=130)
                            top_disd3= Label(top, text= f"₹{val-total}/-", font=("arial 19 bold"), bg="#55BDCA", fg="black")
                            top_disd3.place(x=250, y=130)
                            def open_cashcounter(*args, **kwargs):
                                def back3(*args, **kwargs):
                                    top_opend.config(bg="orange", command= open_cashcounter, cursor="hand2")
                                    top_submitd.config(bg="grey", cursor="arrow", command= passs)
                                    backbtn.config(command=back2)
                                backbtn.config(command=back3)
                                global total_atm
                                total_atm=total
                                top_submitd.focus()
                                top_submitd.bind("<Return>",submit_fun)
                                top_opend.config(bg="grey", command= passs, cursor="arrow")
                                top_submitd.config(state="normal",bg="#B40505", fg="white", cursor="hand2",command= submit_fun)
                                # rest cash counter can be made open from here
                            top_opend= Button(top, text="Open\nCash Counter", bg="orange", font=("Comic Sans", 12, "bold"), cursor="hand2", command=open_cashcounter) 
                            top_opend.place(x=364,y=168)
                            top_opend.bind("<Return>", open_cashcounter)
                            top_opend.focus()
                    top_ld1= Label(top, text= "Received Amount:", font=("arial 19 bold"), bg="#55BDCA", fg="yellow")
                    top_ld1.place(x=10, y=70)
                    top_ed1= Entry(top, width=20 ,  font=("arial 15 bold"), borderwidth=3)
                    top_ed1.place(x=20, y=120)
                    top_ed1.bind("<Return>", rev_atm)
                    top_ed1.focus()
                    top_btn1d= Button(top, text="Calculate", width=20, height=2, bg="#20bebe", font=("arial 8 bold"), cursor="hand2", command=rev_atm) 
                    top_btn1d.place(x=270,y=120)
                    
                    # top_btn1= Button(top, text="Generate Total", width=20, height=2, bg="#20bebe", font=("arial 10 bold"), cursor="hand2", command= discount) 
                    # top_btn1.place(x=300,y=50)
                    top_submitd= Button(top, text="SUBMIT BILL", width=60, height=2, bg="grey", font=("arial 11 bold"), state="disabled") 
                    top_submitd.place(x=0,y=250)
            value_top = StringVar(top)
            value_top.set("Select an Option")
            options= ["By Percentage", "By Specific Price", "No Discount"]
            top_option= tkinter.OptionMenu(top, value_top, *options, command=topp)
            top_option.place(x=330, y=10)
            top_option.focus()
            top_option.config(bg= "orange")

    def detuptst(self, index,*args, **kwargs):
        name=self.tree.item(index, "values")[0]
        quan=self.tree.item(index, "values")[1]
        c= self.conn.cursor()
        c.execute(f"select stock from {TableName} where Product_Name='{name}';")
        st=""
        for i in c:
            st= i[0]
        newst= int(st)+ int(quan)
        c.execute(f"update {TableName} set stock={newst} where Product_Name='{name}';")
        self.conn.commit()
        self.uptstock-=1

    def removeitem(self, *args, **kwargs):
        x=self.tree.selection()
        if x!=():
            items=[]
            for i in x:
                items.append(int(i))
            cont= 1
            contnc=1
            hold=int(items[0])
            uchold=-1
            for check in range(len(items)-1):   #checking if the index of selected are continous or not
                if int(items[check])==int(items[check+1])-1:
                    cont+=1
                elif int(items[check])!=int(items[check+1])-1:
                    contnc+=1
            '''if cont!=len(x) or contnc!=len(x) or len(x)!=1:   #continuous+noncontinuous not working
                for check in range(len(items)-1):
                    if int(items[check])==int(items[check+1])-1:
                        conl.append(items[check])
                    else:
                        nonconl.append(items[check+1])'''
            def pop(index, *args, **kwargs):
                prodname.pop(index)
                prodid.pop(index)
                prodprice.pop(index)
                prodquan.pop(index)
                prodstock.pop(index)
                prodcp.pop(index)
                self.total.pop(index)

            if len(items)==1:   #if only 1 item is selected for deleting
                for i in items:
                    index=int(i)
                    self.detuptst(i)
                    self.tree.delete(i)
                    pop(index)
            elif cont==len(items):    #if all the selected rows are in continous form
                for i in items:
                    self.detuptst(i)
                    self.tree.delete(i)
                    pop(hold)
            elif contnc==len(items):   #if NONE of all the rows is continuous
                for i in items:
                    self.detuptst(i)
                    self.tree.delete(i)
                    uchold+=1
                    ind=int(i)-uchold
                    pop(ind)
            else:     #if rows are selected in a mixed continous and non-continuous form
                tkinter.messagebox.showerror("Invalid selection type","Kindly select single row or only continous rows \nor only non continuous rows!")
                return
            self.x-=len(x)
            self.count-= len(x)
            children= self.tree.get_children()
            movin=0
            for i in children:
                item= self.tree.item(i, "values")
                self.tree.delete(i)
                self.tree.insert(parent='', index='end', iid=movin, text="", values=item)
                movin+=1
            self.rc.configure(text=f"₹{sum(self.total)}/-")
    
    def clear_cart(self, *args, **kwargs):
        for i in range(len(prodid)):
            self.detuptst(i)
        self.tree.delete(*self.tree.get_children())
        self.x=0
        self.count= 0
        self.rc.configure(text=f"")
        prodname.clear()
        prodid.clear()
        prodprice.clear()
        prodquan.clear()
        prodstock.clear()
        self.total.clear()
        prodcp.clear()

#===================================================================================================================================
#running main billing button on header
def bill_btn(*args, **kwargs):
    root1.title("STORE MANAGEMENT-RAJA.Billing")
    headbtn0.config(bg="#88BDBC", cursor="arrow",command= passs,state="disabled" )
    # Billing(root1, left, right)
    left.pack(side=LEFT)
    val_fun()
    try:
        can_add.place_forget()
    except:
        pass
    try:
        can_mod.place_forget()
    except:
        pass
    headbtn1.config(bg="#FFC58B", command=stock_addition, cursor="hand2", state="normal")
    headbtn2.config(cursor="hand2", bg="#FFC58B", command=stock_modify, state="normal")
    bill_combobox.focus()

#for stock_review modification tab changing
xyzz=[]

root1= Tk()       #root window and window codes for the section
root1.geometry("1260x645")
def center(win, *args, **kwargs):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
center(root1)
# root1.eval('tk::PlaceWindow . NORTH')  #placing the window at the center of screen

#main window to work on
root1.resizable(False, False)
root1.title("STORE MANAGEMENT-RAJA.Billing")
try:
    root1.wm_iconbitmap(r".\additionals\icon.ico")
except:
    pass
root1.focus()
# first framing a billing window in the main window with header buttons to access other parts(stock addition, modification, review...)
left= Frame(root1, width=760, height=645, bg= "#88BDBC" )
left.pack(side=LEFT)
right= Frame(root1, width=500, height=645, bg= "#55BDCA")
right.pack(side=RIGHT)
header= Canvas(root1, width=760, height=80, bg="white")
header.place(x=0, y=0)
def passs(*args, **kwargs):
    pass
headbtn0= Button(header, text= "Billing", width=17, height=4, bg="#88BDBC", cursor="arrow",font=("Ariel", 12, ), activebackground="darkblue" , command=passs, state="disabled")
headbtn0.place(relx=0, rely=0)
headbtn1= Button(header, text= "Stock\nAddition", width=17, height=4, bg="#FFC58B", cursor="hand2", font=("Ariel", 12, ),activebackground="darkblue", command=stock_addition)
headbtn1.place(relx=0.2, rely=0)
headbtn2= Button(header, text= "Stock\nModification", width=17, height=4, bg="#FFC58B", cursor="hand2", font=("Ariel", 12),activebackground="darkblue", command=stock_modify)
headbtn2.place(relx=0.4, rely=0)
headbtn3= Button(header, text= "Stock\nReview", width=17, height=4, bg="#FFC58B", cursor="hand2", font=("Ariel", 12),activebackground="darkblue", command=stock_review)
headbtn3.place(relx=0.6, rely=0)
headbtn4= Button(header, text= "Sold item\nReview", width=17, height=4, bg="#FFC58B", cursor="hand2", font=("Ariel", 12),activebackground="darkblue", command=sold_item_review)
headbtn4.place(relx=0.8, rely=0)

Billing(root1, left, right)

root1.mainloop()
