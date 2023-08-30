from gpiozero import LED, Button
import tkinter as tk
from time import sleep
import requests
sega = LED(18)
segb = LED(23)
segc = LED(24)
segd = LED(25)
sege = LED(17)
segf = LED(27)
segg = LED(22)

# Alarm zones
zone1 = Button(13)
zone2 = Button(19)
zone3 = Button(26)
zone4 = Button(19)

# False = unarmed, True = armed
global systemStatus
global z1,z2,z3,z4
systemStatus = 0

def show0():
    # 0
    sega.on()
    segb.on()
    segc.on()
    segd.on()
    sege.on()
    segf.on()
    segg.off()


def show1():
    #1
    sega.off()
    segb.on()
    segc.on()
    segd.off()
    sege.off()
    segf.off()
    segg.off()


def show2():
    #2
    sega.on()
    segb.on()
    segc.off()
    segd.on()
    sege.on()
    segf.off()
    segg.on()  
    

def show3():
    #3
    sega.on()
    segb.on()
    segc.on()
    segd.on()
    sege.off()
    segf.off()
    segg.on() 


def show4():
    #4
    sega.off()
    segb.on()
    segc.on()
    segd.off()
    sege.off()
    segf.on()
    segg.on() 


def show5():
    #5
    sega.on()
    segb.off()
    segc.on()
    segd.on()
    sege.off()
    segf.on()
    segg.on()  
 


def show6():
    #6
    sega.on()
    segb.off()
    segc.on()
    segd.on()
    sege.on()
    segf.on()
    segg.on() 


def show7():
    #7
    sega.on()
    segb.on()
    segc.on()
    segd.off()
    sege.off()
    segf.off()
    segg.off()     



def show8():
    #8
    sega.on()
    segb.on()
    segc.on()
    segd.on()
    sege.on()
    segf.on()
    segg.on()  


def show9():
    #9
    sega.on()
    segb.on()
    segc.on()
    segd.off()
    sege.off()
    segf.on()
    segg.on()    



def showA():
    #A
    sega.on()
    segb.on()
    segc.on()
    segd.off()
    sege.on()
    segf.on()
    segg.on()


def cout_up():
    #0
    show0
    sleep(1)

    #1
    show1()    
    sleep(1)

    #2
    show2() 
    sleep(1)

    #3
    show3()  
    sleep(1)
        
    #4
    show4()
    sleep(1)

    #5
    show5()
    sleep(1)

    #6
    show6() 
    sleep(1)

    #7
    show7() 
    sleep(1)


    #8
    show8()  
    sleep(1)


    #9
    show9()
    sleep(1)



def cout_down():
    #9
    show9    
    sleep(1)

    #8
    show8()  
    sleep(1)

    #7
    show7()   
    sleep(1)

    #6
    show6()  
    sleep(1)

    #5
    show5() 
    sleep(1)

    #4
    show4()  
    sleep(1)

    #3
    show3()    
    sleep(1)

    #2
    show2()  
    sleep(1)

    #1
    show1()    
    sleep(1)
    
    #0
    show0()
    sleep(1)



show0()


def arm_system():
    global systemStatus
    if systemStatus == 0:
        cout_up()
        showA()
        systemStatus = 1

def disarm_system():
    global systemStatus
    if systemStatus == 1:
        cout_down()
        show0()
        systemStatus = 0

api_url = "http://LAPTOP-TDNN94VH:3000/elements"

def update_labels():
    if zone1.is_pressed:
        button1.config(bg="red", fg="white")
        z1 = "activat"
    else:
        button1.config(bg="SystemButtonFace", fg="black")
        z1 = "desactivat"

    if zone2.is_pressed:
        button2.config(bg="red", fg="white")
        z2 = "activat"
    else:
        button2.config(bg="SystemButtonFace", fg="black")
        z2 = "desactivat"

    if zone3.is_pressed:
        button3.config(bg="red", fg="white")
        z3 = "activat"
    else:
        button3.config(bg="SystemButtonFace", fg="black")
        z3 = "desactivat"

    if zone4.is_pressed:
        button4.config(bg="red", fg="white")
        z4 = "activat"
    else:
        button4.config(bg="SystemButtonFace", fg="black")
        z4 = "desactivat"
    data = {
        "z1": z1,
        "z2": z2,
        "z3": z3,
        "z4": z4,
        "systemStatus": systemStatus}
    
    try:
        response = requests.post(api_url, json=data)
        response.raise_for_status()  # Raise an error for non-2xx responses
        print("Data sent successfully:", response.json())
    except requests.exceptions.RequestException as e:
        print("Error sending data to server:", e)

def toggle_system():
    global systemStatus
    if systemStatus == 0:
        systemStatus = 1
        w.config(text="ON/OFF", bg="green", fg="black")
    else:
        systemStatus = 0
        w.config(text="ON/OFF", bg="red", fg="white")

root = tk.Tk()
panel1 = tk.Frame(root)
panel1.pack(side=tk.LEFT, padx=10)

root.title("Alarm")  

title_label = tk.Label(root, text="Alarm", font=("Arial", 16, "bold"))
title_label.pack(fill=tk.X, pady=5)

button1 = tk.Label(panel1, text="Zone 1")
button1.pack(fill=tk.X, pady=5)

button2 = tk.Label(panel1, text="Zone 2")
button2.pack(fill=tk.X, pady=5)

button3 = tk.Label(panel1, text="Zone 3")
button3.pack(fill=tk.X, pady=5)

button4 = tk.Label(panel1, text="Zone 4")
button4.pack(fill=tk.X, pady=5)

w = tk.Button(root, text="Desactivate", bg="red", fg="white", command=disarm_system)
w.pack(fill=tk.X, padx=10)

w = tk.Button(root, text="Activate", bg="green", fg="black", command=arm_system)
w.pack(fill=tk.X, padx=10)

w = tk.Button(root, text="Reset Alarm", bg="blue", fg="white")
w.pack(fill=tk.X, padx=10)

w = tk.Button(root, text="ON/OFF", bg="red", fg="white", command=toggle_system)
w.pack(fill=tk.X, padx=10)

update_labels()



tk.mainloop()
