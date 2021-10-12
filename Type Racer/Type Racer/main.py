# TypeRacer

import sys
from tkinter import *
import random
#import winsound


root = Tk()

# variable assignment
speed1 = 0
count = 0
i = 0
speed2 = 0
inc = 0
wcount = 0

def gameframe(xmove):
    app = Tk()

    mylist1 = "As I sit in my room late at night, staring at the computer screen, I decide it would be a good idea to create this text. There isn't much meaning to it, other than to get some simple practice."
    mylist2 = "An appraisal invites the bond. The wine breaks an instructed employer underneath an economics. The domestic exits near a servant. An ancient comic sweeps. A fashioned autumn stumbles inside a criminal"
    mylist3 = "Lines of weeds criss crossed the cracked parking lot of the Seashell Motor Courts. The flaking paint on the buildings had chalked to a pastel pink on walls covered with graffiti. Many of the windows had been smashed out. Where the sign had been, atop rusting steel posts, only the metal outline of a seashell remained."

    # select random paragraph
    choice = random.choice([mylist1, mylist2, mylist3])

    app.geometry("800x400")
    app.title("TypeRacer")

    # text area 8 70
    #back1= PhotoImage(file="bg2.png")
    x = Text(app, height = 8, width = 100 , bg = "#90cb8d")
    x.pack(anchor=CENTER)
    #x.create_image(8, 100, anchor=CENTER, image=back1)

    # canvas
    w = Canvas(app, width=800, height=400)
    app.configure(background='#DAF7A6')
    w.configure(background='#cfa672')
    w.pack()

    # Display the paragraph 410 180
    if choice == mylist1:
        text1 = "As I sit in my room late at night, staring at the computer screen, I decide it would be a good idea to \ncreate this text. There isn't much meaning to it, other than to get some simple practice."
        w.create_text(400, 190, text=text1, font=("Comic Sans MS", 11))
    if choice == mylist2:
        text2 = "An appraisal invites the bond. The wine breaks an instructed employer underneath an economics. \nThe domestic exits near a servant. An ancient comic sweeps. A fashioned autumn stumbles inside \na criminal"
        w.create_text(400, 190, text=text2, font=("Comic Sans MS", 11))
    if choice == mylist3:
        text3 = "Lines of weeds criss crossed the cracked parking lot of the Seashell Motor Courts. The flaking paint on the \nbuildings had chalked to a pastel pink on walls covered with graffiti. Many of the windows had been \nsmashed out. Where the sign had been, atop rusting steel posts, only the metal outline of a seashell remained."
        w.create_text(400, 190, text=text3, font=("Comic Sans MS", 11))

    # road and cars 60 70
    photo3 = PhotoImage(file="road4.png")
    w.create_image(60, 75, image=photo3)

    photo1 = PhotoImage(file="carb.png")
    car1 = w.create_image(55, 107, image=photo1)

    photo2 = PhotoImage(file="cara.png")
    car2 = w.create_image(55, 45
                          , image=photo2)

    def destroy_frame6():
        frame6.destroy()
        move()

    def destroy_frame5():
        frame5.destroy()

    def destroy_frame4():
        frame4.destroy()

    frame6 = Frame(w, width=60, height=60)
    frame6.place(x=340, y=40)
    Label(frame6, text="  Go  ", font=("Magneto", 36), background="#F39C12").pack(anchor=NW)
    frame6.after(4000, destroy_frame6)

    frame5 = Frame(w, width=60, height=60)
    frame5.place(x=340, y=30)
    Label(frame5, text=" Set ", font=("Magneto", 36), background="#F39C12").pack(anchor=NW)
    frame5.after(3000, destroy_frame5)

    frame4 = Frame(w, width=60, height=60)
    frame4.place(x=340, y=30)
    Label(frame4, text="Ready", font=("Magneto", 36), background="#F39C12").pack(anchor=NW)
    frame4.after(2000, destroy_frame4)

    def retrieve_input(temp):
        global i, count, speed1, wcount
        if temp == "quoteright":
            temp = "'"
        if temp == "space":
            temp = " "
            wcount = wcount + 1
        if temp == "period":
            temp = "."
        if temp == "comma":
            temp = ","
        if temp == "Shift_L" and temp.isalpha():
            temp = temp.upper()
        if temp == "Shift_R" and temp.isalpha():
            temp = temp.upper()
        if temp == "BackSpace" and count == 0:
            if i > 0:
                i = i - 1
        if temp != choice[i]:
            if temp != "Caps_Lock" and temp != "BackSpace" and temp != "Shift_L" and temp != "Shift_R":
                count = count + 1
        if temp == "BackSpace":
            if count > 0:
                count = count - 1
        if temp == choice[i] and count == 0 and speed1 < 690:
            w.move(car1, 5, 0)
            i = i + 1
            speed1 = speed1 + 5
        '''elif count!=0:
            if temp != "BackSpace" and temp != "Caps_Lock" and temp != "Shift_L" and temp != "Shift_R" :
                frequency = 2500  # Set Frequency To 2500 Hertz
                duration = 500  # Set Duration To 1000 ms == 1 second
                winsound.Beep(frequency, duration)'''
    def key(event):
        temp = event.keysym
        retrieve_input(temp)

    x.bind("<Key>", key)

    def destroy():
        app.destroy()

    def check_position():
        global inc, wcount
        if speed2 == 689.5 and speed1 < 690 and inc == 0:
            FRAME = Frame(app, width=245, height=150)
            FRAME.place(x=555, y=0)
            photolost = PhotoImage(file="loser.png")
            lab = Label(FRAME, image=photolost)
            lab.image = photolost
            lab.pack(anchor=NW)
            wpm = wcount // 0.75
            w.create_text(400, 240, text="Words Per Minute = ", font=("Times", 12))
            w.create_text(480, 240, text=wpm, font=("Times", 12))
            inc = inc + 1

        elif speed1 == 690 and speed2 < 689.5 and inc == 0:
            FRAME = Frame(app, width=245, height=150)
            FRAME.place(x=555, y=0)
            photowin = PhotoImage(file="winner.png")
            lab = Label(FRAME, image=photowin)
            lab.image = photowin
            lab.pack(anchor=NW)
            wpm = wcount // 0.75
            w.create_text(400, 240, text="Words Per Minute = ", font=("Times", 12))
            w.create_text(480, 240, text=wpm, font=("Times", 12))
            inc = inc + 1

    def move():
        global speed2
        while speed2 < 690:
            w.move(car2, 0.5, 0)
            w.after(xmove)
            check_position()
            speed2 = speed2 + 0.5
            w.update()

    app.mainloop()

