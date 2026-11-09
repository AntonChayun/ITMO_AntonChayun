import tkinter as tk
from tkinter import font as tkfont
import random
import time 
import pygame 


window = tk.Tk()
window.title('KeYgEn')
window.geometry('500x500')
bg_img = tk.PhotoImage(file='bg_cyberpunk.png')


label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)


Letts = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


label_font = tkfont.Font(family="Courier", size=22, weight="bold")
btn_font = tkfont.Font(family="Courier", size=18, weight="bold")

def generate_key():
    start = random.randint(1, 26)
    end = random.randint(1, 26)
    if end < start:
        start, end = end, start

    interval = Letts[start - 1:end]

    left = str(start)
    mid = "".join(random.choice(interval) for i in range(7)) #кортеж в строку
    right = str(end)
    return left + " " + mid + " " + right

label_plug = tk.Label(text=" ", font=label_font, width=13, bg = "#800080",relief="ridge", bd =4)
label_plug.place(relx=0.5, rely=0.5, anchor="center")

def print_keygen():
    used_label = tk.Label(text=generate_key(), font=label_font, width=13, bg = "#800080", fg = "#00FF00", relief="ridge", bd=4)
    used_label.place(relx=0.5, rely=0.5, anchor="center")#в этих координатах(проценты размера) будет центр лейбла


press = tk.Label(text="Press button to get KeyGen", font="Verdana", bg = "#0000CD", fg = "#00FF00")
press.place(relx=0.5, rely=0.1, anchor="center")
def animation():
    press.config(
        fg=random.choice(["#FF0000", "#FFFF00", "#FF00FF", "#8B4513"])
    )#обновляет fg
    press.after(500, animation) #вызывает функцию через время создавая цикл
animation()




btn = tk.Button(text="GeNeRaTe",command=print_keygen,font=btn_font,bg = "#800080", fg = "#00FF00", activebackground="#800080", activeforeground='#FF0000')
btn.place(relx=0.5, rely=0.7, anchor="center")




pygame.mixer.init()
pygame.mixer.music.load("8bit-lipstick[rebalanced].wav")
pygame.mixer.music.set_volume(0.3)   
pygame.mixer.music.play(-1)   # -1 = зациклить



window.mainloop()
