from tkinter import*
a=Tk()
a.title("2nd tkinter program")

l=Label(a,text="2nd tkintergui program here we learn about the button").pack()
def abc():
    print("i am button")
b1=Button(a,text="ok",width=20,command=abc).pack()

#checkbutton
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
c1=Checkbutton(a,text="value",variable=var1).pack()
c2=Checkbutton(a,text="value",variable=var2).pack()
c3=Checkbutton(a,text="value",variable=var3).pack()
c4=Checkbutton(a,text="value",variable=var4).pack()
c5=Checkbutton(a,text="value",variable=var5).pack()
c6=Checkbutton(a,text="value",variable=var6).pack()
print("value of var1:",var1)
print("value of var2:",var2)
print("value of var3:",var3)
print("value of var4:",var4)
print("value of var5:",var5)
print("value of var6:",var6)


#entry widget
l1=Label(a, text="ENTER YOUR NAME PLEASE").pack()
e1=Entry(a).pack()
b1=Button(a,text="SUBMIT").pack()
#origanal entry widget
def ent(value):
    print(value)
l1=Label(a, text="ENTER YOUR rollno PLEASE").pack()
e1=Entry(a,command=ent(input())).pack()
b1=Button(a,text="SUBMIT").pack()
a.mainloop()
