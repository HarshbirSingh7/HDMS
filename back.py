import pandas as pd
from tkinter import messagebox
import random
import datetime as dtt

alchar = ['Q','P','T','W','A','E','B','C','Z']
nuchar = ['1','2','3','4','5','6','7','8','9','0']
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
df = pd.read_csv("Hotel.csv")

def get_idx(id):#customer id to be used
    r = df[df['CustId']==id].index.to_numpy()
    return r[0]

def read():
    df = pd.read_csv("Hotel.csv")
    return(df)

def readp(id): #customer id to be used
    r = df.iloc[get_idx(id)]
    return r
def readpo(id,col):#id,col
    r = df.at[get_idx(id),col]
    n = df.at[get_idx(id),"CustName"]
    return f'User ID: {id}\nCustomer Name: {n}\n{col}: {r}'

def readcol(col): # reads whole column and gives it as list
    rc = df[col].to_numpy().tolist()
    trc = str(rc)
    return trc

def addrow(roomno,name,mobile,email,suit,pay,bdate,days):#cpd and checkout date
    id1 = random.choice(alchar)+random.choice(nuchar)+random.choice(nuchar)+random.choice(nuchar)
    row = len(df['CustId'].to_list()) # getting the row where to add
    cpd = 0
    if suit == "standard" or suit == "Standard" or suit == "STANDARD":
        cpd += 4500
    elif suit == 'deluxe' or suit == 'Deluxe' or suit == "DELUXE":
        cpd += 6500
    elif suit == 'economy' or suit == 'Economy' or suit == 'ECONOMY':
        cpd += 2500
    else:
        messagebox.showerror("ERROR","PLEASE ENTER A CORRECT SUIT TYPE!!")
        exit()
    totalc = cpd*days
    #converting bdate string into date and calculating check out date
    bvar = bdate.split('-')
    day = bvar[0].strip()
    month = bvar[1].strip()
    year = int(bvar[2].strip())+2000
    monthno = 0
    try:
        if month in months:
            monthno = int(months.index(month))+1
    except ValueError:
        messagebox.showerror("ERROR","PLEASE ENTER A CORRECT MONTH NAME!!") 
        exit()
    except Exception as e:
        messagebox.showerror("ERROR",e)
        exit()
    else:
        if day[0] == "0":
            day = int(day[1])
            bvardate = dtt.date(year,monthno,day)
        else:
            bvardate = dtt.date(year,monthno,int(day))
        # print(bvardate)
    # adding checkout date
    cvardate = str(bvardate+dtt.timedelta(days)).split('-')
    cyear = str(int(cvardate[0].strip())-2000)
    cday = cvardate[2].strip()
    cmonthno = cvardate[1].strip()
    try:
        if cmonthno[0] == "0":
            cmonthno = int(cmonthno[1])-1
        else:
            cmonthno = int(cmonthno)-1
    except Exception as e:
        messagebox.showerror("ERROR",e)
        exit()
    else:
        cmonth = months[cmonthno]
    checkdate = cday+'-'+cmonth+'-'+cyear
    # print(checkdate)
      
    df.loc[row] = [int(roomno),id1,name,int(mobile),email,suit,cpd,pay,bdate,checkdate,time_fill(),'',days,totalc,'CheckIn']
    df.to_csv('Hotel.csv',index=False)
    # return f'Customer Acc. {id1} of {name} has been Created!!'

def delrow(id):
    try:
        row = get_idx(id)
        df.drop(row,axis=0,inplace=True)
        df.to_csv('Hotel.csv',index=False)
        messagebox.showinfo('Editor','The Record Has Been Deleted!')
        # return f"Customer ID {id} Has Been Deleted"
    except:
        messagebox.showerror("ERROR",f'The Enterd ID {id} is INVALID!!!')

