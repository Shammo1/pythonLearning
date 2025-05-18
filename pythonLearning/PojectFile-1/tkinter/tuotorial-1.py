import tkinter as new
#window part size/bg color/title/start

"""Window Properties
Method	Description
root.title("Title")	            Sets window title
root.geometry("WxH")	        Sets window size (e.g., "400x300")
root.resizable(False, False)	Disables window resizing
root.configure(bg="lightblue")	Sets background color
root.iconbitmap("icon.ico")	    Changes window icon"""
root=new.Tk()#it will create the main window

#width x height
root.title("HeroAlive")
root.geometry("300x150")#by geometry it will ensure the size of window how i want to show
"""
#maxSize property(width,height)
root.maxsize(400,400)#we wont be able increase size not more then maxsize
#minsize(width,height)
root.minsize(150,100)
"""
def button_click():
    print("Button clicked!")

button = new.Button(root, text="Click Me", command=button_click)
button.pack()
#we can fixed the size by using resizeble property
root.resizable(False,False)
root.configure(bg="#000000")#must use # in color code
#root.iconbitmap("icon.ico")



# Labels (Display Text)
#label=new.Label(root,text="I am Shammo")old style 
label=new.Label(
    root,
    text="Love To Win",
    font=("Arial", 16, "bold"),
    fg="yellow",  # Text color
    bg="#000000",# Background color
    bd=3,
   # relief="groove"
    #padx=15,  # Horizontal padding
    #pady=50  # Vertical padding
)
label.pack(pady=50, padx=15)






root.mainloop()# Start the event loop (keeps window open) it will create a window