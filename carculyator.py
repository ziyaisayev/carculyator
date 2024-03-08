import tkinter
window=tkinter.Tk()
window.title("Calculatior")
window.configure(background="purple")
input1=tkinter.Entry(window,width=35,borderwidth=5)
input1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_work(number):
  evvelki_reqem=input1.get()
  input1.delete(0,tkinter.END)
  input1.insert(0,str(evvelki_reqem)+str(number))  
def button_ustegel():
    global a1
    global operator
    operator="ustegel"
    a1=int(input1.get())
    input1.delete(0,tkinter.END)
def button_beraber():
    global a2
    a2=int(input1.get())
    input1.delete(0,tkinter.END)
    
def button_cixma():
    global a3
    global operator
    operator="cixma"
    a3=int(input1.get())
    input1.delete(0,tkinter.END)
        
   
def button_vurma():
    global a4
    global operator
    operator="vurma"
    a4=int(input1.get())
    input1.delete(0,tkinter.END) 
    
    
    
def button_bolme():
    global a5
    global operator
    operator="bolme"
    a5=int(input1.get())
    input1.delete(0,tkinter.END)
    
    if operator=="ustegel":
        input1.insert(0,a1+a2)
    if operator=="cixma":
          input1.insert(0,a3-a2)   
    if operator=="vurma":
          input1.insert(0,a4*a2) 
    if operator=="bolme":
          input1.insert(0,a5/a2) 
          
    
button_1=tkinter.Button(window, text='1',padx=40, pady=20,command=lambda:button_work(1))
button_2=tkinter.Button(window, text='2',padx=40, pady=20,command=lambda:button_work(2))
button_3=tkinter.Button(window, text='3',padx=40, pady=20,command=lambda:button_work(3))

button_4=tkinter.Button(window, text='4',padx=40, pady=20,command=lambda:button_work(4))
button_5=tkinter.Button(window, text='5',padx=40, pady=20,command=lambda:button_work(5))
button_6=tkinter.Button(window, text='6',padx=40, pady=20,command=lambda:button_work(6))

button_7=tkinter.Button(window, text='7',padx=40, pady=20,command=lambda:button_work(7))
button_8=tkinter.Button(window, text='8',padx=40, pady=20,command=lambda:button_work(8))
button_9=tkinter.Button(window, text='9',padx=40, pady=20,command=lambda:button_work(9))
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)


button_ustegel=tkinter.Button(window, text='+',padx=40, pady=20,command=button_ustegel)
button_0=tkinter.Button(window, text='0',padx=40, pady=20,command=lambda:button_work(0))
button_beraber=tkinter.Button(window, text='=',padx=40, pady=20,command=button_beraber)
button_cixma=tkinter.Button(window, text='-',padx=40, pady=20,command=button_cixma)
button_vurma=tkinter.Button(window, text='*',padx=40, pady=20,command=button_vurma)
button_bolme=tkinter.Button(window, text='/',padx=40, pady=20,command=button_bolme)

button_0.grid(row=4,column=1)
button_ustegel.grid(row=4,column=0)
button_beraber.grid(row=4,column=2)
button_cixma.grid(row=5,column=0)
button_vurma.grid(row=5,column=1)
button_bolme.grid(row=5,column=2)






window.mainloop()


 



