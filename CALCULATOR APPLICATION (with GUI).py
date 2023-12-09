#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing library 

import tkinter as tk

calculation = " "


#function for calculation

def add_to_calculation(number):
  global calculation
  calculation += str(number)
  text_result.delete(1.0, tk.END)
  text_result.insert(1.0, calculation)



#function for evaluation

def evaluate_calculation():
  global calculation
  try:
    calculation = str(eval(calculation))
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, calculation)

  except:
    clear_field()
    text_result.insert(1.0, "Error")
    
    

#function for clearing the result viewing space of calculator

def clear_field():
  global calculation
  calculation = ""
  text_result.delete(1.0, tk.END)


#configuring the dimensions of calculator

root = tk.Tk()
root.title("CALCULATOR")
root.geometry("300x300")


#creating the result viewing space of calculator

text_result = tk.Text(root, height=2, width=16, font=("arial", 24))
text_result.grid(columnspan=5)


#creating different buttons / keys

button_1 = tk.Button(root,
                     text="1",
                     command=lambda: add_to_calculation(1),
                     width=5,
                     font=("arial", 14))
button_1.grid(row=2, column=1)          #key 1

button_2 = tk.Button(root,
                     text="2",
                     command=lambda: add_to_calculation(2),
                     width=5,
                     font=("arial", 14))
button_2.grid(row=2, column=2)          #Key 2

button_3 = tk.Button(root,
                     text="3",
                     command=lambda: add_to_calculation(3),
                     width=5,
                     font=("arial", 14))
button_3.grid(row=2, column=3)          #Key 3

button_4 = tk.Button(root,
                     text="4",
                     command=lambda: add_to_calculation(4),
                     width=5,
                     font=("arial", 14))
button_4.grid(row=3, column=1)          #Key 4

button_5 = tk.Button(root,
                     text="5",
                     command=lambda: add_to_calculation(5),
                     width=5,
                     font=("arial", 14))
button_5.grid(row=3, column=2)          #Key 5

button_6 = tk.Button(root,
                     text="6",
                     command=lambda: add_to_calculation(6),
                     width=5,
                     font=("arial", 14)) 
button_6.grid(row=3, column=3)          #Key 6

button_7 = tk.Button(root,
                     text="7",
                     command=lambda: add_to_calculation(7),
                     width=5,
                     font=("arial", 14))
button_7.grid(row=4, column=1)          #Key 7

button_8 = tk.Button(root,
                     text="8",
                     command=lambda: add_to_calculation(8),
                     width=5,
                     font=("arial", 14))
button_8.grid(row=4, column=2)          #Key 8

button_9 = tk.Button(root,
                     text="9",
                     command=lambda: add_to_calculation(9),
                     width=5,
                     font=("arial", 14))
button_9.grid(row=4, column=3)          #Key 9

button_0 = tk.Button(root,
                     text="0",
                     command=lambda: add_to_calculation(0),
                     width=5,
                     font=("arial", 14))
button_0.grid(row=5, column=2)          #Key 0

button_plus = tk.Button(root,
                        text="+",
                        command=lambda: add_to_calculation("+"),
                        width=5,
                        font=("arial", 14), background="light blue")
button_plus.grid(row=2, column=4)          #Key +

button_minus = tk.Button(root,
                         text="-",
                         command=lambda: add_to_calculation("-"),
                         width=5,
                         font=("arial", 14), background="light blue")
button_minus.grid(row=3, column=4)          #Key -

button_mul = tk.Button(root,
                       text="*",
                       command=lambda: add_to_calculation("*"),
                       width=5,
                       font=("arial", 14), background="light blue")
button_mul.grid(row=4, column=4)          #Key *

button_div = tk.Button(root,
                       text="/",
                       command=lambda: add_to_calculation("/"),
                       width=5,
                       font=("arial", 14), background="light blue")
button_div.grid(row=5, column=4)          #Key /

button_openP = tk.Button(root,
                        text="(",
                        command=lambda: add_to_calculation("("),
                        width=5,
                        font=("arial", 14))
button_openP.grid(row=5, column=1)        #Key (


button_closeP = tk.Button(root,
                        text=")",
                        command=lambda: add_to_calculation(")"),
                        width=5,
                        font=("arial", 14))
button_closeP.grid(row=6, column=1)        #Key )


button_equals = tk.Button(root,
                          text="=",
                          command=evaluate_calculation,
                          width=11,
                          font=("arial", 14),background="light grey")  
button_equals.grid(row=6, column=2, columnspan=2)  #Key =

button_clear = tk.Button(root,
                         text="AC",
                         command=clear_field,
                         width=5,
                         font=("arial", 14),background="orange")
button_clear.grid(row=5, column=3)           #Key for clearing the result displaying space

root.mainloop()


# In[ ]:





# In[ ]:




