import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("530x600") 
root.resizable(False, False)
root.configure(bg="#15171a")

label_result = tk.Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

equation = ""
def update_display(number):
    global equation
    equation += str(number)
    label_result.config(text=equation)


def clear_result():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculator():
    global equation
    result = ""
    if equation !="":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation =""
    label_result.config(text=result)


def create_round_button(root, x, y, radius, text):
    root.create_oval(x - radius, y - radius, x + radius, y + radius, fill='orange', outline='orange')
    root.create_text(x, y, text=text, fill='white')

# Corrected the color code and font parameters

tk.Button(root, text="AC", width=4, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#3b3e45", command=clear_result).place(x=20, y=110)
tk.Button(root, text=".", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff", bg="#3b3e45",command=lambda: update_display('.')).place(x=145, y=110)
tk.Button(root, text="%", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff", bg="#3b3e45", command=lambda: update_display('%')).place(x=272, y=110)
tk.Button(root, text="/", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff", bg="orange",command=lambda: update_display('/')).place(x=400, y=110)


tk.Button(root, text="7", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff", bg="black", command=lambda: update_display(7)).place(x=20, y=210)
tk.Button(root, text="8", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff", bg="black",command=lambda: update_display(8)).place(x=145, y=210)
tk.Button(root, text="9", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff", bg="black", command=lambda: update_display(9)).place(x=272, y=210)
tk.Button(root, text="*", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff", bg="orange", command=lambda: update_display('*')).place(x=400, y=210)


tk.Button(root, text="4", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff", bg="black", command=lambda: update_display(4)).place(x=20, y=310)
tk.Button(root, text="5", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff", bg="black", command=lambda: update_display(5)).place(x=145, y=310)
tk.Button(root, text="6", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff", bg="black", command=lambda: update_display(6)).place(x=272, y=310)
tk.Button(root, text="-", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff",bg="orange", command=lambda: update_display('-')).place(x=400, y=310)


tk.Button(root, text="1", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff", bg="black", command=lambda: update_display(1)).place(x=20, y=410)
tk.Button(root, text="2", width=4, height=1, font=("arial", 30, "bold"), fg="#fff", bg="black", command=lambda: update_display(2)).place(x=145, y=410)
tk.Button(root, text="3", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff", bg="black", command=lambda: update_display(3)).place(x=272, y=410)
tk.Button(root, text="+", width=4, height=1, font=("arial", 30, "bold"), fg="#fff", bg="orange", command=lambda: update_display('+')).place(x=400, y=410)

tk.Button(root, text="0", width=8, height=1, font=("arial", 30, "bold"), fg="#fff", bg="black",command=lambda: update_display(0)).place(x=35, y=510)
tk.Button(root, text="Pi", width=4, height=1, font=("arial", 30, "bold"),  fg="#fff", bg="black", command=lambda: update_display(3.1416)).place(x=272, y=510)
tk.Button(root, text="=", width=4, height=1, font=("arial", 30, "bold"), fg="#fff", bg="orange", command=lambda: calculator()).place(x=400, y=510)



root.mainloop()
