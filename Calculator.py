from tkinter import *
window = Tk()
window.title("Calculator")
window.resizable(0,0)
window.iconbitmap("C:\Cursos\Calculadora\exe\calc.ico")
window.configure(background='#151618')
i = 0
#Imput
e_text = Entry(window, bg = "#a7b8b5", font = ("Calibri 20"))
e_text.grid(row = 0, column = 0, columnspan= 4, padx = 5, pady = 5)
#Functions
def click_button(value):
    global i
    e_text.insert(i, value)
    i += 1
def delete():
    e_text.delete(0, END)
    i = 0
def do_calc():
    calculus = e_text.get()
    result = eval(calculus)
    e_text.delete(0, END)
    e_text.insert(0, result)
    i = 0
#Buttons
    #Button 1
img_button1 = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\Cbutton1.png")
label_button1 = Label(image=img_button1)
button1 = Button(window, image=img_button1, width = 50, height = 50, borderwidth= 0, 
                    bg = "#151618", activebackground="#151618", command = lambda: click_button(1))
    #Button 2
img_button2 = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\Cbutton2.png")
label_button2 = Label(image=img_button2)
button2 = Button(window, image=img_button2, width = 50, height = 50, borderwidth= 0, 
        bg = "#151618", activebackground="#151618", command = lambda: click_button(2))
    #Button 3
img_button3 = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\Cbutton3.png")
label_button3 = Label(image=img_button3)
button3 = Button(window, image=img_button3, width = 50, height = 50, borderwidth= 0, 
        bg = "#151618", activebackground="#151618", command = lambda: click_button(3))
    #Button 4
img_button4 = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\Cbutton4.png")
label_button4 = Label(image=img_button4)
button4 = Button(window, image=img_button4, width = 50, height = 50, borderwidth= 0, 
                    bg = "#151618", activebackground="#151618", command = lambda: click_button(4))
    #Button 5
img_button5 = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\Cbutton5.png")
label_button5 = Label(image=img_button5)
button5 = Button(window, image=img_button5, width = 50, height = 50, borderwidth= 0, 
        bg = "#151618", activebackground="#151618", command = lambda: click_button(5))
    #Button 6
img_button6 = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\Cbutton6.png")
label_button6 = Label(image=img_button6)
button6 = Button(window, image=img_button6, width = 50, height = 50, borderwidth= 0, 
        bg = "#151618", activebackground="#151618", command = lambda: click_button(6))
    #Button 7
img_button7 = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\Cbutton7.png")
label_button7 = Label(image=img_button7)
button7 = Button(window, image=img_button7, width = 50, height = 50, borderwidth= 0, 
        bg = "#151618", activebackground="#151618", command = lambda: click_button(7))
    #Button 8
img_button8 = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\Cbutton8.png")
label_button8 = Label(image=img_button8)
button8 = Button(window, image=img_button8, width = 50, height = 50, borderwidth= 0, 
        bg = "#151618", activebackground="#151618", command = lambda: click_button(8))
    #Button 9
img_button9 = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\Cbutton9.png")
label_button9 = Label(image=img_button9)
button9 = Button(window, image=img_button9, width = 50, height = 50, borderwidth= 0, 
        bg = "#151618", activebackground="#151618", command = lambda: click_button(9))
    #Button Zero
img_button0 = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\Cbutton0.png")
label_button0 = Label(image=img_button0)
button0 = Button(window, text = "0", image=img_button0, width = 120, height = 50, bg = "#151618", 
        borderwidth= 0, activebackground="#151618", command = lambda: click_button(0))
#Buttons Symbols
    #Button Delete
img_buttonDel = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\CbuttonDel.png")
label_buttonDel = Label(image=img_buttonDel)
button_del = Button(window, image=img_buttonDel, width = 50, height = 50, borderwidth= 0, 
            bg = "#151618", activebackground="#151618", command = lambda: delete())
    #Button Parentesis In
