from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def populate_generated_password():
  password = generate_password()
  pyperclip.copy(password)
  password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def entry_validation(entry_text: str, field_name: str) -> bool:
    if len(entry_text) == 0:
        messagebox.showwarning("Warning", f"{field_name} cannot be empty")
        return False
    return True


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if (
        entry_validation(website, "website")
        and entry_validation(email, "email")
        and entry_validation(password, "password")
    ):
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it ok to save?",
        )

        if is_ok:
            with open("password.txt", mode="a") as date_file:
                date_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="./logo.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(row=1, column=0)
email_username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=21)

website_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

website_entry.focus()
email_entry.insert(0, "pdeng.ps@gmail.com")
generate_password_button = Button(text="Generate Password", command=populate_generated_password)
add_button = Button(text="Add", width=36, command=save)

generate_password_button.grid(row=3, column=2)
add_button.grid(
    row=4,
    column=1,
    columnspan=2,
)
window.mainloop()
