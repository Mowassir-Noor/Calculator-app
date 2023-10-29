from tkinter import *
import tkinter as tk

root=Tk()
root.resizable(False,False)





root.configure(bg='#010000')

show=Entry(root,width=60,borderwidth=0,bg="#010000",fg="white",font=("calibri",20),cursor="xterm")
show.grid(row=0,columnspan=4,padx=(10,0),pady=(100,0))









def clear():
    show.delete(0,END)


def click(num):
    current=show.get()
    show.delete(0,END)
    show.insert(0,str(current)+str(num))

def func(operation):
    global math
    math=operation
    first_num=show.get()
    global f_num 
    f_num=float(first_num)
    show.delete(0,END)

def equals():

    
        try:
            second_num=show.get()
            s_num=float(second_num)
            show.delete(0,END)


            if math=="add":
              
              addition=s_num+f_num
              if addition % 1==0:
                  show.insert(0,str(int(addition)))
              else:
                  show.insert(0,str(addition))

            if math=="subtract":
              subraction=f_num-s_num
              if subraction %1==0:
                  show.insert(0,str(int(subraction)))
              else:
                   show.insert(0,str(f_num-s_num))

            if math=="multiply":
              multiplication=f_num*s_num
              if multiplication %1 ==0:
                  show.insert(0,str(int(multiplication)))

              else:
                   show.insert(0,str(f_num*s_num))

            if math=="divide":
              division=f_num/s_num
              if division %1==0:
                  show.insert(0,str(int(division)))

              else:
                   show.insert(0,str(f_num/s_num))

            if math=="power":
               power=f_num**s_num
               if power %1==0:
                   show.insert(0,str(int(power)))

               else:
                    show.insert(0,str(f_num**s_num))

            
            
        except ValueError:
            value=show.get()
            result=eval(value)
            show.delete(0,END)
            show.insert(0,str(result))
            
          
   
    
#Making fuctions for special buttons
def deletion():
    current_num=show.get()
    new_num=current_num[:-1]
    show.delete(0,END)
    show.insert(0,new_num)

def percent():
    current_num=float(show.get())
    show.delete(0,END)
    show.insert(0,str(current_num/100))

def decimal():
    current_num=show.get()
    show.delete(0,END)
    show.insert(0,str(current_num + "."))


    

    


#Defining buttons 
button_2=Button(root,text="2",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:click(2),font=20)
button_3=Button(root,text="3",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:click(3),font=20)
button_1=Button(root,text="1",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:click(1),font=20)
button_4=Button(root,text="4",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:click(4),font=20)
button_5=Button(root,text="5",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:click(5),font=20)
button_6=Button(root,text="6",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:click(6),font=20)
button_7=Button(root,text="7",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:click(7),font=20)
button_8=Button(root,text="8",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:click(8),font=20)
button_9=Button(root,text="9",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:click(9),font=20)
button_0=Button(root,text="0",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:click(0),font=20)
button_add=Button(root,text="+",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:func("add"),font=("bold",20))
button_sub=Button(root,text="_",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:func("subtract"),font=("bold",20))
button_multi=Button(root,text="x",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:func("multiply"),font=("bold",20))
button_div=Button(root,text="÷",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:func("divide"),font=("bold",20))
button_equal=Button(root,text="=",padx=40,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=equals,font=("bold",20))
button_clear=Button(root,text="Clear",padx=30,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:clear(),font=("bold",15))
button_del=Button(root,text="del",padx=35,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:deletion(),font=("bold",15))
button_percent=Button(root,text="%",padx=38,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:percent(),font=("bold",20))
button_float=Button(root,text=".",padx=41,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:decimal(),font=("bold",30))
button_fake=Button(root,text="^",padx=32,pady=20,bg='#010000',fg='#FFFFFF',border=0,activebackground="#808080", activeforeground="#fff",command=lambda:func("power"),font=("bold",20))



# Positioning buttons

#First row of buttons
button_clear.grid(row=1,column=0)
button_del.grid(row=1,column=1)
button_percent.grid(row=1,column=2)
button_div.grid(row=1,column=3)
#second row of buttons
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_multi.grid(row=2,column=3)
#Third row of buttons
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_sub.grid(row=3,column=3)
#Fourth row of buttons
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_add.grid(row=4,column=3)
#Fifth row of buttons
button_0.grid(row=5,column=1)
button_float.grid(row=5,column=2)
button_fake.grid(row=5,column=0)
button_equal.grid(row=5,column=3)













root.mainloop()


