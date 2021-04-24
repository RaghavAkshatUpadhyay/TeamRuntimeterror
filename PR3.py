from tkinter import *
import tkinter as tk
from tkinter import simpledialog
import datetime
import time
import winsound
from threading import *
ROOT = tk.Tk()
ROOT.withdraw()
f = open("disease.txt" , "r")
lst=[]
d= []
i = 0
for i in range(0 , 100):
    if i > 0 :
        print("and ?...")  
    USER_INP = simpledialog.askstring(title="PR-3",
                                  prompt="Enter your Symptoms(Type Exit when Finished).:")   
    if USER_INP == 'exit' or USER_INP == 'Exit' or USER_INP == 'EXIT':
     print("Ok...")   
     break
    else:
     lst.append(USER_INP)        
print("Possible disease(s):") 
for i in range(0 , 11):
    x=f.readline()
    x=x.split()
    t=x[0]
    a=x[1].split('_')
    for i in a:
        for j in lst:
          i=i.replace("-"," ")
          if j == i:
              d.append(t)
              break
d= list(dict.fromkeys(d))
for i in d:
    print(i)           
f.close()
f=open("Med.txt" , "r")
print("Some Suggested Medicenes are shown below :")
for i in range(0 , 11):
    x=f.readline()
    x=x.split()
    t=x[0]
    a=x[1].split('_')
    for i in d:
        if (t==i):
            print("----------------")
            print("For ",t,' :')
            for i in a:
                print(i)
f=open("Hos.txt" , "r")
USER_INP = simpledialog.askstring(title="PR-3",
                                  prompt="Enter your Location (State):") 
print("----------------------------------")
print("List of Affordable Hospitals in ",USER_INP,":")
for i in range(0 , 179):
    x = f.readline()
    x=x.split()
    x[0]=x[0].replace("-"," ")
    if x[0] == USER_INP.swapcase() or x[0] == USER_INP :
        x[1]=x[1].replace("-"," ")
        print(x[1])
USER_INP = simpledialog.askstring(title="PR-3",
                                  prompt="Do you want to set an Alarm for Medication:")
if USER_INP == "YES" or USER_INP == "yes" or USER_INP == "Yes":
    root = Tk()  
    root.geometry("640x320")
    
    def Threading():
        t1=Thread(target=alarm)
        t1.start()
    
    def alarm():
        while True:
            set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
            time.sleep(1)
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            if current_time == set_alarm_time:
                print("BEEP BEEP!!!")
                print ("Kindly take your Medication") 
                winsound.PlaySound("sound.wav",winsound.SND_ASYNC) 
    Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
    Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()
    frame = Frame(root)
    frame.pack()  
    hour = StringVar(root)
    hours = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23', '24'
            )
    hour.set(hours[0])
    
    hrs = OptionMenu(frame, hour, *hours)
    hrs.pack(side=LEFT)
    
    minute = StringVar(root)
    minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23',
            '24', '25', '26', '27', '28', '29', '30', '31',
            '32', '33', '34', '35', '36', '37', '38', '39',
            '40', '41', '42', '43', '44', '45', '46', '47',
            '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59', '60')
    minute.set(minutes[0])
    
    mins = OptionMenu(frame, minute, *minutes)
    mins.pack(side=LEFT)
    
    second = StringVar(root)
    seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23',
            '24', '25', '26', '27', '28', '29', '30', '31',
            '32', '33', '34', '35', '36', '37', '38', '39',
            '40', '41', '42', '43', '44', '45', '46', '47',
            '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59', '60')
    second.set(seconds[0])  
    secs = OptionMenu(frame, second, *seconds)
    secs.pack(side=LEFT)
    Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)
    button_quit = Button(root, text="Exit", command=root.quit)
    button_quit.place(x=400, y=600)
    button_quit.pack(side = BOTTOM)
    root.mainloop()
else:
    pass                