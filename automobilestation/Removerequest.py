from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


mypass = ""
mydatabase=""

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
carTable = "costomer_details" 

def removerequest():
    
    Customer_id = Info1.get()
    
    deleteSql = "delete from "+carTable+" where Customer_id = '"+Customer_id+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        messagebox.showinfo("Sucess","Request removed successfully")
    except:
        messagebox.showinfo("Error","Please check customerID")
    

    print(Customer_id)
    root.destroy()
    
def delete(): 
    
    global Info1,Canvas1,con,cur,root
    
    root = Tk()
    root.title("Automobile Station")
    root.minsize(width=400,height=400)
    root.geometry("800x600")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#FF0000")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Remove request", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    lb2 = Label(labelFrame,text="costomerID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=removerequest)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
