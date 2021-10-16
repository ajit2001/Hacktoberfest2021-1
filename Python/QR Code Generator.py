import pyqrcode
import os
import tkinter as tk
from tkinter.messagebox import showerror

def create_qr():
    try:
        entered_text = data.get()   
        if entered_text == '' or entered_text == 'Insert Text':
            showerror('Error!','Please Enter Data')
        else:
            # Generate QR code
            qr = pyqrcode.create(entered_text)
            # img.svg('uca-url.svg', scale=8)
            # img.eps('uca-url.eps', scale=2)
            # Saving the Generated QR Code
            qr.png('img.png', scale = 6)
            # img.show()
            data.delete(0, tk.END)
            os.startfile('img.png')
    except:
        showerror('Error','Something Went Wrong,\nTry to check the code of Program')

root = tk.Tk()
root.title('QR Code Generator')
root.geometry('500x500+150+150')
root.iconbitmap('')
root.configure(bg='#6366f1')       # For Background Color

# For using an image as a background refer to below this code.

# bg = tk.PhotoImage(file='bg_image1.png')
# bg_lab = tk.Label(root, image=bg, bg='white')
# bg_lab.place(x=0, y=0, relwidth=1,relheight=1)

data = tk.Entry(root,font=('Century',18),bg='#adc9be', fg='Black')
data.place(x=100,y=250)
data.insert(tk.END, 'Insert Text')

button = tk.Button(root, text='Generate QR Code',bg='#04aa6b', fg='Black', font=('Century',13), relief=tk.RAISED, command=create_qr)
button.place(x=150, y=300)

root.mainloop()

