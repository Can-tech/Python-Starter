from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letter_list+symbol_list+number_list
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(END,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def handle_add():
    Website = website_input.get()
    Username=email_input.get()
    Password=password_input.get()
    new_data = {
        Website: {
            "email": Username,
            "password": Password
    }}
    # messagebox.showinfo(message="Password was saved!")
    if Password == "" or Username == "" :
        messagebox.showinfo(message="Fill the empty spaces!")
    else:
        try:
            with open("./29-password_manager/data.json","r") as file:
                #Reaing the old data
                data = json.load(file)            

        except FileNotFoundError:
            with open("./29-password_manager/data.json","w") as file:
                json.dump(new_data, file, indent=4)
                website_input.delete("0", "end")
                password_input.delete("0", "end")
        else:
            #Update the Data
            data.update(new_data)
            with open("./29-password_manager/data.json","w") as file:
                #Save the Data
                json.dump(data, file, indent=4)
                website_input.delete("0", "end")
                password_input.delete("0", "end")




# ---------------------------- SEARCH  ------------------------------- #
def handle_search():
    pass_and_mail=None
    data=None
    try:
        with open("./29-password_manager/data.json") as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="Data file was not found!")
    else:
        for (key, value) in data.items():
            if key == website_input.get():
                pass_and_mail=value
                pass_and_mail.update({'name':key})

            # if website_input.get() in data:
            #     email = data[website_input.get()]["email"]
            #     password = data[website_input.get()]["password"]
            #     messagebox.showinfo(title=website_input.get(), message=f"Email: {email} Password: {password}")
        if pass_and_mail==None:
            messagebox.showinfo(title="Not Found!",message="No password found for the website")
        else:
            messagebox.showinfo(title="Found!",message=f"Name: {pass_and_mail['name']}\nE-mail: {pass_and_mail['email']} \nPassword: {pass_and_mail['password']}")
                

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PasMan")
window.config(padx=50, pady=50)
# open("./29-password_manager/data.txt","w")

canvas = Canvas(width=200, height=200)

logo_img=PhotoImage(file="./29-password_manager/logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
website_input = Entry(width=32)
website_input.grid(column=1, row=1, columnspan=2, sticky="w")
website_password_search = Button(text="Search", width=14, command=handle_search)
website_password_search.grid(column=2, row=1, sticky="w")
website_input.focus()


email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2,sticky="EW")
email_input.insert(END, "name@mail.com")

password_label = Label(text="Password")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3,sticky="EW")
random_password_button = Button(text="Generate Password", command=generate_password)
random_password_button.grid(column=2,row=3,sticky="EW")

add_button = Button(text="Add", width=36, command=handle_add)
add_button.grid(column=1,row=4, columnspan=2,sticky="EW")

window.mainloop()