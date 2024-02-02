from tkinter import *
from decimal import Decimal
import os

def create_component(window: Tk, row:int, col:int, text:str):
    """
    Creat a "text:(input)" box on the window
    :param text: text that want to display
    :param window: A Tk window
    :param row: row location of window
    :param col: col location of window
    :return: Return the value inside entry box. And create a component at (row,col),(row,col+1)
    """
    component_text = Label(window,text=f"{text}",font=("Arial Bold", 20))
    component_text.grid(row=row, column=col)
    component_Entry = Entry(window,font=("Arial Bold", 20))
    component_Entry.grid(row=row, column=col+1)
    return component_Entry

def calculate():
    """"""
    values_in_string = [entry.get() for entry in entries] #[credit_expense, credit income, debit_expense, debit_income]

    credit_net_income = Decimal(values_in_string[0]) - Decimal(values_in_string[1])
    debit_net_income = Decimal(values_in_string[2]) - Decimal(values_in_string[3])

    amount_calculated.config(text=f"Credit Card Net Income: {credit_net_income}, Debit Card Net Income: {debit_net_income}")
    amount_calculated.grid(row=6, column=0, columnspan=2)

    calculate_button.config(text="Is this amount correct?(Y/N)")
    yes_button.grid(row=7,column=0)
    no_button.grid(row=7, column=1)
    calculate_button.config(state = DISABLED)

def enable_recalculation():
    """"""
    calculate_button.config(state='normal',text="Recalculate the amount")
    for entry in entries:
        entry.delete(0, END)
    amount_calculated.grid_remove()
    yes_button.grid_remove()
    no_button.grid_remove()

def update_and_save_values():
    f = open("C:\\Users\\Ethan Zhang\\Desktop\\Total_money.txt", "a")
    # f = open("C:\\Users\\Ethan Zhang\\Desktop\\Money_Manage.txt", "w")

if __name__ == '__main__':
    window = Tk()
    window.geometry("657x520")  # window's size
    window.title("Money Manager!")  # window's title

    entries = [
        create_component(window, row=0, col=0, text="Credit Card Expense:"),
        create_component(window, row=1, col=0, text="Credit Card Income:"),
        create_component(window, row=2, col=0, text="Debit Card Expense:"),
        create_component(window, row=3, col=0, text="Debit Card Income:")
    ]

    calculate_button = Button(window, text="Calculate the amount", command=calculate,font=("Arial Bold", 20))
    calculate_button.grid(row=4, column=0,columnspan=2)

    amount_calculated = Label(window,font = ("Arial Bold", 13))
    yes_button = Button(window, text = "Yes", command=update_and_save_values, font=("Arial Bold", 20))
    no_button = Button(window, text = "No", command=enable_recalculation, font=("Arial Bold", 20))

    window.mainloop() #