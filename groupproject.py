from tkinter import *
from tax import taxrate


# Build GUI #
window = Tk()
window.title('Monterey County Sales Tax Calculator')
window.geometry('450x400')
window.resizable(0, 0)
window.config(bg='gray')

#price array
num_inputs = 10
inputs = []
def add_input():
   n = len(inputs)
   new_input = {}
   new_input['value'] = DoubleVar()
   new_input['label'] = Label(window, text=f'{i + 1}.', font=('Arial'), bg='gray').place(x=15, y=30 + 25 * n)
   new_input['entry'] = Entry(window, textvariable=new_input['value'], font=('Arial'), justify='center', bg='#ADD8E6').place(x=40, y=30 + 25 * n)
   inputs.append(new_input)

for i in range(num_inputs):
   add_input()

# tax calculation
def total():

   addition = sum(map(lambda inp: inp['value'].get(), inputs))
   taxed = round(taxrate(zipcodeEntry.get()) * addition, 2)
   total = round(addition + taxed, 2)

   additionLabel.config(text=str(addition))
   taxLabel.config(text=str(taxed))
   totalLabel.config(text=str(total))


# Creates numerical labels to display a list appearance within the GUI for entry boxes. #
lbprice = Label(window, text='Prices of Items', font=('Arial'), bg='gray').place(x=75, y=5)
lbregtotal = Label(window, text='Total Without Tax', font=('Arial'), bg='gray').place(x=267, y=5)
lbsalestax = Label(window, text='Sales Tax Applied', font=('Arial'), bg='gray').place(x=263, y=55)
lbtaxtotal = Label(window, text='Total With Tax', font=('Arial'), bg='gray').place(x=277, y=105)


additionLabel = Label(window, height=1, width=20, font=('Arial'), bg='#FED8B1')
additionLabel .place(x=240, y=30)
taxLabel = Label(window, height=1, width=20, font=('Arial'), bg='#FF7F7F')
taxLabel.place(x=240, y=80)
totalLabel = Label(window, height=1, width=20, font=('Arial'), bg='#90EE90')
totalLabel.place(x=240, y=130)

# Buttons For GUI
calculateButton = Button(window, text='Calculate', command=total, bg='#90EE90').place(x=300, y=165)

#zipcode
def enterZipcode():
   zipcodemessage = 'Your zipcode is ' + zipcodeEntry.get() + \
                    ' and the tax rate is ' + str(taxrate(zipcodeEntry.get())*100) +'%'
   showzipcodeLabel = Label(window, text=zipcodemessage)
   showzipcodeLabel.place(x=140, y=290)
   return zipcodeEntry.get()

zipcodeLabel = Label(window, text='Enter your Zipcode')
zipcodeLabel.place(x=264, y=205)
zipcodeEntry = Entry(window)
zipcodeEntry.place(x=240, y=230)
zipcodeButton = Button(window, text='Enter ZipCode',command=enterZipcode)
zipcodeButton.place(x=300, y= 260)

window.mainloop()

