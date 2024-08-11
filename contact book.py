from tkinter import *
from tkinter import messagebox

def close_window():
    root.destroy()
def minimize_window():
    root.iconify()
def toggle_maximize_window():
    global is_maximized
    if is_maximized:
        root.geometry('700x550')
        root.resizable(0, 0)
        is_maximized = False
    else:
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        root.resizable(1, 1)
        is_maximized = True
root = Tk()
root.geometry('700x550')
root.config(bg='#d3f3f5')
root.title('Contact Book')
root.resizable(0, 0)
is_maximized = False
contactlist = []
Name = StringVar()
Number = StringVar()
frame = Frame(root)
frame.pack(side=RIGHT, fill=Y)
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('ariel', 14),
                 bg="#f0fffc", width=30, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)
def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "select a contact")
        return None
    else:
        return int(select.curselection()[0])
def AddContact():
    if Name.get() and Number.get():
        contactlist.append([Name.get(), Number.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Success", "added new contact")
    else:
        messagebox.showerror("Error", "Please fill in the information")
def UpdateDetail():
    if Name.get() and Number.get():
        index = Selected()
        if index is not None:
            contactlist[index] = [Name.get(), Number.get()]
            Select_set()
            EntryReset()
            messagebox.showinfo("Success", "Updated contact")
    else:
        messagebox.showerror("Error", "Please fill in the information")
def Delete_Entry():
    index = Selected()
    if index is not None:
        result = messagebox.askyesno('', 'Do you want to delete the selected contact?')
        if result:
            del contactlist[index]
            Select_set()
            EntryReset()
    else:
        messagebox.showerror("Error", 'Please select a contact')
def VIEW():
    index = Selected()
    if index is not None:
        NAME, PHONE = contactlist[index]
        Name.set(NAME)
        Number.set(PHONE)
def Select_set():
    select.delete(0, END)
    for contact in contactlist:
        select.insert(END, contact[0])
def EntryReset():
    Name.set("")
    Number.set("")
entry_frame = Frame(root)
entry_frame.pack(side=LEFT, padx=10, pady=10)

Label(entry_frame, text="Name:").pack()
name_entry = Entry(entry_frame, textvariable=Name, font=('ariel', 14))
name_entry.pack()

Label(entry_frame, text="Phone Number:").pack()
number_entry = Entry(entry_frame, textvariable=Number, font=('ariel', 14))
number_entry.pack()

Button(entry_frame, text="Add Contact", command=AddContact).pack(pady=5)
Button(entry_frame, text="Update Contact", command=UpdateDetail).pack(pady=5)
Button(entry_frame, text="Delete Contact", command=Delete_Entry).pack(pady=5)
Button(entry_frame, text="View Contact", command=VIEW).pack(pady=5)
root.mainloop()
