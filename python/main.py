from tkinter import *
from turtle import title
from tkintermapview import TkinterMapView

root = Tk() 
root.geometry('800x400')
root.title('pharmacy Online')
root.iconbitmap('icon.gif')
#root.configure(background='white')
#-----------------------------------------------------------
#---------part of software---------------------

def cu():
    country=en.get()
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_address(country, marker=True)


#-------function to button----------
def markazi():
    map = TkinterMapView(root, width=500, height=400, corner_radius=0)
    map.place(x=370,y=35)
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_position(30.1244753084767, 31.438584910076248)
    map.set_zoom(15)
    marker=map.set_marker(30.1244753084767, 31.438584910076248)
    marker.set_text('صيدليه مركزيه')

def markazi2():
    map = TkinterMapView(root, width=500, height=400, corner_radius=0)
    map.place(x=370,y=35)
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_position(30.358411952013547, 31.201951767816873)
    map.set_zoom(15)
    marker=map.set_marker(30.358411952013547, 31.201951767816873)
    marker.set_text('صيدلية مصر')
    
def markazi3():
    map = TkinterMapView(root, width=500, height=400, corner_radius=0)
    map.place(x=370,y=35)
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_position(30.295254585516286, 31.35498255349793)
    map.set_zoom(15)
    marker=map.set_marker(30.295254585516286, 31.35498255349793)
    marker.set_text('صيدلية القرش')
    
def markazi4():
    map = TkinterMapView(root, width=500, height=400, corner_radius=0)
    map.place(x=370,y=35)
    map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
    map.set_position(30.28618129266847, 31.34788200263284)
    map.set_zoom(15)
    marker=map.set_marker(30.28618129266847, 31.34788200263284)
    marker.set_text('صيدلية العرب')    
#-------------- title-------------# 
title1=Label(root,text='Online pharmacy',
             fg='white',
             bg='gray',
             font=('tajwal',18  ),  
            )
title1.pack(fill=X)
#---------------logo--------------#



logo1= PhotoImage(file='mm.png')
lab_log=Label(root, image=logo1, bd=0)
lab_log.place(x=30,y=35)

# -------------entry button----------#
 
l=Label(root, text='country :', font=('tajawal 15') ,fg='black' )
l.place(x=10, y= 230)
# -------------entry square------------#
en=Entry(root, font='tajawal 14', bd=2 , width=10, relief=GROOVE)
en.place(x=140,y=230)
#--------------add butoon---------------#
buttn=Button(root, text='Get country' ,
             font='tajawal 10',
             fg='white', 
             bg='black',
             bd=1,width=10,
             relief=SOLID,
             cursor='hand2', command=cu)
buttn.place(x=250, y=230)
#--------------pharmacy button----------#

b1=Button(root, text='صيدليه مركزيه',
          bg='white',
          fg='black',
          bd=1,
          relief=SOLID,
          font='tajawal 10',
          width=12,
          cursor='hand2',command=markazi)
b1.place(x=10, y=280)

b2=Button(root, text='صيدلية مصر',
          bg='white',
          fg='black',
          bd=1,
          relief=SOLID,
          font='tajawal 10',
          width=12,
          cursor='hand2',command=markazi2)
b2.place(x=130, y=280)

b3=Button(root, text='صيدلية القرش',
          bg='white',
          fg='black',
          bd=1,
          relief=SOLID,
          font='tajawal 10',
          width=12,
          cursor='hand2',command=markazi3)
b3.place(x=10, y=320)

b4=Button(root, text='صيدلية العرب',
          bg='white',
          fg='black',
          bd=1,
          relief=SOLID,
          font='tajawal 10',
          width=12,
          cursor='hand2',command=markazi4)
b4.place(x=130, y=320)

#------------add map----------------#
map = TkinterMapView(root, width=500, height=400, corner_radius=0)
map.place(x=370,y=35)

root.mainloop()
