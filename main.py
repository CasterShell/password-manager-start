import tkinter
from tkinter import PhotoImage
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

#keyword format [new_item for item in list]
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_box.insert(0, password)
    pyperclip.copy(password) #once the pass is gen it will be added to your clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
#inputs by user hitting add must be recorded and added.

def save():
    website = website_entry.get()
    username = user_name_em.get()
    password = password_box.get()
    new_data = {website:{
        "email": username,
        "password": password
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        try:
            with open("user.json", "r") as data_file:
            #entry = f"Website: {website}, Email/Username: {username}, Password:{password}\n"
            #file.write(entry)
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent= 4)
        else:
            data.update(new_data)
            with open("user.json","w") as data_file:
             json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            user_name_em.delete(0, tkinter.END)
            password_box.delete(0, tkinter.END)

# ---------------------------- PASSWORD VISIBILITY ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)



#Logo set up below
canvas = tkinter.Canvas(height=200, width=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= lock_image)
canvas.grid(column=1, row = 0)

#website label and input
#should we make this OOP for fun?
website_label = tkinter.Label()
website_label.config(text="Website:", padx=10)
website_label.grid(column=0, row=1)

website_entry = tkinter.Entry()
website_entry.config(width=35,)
website_entry.grid(column=1, row=1, columnspan=2, sticky ="w")
website_entry.focus()

#email/username text and entry
em_user_name = tkinter.Label()
em_user_name.config(text="Email/Username:", padx=10)
em_user_name.grid(column=0,row=2)

user_name_em = tkinter.Entry()
user_name_em.config(width=35)
user_name_em.insert(0,"k3noms@gmail.com")
user_name_em.grid(column = 1, row=2, columnspan=2, sticky = "w")

#password UI and entry and button below
password_text = tkinter.Label()
password_text.config(text="Password:")
password_text.grid(column=0, row=3)

password_box = tkinter.Entry()
password_box.config(width=35,show="*")
password_box.grid(column=1, row=3, sticky ="w")

password_button = tkinter.Button()
password_button.config(text="Generate Password",command = generate_password, width=30,)
password_button.grid(column=1, row=4, columnspan=2, sticky="w")


#add button
add_button = tkinter.Button()
add_button.config(text="Add", width=30,command = save)
add_button.grid(column=1, row=5, columnspan=2,sticky="w")

window.mainloop()