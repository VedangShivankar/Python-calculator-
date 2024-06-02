
# to import tkinter
import tkinter as  tk

#No value in string
calculation = ""


#function for clear 
def clear():
    global calculation
    calculation = " "
    text_result.delete(1.0,"end")
    pass

# function for equal 
def equal_to_x():
    global calculation
    print(calculation)
    try:
        result = str(eval(calculation))
        calculation = " "
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)

    except:
        clear()
        text_result.insert(1.0, "Error")
    pass
#function for math signs
def addition_to_calc(symbol):
    global calculation
    calculation += str(symbol)    
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


#calculator size
root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

 #all numerical buttons 
btn_1 = tk.Button(root, text="1", command=lambda:addition_to_calc(1), width=5, font=( "Arial", 14))
btn_1.grid(row=2 , column=1)

btn_2 = tk.Button(root, text="2", command=lambda:addition_to_calc(2), width=5, font=("Arial", 14))
btn_2.grid(row=2 , column=2)

btn_3 = tk.Button(root, text="3", command=lambda:addition_to_calc(3), width=5, font=("Arial", 14))
btn_3.grid(row=2 , column=3)

btn_4 = tk.Button(root, text="4", command=lambda:addition_to_calc(4), width=5, font=("Arial", 14))
btn_4.grid(row=3 , column=1)

btn_5 = tk.Button(root, text="5", command=lambda:addition_to_calc(5), width=5, font=("Arial", 14))
btn_5.grid(row=3 , column=2)

btn_6 = tk.Button(root, text="6", command=lambda:addition_to_calc(6), width=5, font=("Arial", 14))
btn_6.grid(row=3 , column=3)

btn_7 = tk.Button(root, text="7", command=lambda:addition_to_calc(7), width=5, font=("Arial", 14))
btn_7.grid(row=4 , column=1)

btn_8 = tk.Button(root, text="8", command=lambda:addition_to_calc(8), width=5, font=("Arial", 14))
btn_8.grid(row=4 , column=2)

btn_9 = tk.Button(root, text="9", command=lambda:addition_to_calc(9), width=5, font=("Arial", 14))
btn_9.grid(row=4 , column=3)

btn_0 = tk.Button(root, text="0", command=lambda:addition_to_calc(0), width=5, font=("Arial", 14))
btn_0.grid(row=5 , column=2)

#math sign buttons
btn_plus = tk.Button(root, text="+", command=lambda:addition_to_calc("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2 , column=4)
btn_min = tk.Button(root, text="-", command=lambda:addition_to_calc("-"), width=5, font=("Arial", 14))
btn_min.grid(row=3 , column=4)
btn_mult = tk.Button(root, text="*", command=lambda:addition_to_calc("*"), width=5, font=("Arial", 14))
btn_mult.grid(row=4 , column=4)
btn_div = tk.Button(root, text="/", command=lambda:addition_to_calc("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5 , column=4)

# "speical" signs
btn_open = tk.Button(root, text="(", command=lambda:addition_to_calc("("), width=5, font=("Arial", 14))
btn_open.grid(row=5 , column=1)
btn_close = tk.Button(root, text=")", command=lambda:addition_to_calc(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5 , column=3)

btn_equal = tk.Button(root, text="=", command=equal_to_x , width=11, font=("Arial", 14))
btn_equal.grid(row=6 , column=3, columnspan=2)
btn_clear = tk.Button(root, text="C", command=clear, width=11, font=("Arial", 14))
btn_clear.grid(row=6 , column=1, columnspan=2)


#loop it 
root.mainloop()
