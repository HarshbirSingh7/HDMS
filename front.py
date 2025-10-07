from back import read,readp,readpo,readcol,addrow,delrow,df,filldata,editrow,editrowp,get_id,bdate_fill,time_fill,datecheck
from graphs import graph_pay,graph_suit
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



class table:
    def __init__(self, root, dataframe):
        self.root = root
        self.dataframe = dataframe
        # self.root.title("HDMS v1.0")
        # self.root.geometry('1200x450')
        
        self.tree = ttk.Treeview(root,height=5,)
        self.tree["columns"] = list(dataframe.columns)
        self.tree['show'] = 'headings'
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.scrollbarx = ttk.Scrollbar(root, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.tree.configure(xscrollcommand=self.scrollbarx.set)
 


        self.scrollbar.pack(side="right", fill="y")
        self.scrollbarx.pack(side="bottom", fill="x")
        for col in self.tree["columns"]:
            self.tree.column(col, width=150)
            
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        
        for index, row in dataframe.iterrows():
            self.tree.insert("", 'end', values=list(row))
        
        self.tree.pack(expand=True, fill="both")  

        
def dispread(): # for readdata
    userid = en1.get()
    en1.delete(0,END)
    users = readcol('CustId')
    if userid in users:
        root2 = Tk()
        root2.geometry('400x400')
        root2.resizable(False,False)
        root2.title('HDMS Reader v1.0')

        lb1 = Label(root2,text=readp(userid),justify='left',font=('Ubuntu Sans Medium',12))
        lb1.pack()
        root2.mainloop()
    else:
        messagebox.showerror("ERROR",'Cust ID Not Found!')  
        root1.destroy()  

def dispval(): # for read_a_data
    userid = en2.get()
    colname = en3.get()
    en2.delete(0,END)
    en3.delete(0,END)
    users = readcol('CustId')
    cols = df.columns.to_list()
    if userid in users and colname in cols:
        root2 = Tk()
        root2.geometry('400x300')
        root2.resizable(False,False)
        root2.title('HDMS Reader v1.0')

        lb1 = Label(root2,text=readpo(userid,colname),justify='left',font=('Ubuntu Sans Medium',18))
        lb1.pack()
        root2.mainloop()
    else:
        messagebox.showerror("ERROR",'Cust ID And Column Not Found!')  
        root3.destroy()     

def getid(): # for getid1
    try:
        cuid = get_id('Mobile',int(mp1.get()))
        mp1.get()
        messagebox.showinfo('CustId',f'The Required Customer Id is {cuid}')
        root8.destroy()
    except:
        messagebox.showerror("ERROR",f'The Enterd Mobile Number is INVALID!!!')
        root8.destroy()

def getide(): # for getid2
    try:
        cuid = get_id('Email',ep1.get())
        ep1.get()
        messagebox.showinfo('CustId',f'The Required Customer Id is {cuid}')
        root9.destroy()
    except:
        messagebox.showerror("ERROR",f'The Enterd Email is INVALID!!!')
        root9.destroy()

def del_row(): #for deleterow
    row = dp1.get()
    delrow(row)
    dp1.delete(0,END)
    root10.destroy()

def checkoutfunc(): #for checkout
    userid = cp1.get()
    users = readcol('CustId')
    if userid in users:
        date_data = datecheck(cp1.get())
        editrowp(cp1.get(),'Status','CheckOut')
        editrowp(cp1.get(),'CheckOutTime',time_fill())
        editrowp(cp1.get(),'CheckOutDate',str(date_data[0]))

        dayc = int(date_data[1])
        editrowp(cp1.get(),'Days',int(dayc))
        
        totalc = int(date_data[2])
        editrowp(cp1.get(),'Total',int(totalc))

        messagebox.showinfo('Editor',f'The Customer Id {cp1.get()} Has Been Checked Out!')
        cp1.delete(0,END)
        root11.destroy()
    else:
        messagebox.showerror('ERROR','THE USER ID ENTERED IS INCORRECT!')
        root11.destroy()

def addrown():#for addnrow
    try:
        addrow(ad1.get(),ad2.get(),ad3.get(),ad4.get(),ad5.get(),ad6.get(),ad7.get(),int(ad8.get()))
        ad1.delete(0,END)
        ad2.delete(0,END)
        ad3.delete(0,END)
        ad4.delete(0,END)
        ad5.delete(0,END)
        ad6.delete(0,END)
        ad7.delete(0,END)
        ad8.delete(0,END)
        messagebox.showinfo('Editor','The New Record Has Been Added')
        root5.destroy()
    except Exception as e:
        messagebox.showerror('Editor',e)
        root5.destroy()

def addupdatedrow(): # for updaterow
    editrow(up1.get(),id2,up2.get(),up3.get(),up4.get(),up5.get(),up6.get(),up7.get(),int(up8.get()))
    up1.delete(0,END)
    up2.delete(0,END)
    up3.delete(0,END)
    up4.delete(0,END)
    up5.delete(0,END)
    up6.delete(0,END)
    up7.delete(0,END)
    up8.delete(0,END)
    messagebox.showinfo('Editor','The Record Has Been Updated!')
    root6.destroy()

def readdata(): # hello
    global root1
    root1 = Tk()
    root1.geometry('350x100')
    root1.title('HDMS Reader v1.0')
    root1.resizable(False,False)
    global en1
    lb1 = Label(root1,text='Cust Id:',font=('Ubuntu Sans Medium',12))
    lb1.grid(row=1,column=0,pady=(10,0),padx=(10,0))
    en1 = Entry(root1,width=30,borderwidth=2,justify='center')
    en1.grid(row=1,column=1,pady=(13,0),padx=(10,0))
    

    def on_enter(e):
        bt1['background'] = 'black'
        bt1['foreground'] = '#2693e6'
    def on_leave(e):
        bt1['background'] = '#2693e6'
        bt1['foreground'] = 'black'

    bt1 = Button(root1,text='Search',command=dispread,width=30,
            border=0,
            bg='#2693e6',
            fg='black',
            relief='groove',
            activeforeground='black',
            activebackground='#2693e6'
                )
    bt1.grid(row=2,column=1,pady=(13,0),padx=(4,0))
    bt1.bind('<Enter>',on_enter)
    bt1.bind('<Leave>',on_leave)

    root1.mainloop()

def read_a_data():
    global root3
    root3 = Tk()
    root3.geometry('350x150')
    root3.title('HDMS Reader v1.0')
    root3.resizable(False,False)
    global en2
    global en3
    lb2 = Label(root3,text='Cust Id:',font=('Ubuntu Sans Medium',12))
    lb2.grid(row=1,column=0,pady=(10,0),padx=(10,0))
    en2 = Entry(root3,width=30,borderwidth=2,justify='center')
    en2.grid(row=1,column=1,pady=(13,0),padx=(10,0))
    lb3 = Label(root3,text='Column:',font=('Ubuntu Sans Medium',12))
    lb3.grid(row=2,column=0,pady=(10,0),padx=(10,0))
    en3 = Entry(root3,width=30,borderwidth=2,justify='center')
    en3.grid(row=2,column=1,pady=(13,0),padx=(10,0))

    def on_enter(e):
        bt2['background'] = 'black'
        bt2['foreground'] = '#2693e6'
    def on_leave(e):
        bt2['background'] = '#2693e6'
        bt2['foreground'] = 'black'

    bt2 = Button(root3,text='Search',command=dispval,width=30,
            border=0,
            bg='#2693e6',
            fg='black',
            relief='groove',
            activeforeground='black',
            activebackground='#2693e6'
                )
    bt2.grid(row=3,column=1,pady=(13,0),padx=(4,0))
    bt2.bind('<Enter>',on_enter)
    bt2.bind('<Leave>',on_leave)

    root3.mainloop()

def addnrow(): # to add a new row
    global root5
    root5 = Tk()
    root5.title("HDMS Editor v1.0")
    root5.geometry('350x350')
    root5.resizable(False,False)

    lb1 = Label(root5,text='RoomNo:',font=('Ubuntu Sans Medium',12),justify="left")
    lb1.grid(row=1,column=0,pady=(10,0),padx=(10,0))
    lb2 = Label(root5,text='Name:',font=('Ubuntu Sans Medium',12))
    lb2.grid(row=2,column=0,pady=(10,0),padx=(10,0))
    lb3 = Label(root5,text='Mobile:',font=('Ubuntu Sans Medium',12),justify="left")
    lb3.grid(row=3,column=0,pady=(10,0),padx=(10,0))
    lb4 = Label(root5,text='Email:',font=('Ubuntu Sans Medium',12),justify="left")
    lb4.grid(row=4,column=0,pady=(10,0),padx=(10,0))
    lb5 = Label(root5,text='Suit:',font=('Ubuntu Sans Medium',12),justify="left")
    lb5.grid(row=5,column=0,pady=(10,0),padx=(10,0))
    lb6 = Label(root5,text='PayType:',font=('Ubuntu Sans Medium',12),justify="left")
    lb6.grid(row=6,column=0,pady=(10,0),padx=(10,0))
    lb7 = Label(root5,text='BookDate:',font=('Ubuntu Sans Medium',12),justify="left")
    lb7.grid(row=7,column=0,pady=(10,0),padx=(10,0))
    lb8 = Label(root5,text='Days:',font=('Ubuntu Sans Medium',12),justify="left")
    lb8.grid(row=8,column=0,pady=(10,0),padx=(10,0))

    global ad1
    global ad2
    global ad3
    global ad4
    global ad5
    global ad6
    global ad7
    global ad8
    ad1 = Entry(root5,width=30,borderwidth=2,justify='center')
    ad1.grid(row=1,column=1,pady=(13,0),padx=(10,0))
    ad2 = Entry(root5,width=30,borderwidth=2,justify='center')
    ad2.grid(row=2,column=1,pady=(13,0),padx=(10,0))
    ad3 = Entry(root5,width=30,borderwidth=2,justify='center')
    ad3.grid(row=3,column=1,pady=(13,0),padx=(10,0))
    ad4 = Entry(root5,width=30,borderwidth=2,justify='center')
    ad4.grid(row=4,column=1,pady=(13,0),padx=(10,0))
    ad5 = Entry(root5,width=30,borderwidth=2,justify='center')
    ad5.grid(row=5,column=1,pady=(13,0),padx=(10,0))
    ad6 = Entry(root5,width=30,borderwidth=2,justify='center')
    ad6.grid(row=6,column=1,pady=(13,0),padx=(10,0))
    ad7 = Entry(root5,width=30,borderwidth=2,justify='center')
    ad7.grid(row=7,column=1,pady=(13,0),padx=(10,0))
    ad7.insert(END,bdate_fill())
    ad8 = Entry(root5,width=30,borderwidth=2,justify='center')
    ad8.grid(row=8,column=1,pady=(13,0),padx=(10,0))

    def on_enter(e):
        bt2['background'] = 'black'
        bt2['foreground'] = '#2693e6'
    def on_leave(e):
        bt2['background'] = '#2693e6'
        bt2['foreground'] = 'black'

    bt2 = Button(root5,text='ADD TO DATABASE',command=addrown,width=30,
            border=0,
            bg='#2693e6',
            fg='black',
            relief='groove',
            activeforeground='black',
            activebackground='#2693e6'
                )
    bt2.grid(row=9,column=1,pady=(13,0),padx=(4,0))
    bt2.bind('<Enter>',on_enter)
    bt2.bind('<Leave>',on_leave)


    root5.mainloop()

def updaterow(): #to update existing data #for rowupdate
    global id2
    id2 = ru1.get()
    users = readcol('CustId')
    if id2 in users:
        global root6
        root6 = Tk()
        root6.title("HDMS Editor v1.0")
        root6.geometry('350x350')
        root6.resizable(False,False)

        lb1 = Label(root6,text='RoomNo:',font=('Ubuntu Sans Medium',12),justify="left")
        lb1.grid(row=1,column=0,pady=(10,0),padx=(10,0))
        lb2 = Label(root6,text='Name:',font=('Ubuntu Sans Medium',12))
        lb2.grid(row=2,column=0,pady=(10,0),padx=(10,0))
        lb3 = Label(root6,text='Mobile:',font=('Ubuntu Sans Medium',12),justify="left")
        lb3.grid(row=3,column=0,pady=(10,0),padx=(10,0))
        lb4 = Label(root6,text='Email:',font=('Ubuntu Sans Medium',12),justify="left")
        lb4.grid(row=4,column=0,pady=(10,0),padx=(10,0))
        lb5 = Label(root6,text='Suit:',font=('Ubuntu Sans Medium',12),justify="left")
        lb5.grid(row=5,column=0,pady=(10,0),padx=(10,0))
        lb6 = Label(root6,text='PayType:',font=('Ubuntu Sans Medium',12),justify="left")
        lb6.grid(row=6,column=0,pady=(10,0),padx=(10,0))
        lb7 = Label(root6,text='BookDate:',font=('Ubuntu Sans Medium',12),justify="left")
        lb7.grid(row=7,column=0,pady=(10,0),padx=(10,0))
        lb8 = Label(root6,text='Days:',font=('Ubuntu Sans Medium',12),justify="left")
        lb8.grid(row=8,column=0,pady=(10,0),padx=(10,0))

        global up1
        global up2
        global up3
        global up4
        global up5
        global up6
        global up7
        global up8
        up1 = Entry(root6,width=30,borderwidth=2,justify='center')
        up1.grid(row=1,column=1,pady=(13,0),padx=(10,0))
        up2 = Entry(root6,width=30,borderwidth=2,justify='center')
        up2.grid(row=2,column=1,pady=(13,0),padx=(10,0))
        up3 = Entry(root6,width=30,borderwidth=2,justify='center')
        up3.grid(row=3,column=1,pady=(13,0),padx=(10,0))
        up4 = Entry(root6,width=30,borderwidth=2,justify='center')
        up4.grid(row=4,column=1,pady=(13,0),padx=(10,0))
        up5 = Entry(root6,width=30,borderwidth=2,justify='center')
        up5.grid(row=5,column=1,pady=(13,0),padx=(10,0))
        up6 = Entry(root6,width=30,borderwidth=2,justify='center')
        up6.grid(row=6,column=1,pady=(13,0),padx=(10,0))
        up7 = Entry(root6,width=30,borderwidth=2,justify='center')
        up7.grid(row=7,column=1,pady=(13,0),padx=(10,0))
        up8 = Entry(root6,width=30,borderwidth=2,justify='center')
        up8.grid(row=8,column=1,pady=(13,0),padx=(10,0))
      

        up1.insert(0,filldata(id2,'RoomNo'))
        up2.insert(0,filldata(id2,'CustName'))
        up3.insert(0,filldata(id2,'Mobile'))
        up4.insert(0,filldata(id2,'Email'))
        up5.insert(0,filldata(id2,'SuitType'))
        up6.insert(0,filldata(id2,'PayType'))
        up7.insert(0,filldata(id2,'BookDate'))
        up8.insert(0,filldata(id2,'Days'))

        def on_enter(e):
            bt2['background'] = 'black'
            bt2['foreground'] = '#2693e6'
        def on_leave(e):
            bt2['background'] = '#2693e6'
            bt2['foreground'] = 'black'

        bt2 = Button(root6,text='UPDATE DATABASE',command=addupdatedrow,width=30,
                border=0,
                bg='#2693e6',
                fg='black',
                relief='groove',
                activeforeground='black',
                activebackground='#2693e6'
                    )
        bt2.grid(row=9,column=1,pady=(13,0),padx=(4,0))
        bt2.bind('<Enter>',on_enter)
        bt2.bind('<Leave>',on_leave)


        root6.mainloop()
    else:
        messagebox.showerror('ERROR','CustID Not found!!')
        root7.destroy()

def rowupdate(): 
    global root7
    root7 = Tk()
    root7.geometry('350x100')
    root7.title('HDMS Reader v1.0')
    root7.resizable(False,False)
    global ru1
    lb1 = Label(root7,text='Cust Id:',font=('Ubuntu Sans Medium',12))
    lb1.grid(row=1,column=0,pady=(10,0),padx=(10,0))
    ru1 = Entry(root7,width=30,borderwidth=2,justify='center')
    ru1.grid(row=1,column=1,pady=(13,0),padx=(10,0))
    

    def on_enter(e):
        bt1['background'] = 'black'
        bt1['foreground'] = '#2693e6'
    def on_leave(e):
        bt1['background'] = '#2693e6'
        bt1['foreground'] = 'black'

    bt1 = Button(root7,text='UPDATE',command=updaterow,width=30,
            border=0,
            bg='#2693e6',
            fg='black',
            relief='groove',
            activeforeground='black',
            activebackground='#2693e6'
                )
    bt1.grid(row=2,column=1,pady=(13,0),padx=(4,0))
    bt1.bind('<Enter>',on_enter)
    bt1.bind('<Leave>',on_leave)

    root7.mainloop()

def getid1(): # to get cust id by mobile no
    global root8
    root8 = Tk()
    root8.geometry('350x100')
    root8.title('HDMS Reader v1.0')
    root8.resizable(False,False)
    global mp1
    lb1 = Label(root8,text='Mobile:',font=('Ubuntu Sans Medium',12))
    lb1.grid(row=1,column=0,pady=(10,0),padx=(10,0))
    mp1 = Entry(root8,width=30,borderwidth=2,justify='center')
    mp1.grid(row=1,column=1,pady=(13,0),padx=(10,0))

    def on_enter(e):
        bt1['background'] = 'black'
        bt1['foreground'] = '#2693e6'
    def on_leave(e):
        bt1['background'] = '#2693e6'
        bt1['foreground'] = 'black'

    bt1 = Button(root8,text='Get CustId',command=getid,width=30,
            border=0,
            bg='#2693e6',
            fg='black',
            relief='groove',
            activeforeground='black',
            activebackground='#2693e6'
                )
    bt1.grid(row=2,column=1,pady=(13,0),padx=(4,0))
    bt1.bind('<Enter>',on_enter)
    bt1.bind('<Leave>',on_leave)

    root8.mainloop()
    
def getid2(): # to get cust id by mobile no
    global root9
    root9 = Tk()
    root9.geometry('350x100')
    root9.title('HDMS Reader v1.0')
    root9.resizable(False,False)
    global ep1
    lb1 = Label(root9,text='Email:',font=('Ubuntu Sans Medium',12))
    lb1.grid(row=1,column=0,pady=(10,0),padx=(10,0))
    ep1 = Entry(root9,width=30,borderwidth=2,justify='center')
    ep1.grid(row=1,column=1,pady=(13,0),padx=(10,0))

    def on_enter(e):
        bt1['background'] = 'black'
        bt1['foreground'] = '#2693e6'
    def on_leave(e):
        bt1['background'] = '#2693e6'
        bt1['foreground'] = 'black'

    bt1 = Button(root9,text='Get CustId',command=getide,width=30,
            border=0,
            bg='#2693e6',
            fg='black',
            relief='groove',
            activeforeground='black',
            activebackground='#2693e6'
                )
    bt1.grid(row=2,column=1,pady=(13,0),padx=(4,0))
    bt1.bind('<Enter>',on_enter)
    bt1.bind('<Leave>',on_leave)

    root9.mainloop()

def deleterow(): # to delete the row
    global root10
    root10 = Tk()
    root10.geometry('350x100')
    root10.title('HDMS Editor v1.0')
    root10.resizable(False,False)
    global dp1
    lb1 = Label(root10,text='CustId:',font=('Ubuntu Sans Medium',12))
    lb1.grid(row=1,column=0,pady=(10,0),padx=(10,0))
    dp1 = Entry(root10,width=30,borderwidth=2,justify='center')
    dp1.grid(row=1,column=1,pady=(13,0),padx=(10,0))

    def on_enter(e):
        bt1['background'] = 'black'
        bt1['foreground'] = '#2693e6'
    def on_leave(e):
        bt1['background'] = '#2693e6'
        bt1['foreground'] = 'black'

    bt1 = Button(root10,text='Delete Record',command=del_row,width=30,
            border=0,
            bg='#2693e6',
            fg='black',
            relief='groove',
            activeforeground='black',
            activebackground='#2693e6'
                )
    bt1.grid(row=2,column=1,pady=(13,0),padx=(4,0))
    bt1.bind('<Enter>',on_enter)
    bt1.bind('<Leave>',on_leave)

    root10.mainloop()

def checkout():# to add checkout date 
    global root11
    root11 = Tk()
    root11.geometry('350x150')
    root11.title('HDMS Editor v1.0')
    root11.resizable(False,False)
    global cp1
    global cp2
    lb1 = Label(root11,text='CustId:',font=('Ubuntu Sans Medium',12))
    lb1.grid(row=1,column=0,pady=(10,0),padx=(10,0))
    cp1 = Entry(root11,width=30,borderwidth=2,justify='center')
    cp1.grid(row=1,column=1,pady=(13,0),padx=(10,0))
    # lb2 = Label(root11,text='Date:',font=('Ubuntu Sans Medium',12))
    # lb2.grid(row=2,column=0,pady=(10,0),padx=(10,0))
    # cp2 = Entry(root11,width=30,borderwidth=2,justify='center')
    # cp2.grid(row=2,column=1,pady=(13,0),padx=(10,0))

    def on_enter(e):
        bt1['background'] = 'black'
        bt1['foreground'] = '#2693e6'
    def on_leave(e):
        bt1['background'] = '#2693e6'
        bt1['foreground'] = 'black'

    bt1 = Button(root11,text='CheckOut',command=checkoutfunc,width=30,
            border=0,
            bg='#2693e6',
            fg='black',
            relief='groove',
            activeforeground='black',
            activebackground='#2693e6'
                )
    bt1.grid(row=3,column=1,pady=(13,0),padx=(4,0))
    bt1.bind('<Enter>',on_enter)
    bt1.bind('<Leave>',on_leave)

    root11.mainloop()

def refresh():
    root.destroy()
    mainwin()


def mainwin():
    global root
    root = Tk()
    root.geometry('950x450')
    root.title('HDMS v1.0')
    root.config(bg='#2693e6')

    #menu
    opmenu = Menu(root)
    root.config(menu=opmenu)

    optmenu = Menu(opmenu,tearoff=0)
    # optmenu.config(background='#2693e6')
    opmenu.add_cascade(label='Options',menu=optmenu)
    #menus#########################################
    #for reading
    readmenu = Menu(opmenu,tearoff=0)
    opmenu.add_cascade(label='Read',menu=readmenu)#cascade for adding menu in the field
    readmenu.add_command(label='Read all Details',command=readdata)
    readmenu.add_command(label='Read a Detail',command=read_a_data)
    readmenu.add_separator()
    #sub menu for custid#####
    custsub = Menu(readmenu,tearoff=0)
    readmenu.add_cascade(label='Get CustId',menu=custsub)
    custsub.add_command(label='By Mobile No',command=getid1)
    custsub.add_command(label='By Email',command=getid2)
    ################################

    ################################
    #for updating
    upmenu = Menu(opmenu,tearoff=0)
    opmenu.add_cascade(label='Update',menu=upmenu)#cascade for adding menu in the field
    upmenu.add_command(label='Add new',command=addnrow)
    upmenu.add_command(label='Update existing',command=rowupdate)
    upmenu.add_command(label='Delete existing',command=deleterow)
    #################################################
    #not sub menus
    optmenu.add_command(label='Check Out',command=checkout)
    #graphs sub menues
    gpmenu = Menu(optmenu,tearoff=0)
    optmenu.add_cascade(label='Graphs',menu=gpmenu)
    gpmenu.add_command(label='Graph of PayType',command=graph_pay)
    gpmenu.add_command(label='Graph of SuitType',command=graph_suit)
    optmenu.add_separator()
    optmenu.add_command(label='Refresh',command=refresh)
    optmenu.add_command(label='Exit',command=root.destroy)

    
    lb1 = Label(root,text='Hotel Database Management System',font=('Ubuntu Sans Medium',18),bg='#2693e6')
    lb1.pack()

    ondisview = table(root,read())

    root.mainloop()

if __name__ == '__main__':
    mainwin()