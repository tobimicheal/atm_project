from tkinter import *
import bankbackend
import sqlite3

window = Tk()

window.wm_title("TOBI'S ATM")

balance = 0        


def get_selected_row(event):
	try:
		global selected_tuple
		index = list1.curselection()[0]
		selected_tuple= list1.get(index)
		e1.delete(0,END)
		e1.insert(END,selected_tuple[1])
		e2.delete(0,END)
		e2.insert(END,selected_tuple[2])
		e3.delete(0,END)
		e3.insert(END,selected_tuple[3])
		e4.delete(0,END)
		e4.insert(END,selected_tuple[4])

	except IndexError:
		pass
		

def acct_details ():
	global balance
	list1.delete(0,END)
	list1.insert(END,("Hello", acct_name.get()))
	list1.insert(END, ("your account number is ", acct_number.get()))
	list1.insert(END, ("and your balance is", balance))


def clear():
	list1.delete(0,END)
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)



def withdraw_fxn(amount):
	list1.delete(0,END)
	try:
		global balance
		if balance < amount:
			list1.insert(END,('Sorry, you have an insufficient Balance'))
		else:
			balance = balance - amount
			list1.insert(END, (acct_name.get(), "Your new balance is ",balance))
	except IndexError:
		pass

	

def deposit_fxn(amount):
	list1.delete(0,END)
	global balance
	try:
		balance += amount
		list1.insert(END,(acct_name.get(), "your new balance is ", balance))
	except ValueError:
		pass

def check_balance():
	list1.delete(0,END)
	global balance
	list1.insert (END, (acct_name.get(), " your account balance is ", balance))


list1 = Listbox (window, height = 6, width = 35)
list1.grid (row = 5, column = 1, rowspan = 6, columnspan = 2)
list1.bind('<<ListboxSelect>>',get_selected_row)


l1 = Label(window, text = 'Account name')
l1.grid (row = 0, column = 0)                           
	  
l2 = Label(window, text = 'Account number')
l2.grid (row = 2, column = 0)      

l3 = Label(window, text = 'Amount')
l3.grid (row = 1, column = 0)


acct_name = StringVar()
e1 =Entry (window, textvariable= acct_name)
e1.grid (row = 0, column = 1)


acct_number = IntVar()
e2 =Entry (window, textvariable = acct_number)
e2.grid (row = 2, column = 1)

amount = IntVar()
e3 =Entry (window, textvariable = amount)
e3.grid (row = 1, column = 1) 



b1=Button(window,text="deposit", width=20, command =lambda:deposit_fxn (int (e3.get() ) ) ) 
b1.grid(row=0,column=2)




b1=Button(window,text="Account Balance", width=20, command = check_balance)
b1.grid(row=1,column=2)



b1=Button(window,text="withdraw", width=20, command = lambda:withdraw_fxn(int (e3.get() ) )  )
b1.grid(row=3,column=1)


b1=Button(window,text="Account_details", width=20, command = acct_details)
b1.grid(row=2,column=2)


b1=Button(window,text="Clear", width=20, command = clear)
b1.grid(row=3,column=2)




window.mainloop()