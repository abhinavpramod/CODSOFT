from tkinter import *
expression = ""
previous_result = None 
def press(num): 
    global expression
    global previous_result
    if previous_result is not None and expression == "":
        expression = str(previous_result)
    expression += str(num)
    equation.set(expression)
def equalpress(): 
    global expression
    global previous_result

    try: 
        total = str(eval(expression))
        equation.set(total)
        previous_result = total
        expression = ""
    except ZeroDivisionError:
        equation.set("Error")
        expression = ""
        previous_result = None
    except Exception as e:
        equation.set("Error")
        expression = ""
        previous_result = None
def clear(): 
    global expression 
    global previous_result
    
    expression = "" 
    equation.set("")
    previous_result = None
if __name__ == "__main__": 

    gui = Tk()  
    gui.configure(background="grey")
    gui.title("Calculator") 
    gui.geometry("1900x1200")
    equation = StringVar() 
    frame = Frame(gui, bg='grey')
    frame.place(relx=0.5, rely=0.5, anchor='center')
    expression_field = Entry(frame, textvariable=equation, font=('Arial', 24), bd=10)
    expression_field.grid(columnspan=4, ipadx=100, ipady=20, padx=10, pady=10) 
    button_texts = [
        ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('4', 3, 0), 
        ('5', 3, 1), ('6', 3, 2), ('7', 4, 0), ('8', 4, 1), 
        ('9', 4, 2), ('0', 5, 0), ('.', 6, 0), ('+', 2, 3), 
        ('-', 3, 3), ('x', 4, 3), ('/', 5, 3), ('=', 5, 2), 
        ('Clear', 5, 1)
    ]
    for (text, row, column) in button_texts:
        if text == 'Clear':
            button = Button(frame, text=text, fg='white', bg='black', command=clear, font=('Arial', 14), height=2, width=4)
        elif text == '=':
            button = Button(frame, text=text, fg='white', bg='black', command=equalpress, font=('Arial', 14), height=2, width=4)
        else:
            button = Button(frame, text=f' {text} ', fg='white', bg='black', command=lambda t=text: press(t), font=('Arial', 14), height=2, width=4)
        button.grid(row=row, column=column, padx=5, pady=5)
    gui.mainloop()