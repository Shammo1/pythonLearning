import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S')  
    time_label.config(text=current_time)
    time_label.after(1000, update_time) 
    
# Create main window
root = tk.Tk()
root.title("Enhanced Digital Clock")
root.geometry("300x200")
##root.maxsize(300,200)
root.resizable(False, False)
root.configure(bg='black')

# Time label
time_label = tk.Label(root, font=('arial', 50, 'bold'),
                     bg='black', fg='cyan')
time_label.pack(pady=60)

update_time()

root.mainloop()
