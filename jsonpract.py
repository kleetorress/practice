import tkinter as tk
from tkinter import messagebox
ui=tk.Tk()
ui.title("Practice")
ui.geometry("400x300")
import json
#import os

FILENAME = "data.json"
product ={}
def add():
    try:
        ID = tk.Entry(buypage)
        ID.grid(row=1, column=1)
        productid = ID.get()
        if productid in product:
            print("Already added")
        else:
            Product = input("Product: ")
            price = int(input("Price: "))
            product[productid] = (Product, price)
            with open(FILENAME, "w") as f:
                json.dump(product, f)
    except:
        print("Invalid input")
def cart():
    TotalPrice=0
    ID = tk.Entry(buypage)
    ID.grid(row=1, column=1)
    id = ID.get()
    if id in product:

        Product, price = product[id]
        TotalPrice +=price

        return TotalPrice, Product
def save():

def buy():
    try:
        tk.Label(buypage,text="Money").grid(row=0,column=0)
        money = int(input("Money"))
        price, Product = cart()

        if price > money:
            print("Not enough balance")
        else:
            remaining = money - price
            product[id] = (Product, price)
            #if Product,price in product[id]:
            label = tk.Label(
                text="Hello"
            )
            print(f"Product: {Product} \n Total: {price}")
            print(f"Remainin balance: {remaining}")
    except:
        print("invalid input")
#GUI LOGIC (SWITCHING SCREENS)
homepage = tk.Frame(ui)
addpage = tk.Frame(ui)
buypage = tk.Frame(ui)

def Buy():
    homepage.grid_forget()
    addpage.grid_forget()
    buypage.grid(row=0,column=0)
    cart()
def Add():
    homepage.grid_forget()
    buypage.grid_forget()
def Home():
    addpage.grid_forget()
    buypage.grid_forget()
    homepage.grid(row=0,column=0)
    tk.Button(homepage, text="ADD", command=add).grid(row=2, column=2,)
    tk.Button(homepage, text="BUY", command=Buy).grid(row=2, column=3)
Home()

ui.mainloop()



