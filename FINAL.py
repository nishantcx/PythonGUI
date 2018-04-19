from tkinter import *
import tkinter
import os
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

top=Tk()
count=0


C = Canvas(top, bg="blue", height=500, width=500)
filename = PhotoImage(file = "C:\\Users\\NISHANT\\Desktop\\PY\\aa.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


top.title("Nishant 16CSU230")
top.geometry("1820x1820")
top.configure(background="#a1dbcd")


modelno=StringVar()
ram=StringVar()
im=StringVar()
ds=StringVar()
processor=StringVar()



def myfunction(*args):
    x = var.get()
    y = stringvar1.get()
    z = stringvar2.get()
    if x and y and z:
        button.config(state='normal')
        
    else:
        button.config(state='disabled')
       


def NewFile():
    print ("New File!")
def OpenFile():
    name = askopenfilename()
    print (name)
def About():
    print ("This is a simple example of a menu")


def Add_Model():
    f=open('C:/Users/NISHANT/Desktop/PY/model.txt','a')
    modelno=E1.get()
    ram=E2.get()
    im=E3.get()
    ds=E4.get()
    processor=E5.get()
    if(modelno=='' or ram=='' or im=='' or ds=='' or processor==''):
        print("Details can't be empty!")
        exit()
    f.writelines(modelno.ljust(20)+ram.ljust(20)+im.ljust(20)+ds.ljust(20)+processor.ljust(3)+"\n")
    print("Record added to file!")
    f.close()

def Delete_Model():
    k=modelno.get()
    f=open('C:/Users/NISHANT/Desktop/PY/model.txt','r')
    ctr=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    print(lines)
    f.close()
    f=open('C:/Users/NISHANT/Desktop/PY/model.txt','w')
    for model in lines: 
        j=model.split()
        print(j)
        if(j[0]!=k): 
             f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(5)+"\n")
    f.close()

def Update_Model():
    new_id=modelno.get() 
    new_name=ram.get() 
    new_price=im.get() 
    new_author=ds.get() 
    new_publisher=processor.get() 
    f=open('C:/Users/NISHANT/Desktop/PY/model.txt','r')
    ctr=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines() 
    f.close() 
    f=open('C:/Users/NISHANT/Desktop/PY/model.txt','w') 
    for model in lines: 
        j=model.split() 
        if(j[0]!=new_id): 
            f.writelines(j[0].ljust(3)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(5)+"\n") 
     
        else: 
            f.writelines(j[0].ljust(3)+new_name.ljust(20)+new_price.ljust(20)+new_author.ljust(20)+new_publisher.ljust(5)+"\n")
    print("Record updated!!")        
    f.close()
    
def Search_Model():
    k=modelno.get()
    f=open('C:/Users/NISHANT/Desktop/PY/model.txt','r')
    ctr=0
    flag=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    print(lines)
    for model in lines: 
        j=model.split() 
        if(j[0]==k):   
            print(j) 
            modelno.set(j[0]) 
            ram.set(j[1]) 
            im.set(j[2]) 
            ds.set(j[3]) 
            processor.set(j[4])
            flag=1
            break
    if(flag==0):
        print("Record not found!")
    else:
        print("Record found!")
    f.close()

   

def First():
    f=open('C:/Users/NISHANT/Desktop/PY/model.txt','r')
    ctr=0
    flag=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    l=list(lines)
    print("\n")
    print(l)
    j=l[0].split()
    modelno.set(j[0])
    ram.set(j[1]) 
    im.set(j[2]) 
    ds.set(j[3]) 
    processor.set(j[4])
    print("\n First Record of file is as:")
    print(l[0])
    f.close()
    
 
def Last():
    f=open('C:/Users/NISHANT/Desktop/PY/model.txt','r')
    ctr=0
    flag=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")    
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    l=list(lines)
    print(l)
    j=l[ctr-1].split()
    modelno.set(j[0])
    ram.set(j[1]) 
    im.set(j[2]) 
    ds.set(j[3]) 
    processor.set(j[4])
    print("\n Last Record of file is as:")
    print(l[ctr-1])
    f.close()

def Prev():
    global count 
    i=0
    ctr=0
    f=open('C:/Users/NISHANT/Desktop/PY/model.txt','r')
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")    
    print(ctr)
    f.seek(0)
    try: 
         
        while(i<=count-1): 
            l=f.readline() 
            i=i+1 
 
        m=l.split() 
        modelno.set(m[0]) 
        ram.set(m[1]) 
        im.set(m[2]) 
        ds.set(m[3]) 
        processor.set(m[4]) 
        print(m)
        
    except:
        modelno.set("") 
        ram.set("") 
        im.set("") 
        ds.set("") 
        processor.set("")
        print("Sorry, no more records!")
    count=count-1 
    f.close()

