from tkinter import*
a=Tk()
a.title("3rd tk inter program")
#listbox widget
l=Listbox(a,height=5)
l.pack()
l.insert(END,"item1")

l.insert(END,"item2")
l.insert(END,"item3")
l.insert(END,"item4")
l.insert(END,"items5")
#Radio button
var=IntVar()
Radiobutton(a,text="radio1",variable=var,value=1).pack(anchor=W)
Radiobutton(a,text="radio2",variable=var,value=2).pack(anchor=W)
Radiobutton(a,text="radio3",variable=var,value=3).pack(anchor=W)
#scrollbar
scrollbar=Scrollbar(a)
scrollbar.pack(side=RIGHT,fill=X)
scrollbar.pack(side=LEFT,fill=Y)

#text widget
t1=Text(a,height=4,width=50)
t1.pack()
t1.insert(END,"this is first line\n this is second line\n this is third line")
#contener widget
l1=Label(a,text="Enter user name").grid(row=0,column=0)
e1=Entry(a)
e1.grid(row=0,column=1)
l2=Label(a,text="enter the password").grid(row=1,column=0)
e2=Entry(a)
e2.grid(row=2,column=1)
b1=Button(a,text="submit",width=20).grid(row=2,column=1)
a.mainloop()
