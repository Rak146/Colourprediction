from cProfile import label
from fileinput import filename
from logging import root
from msilib.schema import Font
from tkinter import *
from tkinter import font
from turtle import width
from webbrowser import BackgroundBrowser
from PIL import ImageTk,Image,ImageEnhance
from tkinter import filedialog
from matplotlib import image
from matplotlib.pyplot import text, title


h=""
#root.iconbitmap('')
def open():
    global h
    def open_file():
        
        global my_image
        global h
        #('Jpg Files', '*.jpg'),('PNG Files','*.png')
        root.filename=filedialog.askopenfilename(initialdir="",title="select a file",filetypes=(("PNG Files","*.png"),("Jpg Files","*.jpg"),("all files","*.*")))
        h=root.filename
        if h:
           top.destroy()
           root.destroy()
    root = Tk()
    
    root.withdraw()
    top = Toplevel()
    top.title("recognizer")
    #size the window according coordinates in top level
    top.geometry("3172x3172")
    #size the window according coordinates in root level
    root.geometry("600x600")

    #create a canvas in top level for labels alias text
    c=Canvas(top,bg="gray16",height=300,width=1600)
    text= c.create_text(1180,140,fill="green",text="COLOUR RECOGNITION", font=('Helvetica','30','bold'))  
    text= c.create_text(1200,180,fill="green",text="To play with colours Click the Upload button!!!", font=('italic','14'))  
    c.pack()
    #path of the image 
    image= Image.open("C://Users//raksr//OneDrive//Pictures//Documents//Colourrecognition//colours.png")
    #resize the image according to x and y
    image = image.resize((800,800), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(image)
    label = Label(top,image=my_img)
    label.place(x=0, y=0)  
    c.pack()
    
  
    btn=Button(top, text="upload", command=open_file ,height = 2, width = 18, bg="black",fg="white",font="Times 20 bold",borderwidth=3)
    btn.pack(side=RIGHT,padx=200,pady=200)
    #.place(relx=0.5, rely=0.5,anchor=CENTER)
    top.mainloop()
    


