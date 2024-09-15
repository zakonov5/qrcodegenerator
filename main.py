import tkinter

import qrcode, PIL
from PIL import ImageTk, Image

import tkinter as tk
from tkinter import ttk, filedialog, messagebox


def createQR(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280,205))
        tkimage = ImageTk.PhotoImage(resized_img)
        qr_canvas.delete('all')
        qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage
    else:
        messagebox.showwarning('Error', 'Enter Some Data First')



def saveQR(*args):
    data = text_entry.get()

    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280, 205))

        path = filedialog.asksaveasfilename(defaultextension='.png')
        if path:
            resized_img.save(path)
            messagebox.showinfo('Sucess', 'QR Code is Saved')
    else:
        messagebox.showwarning('Error', 'Enter Some Data First')


root = tk.Tk()
root.title('QR Code Generator')
root.geometry('300x380')
root.config(bg='Grey')
root.resizable(0,0)

frame1 = tk.Frame(root, bd=2)
frame1.place(x=10,y=7,width=280,height=250)

frame2 = tk.Frame(root, bd=2)
frame2.place(x=10,y=260,width=280,height=100)

original_img = Image.open('qrCodeCover.png')
resized_img = original_img.resize((280, 200))
cover_img = ImageTk.PhotoImage(resized_img)

qr_canvas = tk.Canvas(frame1)
qr_canvas.create_image(0,0,anchor=tk.NW, image=cover_img)
qr_canvas.image = cover_img
qr_canvas.bind('<Double-1>', saveQR)
qr_canvas.pack(fill=tk.BOTH)

text_entry = ttk.Entry(frame2, width=26, font=('Sitka Small', 11), justify=tk.CENTER)
text_entry.bind('<Return>', createQR)
text_entry.place(x=40, y=5)

btn_1 = ttk.Button(frame2, text='Create', width=4, command=createQR)
btn_1.place(x=15,y=50)

btn_2 = ttk.Button(frame2, text='Save', width=4, command=saveQR)
btn_2.place(x=100,y=50)

btn_3 = ttk.Button(frame2, text='Exit', width=4, command=root.quit)
btn_3.place(x=185,y=50)


root.mainloop()
