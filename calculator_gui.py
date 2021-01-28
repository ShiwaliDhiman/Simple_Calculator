from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("SIMPLE CALCULATOR")
window.geometry('312x370')
window.resizable(0,0)

def btn_click(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)

def btn_clear():
    global  expression
    expression=""
    input_text.set(expression)

def btn_equal():
    try:
        global expression
        result=str(eval(expression))
        expression=""
        btn_click(result)
    except:
        input_text.set("Error!!!!")
        expression=""

expression=""
input_text=StringVar()

input_frame=Frame(window,height=50,width=312)
input_frame.pack(side=TOP)

input_field=Entry(input_frame,width=50,font=('arial',18,'bold'),textvariable=input_text)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)   #ipady is the internal padding to increase the height of input field

btn_frame=Frame(window,height=272,width=312,bg='grey')
btn_frame.pack()

clear=Button(btn_frame,text='C',bg='grey',fg='black',width=33,height=3,command=btn_clear).grid(row=0,columnspan=3)
divide=Button(btn_frame,text='/',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click('/')).grid(row=0,column=3)
seven=Button(btn_frame,text='7',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click(7)).grid(row=1,column=0)
eight=Button(btn_frame,text='8',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click(8)).grid(row=1,column=1)
nine=Button(btn_frame,text='9',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click(9)).grid(row=1,column=2)
multiply=Button(btn_frame,text='*',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click('*')).grid(row=1,column=3)
four=Button(btn_frame,text='4',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click(4)).grid(row=2,column=0)
five=Button(btn_frame,text='5',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click(5)).grid(row=2,column=1)
six=Button(btn_frame,text='6',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click(6)).grid(row=2,column=2)
minus=Button(btn_frame,text='-',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click('-')).grid(row=2,column=3)
one=Button(btn_frame,text='1',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click(1)).grid(row=3,column=0)
two=Button(btn_frame,text='2',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click(2)).grid(row=3,column=1)
three=Button(btn_frame,text='3',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click(3)).grid(row=3,column=2)
plus=Button(btn_frame,text='+',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click('+')).grid(row=3,column=3)
zero=Button(btn_frame,text='0',bg='grey',fg='black',width=21,height=3,command=lambda:btn_click(0)).grid(row=4,columnspan=2)
point=Button(btn_frame,text='.',bg='grey',fg='black',width=10,height=3,command=lambda:btn_click('.')).grid(row=4,column=2)
equalto=Button(btn_frame,text='=',bg='grey',fg='black',width=10,height=3,command=btn_equal).grid(row=4,column=3)

window.mainloop()