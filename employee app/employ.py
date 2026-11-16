from tkinter import *
from tkinter import ttk
from sqlite import Database
from tkinter import messagebox
db = Database("employee.db")





root = Tk()
root.title("Employ Management Systam")
root.resizable(False,False)
root.geometry("1540x800+0+0")   
root.configure(bg="#2c3e50")  

name = StringVar()
age = StringVar()
job = StringVar()
gender = StringVar()
email = StringVar()
mobail = StringVar()
search = StringVar()

#=====enries frame========
entreis_frame = Frame(root,bg="#2c3e50")
entreis_frame.place(x=1,y=1,width=360,height=510)

labeltitle = Label(entreis_frame,text="Employee Company",bg="#2c3e50",font="calibri,18,bold",fg="white")
labeltitle.place(x=10,y=10)

labelname = Label(entreis_frame,text="NAME",bg="#2c3e50",font="calibri,18,bold",fg="white")
labelname.place(x=10,y=50)
entryname = Entry(entreis_frame,width=20,font="calibri,18",textvariable = name)
entryname.place(x=120,y=50)


labeljob = Label(entreis_frame,text='Job',font='calibri,18,bold',bg='#2c3e50',fg='white')
labeljob.place(x=10,y=90)

entryjob = Entry(entreis_frame,width=20,font="calibri,18",textvariable = job)
entryjob.place(x=120,y=90)

labelgender = Label(entreis_frame,text='Gender',font='calibri,18,bold',bg='#2c3e50',fg='white')
labelgender.place(x=10,y=130)

combogender = ttk.Combobox(entreis_frame,width=18,font='calibri,18',state="readonly",textvariable = gender)
combogender['values']=('Male','female')
combogender.place(x=120,y=130)

labelage= Label(entreis_frame,text='age',font='calibri,18,bold',bg='#2c3e50',fg='white')
labelage.place(x=10,y=170)

entryage = Entry(entreis_frame,width=20,font="calibri,18",textvariable = age)
entryage.place(x=120,y=170)



labelemail= Label(entreis_frame,text='Email',font='calibri,18,bold',bg='#2c3e50',fg='white')
labelemail.place(x=10,y=210)

entryemail = Entry(entreis_frame,width=20,font="calibri,18",textvariable = email)
entryemail.place(x=120,y=210)



labelmobail= Label(entreis_frame,text='Mobail',font='calibri,18,bold',bg='#2c3e50',fg='white')
labelmobail.place(x=10,y=250)

entrymobail = Entry(entreis_frame,width=20,font="calibri,18",textvariable = mobail)
entrymobail.place(x=120,y=250)


labeladdress= Label(entreis_frame,text='Address :',font='calibri,18,bold',bg='#2c3e50',fg='white')
labeladdress.place(x=10,y=290)

entryaddress = Text(entreis_frame,width=30,height=2,font="calibri,18")
entryaddress.place(x=10,y=325)

entry_search = Entry(root,font="Calibri,15",width=15,textvariable=search)
entry_search.place(x=1365,y=3,height=25)

#=======define=========
def hide():
    root.geometry("350x510+0+0")
def show():
    root.geometry("1540x800+0+0")
btn_hide = Button(entreis_frame,text="HIDE",font=("calibri,10"),bg="green1",command=hide)
btn_hide.place(x=190,y=10,width=50,height=30)


btn_show = Button(entreis_frame,text="SHOW",font=("calibri,10"),bg="light goldenrod",command=show)
btn_show.place(x=250,y=10,width=60,height=30)



def dateget(event):
    selected_row = Treeview.focus()
    date = Treeview.item(selected_row)
    global row
    row = date["values"]
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    mobail.set(row[6])
    entryaddress.delete(1.0,END)
    entryaddress.insert(END,row[7])


def add_employy():
    if entryname.get() ==""or entryage.get() == ""or entryemail.get()=="" or entryjob.get() == "" or entrymobail.get() == "" or combogender.get() == "" or entryaddress.get(1.0,END) == "":
        messagebox.showerror("Error","plaese fill all the ENTRY")
        return
    db.insert(
        entryname.get(),
        entryage.get(),
        entryjob.get(),
        entryemail.get(),
        combogender.get(),
        entrymobail.get(),
        entryaddress.get(1.0,END))
    messagebox.showinfo("Successs","Added New Employee")
    clear()
    display()
   

