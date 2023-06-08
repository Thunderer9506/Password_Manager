from password_genrator import Password                                                #importing necessary modules
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- CONSONANTS ------------------------------- #

ONE = "#0077B6"
TWO = "#00B4D8"                                                                     #declared some variables so that i dont have to use it many times
THREE = "#90E0EF"
F = ('Roboto',10,'normal')

# ---------------------------- BUTTON FUNCTIONS ------------------------------- #

#Funciton is for submit button, firstly it will take the input and if there is no input then it is going to show error message
#and if all the details are filled then it will go through some exception handling which is about file not found error
#after that when every thing is good then it is going to be saved in a json file named as password
def display():
    web = (Website_entry.get()).title()
    ema = Email_entry.get()
    pa = Pass_entry.get()
    new_data = {
        web:{
            'Email': ema,
            'password':pa,
        }
    }
    if len(web) == 0 or len(pa) == 0:
        messagebox.showerror(title = "OOPS!", message = "You have left the blanks empty.")
    else:
        is_ok = messagebox.askokcancel(title = "Password Manager", message=f"These are the details you have entered: \nWebsite: {web}\nEmail: {ema}\nPassword: {pa} \nIs it OK to be saved?")
        if is_ok:
            #Error Checking
            try:
                with open("python/password manager/password.json", "r") as file:
                    data = json.load(file)          #1 step reading the data from the json file
            except FileNotFoundError:
                with open("python/password manager/password.json", "w") as file:
                    json.dump(new_data,file,indent=4)
            else:   
                with open("python/password manager/password.json", "w") as file:
                    data.update(new_data)           #2 making it ready for the new data or updating the old data with new data
                    json.dump(data,file,indent=4)   #3 step writing the data in json file
            finally:
                Website_entry.delete(0, END)
                Pass_entry.delete(0, END)

#Function for the search button, it will get the input from website entry, function will check for the website name and if it exist in it then
#it will give you detail through message box and if not then it is going to show the error message
def find_password():
    website = (Website_entry.get()).title()
    #Error checking
    try:
        with open("python/password manager/password.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title = "File Not Found", message = "No Data file Found")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]['password']
            messagebox.showinfo(title = "Your Data", message = "Website: "+website+"\nEmail: "+email+"\nPassword: "+password)
        else:
            messagebox.showerror(title = "Data not found", message = "No detail for the website exists")

#Function for the generate button it will generate a new password and remove the previous password and it will copy it for you
def fill_entry():
    a = Password().passw()
    Pass_entry.delete(0, END)                                              
    Pass_entry.insert(0, a) 
    pyperclip.copy(a)

# ---------------------------- UI SETUP ------------------------------- #

#making of the screen
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background=THREE)

#putting an image on the screen
canvas = Canvas(height=200,width=200, highlightthickness=0,background=THREE)
lock_img = PhotoImage(file="python/password manager/logo.png")                              
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#Label
Website = Label(text='Website:',foreground=ONE,font=F,background=THREE).grid(row=1, column=0)
Email = Label(text='Email/Username:',foreground=ONE,font=F,background=THREE).grid(row=2, column=0)
Pass = Label(text='Password:',foreground=ONE,font=F,background=THREE).grid(row=3, column=0)

#Where we are going to fill details
Website_entry = Entry(width = 40)
Website_entry.grid(row=1, column=1)
Website_entry.focus()
Email_entry = Entry(width = 53)
Email_entry.grid(row=2, column=1, columnspan=2)
Email_entry.insert(0,"srivastavashaurya225@gmail.com")
Pass_entry = Entry(width = 40)
Pass_entry.grid(row=3, column=1)

#Buttons
Search = Button(text='Search',command=find_password,width=8,foreground=THREE,background=ONE,font=F)                # To search about the website's password
Search.grid(row=1,column=2)

Submit = Button(text='Submit',command = display,width=39,foreground=THREE,background=ONE,font=F)                                        #submit button
Submit.grid(row=4, column=1, columnspan=2)

Generate = Button(text='Generate',command=fill_entry,width=8,foreground=THREE,background=ONE,font=F)                                   #generate button
Generate.grid(row=3, column=2)

window.mainloop()