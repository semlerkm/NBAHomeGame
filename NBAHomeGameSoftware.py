
import random as rand
import tkinter as tk
from tkinter import *

master=Tk()

master.geometry("750x270")
master.title("NBA Home Game Software")
Label(master, text='Team #1').grid(row=0, column=2)
Label(master, text='Team #2').grid(row=0, column=4)
team1=Entry(master)
team2=Entry(master)
team1.grid(row=0, column=3)
team2.grid(row=0, column=5)

canvas = Canvas(master, bg="#1D428A")
canvas.grid(row=2, column=3)

def matchUp():
    t1 = team1.get()
    t2 = team2.get()
    global teams
    teams = [t1, t2]
    i = rand.randint(0,1)
    winner=teams[i]
    canvas.create_text(200, 50, text="\nThe "f"{winner} win\n this matchup. This is due\nto the Knicks higher\nhome game win percentage\nand higher team strength.", fill="black", font=('Helvetica 15 bold'))

    
#canvas.create_text(300, 50, text="The New York Knicks win this matchup.This is due to the Knicks higher\nhome game win percentage\nand higher team strength", fill="black", font=('Helvetica 15 bold'))

Button(master, text="Submit Matchup",
           command=matchUp).grid(row=5)


master.mainloop()