# Import Libraries #
from tkinter import *
# Imports all functions from the tkinter library. #

# Build GUI #
window = Tk()
# Beginning code to construct GUI for Sales Tax Calculator. #
window.title('Monterey County Sales Tax Calculator')
# Displays title of application in GUI. #
window.geometry('450x300')
# Based dimensions of the GUI window. #
window.resizable(0, 0)
# Locks the base dimensions of the GUI window. #
window.config(bg='gray')
# Background color palette of the GUI window. #

# Defining Functions #
def total():
    int0 = e0_value.get()
    int1 = e1_value.get()
    int2 = e2_value.get()
    int3 = e3_value.get()
    int4 = e4_value.get()
    int5 = e5_value.get()
    int6 = e6_value.get()
    int7 = e7_value.get()
    int8 = e8_value.get()
    int9 = e9_value.get()
    # Gathers the inputted values of the entry boxes as variables for equation. #
    addition = int0 + int1 + int2 + int3 + int4 + int5 + int6 + int7 + int8 + int9
    # Equation for total cost w/o sales tax applied. #
    tax = round(0.0925 * addition, 2)
    # Equation for sales tax applied by utilizing addition variable and the county sales tax % rate. #
    total = round(addition + tax, 2)
    # Equation for total cost w/ sales tax applied utilizing the addition and tax variables. #
    t1.delete('1.0', END)
    t1.insert(END, addition)
    t2.delete('1.0', END)
    t2.insert(END, tax)
    t3.delete('1.0', END)
    t3.insert(END, total)
    # Deletes and inserts output values into provided text boxes of the GUI. #

# String Conversions #
e0_value = IntVar()
e1_value = IntVar()
e2_value = IntVar()
e3_value = IntVar()
e4_value = IntVar()
e5_value = IntVar()
e6_value = IntVar()
e7_value = IntVar()
e8_value = IntVar()
e9_value = IntVar()
# Converts all the entry boxes values into integer variables for later use of the def total function. #

# Labels For GUI #
lb0 = Label(window, text='1.', font=('Arial'),  bg='gray').place(x=15, y=30)
lb1 = Label(window, text='2.', font=('Arial'),  bg='gray').place(x=15, y=55)
lb2 = Label(window, text='3.', font=('Arial'),  bg='gray').place(x=15, y=80)
lb3 = Label(window, text='4.', font=('Arial'),  bg='gray').place(x=15, y=105)
lb4 = Label(window, text='5.', font=('Arial'),  bg='gray').place(x=15, y=130)
lb5 = Label(window, text='6.', font=('Arial'),  bg='gray').place(x=15, y=155)
lb6 = Label(window, text='7.', font=('Arial'),  bg='gray').place(x=15, y=180)
lb7 = Label(window, text='8.', font=('Arial'),  bg='gray').place(x=15, y=205)
lb8 = Label(window, text='9.', font=('Arial'),  bg='gray').place(x=15, y=230)
lb9 = Label(window, text='10.', font=('Arial'), bg='gray').place(x=10, y=255)
# Creates numerical labels to display a list appearance within the GUI for entry boxes. #
lbprice = Label(window, text='Prices of Items', font=('Arial'), bg='gray').place(x=75, y=5)
lbregtotal = Label(window, text='Total Without Tax', font=('Arial'), bg='gray').place(x=267, y=5)
lbsalestax = Label(window, text='Sales Tax Applied', font=('Arial'), bg='gray').place(x=263, y=55)
lbtaxtotal = Label(window, text='Total With Tax', font=('Arial'), bg='gray').place(x=277, y=105)
# Creates labels to display descriptions of outputs for text boxes within the GUI. #

# Entry Boxes For GUI #
e0 = Entry(window, textvariable=e0_value, font=('Arial'), justify='center', bg='#ADD8E6').place(x=40, y=30)
e1 = Entry(window, textvariable=e1_value, font=('Arial'), justify='center', bg='#ADD8E6').place(x=40, y=55)
e2 = Entry(window, textvariable=e2_value, font=('Arial'), justify='center', bg='#ADD8E6').place(x=40, y=80)
e3 = Entry(window, textvariable=e3_value, font=('Arial'), justify='center', bg='#ADD8E6').place(x=40, y=105)
e4 = Entry(window, textvariable=e4_value, font=('Arial'), justify='center', bg='#ADD8E6').place(x=40, y=130)
e5 = Entry(window, textvariable=e5_value, font=('Arial'), justify='center', bg='#ADD8E6').place(x=40, y=155)
e6 = Entry(window, textvariable=e6_value, font=('Arial'), justify='center', bg='#ADD8E6').place(x=40, y=180)
e7 = Entry(window, textvariable=e7_value, font=('Arial'), justify='center', bg='#ADD8E6').place(x=40, y=205)
e8 = Entry(window, textvariable=e8_value, font=('Arial'), justify='center', bg='#ADD8E6').place(x=40, y=230)
e9 = Entry(window, textvariable=e9_value, font=('Arial'), justify='center', bg='#ADD8E6').place(x=40, y=255)
# Creates entry boxes to temporarily store input values within the GUI for use in the def total function. #

# Text Boxes For GUI #
t1 = Text(window, height=1, width=20, font=('Arial'), bg='#FED8B1')
t1.place(x=240, y=30)
t2 = Text(window, height=1, width=20, font=('Arial'), bg='#FF7F7F')
t2.place(x=240, y=80)
t3 = Text(window, height=1, width=20, font=('Arial'), bg='#90EE90')
t3.place(x=240, y=130)
# Creates text boxes to display outputs calculated by the def total function within the GUI. #

# Buttons For GUI
b1 = Button(window, text='Calculate', command=total, bg='#90EE90').place(x=300, y=165)
# Creates the GUI for the Calculate button to be used to execute def total function code/settings. #

# Loop GUI #
window.mainloop()
# Loops the GUI to be continuous until all functions are executed or terminated as an application. #