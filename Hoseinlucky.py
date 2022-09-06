from cgitb import text
from distutils import command
from logging import root
from select import select
from struct import pack
from tkinter import *
import tkinter
from turtle import color, width
from tkinter import messagebox  
from numpy import size
import webbrowser
from playsound import playsound
import pygame
import time
import os
from tkinter import filedialog as fd
import datetime
root=Tk()
root.title("Hosein lucky")
root.geometry("1280x720")
root.resizable(width=False,height =False)
bg = PhotoImage(file = "data/This made by Hoseinlucky.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

x = datetime.datetime.now()

l = x.day - 6




h_text = Label(root, text = f"Updated {l} days ago",bg="grey",font=('Helvetica','10','bold'))
h_text.place(x =80 ,y=650)

l_text = Label(root, text = "Salvatore Family",bg="grey",font=('Helvetica','20','bold'))
l_text.place(x =960 ,y=80)




a_text = Label(root, text = "last Updated 4/6/2022",bg="grey",font=('Helvetica','15','bold'))
a_text.place(x =975 ,y=670)


def wemod():
    webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open_new("https://storage-cdn.wemod.com/app/releases/stable/WeMod-7.2.0.exe")

btn0=tkinter.Button(height="1",width="50",text="Wemod",command=wemod)
btn0.place(x =900 ,y=400)


def youtube():
    webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open_new("https://www.youtube.com/c/Hoseinlucky")

btn1=tkinter.Button(height="1",width="15",text="youtube",command=youtube)
btn1.place(x =1100 ,y=160)

def link():
    webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open_new("https://cdn.discordapp.com/attachments/920390293755424839/961255571691044894/lucky_TM.CT")

btn2=tkinter.Button(height="1",width="50",text="Unlock all",command=link)
btn2.place(x =900 ,y=200)

def discord():
    webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open_new("https://discord.gg/hR6Dg48Nyx")

btn3=tkinter.Button(height="1",width="50",text="discord Channel",command=discord)
btn3.place(x =900 ,y=240)


def savefiles1():
    webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open_new("https://cdn.discordapp.com/attachments/901393507229515787/922170923732303883/1.save")

btn4=tkinter.Button(height="1",width="50",text="Save Files Proleague",command=savefiles1)
btn4.place(x =900 ,y=280)


def savefiles2():
    webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open_new("https://cdn.discordapp.com/attachments/901393507229515787/923996862221017188/1.save")

btn4=tkinter.Button(height="1",width="50",text="Save Files Black ice",command=savefiles2)
btn4.place(x =900 ,y=320)

def engine():
        webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open_new("https://d1tvmj3dyb0q0v.cloudfront.net/installer/44937140/497740976906629284")
btn7=tkinter.Button(height="1",width="50",text="Cheat engine",command=engine)
btn7.place(x =900 ,y=360)


    

def info():
    messagebox.showinfo("Information","This made by Hosein lucky")
btn5=tkinter.Button(height="1",width="20",text="Info",command=info)
btn5.place(x =920 ,y=630)


def Exit():
    exit()


btn6=tkinter.Button(height="1",width="20",text="Exit",command=Exit)
btn6.place(x =1090 ,y=630)



pygame.init()

def play():
    pygame.mixer.music.load("data/dataM/Stephen.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
root.command = play()


def stopm():
    pygame.mixer.music.stop()
    

stop = Button(root,text="Stop Music",command=stopm)
stop.place(x = 1000,y=450)




start = Button(root,text="Start Music",command=play)
start.place(x =1100 ,y=450)



def tick():
    setTime = time.strftime('%I: %M %S %p')
    clock.config(text=setTime )
    clock.after(200, tick)
clock = Label(root,height="1",width="20", font=('time','15','bold'),bg = "gray")
clock.place(x =20 ,y=680)
if __name__ == '__main__' :
    tick()



# def ost():
#     os.startfile("WeMod-Setup.exe")


# ost = Button(root,text="ostst",command=ost)
# ost.place(x =500 ,y=450)




def twitch():
    webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open_new("https://www.twitch.tv/hosein__lucky")
btn9=tkinter.Button(height="1",width="15",text="twitch",command=twitch)
btn9.place(x =950 ,y=160)





root.mainloop()

