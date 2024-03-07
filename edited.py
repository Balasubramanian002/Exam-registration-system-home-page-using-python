
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')

def on_ent(e):
    code.delete(0,'end')

def on_lea(e):
    name=code.get()
    if name=='':
        code.insert(0,'password')

def login():
    uname=user.get()
    password=code.get()
    if uname=='' or password=='':
        messagebox.showerror("Error","fill the empty field!!!")
    else:
      if uname=="1" and password=="1":
       message.set("Login success")
      else:
       messagebox.showerror("Error","Wrong username or password!!!")
       
       
    

def loginform():
    
    global root
    global user
    global code
    root=Tk()
    root.title('Login')
    root.geometry('1450x920')
    root.configure(bg="#fff")
    root.resizable(False,False)
    
    global uname
    global password
    global message;
    message=StringVar()
    uname=StringVar()
    password=IntVar()
    Label(root,width="250", text="Exam Registration System",font=('WonderBar',45), bg="white",fg="Red").pack()
    #image
    loc = ImageTk.PhotoImage(Image.open("C:\\Users\\sivam\\Pictures\\new1.png"))
    label = Label(root, image = loc,bg='white').place(x=5,y=125)
    frame=Frame(root,width=450,height=450,bg="white")
    frame.place(x=960,y=300)
    heading=Label(frame,text='Sign in',fg='#000080',bg='white',font=('Times new Roman',35,'bold'))
    heading.place(x=150,y=5)

    #username
    user=Entry(frame,width=30,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',20))
    user.place(x=30,y=135)
    user.insert(150,'username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)
    Frame(frame,width=400,height=2,bg="#9A3839").place(x=25,y=180)

    #password
    code=Entry(frame,width=30,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',20))
    code.place(x=30,y=225)
    code.insert(0,'password')
    code.bind('<FocusIn>',on_ent)
    code.bind('<FocusOut>',on_lea)
    Frame(frame,width=400,height=2,bg="#9A3839").place(x=25,y=265)


    #Button
    Button(frame,width=39,pady=10,text='Login in',font=('Microsoft YaHei UI Light',12),bg='#000080',fg='white',border=0,command=login).place(x=70,y=370)
    label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
    label.place(x=90,y=300)

    #label for message
    Label(root, text="",font=('arial',18),bg="white",fg="green",textvariable=message).place(x=1335,y=750)

    
    #sign up
    sign_up=Button(frame,width=6,text='Register',font=('arial',13),border=0,bg='white',cursor='hand2',fg='#57a1f8')
    sign_up.place(x=318,y=305)
    root.mainloop()
loginform()


