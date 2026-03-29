import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        a1 = float(entry_a1.get())
        a2 = float(entry_a2.get())
        a3 = float(entry_a3.get())

        m1 = float(entry_m1.get())
        m2 = float(entry_m2.get())
        m3 = float(entry_m3.get())

        d1 = float(entry_d1.get()) / 2.54
        d2 = float(entry_d2.get()) / 2.54
        d3 = float(entry_d3.get()) / 2.54

        SN = (a1*m1*d1) + (a2*m2*d2) + (a3*m3*d3)

        sn_provided_var.set(f"{SN:.3f}")

        SN_required = 8.863
        sn_required_var.set(f"{SN_required:.3f}")

        total = float(entry_d1.get()) + float(entry_d2.get()) + float(entry_d3.get())
        thickness_var.set(f"{total:.1f} cm")

    except:
        pass


root = tk.Tk()
root.title("AASHTO 1993 Pavement Design")
root.geometry("900x500")
root.configure(bg="#0b1220")

title = tk.Label(root, text="ออกแบบผิวทางลาดยาง 5 ชั้น — AASHTO 1993",
                 fg="white", bg="#0b1220", font=("Arial",16,"bold"))
title.pack(pady=10)

frame_cards = tk.Frame(root, bg="#0b1220")
frame_cards.pack()

sn_required_var = tk.StringVar(value="0.000")
sn_provided_var = tk.StringVar(value="0.000")
thickness_var = tk.StringVar(value="0 cm")

def card(parent, title, var):
    f = tk.Frame(parent, bg="#13203b", padx=20, pady=10)
    tk.Label(f,text=title,fg="white",bg="#13203b").pack()
    tk.Label(f,textvariable=var,fg="white",bg="#13203b",
             font=("Arial",14,"bold")).pack()
    f.pack(side="left", padx=10)

card(frame_cards,"SN REQUIRED",sn_required_var)
card(frame_cards,"SN PROVIDED",sn_provided_var)
card(frame_cards,"รวมความหนา",thickness_var)

table = tk.Frame(root,bg="#0b1220")
table.pack(pady=20)

headers = ["Layer","a","m","Thickness (cm)"]
for i,h in enumerate(headers):
    tk.Label(table,text=h,fg="white",bg="#0b1220").grid(row=0,column=i)

def row(r,name):
    tk.Label(table,text=name,fg="white",bg="#0b1220").grid(row=r,column=0)

row(1,"AC")
row(2,"Base")
row(3,"Subbase")

entry_a1 = tk.Entry(table); entry_a1.insert(0,"0.40")
entry_m1 = tk.Entry(table); entry_m1.insert(0,"1.1")
entry_d1 = tk.Entry(table); entry_d1.insert(0,"20")

entry_a2 = tk.Entry(table); entry_a2.insert(0,"0.18")
entry_m2 = tk.Entry(table); entry_m2.insert(0,"1.1")
entry_d2 = tk.Entry(table); entry_d2.insert(0,"40")

entry_a3 = tk.Entry(table); entry_a3.insert(0,"0.13")
entry_m3 = tk.Entry(table); entry_m3.insert(0,"1.1")
entry_d3 = tk.Entry(table); entry_d3.insert(0,"40")

entries = [
    (entry_a1,entry_m1,entry_d1),
    (entry_a2,entry_m2,entry_d2),
    (entry_a3,entry_m3,entry_d3)
]

for r,(a,m,d) in enumerate(entries, start=1):
    a.grid(row=r,column=1)
    m.grid(row=r,column=2)
    d.grid(row=r,column=3)

btn = tk.Button(root,text="คำนวณ",command=calculate,
                bg="#3b82f6",fg="white",font=("Arial",12))
btn.pack(pady=10)

root.mainloop()
