from tkinter import *

dis_msg = ''

def bhan(arg):
    global dis_msg
    
    if  arg == '=':
        t1.set(str(eval(dis_msg)))
    elif arg == 'ce':
        dis_msg =''
        t1.set('cleared')
    else:
        dis_msg += arg
        t1.set(dis_msg)
    

mwin = Tk()
mwin.title("My Calculator")
#text area as display
t1=StringVar()
e1=Entry(mwin,textvariable=t1)
e1.grid(row=0,column=0,columnspan=4)

# Buttons
b1=Button(mwin,text='1',command=lambda: bhan('1'))
b2=Button(mwin,text='2',command=lambda: bhan('2'))
b3=Button(mwin,text='3',command=lambda: bhan('3') )
b4=Button(mwin,text='4',command=lambda: bhan('4'))
b5=Button(mwin,text='5',command=lambda: bhan('5'))
b6=Button(mwin,text='6',command=lambda: bhan('6'))
b7=Button(mwin,text='7',command=lambda: bhan('7') )
b8=Button(mwin,text='8',command=lambda: bhan('8'))
b9=Button(mwin,text='9',command=lambda: bhan('9') )
b0=Button(mwin,text='0',command=lambda: bhan('0'))
bp=Button(mwin,text='+',command=lambda: bhan('+'))
bm=Button(mwin,text='-',command=lambda: bhan('-'))
bclr=Button(mwin,text='CE',command=lambda: bhan('ce'))
be=Button(mwin,text='=',command=lambda: bhan('='))

b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=2,column=0)
b4.grid(row=2,column=1)
b5.grid(row=3,column=0)
b6.grid(row=3,column=1)
b7.grid(row=4,column=0)
b8.grid(row=4,column=1)
b9.grid(row=5,column=0)
b0.grid(row=5,column=1)
bp.grid(row=1,column=2)
bm.grid(row=1,column=3)
bclr.grid(row=2,column=2)
be.grid(row=2,column=3)

mwin.mainloop()