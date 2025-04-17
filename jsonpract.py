import tkinter as tk
from tkinter import messagebox
ui=tk.Tk()
ui.title("Practice")
ui.geometry("400x300")
import json
import os


FILENAME = "data.json"
product ={}
if os.path.exists(FILENAME):
    try:
        with open(FILENAME, "r") as f:
            product = json.load(f)
    except json.JSONDecodeError:
        product = {}
def add():
    try:
        prodint = pID.get()
        productid = int(prodint)
        Product = prod.get()
        pricint = pric.get()
        price = int(pricint)
        if productid in product:
            messagebox.showinfo("!!!","Already added")

        else:
            product[productid] = (Product, price)
            with open(FILENAME, "w") as f:
                json.dump(product, f)
    except Exception as e:
        print("Invalid input", e)
cartList = []
TotalPrice = 0
def cart():
    global IID,TotalPrice
    try:
        id = int(IID.get())
        if id in product:

            Product, price = product[id]
            TotalPrice +=price
            cartList.append((Product, price))
            for i in cartList:
                labelTotal.config(text=f"Total price: {TotalPrice}")
            return TotalPrice, Product
        else:
            messagebox.showinfo("!!!","ID does not exist")
    except:
        messagebox.showinfo("","invalid input")


def buy():
    global TotalPrice
    global cartList
    try:
        M = Money.get()
        money = int(M)
        price = TotalPrice
        Total.config(text=f" Total: {TotalPrice}")
        Total.grid(row=3, column=3)
        #price,Product = cart()
        if price > money:
            messagebox.showinfo("!!!","Not enough balance")
            Buy()
        else:
            remaining = money - price
            #product[id] = (Product, price)
            #if Product,price in product[id]:

            change.config(text=f"Change: {remaining}")
            change.grid(row=2,column=3)
            messagebox.showinfo("", "Transaction successful")
            TotalPrice = 0
            cartList.clear()
            labelTotal.config(text=f"Total price: {TotalPrice}")
            Buy()
    except Exception as v:
        print("invalid input", v)
#GUI LOGIC (SWITCHING SCREENS)
homepage = tk.Frame(ui)
addpage = tk.Frame(ui)
buypage = tk.Frame(ui)
Buying = tk.Frame(ui)

def erase():
    cart()
    IID.delete(0, tk.END)
def clearcart():
    cartList.clear()
#for BUYPAGE
IID = tk.Entry(buypage)
IID.grid(row=1, column=1)
#Button for the buypage
tk.Button(buypage, text="Add to cart", command=erase).grid(row=2, column=1)
tk.Button(buypage, text="Clear cart", command=clearcart).grid(row=5, column=1)
labelTotal = tk.Label(
    buypage,
    text="Total price:"
)
labelTotal.grid(row=2,rowspan=2,columnspan=2, column=2)

#for ADDPAGE
def eraseADD():
    add()
    pID.delete(0, tk.END)
    prod.delete(0, tk.END)
    pric.delete(0, tk.END)
#UI for add mode
tk.Label(addpage,text= "Product ID").grid(row=1,column=1)
pID = tk.Entry(addpage)
pID.grid(row=1, column=2)
tk.Label(addpage,text= "Product").grid(row=2,column=1)
prod = tk.Entry(addpage)
prod.grid(row=2, column=2)
tk.Label(addpage,text= "Price").grid(row=3,column=1)
pric = tk.Entry(addpage)
pric.grid(row=3, column=2)
tk.Button(addpage, text="Add product", command=eraseADD).grid(row=4, column=2)

#for buying
def moneyerase():
    buying()
    buy()
    Money.delete(0, tk.END)

tk.Label(Buying,text= "Money").grid(row=1,column=1)
Money = tk.Entry(Buying)
Money.grid(row=1, column=2)
tk.Button(Buying,text="confirm",command=moneyerase).grid(row=2,column=1)
Total = tk.Label(Buying, text= f" Total: ")
Total.grid(row=3,column=3)
change = tk.Label(Buying, text=f"Change: ")
change.grid(row=2,column=3)


def buying():
    if not cartList:# checks if carList is empty
        messagebox.showinfo("", "No items in cart")
        return
    else:
        Total.config(text=f" Total: {TotalPrice}")
        buypage.grid_forget()
        addpage.grid_forget()
        homepage.grid_forget()
        Buying.grid(row=0,column=0)

def Buy():
    change.config(text=f"Change: 0")
    change.grid(row=2, column=3)
    Buying.grid_forget()
    homepage.grid_forget()
    addpage.grid_forget()
    buypage.grid(row=0,column=0)

def Add():
    homepage.grid_forget()
    buypage.grid_forget()
    addpage.grid(row=0,column=0)
def Home():
    addpage.grid_forget()
    buypage.grid_forget()
    homepage.grid(row=0,column=0)
    tk.Button(homepage, text="ADD", command=Add).grid(row=2, column=2,)
    tk.Button(homepage, text="BUY", command=Buy).grid(row=2, column=3)
tk.Button(addpage, text="Back to home", command=Home).grid(row=4, column=1)
tk.Button(buypage, text="Back to home", command=Home).grid(row=3, column=1)
tk.Button(buypage, text="Buy", command= buying).grid(row=4, column=1)
Home()

ui.mainloop()



