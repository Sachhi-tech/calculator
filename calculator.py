from tkinter import*
root= Tk()

def click(event):
    global scvalue                          #this is need for changing the scvalue in method
    text=event.widget.cget("text")


    print(text)

    if text=="A":
        scvalue.set("")
        screen.update()

    elif text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get()) #eval is function which covert string into the integer

        scvalue.set(value)
        screen.update

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()






root.geometry("530x600")
root.title("MY_CALCULATOR")
root.configure(background="black")
root.maxsize(530,600)


frame1=Frame(root)
frame1.pack(fill=X)
label1=Label(frame1,text="CALCULATOR",font=("sans",30,"bold","underline"))
label1.pack()

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font=("Helvetica",30,"bold"))
screen.pack(pady=15,fill=X)

f=Frame(root,bg="black")
b=Button(f,padx=14,pady=5,text="7",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=14,pady=5,text="8",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=14,pady=5,text="9",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=12,pady=5,text="=",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=10,pady=5,text="A",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
f.pack()

f=Frame(root,bg="black")
b=Button(f,padx=14,pady=5,text="4",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=14,pady=5,text="5",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=14,pady=5,text="6",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=14,pady=5,text="*",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=16,pady=5,text="/",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
f.pack()

f=Frame(root,bg="black")
b=Button(f,padx=14,pady=5,text="1",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=14,pady=5,text="2",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=14,pady=5,text="3",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=14,pady=5,text="+",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=16,pady=5,text="-",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
f.pack()

f=Frame(root,bg="black")
b=Button(f,padx=14,pady=5,text="0",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=10,pady=5,text="%",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=17,pady=5,text=",",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=13,pady=5,text="//",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,padx=17,pady=5,text=".",font=("Helvetica",20,"bold"))
b.pack(side=LEFT,padx=18,pady=12)
b.bind('<Button-1>',click)
f.pack()

root.mainloop()