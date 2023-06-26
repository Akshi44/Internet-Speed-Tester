# pip install tkinter
from tkinter import *
# pip install speedtest-cli
import speedtest  
def speedcheck():
    sp=speedtest.Speedtest(secure=True)
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+'Mbps'
    up=str(round(sp.upload()/(10**6),3))+'Mbps'
    lab_down.config(text=down)
    lab_up.config(text=up)
    
    
sp=Tk()
sp.title("Internet Speed Test ")
sp.geometry("500x520")
sp.config(bg="Blue")
lab = Label(sp,text="Internet Speed Test",font=('Time New Roman',30,"bold"),bg='Blue',fg='White')
lab.place(x=50,y=30,height=50,width=400)
lab = Label(sp,text="Download Speed",font=('Time New Roman',30,"bold"))
lab.place(x=50,y=120,height=50,width=400)
lab_down = Label(sp,text="00",font=('Time New Roman',30,"bold"))
lab_down.place(x=50,y=190,height=50,width=400)
lab = Label(sp,text="Upload Speed",font=('Time New Roman',30,"bold"))
lab.place(x=50,y=280,height=50,width=400)
lab_up = Label(sp,text="00",font=('Time New Roman',30,"bold"))
lab_up.place(x=50,y=350,height=50,width=400)
button=Button(sp,text="Check Speed",font=('Time New Roman',30,"bold"),relief=RAISED,bg='Red',command=speedcheck)
button.place(x=50,y=440,height=50,width=400)

sp.mainloop() 


 