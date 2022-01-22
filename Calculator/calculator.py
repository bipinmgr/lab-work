from tkinter import *
root=Tk()
root.title("simple calculator")



e=Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current=e.get()
    # print(type(current)) checking the datatype of current variable 
    e.delete(0,END)
    e.insert(0,current+str(number))

def button_clear():
    e.delete(0,END)



def button_add():
    first_number=e.get()
    global f_num
    global math
    math="button_add"
    f_num=int(first_number)
    e.delete(0,END)
def button_sub():
    first_number=e.get()
    global f_num
    global math
    math="button_sub"
    f_num=int(first_number)
    e.delete(0,END)

def button_mul():
    first_number=e.get()
    global f_num
    global math
    math="button_mul"
    f_num=int(first_number)
    e.delete(0,END)

def button_div():
    first_number=e.get()
    global f_num
    global math
    math="button_div"
    f_num=int(first_number)
    e.delete(0,END)
    
def button_equal():
    second_number=e.get()
    s_num=int(second_number)
    e.delete(0,END)
    if math=="button_add":
        e.insert(0,f_num + s_num)
    elif math=="button_sub":
        e.insert(0,f_num - s_num)
    elif math=="button_mul":
        e.insert(0,f_num * s_num)
    elif math=="button_div":
        e.insert(0,f_num // s_num)


button1=Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1))
button2=Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))
button3=Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3))
button4=Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))
button5=Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
button6=Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
button7=Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
button8=Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
button9=Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))
button0=Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))


b1=Button(root, text="+", padx=40, pady=20, command=button_add)
b2=Button(root, text="*", padx=40, pady=20, command=button_mul)
b3=Button(root, text="/", padx=40, pady=20, command=button_div)
b4=Button(root, text="-", padx=40, pady=20, command=button_sub)

b5=Button(root, text="C", padx=40, pady=20, command=button_clear)
b6=Button(root, text="=", padx=40, pady=20, command=button_equal)




button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=1,column=3)
button5.grid(row=2,column=0)
button6.grid(row=2,column=1)
button7.grid(row=2,column=2)
button8.grid(row=2,column=3)
button9.grid(row=3,column=0)
button0.grid(row=4,column=2)
b1.grid(row=3,column=1)
b2.grid(row=3,column=2)
b3.grid(row=3,column=3)
b4.grid(row=4,column=0)
b5.grid(row=4,column=1)
b6.grid(row=4,column=3)


root.mainloop()