import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox

df = pd.read_csv('Hotel.csv')

def graph_pay():
    cash = 0
    upi = 0
    card = 0

    x = df['PayType'].tolist()
    a = list(df['PayType'].drop_duplicates())
    # print(a)
    for y in x:
        if y == 'Cash' or y == 'cash' or y == 'CASH':
            cash += 1
        elif y == 'upi' or y == 'UPI' or y == 'Upi':
            upi += 1
        elif y == 'card' or y == 'CARD' or y == 'Card':
            card += 1
    try:
        plt.bar(a,[card,upi,cash])
        plt.xlabel('Payment Mode')
        plt.ylabel('Number of Customers')
        plt.title("Payment Mode Used By Customers")
        plt.show()
    except ValueError:
        messagebox.showerror('ERROR','Please Add More Records(min 3 records)!')
    except Exception as e:
        messagebox.showerror('ERROR',e)

def graph_suit():
    delx = 0
    stand = 0
    eco = 0
    x = df['SuitType'].tolist()
    b = list(df['SuitType'].drop_duplicates())
    for y in x:
        if y == 'deluxe' or y == 'DELUXE' or y == 'Deluxe':
            delx += 1
        elif y == 'Standard' or y == 'STANDARD' or y == 'standard':
            stand += 1
        elif y == 'Economy' or y == 'ECONOMY' or y == 'economy':
            eco += 1
    try:
        plt.bar(b,[delx,stand,eco])
        plt.xlabel('Suite Types')
        plt.ylabel('Number of Customers')
        plt.title("Suite Booked By Customers")
        plt.show()
    except ValueError:
        messagebox.showerror('ERROR','Please Add More Records(min 3 records)!')
    except Exception as e:
        messagebox.showerror('ERROR',e)



