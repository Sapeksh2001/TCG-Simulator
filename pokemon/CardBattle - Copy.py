import csv
from tkinter import *
from tkinter import ttk
import ttkbootstrap as tboot
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from PIL import ImageTk, Image
import pyttsx3
import random
import time
from tkinter.ttk import Style
from PIL import Image, ImageTk  # Pillow library for image handling
import time
import os
import pygame
import tkinter as tk
from ttkbootstrap import Style
import threading
from tkinter import Frame, Canvas, BOTH, LEFT
from pygame import mixer



class Player:
    plno = 0
    coln = [0, 5, 10, 15, 20, 25, 30, 35]
    rown = 1
    wetv = [0, 1]
    pv = [0, 1, 2]

    def __init__(self, pdata):
        Player.plno += 1
        self.data = [0, 0, 0, 0, 0, 0, 0, 0]
        self.pnm = 1
        self.pn = 1
        self.chbut = [0, 0, 0, 0, 0, 0, 0, 0]
        self.pok = [0, 1, 1, 1, 1, 1, 1, 1]
        self.pics = [0, 0, 0, 0, 0, 0, 0, 0]
        self.typs = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.chimg = [0, 0, 0, 0, 0, 0, 0, 0]
        self.data[0] = [
            pdata[0],
            int(pdata[1]),
            int(pdata[2]),
            int(pdata[3]),
            int(pdata[4]),
            int(pdata[5]),
            int(pdata[6]),
            int(pdata[1]),
            int(pdata[2]),
            int(pdata[3]),
            int(pdata[4]),
            int(pdata[5]),
            int(pdata[6]),
            pdata[7],
            pdata[8],
            pdata[9],
            pdata[10],
        ]
        self.name = Label(
            poke,
            text=self.data[self.pnm - 1][0],
            font="Lato-Bold 25 bold",
            fg="#FFCB05",
            bg="#ffffff",
        )
        self.evopic = Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/Evolve.png")
        self.evorpic = self.evopic.resize((100, 40))
        self.evop = ImageTk.PhotoImage(self.evorpic)
        self.updpic = Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/Update.png")
        self.updrpic = self.updpic.resize((100, 40))
        self.updp = ImageTk.PhotoImage(self.updrpic)
        self.pic = Image.open(self.data[self.pnm - 1][15])
        self.rpic = self.pic.resize((120, 120))
        self.p = ImageTk.PhotoImage(self.rpic)
        self.pics[0] = self.p
        self.imj = Label(poke, image=self.p)
        self.typ1 = ImageTk.PhotoImage(Image.open(self.data[self.pnm - 1][13]))
        self.tp1 = Label(poke, image=self.typ1)
        self.typs[0][0] = self.typ1
        if self.data[self.pnm - 1][13] != self.data[self.pnm - 1][14]:
            self.typ2 = ImageTk.PhotoImage(Image.open(self.data[self.pnm - 1][14]))
            self.tp2 = Label(poke, image=self.typ2)
            self.typs[0][1] = self.typ2
        else:
            self.typ2 = ImageTk.PhotoImage(Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/white.png"))
            self.tp2 = Label(poke, image=self.typ2)
            self.typs[0][1] = self.typ2
        for i in range(6):
            self.chimg[i] = ImageTk.PhotoImage(Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/change.png"))
        self.chimg[0] = ImageTk.PhotoImage(
            Image.open(self.data[self.pnm - 1][15]).resize((35, 35))
        )
        self.hp = tboot.Meter(
            poke,
            amounttotal=self.data[self.pnm - 1][7],
            amountused=self.data[self.pnm - 1][1],
            meterthickness=20,
            subtext=self.data[self.pnm - 1][7],
            bootstyle=SUCCESS,
            stripethickness=5,
            arcrange=270,
            metersize=150,
            arcoffset=135,
            textfont=["Lato-Bold", 30, "bold"],
        )
        self.status_val = Frame(poke)
        self.status_val.grid(
            row=Player.rown + 12, column=Player.coln[Player.plno - 1], columnspan=4
        )
        self.Atk = Label(
            self.status_val,
            text=self.data[self.pnm - 1][8],
            font="Lato-Bold 20 bold",
            fg="#FFCB05",
            bg="#ffffff",
        )
        self.Def = Label(
            self.status_val,
            text=self.data[self.pnm - 1][9],
            font="Lato-Bold 20 bold",
            fg="#FFCB05",
            bg="#ffffff",
        )
        self.SpAtk = Label(
            self.status_val,
            text=self.data[self.pnm - 1][10],
            font="Lato-Bold 20 bold",
            fg="#FFCB05",
            bg="#ffffff",
        )
        self.SpDef = Label(
            self.status_val,
            text=self.data[self.pnm - 1][11],
            font="Lato-Bold 20 bold",
            fg="#FFCB05",
            bg="#ffffff",
        )
        self.Spd = Label(
            self.status_val,
            text=self.data[self.pnm - 1][12],
            font="Lato-Bold 20 bold",
            fg="#FFCB05",
            bg="#ffffff",
        )
        self.clack = tboot.Combobox(
            poke, bootstyle="danger", values=defno, width=5, text="Foe"
        )
        self.clacker = tboot.Combobox(
            poke, bootstyle="danger", values=cnn, width=5, text="Stat"
        )

        self.dmg = Entry(poke, width=5)
        self.checks1 = IntVar()
        self.checks2 = IntVar()
        self.checks3 = IntVar()
        self.checks4 = IntVar()
        self.checks5 = IntVar()
        self.checks6 = IntVar()
        self.checks7 = IntVar()

        self.weather = tboot.Checkbutton(
            poke,
            variable=self.checks1,
            bootstyle="danger-round-toggle",
            text="Weather",
            onvalue=1,
            offvalue=0,
        )
        self.burn = tboot.Checkbutton(
            poke,
            variable=self.checks2,
            bootstyle="danger-round-toggle",
            text="Burn",
            onvalue=1,
            offvalue=0,
        )
        self.badp = tboot.Checkbutton(
            poke,
            variable=self.checks3,
            bootstyle="danger-round-toggle",
            text="Bad Poison",
            onvalue=1,
            offvalue=0,
        )
        self.poison = tboot.Checkbutton(
            poke,
            variable=self.checks4,
            bootstyle="danger-round-toggle",
            text="Poison",
            onvalue=1,
            offvalue=0,
        )
        self.paralyze = tboot.Checkbutton(
            poke,
            variable=self.checks5,
            bootstyle="danger-round-toggle",
            text="Paralyze",
            onvalue=1,
            offvalue=0,
            command=self.paral,
        )
        self.curse = tboot.Checkbutton(
            poke,
            variable=self.checks6,
            bootstyle="danger-round-toggle",
            text="Curse",
            onvalue=1,
            offvalue=0,
        )
        self.poise = 1
        self.display()

    def pokeswitch(self, pokn):
        global PokNam
        if self.pok[pokn - 1] == 1:
            self.pok[pokn - 1] = 0
            ps = tboot.Window(themename="cyborg")
            ps.title("Players")
            PokNam = Entry(ps)
            PokNam.pack()
            PokBut = Button(
                ps,
                text="Enter",
                font="Lato-Bold 18 bold",
                fg="#FFCB05",
                bg="#ffffff",
                command=lambda: self.newpoke(ps, pokn),
            )
            PokBut.pack()
            ps.mainloop()
        else:
            self.pn = pokn
            self.name.configure(text=self.data[self.pn - 1][0])
            self.imj.configure(image=self.pics[self.pn - 1])
            self.tp1.configure(image=self.typs[self.pn - 1][0])
            self.tp2.configure(image=self.typs[self.pn - 1][1])
            self.hp.configure(
                amounttotal=self.data[self.pn - 1][7],
                amountused=self.data[self.pn - 1][1],
            )
            self.hp.amountusedvar.trace("w", self.hpm)
            self.data[self.pn - 1][2] = self.data[self.pn - 1][8]
            self.data[self.pn - 1][3] = self.data[self.pn - 1][9]
            self.data[self.pn - 1][4] = self.data[self.pn - 1][10]
            self.data[self.pn - 1][5] = self.data[self.pn - 1][11]
            self.data[self.pn - 1][6] = self.data[self.pn - 1][12]
            self.Atk.configure(text=self.data[self.pn - 1][8])
            self.Def.configure(text=self.data[self.pn - 1][9])
            self.SpAtk.configure(text=self.data[self.pn - 1][10])
            self.SpDef.configure(text=self.data[self.pn - 1][11])
            self.Spd.configure(text=self.data[self.pn - 1][12])

    def newpoke(self, ps, pokn):
        global PokNam
        Mame = PokNam.get()
        for j in rows:
            if j[0] == Mame:
                self.data[pokn - 1] = [
                    j[0],
                    int(j[1]),
                    int(j[2]),
                    int(j[3]),
                    int(j[4]),
                    int(j[5]),
                    int(j[6]),
                    int(j[1]),
                    int(j[2]),
                    int(j[3]),
                    int(j[4]),
                    int(j[5]),
                    int(j[6]),
                    j[7],
                    j[8],
                    j[9],
                    j[10],
                ]
                self.pnm += 1
                self.pn = pokn
                self.chimg[self.pn - 1] = ImageTk.PhotoImage(
                    Image.open(self.data[self.pn - 1][15]).resize((35, 35))
                )
                self.chbut[self.pn - 1].configure(image=self.chimg[self.pn - 1])
                self.name.configure(text=j[0])
                self.pics[self.pn - 1] = ImageTk.PhotoImage(
                    Image.open(self.data[self.pn - 1][15]).resize((120, 120))
                )
                self.imj.configure(image=self.pics[self.pn - 1])
                self.typs[self.pn - 1][0] = ImageTk.PhotoImage(
                    Image.open(self.data[self.pn - 1][13])
                )
                self.tp1.configure(image=self.typs[self.pn - 1][0])
                if self.data[self.pn - 1][13] != self.data[self.pn - 1][14]:
                    self.typs[self.pn - 1][1] = ImageTk.PhotoImage(
                        Image.open(self.data[self.pn - 1][14])
                    )
                    self.tp2.configure(image=self.typs[self.pn - 1][1])
                else:
                    self.typs[self.pn - 1][1] = ImageTk.PhotoImage(
                        Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/white.png")
                    )
                    self.tp2.configure(image=self.typs[self.pn - 1][1])
                self.hp.configure(
                    amounttotal=self.data[self.pn - 1][7],
                    amountused=self.data[self.pn - 1][1],
                )
                self.hp.amountusedvar.trace("w", self.hpm)
                self.Atk.configure(text=self.data[self.pn - 1][8])
                self.Def.configure(text=self.data[self.pn - 1][9])
                self.SpAtk.configure(text=self.data[self.pn - 1][10])
                self.SpDef.configure(text=self.data[self.pn - 1][11])
                self.Spd.configure(text=self.data[self.pn - 1][12])
                ps.destroy()

    def paral(self):
        nero = self.checks5.get()
        if nero == 1:
            self.data[self.pn - 1][6] = self.data[self.pn - 1][6] - (
                self.data[self.pn - 1][12] // 2
            )
            self.Spd.configure(text=self.data[self.pn - 1][6])
        elif nero == 0:
            self.data[self.pn - 1][6] = self.data[self.pn - 1][6] + (
                self.data[self.pn - 1][12] // 2
            )
            self.Spd.configure(text=self.data[self.pn - 1][6])

    def dyna(self):
        tvall = self.checks7.get()
        if tvall == 1:
            self.data[self.pn - 1][1] += 100
            self.hp.configure(text=self.data[self.pn - 1][1])
            self.data[self.pn - 1][2] += 100
            self.Atk.configure(text=self.data[self.pn - 1][2])
            self.data[self.pn - 1][3] += 100
            self.Def.configure(text=self.data[self.pn - 1][3])
            self.data[self.pn - 1][4] += 100
            self.SpAtk.configure(text=self.data[self.pn - 1][4])
            self.data[self.pn - 1][5] += 100
            self.SpDef.configure(text=self.data[self.pn - 1][5])
            self.data[self.pn - 1][6] -= 100
            self.Spd.configure(text=self.data[self.pn - 1][6])
        else:
            self.data[self.pn - 1][1] = self.data[self.pn - 1][7]
            self.hp.configure(text=self.data[self.pn - 1][1])
            self.data[self.pn - 1][2] = self.data[self.pn - 1][8]
            self.Atk.configure(text=self.data[self.pn - 1][2])
            self.data[self.pn - 1][3] = self.data[self.pn - 1][9]
            self.Def.configure(text=self.data[self.pn - 1][3])
            self.data[self.pn - 1][4] = self.data[self.pn - 1][10]
            self.SpAtk.configure(text=self.data[self.pn - 1][4])
            self.data[self.pn - 1][5] = self.data[self.pn - 1][11]
            self.SpDef.configure(text=self.data[self.pn - 1][5])
            self.data[self.pn - 1][6] = self.data[self.pn - 1][12]
            self.Spd.configure(text=self.data[self.pn - 1][6])

    def display(self):
        self.name.grid(
            row=Player.rown, column=Player.coln[Player.plno - 1], columnspan=4
        )
        self.chbut[0] = Button(
            image=self.chimg[0],
            font="Lato-Bold 18 bold",
            fg="#FFCB05",
            bg="#ffffff",
            command=lambda: self.pokeswitch(1),
        )
        self.chbut[0].grid(
            row=Player.rown + 1, column=Player.coln[Player.plno - 1], sticky="E"
        )
        self.chbut[1] = Button(
            image=self.chimg[1],
            font="Lato-Bold 18 bold",
            fg="#FFCB05",
            bg="#ffffff",
            command=lambda: self.pokeswitch(2),
        )
        self.chbut[1].grid(
            row=Player.rown + 2, column=Player.coln[Player.plno - 1], sticky="E"
        )
        self.chbut[2] = Button(
            image=self.chimg[2],
            font="Lato-Bold 18 bold",
            fg="#FFCB05",
            bg="#ffffff",
            command=lambda: self.pokeswitch(3),
        )
        self.chbut[2].grid(
            row=Player.rown + 3, column=Player.coln[Player.plno - 1], sticky="E"
        )

        self.imj.grid(
            row=Player.rown + 1,
            column=Player.coln[Player.plno - 1] + 1,
            columnspan=2,
            rowspan=3,
            sticky="NEWS",
        )
        self.chbut[3] = Button(
            image=self.chimg[3],
            font="Lato-Bold 18 bold",
            fg="#FFCB05",
            bg="#ffffff",
            command=lambda: self.pokeswitch(4),
        )
        self.chbut[3].grid(
            row=Player.rown + 1, column=Player.coln[Player.plno - 1] + 3, sticky="W"
        )
        self.chbut[4] = Button(
            image=self.chimg[4],
            font="Lato-Bold 18 bold",
            fg="#FFCB05",
            bg="#ffffff",
            command=lambda: self.pokeswitch(5),
        )
        self.chbut[4].grid(
            row=Player.rown + 2, column=Player.coln[Player.plno - 1] + 3, sticky="W"
        )
        self.chbut[5] = Button(
            image=self.chimg[5],
            font="Lato-Bold 18 bold",
            fg="#FFCB05",
            bg="#ffffff",
            command=lambda: self.pokeswitch(6),
        )
        self.chbut[5].grid(
            row=Player.rown + 3, column=Player.coln[Player.plno - 1] + 3, sticky="W"
        )
        self.tp1.grid(
            row=Player.rown + 4, column=Player.coln[Player.plno - 1], columnspan=2
        )

        self.tp2.grid(
            row=Player.rown + 4,
            column=Player.coln[Player.plno - 1] + 2,
            columnspan=2,
        )
        Status = Entry(poke)
        Status.grid(
            row=Player.rown + 5,
            column=Player.coln[Player.plno - 1],
            columnspan=4,
            sticky="EW",
        )
        self.curse.grid(
            row=Player.rown + 6,
            column=Player.coln[Player.plno - 1] + 1,
            columnspan=2,
            padx=5,
            pady=5,
            sticky="W",
        )
        self.paralyze.grid(
            row=Player.rown + 7,
            column=Player.coln[Player.plno - 1] + 1,
            columnspan=2,
            padx=5,
            pady=5,
            sticky="W",
        )
        self.burn.grid(
            row=Player.rown + 8,
            column=Player.coln[Player.plno - 1] + 1,
            columnspan=2,
            padx=5,
            pady=5,
            sticky="W",
        )
        self.poison.grid(
            row=Player.rown + 6,
            column=Player.coln[Player.plno - 1] + 2,
            columnspan=2,
            padx=5,
            pady=5,
            sticky="W",
        )
        self.weather.grid(
            row=Player.rown + 7,
            column=Player.coln[Player.plno - 1] + 2,
            columnspan=2,
            padx=5,
            pady=5,
            sticky="W",
        )
        self.badp.grid(
            row=Player.rown + 8,
            column=Player.coln[Player.plno - 1] + 2,
            columnspan=2,
            padx=5,
            pady=5,
            sticky="W",
        )
        AtkBut = Button(
            poke,
            image=atimg,
            fg="#FFCB05",
            bg="#ffffff",
            relief="flat",
            command=lambda: self.fight(0),
        )
        SpBut = Button(
            poke,
            image=spimg,
            fg="#FFCB05",
            bg="#ffffff",
            relief="flat",
            command=lambda: self.fight(1),
        )
        self.evol = Button(
            image=self.evop,
            font="Lato-Bold 18 bold",
            fg="#FFCB05",
            bg="#ffffff",
            command=self.evolve,
        )
        stbut = Button(
            poke,
            image=self.updp,
            fg="#FFCB05",
            bg="#ffffff",
            font="Lato-Bold 18 bold",
            relief="flat",
            command=self.updat,
        )
        self.evol.grid(
            row=Player.rown + 9, column=Player.coln[Player.plno - 1], columnspan=2
        )
        stbut.grid(
            row=Player.rown + 9, column=Player.coln[Player.plno - 1] + 2, columnspan=2
        )
        self.hp.grid(
            row=Player.rown + 10,
            column=Player.coln[Player.plno - 1],
            rowspan=2,
            columnspan=4,
        )
        self.hp.amountusedvar.trace("w", self.hpm)

        button_images = [atkimg, defimg, spatkimg, spdefimg, spdimg]
        for i, img in enumerate(button_images):
            button = Button(
                self.status_val, image=img, fg="#FFCB05", bg="#ffffff", relief="flat"
            )
            button.grid(row=0, column=Player.coln[Player.plno - 1] + i)

        stats = [self.Atk, self.Def, self.SpAtk, self.SpDef, self.Spd]
        for i, sts in enumerate(stats):
            sts.grid(row=1, column=Player.coln[Player.plno - 1] + i)

        self.clack.grid(row=Player.rown + 15, column=Player.coln[Player.plno - 1] + 1)
        self.clacker.grid(row=Player.rown + 15, column=Player.coln[Player.plno - 1] + 2)
        self.dmg.grid(
            row=Player.rown + 16, column=Player.coln[Player.plno - 1] + 1, columnspan=2
        )
        AtkBut.grid(row=Player.rown + 17, column=Player.coln[Player.plno - 1] + 1)
        SpBut.grid(row=Player.rown + 17, column=Player.coln[Player.plno - 1] + 2)

    def hpm(self, *args):
        if self.data[self.pn - 1][1] == 0:
            mixer.music.load("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/0hp.mp3")
            mixer.music.play(loops=0)
        if self.data[self.pn - 1][1] == 1:
            mixer.music.load("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/1hp.mp3")
            mixer.music.play(loops=0)
        if (self.data[self.pn - 1][1] / self.data[self.pn - 1][7]) * 100 <= 25:
            self.hp["bootstyle"] = DANGER
        elif (self.data[self.pn - 1][1] / self.data[self.pn - 1][7]) * 100 <= 50:
            self.hp["bootstyle"] = WARNING
        else:
            self.hp["bootstyle"] = SUCCESS

    def fight(self, tp):
        b = int(self.clack.get())
        pr = int(self.dmg.get())
        if tp == 0:
            dm = (
                pr
                + self.data[self.pn - 1][2]
                - players[b - 1].data[players[b - 1].pn - 1][3]
            )
            if dm <= 0:
                dm = 0
                engine.say(f"No Damage")
                engine.runAndWait()
                return
            players[b - 1].data[players[b - 1].pn - 1][1] = (
                players[b - 1].data[players[b - 1].pn - 1][1] - dm
            )

            if players[b - 1].data[players[b - 1].pn - 1][1] <= 0:
                players[b - 1].data[players[b - 1].pn - 1][1] = 0
                players[b - 1].hp.configure(amountused=0)
                players[b - 1].hp.amountusedvar.trace("w", players[b - 1].hpm)
                engine.say(
                    f"{players[b - 1].data[players[b - 1].pn-1][0]} is unable to battle"
                )
                engine.runAndWait()
                even = Label(
                    secfra,
                    text=f"{players[b - 1].data[players[b - 1].pn-1][0]} is unable to battle",
                    font="Lato-Bold 10 bold",
                    fg="#FFCB05",
                    bg="#295290",
                )
                even.pack()
                return
            else:
                players[b - 1].hp.configure(
                    amountused=players[b - 1].data[players[b - 1].pn - 1][1]
                )
                players[b - 1].hp.amountusedvar.trace("w", players[b - 1].hpm)
                engine.say(
                    f"{self.data[self.pn-1][0]} has dealt {dm} damage to {players[b - 1].data[players[b - 1].pn-1][0]} and {players[b - 1].data[players[b - 1].pn -  1][1]} hp remains"
                )
                engine.runAndWait()
                even = Label(
                    secfra,
                    text=f"{self.data[self.pn-1][0]} has dealt {dm} damage to {players[b - 1].data[players[b - 1].pn-1][0]} and {players[b - 1].data[players[b - 1].pn -  1][1]} hp remains",
                    font="Lato-Bold 10 bold",
                    fg="#FFCB05",
                    bg="#295290",
                )
                even.pack()
                return
        elif tp == 1:
            dm = (
                pr
                + self.data[self.pn - 1][4]
                - players[b - 1].data[players[b - 1].pn - 1][5]
            )
            if dm <= 0:
                dm = 0
                engine.say(f"No Damage")
                engine.runAndWait()
                return
            players[b - 1].data[players[b - 1].pn - 1][1] = (
                players[b - 1].data[players[b - 1].pn - 1][1] - dm
            )
            if players[b - 1].data[players[b - 1].pn - 1][1] <= 0:
                players[b - 1].data[players[b - 1].pn - 1][1] = 0
                players[b - 1].hp.configure(amountused=0)
                players[b - 1].hp.amountusedvar.trace("w", players[b - 1].hpm)
                engine.say(
                    f"{players[b - 1].data[players[b - 1].pn-1][0]} is unable to battle"
                )
                engine.runAndWait()
                even = Label(
                    secfra,
                    text=f"{players[b - 1].data[players[b - 1].pn-1][0]} is unable to battle",
                    font="Lato-Bold 10 bold",
                    fg="#FFCB05",
                    bg="#295290",
                )
                even.pack()
                return
            else:
                players[b - 1].hp.configure(
                    amountused=players[b - 1].data[players[b - 1].pn - 1][1]
                )
                players[b - 1].hp.amountusedvar.trace("w", players[b - 1].hpm)
                engine.say(
                    f"{self.data[self.pn-1][0]} has dealt {dm} damage to {players[b - 1].data[players[b - 1].pn-1][0]} and {players[b - 1].data[players[b - 1].pn -  1][1]} hp remains"
                )
                engine.runAndWait()
                even = Label(
                    secfra,
                    text=f"{self.data[self.pn-1][0]} has dealt {dm} damage to {players[b - 1].data[players[b - 1].pn-1][0]} and {players[b - 1].data[players[b - 1].pn -  1][1]} hp remains",
                    font="Lato-Bold 10 bold",
                    fg="#FFCB05",
                    bg="#295290",
                )
                even.pack()
                return

    def updat(self):
        honey = [self.Atk, self.Def, self.SpAtk, self.SpDef, self.Spd]
        snx = self.clacker.get()
        cn = int(self.dmg.get())
        sn = cnl[snx]
        if sn == 1:
            self.data[self.pn - 1][1] = self.data[self.pn - 1][1] + (
                (self.data[self.pn - 1][7] * cn) // 100
            )
            if self.data[self.pn - 1][1] < 0:
                self.data[self.pn - 1][1] = 0
            if self.data[self.pn - 1][1] > self.data[self.pn - 1][7]:
                self.data[self.pn - 1][1] = self.data[self.pn - 1][7]
            self.hp.configure(amountused=self.data[self.pn - 1][1])
            self.hp.amountusedvar.trace("w", self.hpm)
        elif sn > 7:
            self.data[self.pn - 1][sn - 6] = cn
            honey[sn - 8].configure(text=self.data[self.pn - 1][sn - 6])
        elif sn == 7:
            self.data[self.pn - 1][1] = cn
            self.hp.configure(amountused=self.data[self.pn - 1][1])
            self.hp.amountusedvar.trace("w", self.hpm)
        else:
            self.data[self.pn - 1][sn] = self.data[self.pn - 1][sn] + (
                (self.data[self.pn - 1][sn + 6] * cn) // 100
            )
            honey[sn - 2].configure(text=self.data[self.pn - 1][sn])

    def evolve(self):
        global PokNam
        ps = tboot.Window(themename="cyborg")
        ps.title("Players")
        PokNam = Entry(ps)
        PokNam.pack()
        PokBut = Button(
            ps,
            text="Evolve",
            font="Lato-Bold 18 bold",
            fg="#FFCB05",
            bg="#ffffff",
            command=lambda: self.evolution(ps),
        )
        PokBut.pack()
        ps.mainloop()

    def evolution(self, ps):
        global PokNam
        Mame = PokNam.get()
        for j in rows:
            if j[0] == Mame:
                self.data[self.pn - 1] = [
                    j[0],
                    int(j[1]),
                    int(j[2]),
                    int(j[3]),
                    int(j[4]),
                    int(j[5]),
                    int(j[6]),
                    int(j[1]),
                    int(j[2]),
                    int(j[3]),
                    int(j[4]),
                    int(j[5]),
                    int(j[6]),
                    j[7],
                    j[8],
                    j[9],
                    j[10],
                ]
                self.chimg[self.pn - 1] = ImageTk.PhotoImage(
                    Image.open(self.data[self.pn - 1][15]).resize((35, 35))
                )
                self.chbut[self.pn - 1].configure(image=self.chimg[self.pn - 1])
                self.name.configure(text=j[0])
                self.pics[self.pn - 1] = ImageTk.PhotoImage(
                    Image.open(self.data[self.pn - 1][15]).resize((120, 120))
                )
                self.imj.configure(image=self.pics[self.pn - 1])
                self.typs[self.pn - 1][0] = ImageTk.PhotoImage(
                    Image.open(self.data[self.pn - 1][13])
                )
                self.tp1.configure(image=self.typs[self.pn - 1][0])
                if self.data[self.pn - 1][13] != self.data[self.pn - 1][14]:
                    self.typs[self.pn - 1][1] = ImageTk.PhotoImage(
                        Image.open(self.data[self.pn - 1][14])
                    )
                    self.tp2.configure(image=self.typs[self.pn - 1][1])
                else:
                    self.typs[self.pn - 1][1] = ImageTk.PhotoImage(
                        Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/white.png")
                    )
                    self.tp2.configure(image=self.typs[self.pn - 1][1])
                self.hp.configure(
                    amounttotal=self.data[self.pn - 1][7],
                    amountused=self.data[self.pn - 1][1],
                )
                self.hp.amountusedvar.trace("w", self.hpm)
                self.Atk.configure(text=self.data[self.pn - 1][8])
                self.Def.configure(text=self.data[self.pn - 1][9])
                self.SpAtk.configure(text=self.data[self.pn - 1][10])
                self.SpDef.configure(text=self.data[self.pn - 1][11])
                self.Spd.configure(text=self.data[self.pn - 1][12])
                ps.destroy()


def playing():
    global pnames
    plays = tboot.Window(themename="cyborg")
    plays.title("Players")
    L2 = Label(
        plays,
        text="Enter names of Pokemons",
        font="Lato-Bold 18 bold",
        fg="#FFCB05",
        bg="#ffffff",
    )
    L2.pack()
    pnames = Entry(plays)
    pnames.pack()
    Enbut = Button(
        plays,
        text="Enter",
        font="Lato-Bold 18 bold",
        fg="#FFCB05",
        bg="#ffffff",
        command=lambda: starter(plays),
    )
    Enbut.pack()
    plays.mainloop()


def starter(plays):
    global pnames, players, defno, vsn, names
    nam = pnames.get()
    names = nam.split(",")
    vsn = len(names)
    for i in range(vsn):
        defno.append(str(i + 1))
    vso = 0
    for yo in names:
        for ro in rows:
            if yo == ro[0]:
                players.append(Player(ro))
                vso += 1
                if vso != vsn:
                    vs = Label(
                        poke,
                        image=vsimg,
                    )
                    vs.grid(row=4, column=vscol[vso - 1], sticky="NS")
    plays.destroy()
global pnames, players, defno, vsn, names

mixer.init()
engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
vscol = [4, 9, 14, 19, 24, 29]
filename = "C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/pokemon.csv"
rows = []
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
players = []
# Merge it with this code
poke = tboot.Window()
poke.title("POKEMON")
poke.geometry("1920x1080")
poke.wm_attributes("-transparentcolor", "#FFFF00")
style = Style()


vsimg = ImageTk.PhotoImage(Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/separate.png"))
wel = Button(
    poke,
    text="WELCOME TO THE POKEMON BATTLE",
    font="Lato-Bold 25 bold",
    fg="#FFCB05",
    bg="#ffffff",
)


# Initialize pygame
pygame.init()

# Game variables
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
FPS = 60
scroll_speed = 2

# Function to initialize Pygame display
def initialize_pygame(embed_frame):
    os.environ["SDL_WINDOWID"] = str(embed_frame.winfo_id())  # Embed Pygame into tkinter
    os.environ["SDL_VIDEODRIVER"] = "windib"  # Use windib video driver
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.init()
    pygame.display.set_caption("Parallax Game")
    return screen

# Load images
def load_images():
    bg_images = []
    for i in range(1, 6):
        bg_image = pygame.image.load(f"C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/plx-{i}.png").convert_alpha()
        bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        bg_images.append(bg_image)

    ground_image = pygame.image.load("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/ground.png").convert_alpha()
    ground_image = pygame.transform.scale(ground_image, (SCREEN_WIDTH, 200))  # Resize ground
    return bg_images, ground_image

# Function to draw the background and ground
def draw_bg(screen, bg_images, bg_scrolls):
    for i, bg_image in enumerate(bg_images):
        speed = 1 + i * 0.2  # Parallax effect
        bg_scrolls[i] = (bg_scrolls[i] + scroll_speed * speed) % SCREEN_WIDTH
        for x in range(2):  # Draw two copies of the image for seamless scrolling
            screen.blit(bg_image, ((x * SCREEN_WIDTH) - bg_scrolls[i], 0))

def draw_ground(screen, ground_image, ground_scroll):
    for x in range(2):
        screen.blit(ground_image, ((x * SCREEN_WIDTH) - ground_scroll, SCREEN_HEIGHT - 200))

# Main game loop for pygame
def run_game(embed_frame):
    # Initialize Pygame display
    screen = initialize_pygame(embed_frame)

    # Load assets
    bg_images, ground_image = load_images()
    bg_scrolls = [0] * len(bg_images)
    ground_scroll = 0

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update scroll positions
        ground_scroll = (ground_scroll + scroll_speed * 2.5) % SCREEN_WIDTH

        # Draw everything
        screen.fill((0, 0, 0))  # Clear screen
        draw_bg(screen, bg_images, bg_scrolls)
        draw_ground(screen, ground_image, ground_scroll)

        pygame.display.flip()  # Update display
        clock.tick(FPS)  # Maintain frame rate

    pygame.quit()

# Function to start the pygame loop in a separate thread
def start_game_thread(embed_frame):
    game_thread = threading.Thread(target=run_game, args=(embed_frame,))
    game_thread.daemon = True  # Allow the thread to close when the main program ends
    game_thread.start()

# Initialize tkinter and ttkbootstrap
event = tk.Tk()
event.title("POKEMON")
event.geometry("1920x1080")


# Apply ttkbootstrap style
main_eve = Frame(event)
main_eve.pack(fill=BOTH, expand=1)

# Create canvas for embedding Pygame
evecan = Canvas(main_eve)
evecan.pack(side=LEFT, fill=BOTH, expand=1)


# Start the game loop in a separate thread
event.after(100, start_game_thread, evecan)


scr = ttk.Scrollbar(main_eve, orient=VERTICAL, command=evecan.yview)
scr.pack(side=RIGHT, fill=Y)
evecan.configure(yscrollcommand=scr.set)
evecan.bind("<Configure>", lambda e: evecan.configure(scrollregion=evecan.bbox("all")))
secfra = Frame(evecan)
evecan.create_window((0, 0), window=secfra, anchor="nw")
evel = Button(
    secfra,
    text="Event Track",
    font="Lato-Bold 10 bold",
    fg="#FFCB05",
    bg="#295290",
)
evel.pack()

defno = []
cnn = [
    "Hp%",
    "Atk%",
    "Def%",
    "SpAtk%",
    "SpDef%",
    "Spd%",
    "Hp",
    "Atk",
    "Def",
    "SpAtk",
    "SpDef",
    "Spd",
]
cnl = {
    "Hp%": 1,
    "Atk%": 2,
    "Def%": 3,
    "SpAtk%": 4,
    "SpDef%": 5,
    "Spd%": 6,
    "Hp": 7,
    "Atk": 8,
    "Def": 9,
    "SpAtk": 10,
    "SpDef": 11,
    "Spd": 12,
}
wel.grid(row=0, column=0, columnspan=48)
atimg = ImageTk.PhotoImage(Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/physical.png"))
spimg = ImageTk.PhotoImage(Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/special.png"))
vsi = Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/separate.png")
vsim = vsi.resize((36, 36))
vsimg = ImageTk.PhotoImage(vsim)
atkimg = ImageTk.PhotoImage(Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/atk.png"))
defimg = ImageTk.PhotoImage(Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/def.png"))
spatkimg = ImageTk.PhotoImage(Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/spatk.png"))
spdefimg = ImageTk.PhotoImage(Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/spdef.png"))
spdimg = ImageTk.PhotoImage(Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/spd.png"))

count = 1


def round():
    global count
    mixer.music.load("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/Sound.mp3")
    mixer.music.play(loops=0)
    count = count + 1  # increase by 1
    rnd.config(text="Round\n\n" + str(count))  # update text
    roun = Label(
        secfra,
        text=f"Round {count}",
        font="Lato-Bold 25 bold",
        fg="#FFCB05",
        bg="#295290",
    )
    roun.pack()
    for i in players:
        poi = i.checks4.get()
        brn = i.checks2.get()
        bpoi = i.checks3.get()
        crs = i.checks6.get()
        weth = i.checks1.get()
        if brn == 1:
            i.data[i.pn - 1][1] = i.data[i.pn - 1][1] - (i.data[i.pn - 1][7] // 10)
        if bpoi == 1:
            i.data[i.pn - 1][1] = i.data[i.pn - 1][1] - (i.data[i.pn - 1][7] // 10)
        if crs == 1:
            i.data[i.pn - 1][1] = i.data[i.pn - 1][1] - (i.data[i.pn - 1][7] // 10) * 3
        if weth == 1:
            i.data[i.pn - 1][1] = i.data[i.pn - 1][1] - (i.data[i.pn - 1][7] // 20)
        if poi == 1:
            ddm = i.poise * 5
            i.data[i.pn - 1][1] = (
                i.data[i.pn - 1][1] - (i.data[i.pn - 1][7] // 100) * ddm
            )
            i.poise += 1
            if i.poise == 4:
                i.poise = 1
        if i.data[i.pn - 1][1] < 0:
            i.data[i.pn - 1][1] = 0
            engine.say(
                f"{players[i.pn - 1].data[players[i.pn - 1].pn-1][0]} is unable to battle"
            )
            engine.runAndWait()
            even = Label(
                secfra,
                text=f"{players[i.pn - 1].data[players[i.pn - 1].pn-1][0]} is unable to battle",
                font="Lato-Bold 10 bold",
                fg="#FFCB05",
                bg="#295290",
            )
            even.pack()
        i.hp.configure(amountused=i.data[i.pn - 1][1])
        i.hp.amountusedvar.trace("w", i.hpm)


genpic = Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/Generate.png")
genrpic = genpic.resize((160, 55))
genp = ImageTk.PhotoImage(genrpic)

pokemon_frame = ttk.Frame(poke, padding=10)
asset_frame = ttk.Frame(poke, padding=10)
# Create a frame for the clock
clock_frame = ttk.Frame(asset_frame, padding=10)
gnrt_frame = ttk.Frame(asset_frame)
  # Adjust column to align with the timer, and stick to the east.




rnd = Button(
    asset_frame,
    text="Round\n1 ",
    command=round,
    font="Lato-Bold 20 bold",
    fg="#FFCB05",
    bg="#ffffff",
)


def animate_number(min_val, max_val, number):
    # Generate 10 random numbers and display them with a delay of 100 milliseconds
    for i in range(15):
        n = random.randint(min_val, max_val)
        gnrt_num.config(text=n)  # Process all pending events
        poke.after(30)  # Wait for 30 milliseconds

    # Display the final generated number with text-to-speech
    gnrt_num.config(text=number)
    engine.say(f"The number is {number}")
    engine.runAndWait()


def generate_number():
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    number = random.randint(min_val, max_val)
    animate_number(min_val, max_val, number)


# Create a frame for the clock

# Add MIN and MAX labels, entries, and Generate button in the frame
min_label = Label(gnrt_frame, text="MIN", font="Lato-Bold 12 bold")
max_label = Label(gnrt_frame, text="MAX", font="Lato-Bold 12 bold")
min_entry = Entry(gnrt_frame, width=5)
max_entry = Entry(gnrt_frame, width=5)
button = Button(gnrt_frame, image=genp, font="Lato-Bold 18 bold", command=generate_number)
gnrt_num = Label(gnrt_frame,text="",font="Lato-Bold 16 bold",fg="#FFCB05",bg="#295290")

# Adjust grid layout within gnrt_frame

##
# Initialize variables for the clock
is_paused = False
timer_running = False
start_time = paused_time = time.time()

# Function to update the timer
def update_timer(timer_label, target_time, is_paused):
    global timer_running
    if is_paused or not timer_running:
        return

    current_time = time.time() - start_time
    remaining_time = max(0, target_time - current_time)
    minutes = int(remaining_time) // 60
    seconds = int(remaining_time) % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
    if remaining_time <= 0:
        timer_label.config(text="00:00")
        timer_running = False
        enable_start_buttons()
    else:
        poke.after(1000, update_timer, timer_label, target_time, is_paused)

# Functions to start, pause, and reset the timer
def start_timer(timer_label, target_time, start_btn):
    global start_time, paused_time, is_paused, timer_running
    if timer_running:
        return
    timer_running = True
    if not is_paused:
        start_time = time.time()
    else:
        start_time = time.time() - (paused_time - start_time)
        is_paused = False
    start_btn.state(['disabled'])
    update_timer(timer_label, target_time, is_paused)

def pause_timer(start_btn):
    global is_paused, paused_time, timer_running
    is_paused = True
    timer_running = False
    paused_time = time.time()
    start_btn.state(['!disabled'])

def reset_timer(timer_label, target_time, start_btn):
    global is_paused, paused_time, start_time, timer_running
    timer_running = False
    is_paused = False
    start_time = time.time()
    paused_time = start_time
    timer_label.config(text=f"{target_time // 60:02d}:{target_time % 60:02d}")
    start_btn.state(['!disabled'])

def enable_start_buttons():
    """Enable all start buttons when necessary."""
    start_button1.state(['!disabled'])

# Load images for the clock buttons
reset_image = Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/Reset.png")
reset_image = reset_image.resize((35, 35), Image.Resampling.LANCZOS)
reset_image = ImageTk.PhotoImage(reset_image)

pause_image = Image.open("C:/Users/Honey/AppData/Local/Programs/Python/Python313/pokemon/Pause.png")
pause_image = pause_image.resize((35, 35), Image.Resampling.LANCZOS)
pause_image = ImageTk.PhotoImage(pause_image)

# Create a separate frame for Pokémon to avoid layout conflicts

# Timer Label in Clock Frame
timer_label = ttk.Label(clock_frame, text="02:00", font="Lato-Bold 20 bold")


# Buttons for the timer in Clock Frame
start_button1 = ttk.Button(clock_frame, image=pause_image, command=lambda: start_timer(timer_label, 120, start_button1))

pause_button1 = ttk.Button(clock_frame, image=pause_image, command=lambda: pause_timer(start_button1))


reset_button1 = ttk.Button(clock_frame, image=reset_image, command=lambda: reset_timer(timer_label, 120, start_button1))
pokemon_frame.grid(row=0, column=1, rowspan=20, columnspan=40, sticky="NW")
asset_frame.grid(row=21, column=0, rowspan=20, columnspan=40, sticky="W")
rnd.grid(row=0,column=0,rowspan=2,columnspan=2,padx=1,pady=1)
clock_frame.grid(row=0, column=4, columnspan=3)
gnrt_frame.grid(row=0, column=7,columnspan=4)



timer_label.grid(row=0, column=0, columnspan=3)
start_button1.grid(row=1, column=0)
pause_button1.grid(row=1, column=1)
reset_button1.grid(row=1, column=2)

min_label.grid(row=0, column=0)
min_entry.grid(row=0, column=1)
max_label.grid(row=0, column=2)
max_entry.grid(row=0, column=3)
button.grid(row=1, column=0, columnspan=4) 
gnrt_num.grid(row=2, column=0, columnspan=4)


playing()
poke.mainloop()
