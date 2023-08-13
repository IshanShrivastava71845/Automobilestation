from asyncio import _register_task
from tkinter import *
from tkinter import messagebox
import pymysql

def Customer_Register():
    
    Customer_id = Info1.get()
    Customer_name = Info2.get()
    Contact_no = Info3.get()
    Address = Info4.get()
    Car_details = Info5.get()

    
    insertdetails = "insert into "+Cartable+" values('"+Customer_id+"','"+Customer_name+"','"+Contact_no+"','"+Address+"', '"+Car_details+"')"
    try:
        cur.execute(insertdetails)
        con.commit()
        messagebox.showinfo('Success',"details added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(Customer_id)
    print(Customer_name)
    print(Contact_no)
    print(Address)
    print(Car_details)


    root.destroy()
    
def addcustomer(): 
    
    global Canvas1,con,cur,root, Info1, Info2, Info3, Info4, Info5, Cartable
    
    root = Tk()
    root.title("Automobile station")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    mypass = "OnkarBelure8668"
    mydatabase="automobilestation"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    
    Cartable = "costomer_details" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.15)

    headingLabel = Label(headingFrame1, text="New costomer", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    lb1 = Label(labelFrame,text="costomer_ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
    
    lb2 = Label(labelFrame,text="Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    Info2 = Entry(labelFrame)
    Info2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    lb3 = Label(labelFrame,text="Contact_no: ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    Info3= Entry(labelFrame)
    Info3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    lb4 = Label(labelFrame,text="Address: ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    Info4 = Entry(labelFrame)
    Info4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
    
    lb5 = Label(labelFrame,text="Car details: ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.80, relheight=0.08)
        
    Info5 = Entry(labelFrame)
    Info5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.08)
        
    
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=Customer_Register)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()