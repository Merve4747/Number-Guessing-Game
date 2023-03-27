import tkinter as tk
import random

def kontrolEt():
  global sayac
  if sayi1.get().isdigit():
      s1=int(sayi1.get())
      sayac=sayac + 1
      if s1 > sayi2:
          yazi2.configure(text="Daha az")
      elif s1 < sayi2:
          yazi2.configure(text="Daha fazla")
      else:
          yazi2.configure(text="{} defada tahmin ettiniz".format(sayac))
  sayi1.selection_range(0,tk.END)
pencere=tk.Tk()
pencere.title("Sayı Tahmin Oyunu")
pencere.configure(background="pink")
pencere.geometry("320x200")

yazi1=tk.Label(pencere,text="1-10 arasında sayı giriniz",font="Courier 14 bold",width=25,justify="center",background="pink")
yazi1.place(x=15,y=15)

sayi1=tk.Entry(pencere,font="Courier 14 bold",width=15,justify="center",background="#FF91A4")
sayi1.place(x=70,y=50)
sayi1.focus()


kontrol=tk.Button(pencere,text="Kontrol",font="Courier 14 bold",activeforeground="#FF91A4",cursor="hand2",bg="#FF91A4",relief="groove", overrelief="raised",bd=7,activebackground="#FF91A4",command=kontrolEt)
kontrol.place(x=100,y=90)

yazi2=tk.Label(pencere,text="",font="Courier 16 bold",width=25,justify="center",background="pink")
yazi2.place(x=-10,y=140)

sayi2=random.randint(1,10)
sayac = 0

pencere.mainloop()
