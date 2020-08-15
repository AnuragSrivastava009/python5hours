from tkinter import*
a=Tk()
#title
a.title("first Tkinter program")
#label
l=Label(a,text="this is a lable")
#l.pack()
#photoimage method used in label
#i=PhotoImage(file="D:\mannu\IMG-20181007-WA0012.jpg",type=".jpg")
#l2=Label(a,image=i).pack()
# button
def abc():
    print("ok button is clicked")
b1=Button(a,text="OK",width=30,command=abc).pack()
def aks():
    print("testing ok ")
b2=Button(a,text="test",width="40",command=aks).pack()

#argument pased to the command using lambda expression
def xyz(number):
    print(number,"button click")


b3=Button(a,text="submitb3",width=20,command=lambda:xyz(1)).pack()

b4=Button(a,text="submitb4",width=25,command=lambda:xyz(2)).pack()

#using class
class first:
    def ghj(number):
        print(number, "hii")
b5=Button(a,text="ghj",width=35,command=lambda:first.ghj(3)).pack()        
a.mainloop()
