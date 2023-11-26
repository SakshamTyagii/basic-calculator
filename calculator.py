import tkinter as tk

calculation= ""

def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
    pass
def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Cannot be divided by zero :)")
    
def clear_field():
     global calculation
     calculation = ""
     text_result.delete(1.0,"end") 
     pass
root=tk.Tk()
root.geometry("530x650")
text_result = tk.Text(root, height=1.5,width=30 , font=("Arial",24))
text_result.grid(columnspan=7)
bt1=tk.Button(root,text="1",command=lambda: add_to_calculation(1),width=6,height=3,font=("Arial",18))
bt1.grid(row=2, column=1 )
bt2=tk.Button(root,text="2",command=lambda: add_to_calculation(2),width=6,height=3,font=("Arial",18))
bt2.grid(row=2, column=2  )
bt3=tk.Button(root,text="3",command=lambda: add_to_calculation(3),width=6,height=3,font=("Arial",18))
bt3.grid(row=2, column=3 )
bt4=tk.Button(root,text="4",command=lambda: add_to_calculation(4),width=6,height=3,font=("Arial",18))
bt4.grid(row=3, column=1 )
bt5=tk.Button(root,text="5",command=lambda: add_to_calculation(5),width=6,height=3,font=("Arial",18))
bt5.grid(row=3, column=2 )
bt6=tk.Button(root,text="6",command=lambda: add_to_calculation(6),width=6,height=3,font=("Arial",18))
bt6.grid(row=3, column=3 )
bt7=tk.Button(root,text="7",command=lambda: add_to_calculation(7),width=6,height=3,font=("Arial",18))
bt7.grid(row=4, column=1 )
bt8=tk.Button(root,text="8",command=lambda: add_to_calculation(8),width=6,height=3,font=("Arial",18))
bt8.grid(row=4, column=2 )
bt9=tk.Button(root,text="9",command=lambda: add_to_calculation(9),width=6,height=3,font=("Arial",18))
bt9.grid(row=4, column=3 )
bt0=tk.Button(root,text="0",command=lambda: add_to_calculation(0),width=6,height=3,font=("Arial",18))
bt0.grid(row=5, column=2 )
btplus=tk.Button(root,text="+",command=lambda: add_to_calculation("+"),width=6,height=3,font=("Arial",18))
btplus.grid(row=2, column=4 )
btminus=tk.Button(root,text="-",command=lambda: add_to_calculation("-"),width=6,height=3,font=("Arial",18))
btminus.grid(row=3, column=4 )
btmultiply=tk.Button(root,text="*",command=lambda: add_to_calculation("*"),width=6,height=3,font=("Arial",18))
btmultiply.grid(row=4, column=4 )
btdiv=tk.Button(root,text="/",command=lambda: add_to_calculation("/"),width=6,height=3,font=("Arial",18))
btdiv.grid(row=5, column=4 )
btparenL=tk.Button(root,text="(",command=lambda: add_to_calculation("("),width=6,height=3,font=("Arial",18))
btparenL.grid(row=5, column=1 )
btparenR=tk.Button(root,text=")",command=lambda: add_to_calculation(")"),width=6,height=3,font=("Arial",18))
btparenR.grid(row=5, column=3 )
btEQUALS=tk.Button(root,text="=",command=evaluate_calculation,width=15,height=3,font=("Arial",18))
btEQUALS.grid(row=6, column=3,columnspan=2)
btCLEAR=tk.Button(root,text="C",command=clear_field ,width=15,height=3,font=("Arial",18))
btCLEAR.grid(row=6, column=1,columnspan=2)
root.mainloop()

