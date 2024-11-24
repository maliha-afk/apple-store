from tkinter import *

screen=Tk()
screen.title("Apple Store")
screen.config(bg="Azure2")
screen.geometry("500x500")

welcom=Label(screen,text="WELCOME TO APPLE STORE",font=("logo",15,"italic","bold"),fg="black",bg="Azure2")
welcom.grid(row=0,column=1)


w_text=Label(screen,text="Watch(375$)",font=("Alice",15,"bold"),fg="black",bg="Azure2")
w_text.grid(row=2,column=0,padx=5)
w_q=Entry(screen,font=("Alice",10,"bold"))
w_q.grid(row=2,column=1,padx=15)


m_text=Label(screen,text="macbook(1599$)",font=("Alice",15,"bold"),fg="black",bg="Azure2")
m_text.grid(row=3,column=0,padx=10)
m_q=Entry(screen,font=("Alice",10,"bold"))
m_q.grid(row=3,column=1,padx=15)


iph_text=Label(screen,text="iphone(799$)",font=("Alice",15,"bold"),fg="black",bg="Azure2")
iph_text.grid(row=4,column=0,padx=5)
iph_q=Entry(screen,font=("Alice",10,"bold"))
iph_q.grid(row=4,column=1,padx=15)


ip_text=Label(screen,text="ipad(999$)",font=("Alice",15,"bold"),fg="black",bg="Azure2")
ip_text.grid(row=5,column=0,padx=5)
ip_q=Entry(screen,font=("Alice",10,"bold"))
ip_q.grid(row=5,column=1,padx=15)


TV_text=Label(screen,text="TV(1290$)",font=("Alice",15,"bold"),fg="black",bg="Azure2")
TV_text.grid(row=6,column=0,padx=5)
TV_q=Entry(screen,font=("Alice",10,"bold"))
TV_q.grid(row=6,column=1,padx=15)


def generatebill():
    w_count=int(w_q.get())
    m_count=int(m_q.get())
    ip_count=int(ip_q.get())
    iph_count=int(iph_q.get())
    Tv_count=int(TV_q.get())
    price=(w_count*375)+(ip_count*999)+(m_count*1599)+(iph_count*799)+(Tv_count*1290)
    my_price.config(text=f"your total bill is {price} $ \n the items you have purchased: \n watch:{w_count}\n macbook:{m_count}\n ipad:{ip_count}\n iphone: {iph_count}\n TV:{Tv_count}")

bill=Button(screen,text=("Generate bill"),font=("Alice",10,"bold"),command=generatebill)
bill.grid(row=7,column=0,padx=5)

def refresh():
    my_price.config(text="")

reset=Button(screen,text="Reset",font=("Alice",10,"bold"),fg="black",command=refresh)
reset.grid(row=7,column=1,padx=5)
my_price=Label(screen,font=("Alice",10,"bold"),fg="black",bg="Azure2")
my_price.grid(row=8,column=1,padx=5)





screen.mainloop()