def Next():
    global count 
    i=0
    ctr=0
    f=open('C:/Users/NISHANT/Desktop/PY/model.txt','r')
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")    
    print(ctr)
    f.seek(0)
    try: 
         
        while(i<=count): 
            l=f.readline() 
            i=i+1 
 
        m=l.split() 
        modelno.set(m[0]) 
        ram.set(m[1]) 
        im.set(m[2]) 
        ds.set(m[3]) 
        processor.set(m[4]) 
        print(m)
        
    except:
        modelno.set("") 
        ram.set("") 
        im.set("") 
        ds.set("") 
        processor.set("")
        print("Sorry, no more records!")
    count=count+1 
    f.close()



menu = Menu(top)
top.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Shop1", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=top.quit)
helpmenu = Menu(menu)
menu.add_cascade(label="Shop2", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)


    
tkinter.Label(text="NishantSachdeva16CSU230 Inventory \n Login with USERNAME AND PASS",font=('Ariel',15,'bold')).grid(row=0)
tkinter.Label(top, text="Model Name:",font=('Helvetica',15,'bold')).grid(row=1)
tkinter.Label(top, text="RAM:",font=('Helvetica',15,'bold')).grid(row=2)
tkinter.Label(top, text="Internal Memory:",font=('Helvetica',15,'bold')).grid(row=3)
tkinter.Label(top, text="Display Size:",font=('Helvetica',15,'bold')).grid(row=4)
tkinter.Label(top, text="Processor Used:",font=('Helvetica',15,'bold')).grid(row=5)



E1 = tkinter.Entry(top,textvariable=modelno)
E2 = tkinter.Entry(top,textvariable=ram)
E3 = tkinter.Entry(top,textvariable=im)
E4 = tkinter.Entry(top,textvariable=ds)
E5 = tkinter.Entry(top,textvariable=processor)

E1.grid(row=1, column=1)
E2.grid(row=2, column=1)
E3.grid(row=3, column=1)
E4.grid(row=4, column=1)
E5.grid(row=5, column=1)



fr=tkinter.Button(top,text="|<",width=15,bg="orange",font=('Helvetica',15,'bold'),command=First).grid(row=6, column=0)
pr=tkinter.Button(top,text="<",width=15,bg="orange",font=('Helvetica',15,'bold'),command=Prev).grid(row=6, column=1)
nr=tkinter.Button(top,text=">",width=15,bg="orange",font=('Helvetica',15,'bold'),command=Next).grid(row=6, column=2)
lr=tkinter.Button(top,text=">|",width=15,bg="orange",font=('Helvetica',15,'bold'),command=Last).grid(row=6, column=3)

photoapple=PhotoImage(file="apple.png")
photomoto=PhotoImage(file="moto.png")
photoone=PhotoImage(file="oneplus.png")
photosony=PhotoImage(file="sony.png")
b1=Button(top,image=photoapple,width=300,height=300).grid(row=7, column=0)
b2=Button(top,image=photomoto,width=300,height=300).grid(row=7, column=1)
b3=Button(top,image=photoone,width=300,height=300).grid(row=7, column=2)
b4=Button(top,image=photosony,width=300,height=300).grid(row=7, column=3)

rb=tkinter.Button(top,text="ADD MODEL",width=15,bg="lightblue",font=('Helvetica',15,'bold'),command=Add_Model).place(x=150, y=600)
db=tkinter.Button(top,text="DELETE MODEL",width=15,bg="lightblue",font=('Helvetica',15,'bold'),command=Delete_Model).place(x=450, y=600)
sb=tkinter.Button(top,text="SEARCH MODEL",width=15,bg="lightblue",font=('Helvetica',15,'bold'),command=Search_Model).place(x=750, y=600)
ub=tkinter.Button(top,text="UPDATE MODEL",width=15,bg="lightblue",font=('Helvetica',15,'bold'),command=Update_Model).place(x=1000 , y=600)

stringvar1 = tkinter.StringVar(top)
stringvar2 = tkinter.StringVar(top)
var = tkinter.StringVar(top)
stringvar1.trace("w", myfunction)
stringvar2.trace("w", myfunction)
var.trace("w", myfunction)
#tkinter.Label(top, text="Username:",font=('Helvetica',15,'bold')).grid(row=0, column=1)
#tkinter.Label(top, text="Pass:",font=('Helvetica',15,'bold')).grid(row=0, column=3)
entry1 = tkinter.Entry(top, width=15, textvariable=stringvar1)
entry1.grid(row=0,column=1)
entry2 = tkinter.Entry(top, width=15, textvariable=stringvar2)
entry2.grid(row=0,column=2)
choices = ('User','Admin','Owner')
option = tkinter.OptionMenu(top, var, *choices)
option.grid(row=0,column=3)
button = tkinter.Button(top,text="submit")
button.grid(row=0, column=4)

top.mainloop()
