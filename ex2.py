from tkinter import *
from tkinter import messagebox
root = Tk()

# สร้าง frame
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame1.pack()
frame2.pack()
frame3.pack()

chk_var = BooleanVar()

def onChkButtonClick():
    if(chk_var.get() == True):
        btn_browse["state"] = "normal"
    else:
        btn_browse["state"] = "disabled"

def onBtnSendClick():
    from_message = ent_from.get()
    to_message = ent_to.get()
    detail_message = txt_message.get("1.0", 'end-1c')
    total_message = "message from : " + from_message + "\n" + \
                    "message to : " + to_message + "\n" + \
                    "message detail : " + detail_message
    messagebox.showinfo("Basic example", total_message)

# สร้าง widget ใน frame1
lbl_from = Label(frame1, text="From")
lbl_to = Label(frame1, text="To")
ent_from = Entry(frame1)
ent_to = Entry(frame1)
# แปะ widget ลงใน frame1 ด้วย
lbl_from.grid(row=0, column=0)
ent_from.grid(row=0, column=1)
lbl_to.grid(row=1, column=0)
ent_to.grid(row=1, column=1)

# สร้าง widget ใน frame2
txt_message = Text(frame2, width=40, height=10)
# แปะ pack widget ลงใน frame2 ด้วย
txt_message.pack()

# สร้าง widget ใน frame3
chk_attach = Checkbutton(frame3, text="Attach file", variable= chk_var, command=onChkButtonClick)
btn_browse = Button(frame3, text="Browse file", state="disabled")
btn_send = Button(frame3, text="Send", command=onBtnSendClick)
# แปะ pack widget ทั้งหมดลงใน frame3 ด้วย
chk_attach.pack()
btn_browse.pack()
btn_send.pack()

root.mainloop()