def delete():
    confirm = messagebox.askyesno("delete warning","DO YOU SURE TO DELETE THIS EMPLOYEE")
    if confirm == True:
        db.REMOVE(row[0])
        clear()
        display()
    else:
        clear()
        





def clear():
    name.set("")
    age.set("")
    job.set("")
    gender.set("")
    email.set("")
    mobail.set("")
    entryaddress.delete(1.0,END)


def display():
    Treeview.delete(*Treeview.get_children())
    for x in db.fetch():
        Treeview.insert("",END,values=x)
    counting = len(Treeview.get_children())
    label_counting.config(text=f"The employee Number:{counting}")


    

def update_employy():
    if entryname.get() ==""or entryage.get() == ""or entryemail.get()=="" or entryjob.get() == "" or entrymobail.get() == "" or combogender.get() == "" or entryaddress.get(1.0,END) == "":
        messagebox.showerror("Error","plaese fill all the ENTRY")
        return
    db.Update(row[0],
        entryname.get(),
        entryage.get(),
        entryjob.get(),
        entryemail.get(),
        combogender.get(),
        entrymobail.get(),
        entryaddress.get(1.0,END)
        )
    messagebox.showinfo("Successs","THE EMPLOYEE DETAIL IS UPDATE")
    clear()
    display()

def search_employ():
    Treeview.delete(*Treeview.get_children())
    search_small = search.get().strip()
    found = False
    for x in db.fetch():
        if search_small.lower() in str(x[1]).lower():
            Treeview.insert("",END,value = x)
            found = True
    if not found or search_small == "":
        messagebox.showerror("error","this employ is not found")

def Reset():
    search.set("")
    display()




#======buttun frame========
btn_frame = Frame(entreis_frame,bg="#2c3e50")
btn_frame.place(x=10,y=380,width=275,height=100)

btn_add = Button(btn_frame,
                 text='Add Details',
                 width=14,
                 height=2,
                 font=('Calibri,10'),
                 bg='deep sky blue',
                 bd=0,
                 fg="white",
                 command=add_employy
                 ).place(x=2,y=2)

btn_delete= Button(btn_frame,
                 text='Delete Details',
                 width=13,
                 height=2,
                 font=('Calibri,10'),
                 bg='red1',
                 bd=0,
                 fg="white",
                 command=delete
                 ).place(x=145,y=2)


btn_ubdate = Button(btn_frame,
                 text='Ubdate Details',
                 width=14,
                 height=2,
                 font=('Calibri,10'),
                 bg='green3',
                 bd=0,
                 fg="white",
                 command=update_employy
                 ).place(x=2,y=50)


btn_clear= Button(btn_frame,
                 text='Clear Details',
                 width=13,
                 height=2,
                 font=('Calibri,10'),
                 bg='gray53',
                 bd=0,
                 fg="white",
                 command=clear
                 ).place(x=145,y=50)

#=====TREEE VIEW FRAME========
tree_frame_view = Frame(root,bg="white")
tree_frame_view.place(x=350,y=1,width=940,height=510)


style = ttk.Style()
style.configure("my style.Treeview",font=('Calibri',13),rowheight=60)
style.configure("my style.Treeview.Heading",font=('calibri',13))

Treeview = ttk.Treeview(tree_frame_view,columns=(1,2,3,4,5,6,7,8),style="my style.Treeview",show="headings")
Treeview.pack(fill=BOTH,expand=True)
Treeview.heading("1",text="ID")
Treeview.column("1",width="40")

Treeview.heading("2",text="Name")
Treeview.column("2",width="120")


Treeview.heading("3",text="Age")
Treeview.column("3",width="70")

Treeview.heading("4",text="Job")
Treeview.column("4",width="120")

Treeview.heading("5",text="Email")
Treeview.column("5",width="150")

Treeview.heading("6",text="Gender")
Treeview.column("6",width="80")

Treeview.heading("7",text="Mobile")
Treeview.column("7",width="150")

Treeview.heading("8",text="Address")
Treeview.column("8",width="150")
Treeview.bind("<ButtonRelease-1>",dateget)



#search + warning butto + counting
btn_search = Button(root,text="Search",bg="#13bee0",font="Calibri,20",command=search_employ)
btn_search.place(x=1295,y=1)

btn_reset_search = Button(text="Reset",font = "Calibri,15",bg="#ff40a3",command=Reset)
btn_reset_search.place(x=1295,y=35)

label_counting = Label(font="Caribil,15",bg="#eaff00",text="The employee Number : 0")
label_counting.place(x=1295,y=70)


display()


root.mainloop()
