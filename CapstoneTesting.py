import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import requests
import json

# 1UP5G2PUX1XAO5KM
window = tkinter.Tk()
window.title("Personal Stock Calculator")

frame = tkinter.Frame(window)
frame.pack()



def submit_data():

    accepted = accept_var.get()

    if accepted=="Accepted":

        search_label = search_entry.get()
        price_per_share = price_per_entry.get()
        if search_label and price_per_share:
            total_shares = total_shares_spinbox.get()
            investment_amount = investment_amount_entry.get()

            diviend_pay_label = diviend_pay_label_spinbox.get()
            calender_data_label = dividend_yield_input.get()
            dividend_check = dividend_status_var.get()

            
            print("Stock Ticker: ", search_label, "Price Per Share: ", price_per_share)
            print("Total Number of Shares: ", total_shares, "Investment Amount Total: ", investment_amount)
            print("Dividend Yield: ", diviend_pay_label, "Date", calender_data_label)
            print("Dividend Status:", dividend_check)
            print("-------------------------------")

            conn = sqlite3.connect('date.db') #creates the table
            table_create_query = '''CREATE TABLE IF NOT EXISTS Stock_Data
                    (search_label TEXT, price_per_share INT, total_shares INT, investment_amount INT, diviend_pay_label INT, calender_data_label INT, dividend_check TEXT)'''
            
            conn.execute(table_create_query)

            data_insert_query = '''INSERT INTO Stock_Data (search_label, price_per_share, total_shares, investment_amount, diviend_pay_label, calender_data_label, dividend_check) VALUES (?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (search_label, price_per_share, total_shares, investment_amount, diviend_pay_label, calender_data_label, dividend_check)
            cursor= conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()

            conn.close()
            
        else:
            tkinter.messagebox.showwarning(title="Error", message="Stock ticker and Price required")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have no accepted the terms")
    
    


def my_func():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+ question_entry.get()+"&outputsize=full&apikey=1UP5G2PUX1XAO5KM"
    api_request = requests.get(url)  #gets the url
    api = json.loads(api_request.content) #loads api and its content
    result = api_request.json() 
    allData = result["Time Series (Daily)"]  #Times Series (Daily) is only the stock market price for the whole year
    singleDayData = allData["2023-04-21"]  # We want stock market price for today's date (Holds 3 prices and volume)
    stock = tkinter.Label(window, text=singleDayData['1. open']) #This is the share price at open!
    stock.pack()



question_entry = tkinter.Entry(window)
question_entry.pack()

#Saving and storing stock info
stock_info_frame =tkinter.LabelFrame(frame, text="Stock Information")
stock_info_frame.grid(row= 0, column=0, padx=20, pady=10)
#Creating search label
search_label = tkinter.Label(stock_info_frame, text="Stock Ticker: ")
search_label.grid(row=0, column=0)
price_per_share = tkinter.Label(stock_info_frame, text="Enter Price Per Share:")
price_per_share.grid(row=0, column=1)

search_entry = tkinter.Entry(stock_info_frame) #Entry box for search engine
price_per_entry = tkinter.Entry(stock_info_frame) #Entry box for price per share

search_entry.grid(row=1, column=0)
price_per_entry.grid(row=1, column=1)
#Total number of shares the user will have
total_shares = tkinter.Label(stock_info_frame, text="Total Number of Shares:")
total_shares_spinbox = tkinter.Spinbox(stock_info_frame, from_=1, to=1000)
total_shares_spinbox.grid(row=1, column=2)
total_shares.grid(row=0, column=2)
#Total amount of $$ you will be getting for the stock
investment_amount = tkinter.Label(stock_info_frame, text="Investment Total:")
investment_amount.grid(row=2, column=0)
investment_amount_entry = tkinter.Entry(stock_info_frame) #Total amount entry label
investment_amount_entry.grid(row=3, column=0)

for widget in stock_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Saving Dividend Info
dividend_frame = tkinter.LabelFrame(frame)
dividend_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

dividend_label = tkinter.Label(dividend_frame, text="Dividend Status")
dividend_status_var = tkinter.StringVar()
dividend_check = tkinter.Checkbutton(dividend_frame, text="Does Stock have Dividend?", variable=dividend_status_var, onvalue="Has Dividend" , offvalue="No Dividend")
dividend_label.grid(row=0, column=0)
dividend_check.grid(row=1, column=0)


diviend_pay_label = tkinter.Label(dividend_frame, text="Dividend price per share:")
diviend_pay_label_spinbox = tkinter.Spinbox(dividend_frame, from_=0, to="infinity")
diviend_pay_label.grid(row=0, column=2)
diviend_pay_label_spinbox.grid(row=1, column=2)

calender_data_label = tkinter.Label(dividend_frame, text="Please enter date:")
dividend_yield_input = tkinter.Entry(dividend_frame)
calender_data_label.grid(row=0, column=3)
dividend_yield_input.grid(row=1, column=3)

for widget in dividend_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

    
# Accept terms   
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)
accept_var = tkinter.StringVar(value= "Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "Information is provided 'as is' and solely for informational purposes, not for trading purposes or advice.\n By Accepting the terms and conditions you agree with said statement.", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

#enter data button
button = tkinter.Button(frame, text='Submit data', command= submit_data)
button.grid(row=3, column=0)


#search button
search_button = tkinter.Button(frame, text="Search by stock ticker below:", command=my_func)
search_button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

window.mainloop()

