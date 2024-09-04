from tkinter import *
from Vol_Plus_Minus_def import *

rc = RemoteControl(5)

def nextProgram():
    rc.next_program()
    lbl_ch.config(text=rc.getProgramName())

def prevProgram():
    rc.prev_program()
    lbl_ch.config(text=rc.getProgramName())

def vol_up():
    rc.plus_vol()
    lbl_vol.config(text=rc.volume)

def vol_down():
    rc.minus_vol()
    lbl_vol.config(text=rc.volume)

def set_pgm():
    rc.setProgramName(ent_program.get())
    lbl_ch.config(text=rc.getProgramName())

tkFenster = Tk()
tkFenster.title("RemoteControl")

frm_ch = Frame(master=tkFenster, bg="skyblue")
frm_ch.pack(padx=15, pady=15, side="left")
Label(master=frm_ch, text="Program").pack(padx=5, pady=5)
btn_ch_plus = Button(master=frm_ch, text="CH+", width=7, relief="raised", command=nextProgram)
lbl_ch = Label(master=frm_ch, text=rc.getProgramName(), width=7)
btn_ch_minus = Button(master=frm_ch, text="CH-", width=7, relief="raised", command=prevProgram)
btn_ch_plus.pack(padx=5, pady=5)
lbl_ch.pack(padx=5, pady=5)
btn_ch_minus.pack(padx=5, pady=5)

frm_vol = Frame(master=tkFenster, bg="sienna")
frm_vol.pack(padx=15, pady=15, side="left")
Label(master=frm_vol, text="Volume").pack(padx=5, pady=5)
btn_vol_plus = Button(master=frm_vol, text="+", width=7, relief="raised", command=vol_up)
lbl_vol = Label(master=frm_vol, text=rc.volume, width=7)
btn_vol_minus = Button(master=frm_vol, text="-", width=7, relief="raised", command=vol_down)
btn_vol_plus.pack(padx=5, pady=5)
lbl_vol.pack(padx=5, pady=5)
btn_vol_minus.pack(padx=5, pady=5)

frm_pgm = Frame(master=tkFenster, bg="green yellow")
frm_pgm.pack(padx=15, pady=15, side="left")
ent_program = Entry(master=frm_pgm, width=10)
ent_program.pack(padx=5, pady=5, side="left")
btn_set_pgm = Button(master=frm_pgm, text="set", width=10, relief="raised", command=set_pgm)
btn_set_pgm.pack(padx=5, pady=5)

tkFenster.mainloop()