def easy():
    root.destroy()
    gameframe(40)

def normal():
    root.destroy()
    gameframe(30)

def difficult():
    root.destroy()
    gameframe(25)

def difficultylevel():
    root = Toplevel()
    back= PhotoImage(file="bg.png")
    root.geometry("800x400")
    z = Canvas(root, bg="#F5F5F5",width=800, height=400)
    z.pack()
    z.create_image(0, 0, anchor=NW, image=back)
    FRAME7 = Frame(z, width=800, height=400)
    FRAME7.configure(background="#F5F5F5")
    FRAME7.place(x=298, y=60)
    Label(FRAME7, text=" Difficulty ", font=("Copperplate Gothic Bold", 24), background="#F5F5F5" ,).pack(anchor=N)
    buttona = Button(FRAME7, text="Rookie", fg="#31d684", bg='#F5F5F5', font=("Lucida Handwriting", 20), bd="4px",cursor ="hand2",padx = 3,pady = 1 , command=easy).pack(side=TOP)
    
    buttonb = Button(FRAME7, text="Challenger", fg="#f7a643", bg='#F5F5F5', font=("Lucida Handwriting", 20), bd="4px",cursor ="hand2", padx = 4,pady = 2,command=normal).pack(anchor=CENTER)
    
    buttonc = Button(FRAME7, text="  Master  ", fg="#f01111", bg='#F5F5F5', font=("Lucida Handwriting", 20), bd="4px",cursor ="hand2", padx = 37,pady = 3, command=difficult).pack(side=BOTTOM)
    root.mainloop()

def rulesframe():
    root = Toplevel()
    instructions = PhotoImage(file="instructions.png")
    y = Canvas(root, bg='black', width=800, height=350)
    y.pack()
    y.create_image(0, 0, anchor=NW, image=instructions)
    root.mainloop()

# photoImages
photo = PhotoImage(file="title.png")

play = PhotoImage(file="play.png")
exite = PhotoImage(file="exit.png")
rules = PhotoImage(file="rules.png")
back= PhotoImage(file="bg.png")

# root
root.title("TypeRacer")
root.geometry("800x400")

# canvas 800 337
w = Canvas(root, bg='white', width=800, height=337)
w.pack()
w.create_image(0, 0, anchor=NW, image=photo)

# frames
leftframe = Frame(root)
leftframe.pack(side=LEFT)
rightframe = Frame(root)
rightframe.pack(side=RIGHT)
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

# buttons
Buttonstart = Button(leftframe, width=150, height=50, bd="2px", bg ="orange",cursor ="hand2", command=difficultylevel)
Buttonstart.config(image = play)
Buttonstart.grid(row=0, column=0)

Buttonrules = Button(bottomframe,width=150, height=50,bd="2px", bg ="blue", cursor ="hand2",command=rulesframe)
Buttonrules.config(image=rules)
Buttonrules.grid(row=0, column=0)

Buttonexit = Button(rightframe,width=150, height=50,bd="2px", bg ="green", cursor ="hand2",command=quit)
Buttonexit.config(image = exite)
Buttonexit.grid(row=0, column=0)

root.mainloop()
