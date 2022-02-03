from tkinter import *



def takk(event):
    sys.exit(0)

def hwdp():
    okno = Tk()


    wk1 = Label(okno, text="czy chcesz napewno opuścic grę ???")

    butonTAK = Button(okno, text="TAK", fg="red")
    butonTAK.bind("<Button-1>", takk)
    wk1.pack()
    butonTAK.pack(side=BOTTOM)

    okno.mainloop()
