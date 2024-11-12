from tkinter import*

temp=3

root=Tk()
root.geometry("500x800")
heading = Label(root, text="CHAT APPLICATION",font=("Garamond",16,"bold"),fg="#33C2C8")
heading.pack()

class communication_class:
    def __init__(self, store) -> int:  # store is a required argument
        self.store = store
    
    def passit(self):
        print("Successful")  # Moved the print statement above the return
        return self.store

com1=communication_class()

def connbtnfn():
    com1.store=Entry(root,text="Enter an IP: ")
    com1.store.pack()
    submitbtn = Button(root, text="Submit",command=com1.passit)
    submitbtn.place(relx=0.7,rely=0.03)

    check=connbtn.cget("state")
    if check == 'ENABLED':
        connbtn.config(state='disabled')
    else: 
        connbtn.config(state='disabled')

connbtn = Button(root, text="Connect IP to start a chat.",wraplength=100,bg="#c83933",fg="white",command=connbtnfn)
exitbtn = Button(root, text="Exit from this application.", wraplength=100,bg="#c83933",fg="white",command=root.quit)
connbtn.place(relx=0.2, rely=0.85)
exitbtn.place(relx=0.6,rely=0.85)

root.mainloop()