img_buttonParentIn = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\CbuttonParentIn.png")
label_buttonParentIn = Label(image=img_buttonParentIn)
button_parent1 = Button(window, image=img_buttonParentIn, width = 50, height = 50, borderwidth= 0, 
                bg = "#151618", activebackground="#151618", command = lambda: click_button("("))
    #Button Parentesis Out
img_buttonParentOut = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\CbuttonParentOut.png")
label_buttonParentOut = Label(image=img_buttonParentOut)
button_parent2 = Button(window, image=img_buttonParentOut, width = 50, height = 50, borderwidth= 0, 
                 bg = "#151618", activebackground="#151618", command = lambda: click_button(")"))
    #Button Dot
img_buttonDot = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\CbuttonDot.png")
label_buttonDot = Label(image=img_buttonDot)
button_dot = Button(window, image=img_buttonDot, width = 50, height = 50, borderwidth= 0, 
            bg = "#151618", activebackground="#151618", command = lambda: click_button("."))
    #Button Div
img_buttonDiv = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\CbuttonDiv.png")
label_buttonDiv = Label(image=img_buttonDiv)
button_div = Button(window, image=img_buttonDiv, width = 50, height = 50, borderwidth= 0, 
            bg = "#151618", activebackground="#151618", command = lambda: click_button("/"))
    #Button Mult
img_buttonMult = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\CbuttonMult.png")
label_buttonMult = Label(image=img_buttonMult)
button_mult = Button(window, image=img_buttonMult, width = 50, height = 50, borderwidth= 0, 
            bg = "#151618", activebackground="#151618", command = lambda: click_button("*"))
    #Button Sum
img_buttonSum = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\CbuttonSum.png")
label_buttonSum = Label(image=img_buttonSum)
button_sum = Button(window, image=img_buttonSum, width = 50, height = 50, borderwidth= 0, 
             bg = "#151618", activebackground="#151618", command = lambda: click_button("+"))
    #Button Min
img_buttonMin = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\CbuttonMin.png")
label_buttonMin = Label(image=img_buttonMin)
button_min = Button(window, image=img_buttonMin, width = 50, height = 50, borderwidth= 0, 
            bg = "#151618", activebackground="#151618", command = lambda: click_button("-"))
    #Button Equal
img_buttonEqual = PhotoImage(file="C:\Cursos\Calculadora\Cbuttons\CbuttonEqual.png")
label_buttonEqual = Label(image=img_buttonEqual)
button_equal = Button(window, image=img_buttonEqual, width = 50, height = 50, borderwidth= 0,
            bg = "#151618", activebackground="#151618", command = lambda: do_calc())
#Print buttons in window
button_del.grid(row = 1, column = 0, padx = 5, pady = 5,)
button_parent1.grid(row = 1, column = 1, padx = 5, pady = 5,)
button_parent2.grid(row = 1, column = 2, padx = 5, pady = 5,)
button_div.grid(row = 1, column = 3, padx = 5, pady = 5,)
button7.grid(row = 2, column = 0, padx = 5, pady = 5,)
button8.grid(row = 2, column = 1, padx = 5, pady = 5,)
button9.grid(row = 2, column = 2, padx = 5, pady = 5,)
button_mult.grid(row = 2, column = 3, padx = 5, pady = 5,)
button4.grid(row = 3, column = 0, padx = 5, pady = 5,)
button5.grid(row = 3, column = 1, padx = 5, pady = 5,)
button6.grid(row = 3, column = 2, padx = 5, pady = 5,)
button_sum.grid(row = 3, column = 3, padx = 5, pady = 5,)
button1.grid(row = 4, column = 0, padx = 5, pady = 5,)
button2.grid(row = 4, column = 1, padx = 5, pady = 5,)
button3.grid(row = 4, column = 2, padx = 5, pady = 5,)
button_min.grid(row = 4, column = 3, padx = 5, pady = 5,)
button0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5,)
button_dot.grid(row = 5, column = 2, padx = 5, pady = 5,)
button_equal.grid(row = 5, column = 3, padx = 5, pady = 5,)
window.mainloop()