def editrow(roomno,id1,name,mobile,email,suit,pay,bdate,days): #to edit an entire row
    row = get_idx(id1)
    cpd = 0
    if suit == "standard" or suit == "Standard" or suit == "STANDARD":
        cpd += 4500
    elif suit == 'deluxe' or suit == 'Deluxe' or suit == "DELUXE":
        cpd += 6500
    elif suit == 'economy' or suit == 'Economy' or suit == 'ECONOMY':
        cpd += 2500
    else:
        messagebox.showerror("ERROR","PLEASE ENTER A CORRECT SUITE TYPE!!")
        exit()
    totalc = cpd*days
    bvar = bdate.split('-')
    day = bvar[0].strip()
    month = bvar[1].strip()
    year = int(bvar[2].strip())+2000
    monthno = 0
    try:
        if month in months:
            monthno = int(months.index(month))+1
    except ValueError:
        messagebox.showerror("ERROR","PLEASE ENTER A CORRECT MONTH NAME!!")
        exit()
    except Exception as e:
        messagebox.showerror("ERROR",e)
        exit()
    else:
        if day[0] == "0":
            day = int(day[1])
            bvardate = dtt.date(year,monthno,day)
        else:
            bvardate = dtt.date(year,monthno,int(day))
        # print(bvardate)
    # adding checkout date
    cvardate = str(bvardate+dtt.timedelta(days)).split('-')
    cyear = str(int(cvardate[0].strip())-2000)
    cday = cvardate[2].strip()
    cmonthno = cvardate[1].strip()
    try:
        if cmonthno[0] == "0":
            cmonthno = int(cmonthno[1])-1
        else:
            cmonthno = int(cmonthno)-1
    except Exception as e:
        messagebox.showerror("ERROR",e)
        exit()
    else:
        cmonth = months[cmonthno]
    checkdate = cday+'-'+cmonth+'-'+cyear
    df.loc[row] = [int(roomno),id1,name,int(mobile),email,suit,cpd,pay,bdate,checkdate,filldata(id1,'CheckINTime'),'',days,totalc,'CheckIn']
    df.to_csv('Hotel.csv',index=False)

def editrowp(id1,col,coldata): # to edit a column data
    row = get_idx(id1)
    df.at[row,col] = coldata
    df.to_csv('Hotel.csv',index=False)

def filldata(id,col): # to fill the entry boxes with existing data
    rowindex = get_idx(id)
    data = df.at[rowindex,col]
    return data

def get_id(col,value): # to get cust id
    try:
        idx = df[df[col]==value].index.to_numpy()
        custid = df.at[idx[0],'CustId']
        return custid
    except:
        messagebox.showerror("ERROR",f'The Entered Value for {col} is INVALID!!!')

def bdate_fill():
    dateb = dtt.datetime.today().date()
    day = str(dateb.day)
    month = int(dateb.month)
    year = int(dateb.year)
    monthname = months[month-1]
    str_year = str(year-2000)
    return f'{day}-{monthname}-{str_year}'

def time_fill():
    time = dtt.datetime.today().time()
    return f'{time:%I:%M:%S %p}'

def datecheck(id1): # to check wheter the checkout date is same if not then makes required changes
    cdate = filldata(id1,'CheckOutDate')
    bdate = filldata(id1,'BookDate')
    cpd = filldata(id1,'CPD')
    # converting in datetime format
    #checkout date
    cdate_split = cdate.split('-')
    day = int(cdate_split[0].strip())
    month = int(months.index(cdate_split[1].strip())+1)
    year = int(cdate_split[2].strip())+2000
    date = dtt.date(year,month,day)
    #book date
    bdate_split = bdate.split('-')
    bday = int(bdate_split[0].strip())
    bmonth = int(months.index(bdate_split[1].strip())+1)
    byear = int(bdate_split[2].strip())+2000
    bbdate = dtt.date(byear,bmonth,bday)
    # now comparing the dates
    today = dtt.datetime.today().date()
    if date != today:
        days = today-bbdate
        day = str(today.day)
        monthname = months[int(today.month)-1]
        year = str(today.year-2000)
        if days.days ==  0:
            DAY = 1
            return f'{day}-{monthname}-{year}', int(DAY), int(cpd)*1
        else:
            return f'{day}-{monthname}-{year}', int(days.days), int(cpd)*int(days.days)
    else:
        return cdate, int(filldata(id1,'Days')), int(filldata(id1,'Total'))
