# Imports
from random import Random, randrange
from tkinter import *

top = Tk()
top.geometry("800x500")
# creating a simple canvas
c = Canvas(top, bg="black", height="500", width="800")

# Loop in charge of making stars for the background on the canvas 100 stars.
for i in range(100):
    # Variables generating random values 0-500 and 0-800 the span of canvas.
    x = randrange(800)
    y = randrange(500)
    r = 1.5

    # Creating coordinates for stars.
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    c.create_oval(x0, y0, x1, y1, outline="#ffffff", fill="#fffdc7", width=2)
    c.pack()

textSpaceInvaders = c.create_text(400, 50, text="SPACE INVADERS", fill="white", font=('Helvetica 50 bold'))
c.pack()


# This function takes in the action of a button being pressed (easy, medium, hard)
def action(buttonClicked):
    # This function is in charge of the event handling including the movement keys of the spaceship 'a' and 'd' and
    # the shooter 'w.
    def move(event):

        # This if statement handles the 'a' key and the spaceship moving left.
        if event.char == "a":
            c.move(spaceship, -10, 0)
        # This if statement handles the 'a' key and the spaceship moving right.
        if event.char == "d":
            c.move(spaceship, 10, 0)
        # This if statement handles the 'w' key and the laser shooting.
        if event.char == "w":
            spaceshipCoor = c.coords(spaceship)
            laser = c.create_line(spaceshipCoor[0], 400 - 10, spaceshipCoor[0], 400 - 100, width=5, fill='red')
            top.after(200, lambda: c.delete(laser))

            # These if statements measure and determine if the laser shoots the bad guys.
            if 30 <= spaceshipCoor[0] <= 120:
                c.delete(rect1)

            if 130 <= spaceshipCoor[0] <= 220:
                c.delete(rect2)

            if 230 <= spaceshipCoor[0] <= 320:
                c.delete(rect3)

            if 330 <= spaceshipCoor[0] <= 420:
                c.delete(rect4)

            if 430 <= spaceshipCoor[0] <= 520:
                c.delete(rect5)

            if 530 <= spaceshipCoor[0] <= 620:
                c.delete(rect6)

            if 630 <= spaceshipCoor[0] <= 720:
                c.delete(rect7)

            # This if statement is in charge of checking if the badguys are all gone it then would delete the
            # spaceship and display 'you win'.
            if rect1 not in c.find_all() and rect2 not in c.find_all() and rect3 not in c.find_all() and rect4 not in c.find_all() and rect5 not in c.find_all() and rect6 not in c.find_all() and rect7 not in c.find_all():
                c.delete(spaceship)
                text = c.create_text(400, 50, text="YOU WIN", fill="white", font=('Helvetica 50 bold'))
                c.pack()

    # This if statement is when the easy button is clicked.
    if buttonClicked == 1:
        # Get rid of main screen.
        c.delete(textSpaceInvaders)
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        c.pack()

        # Create all the characters.
        spaceship = c.create_polygon((400, 400, 350, 500, 450, 500), fill="grey")
        rect1 = c.create_rectangle(30, 10, 120, 80,
                                   outline="#fb0", fill="#fff")
        rect2 = c.create_rectangle(130, 10, 220, 80,
                                   outline="#fb0", fill="#fff")
        rect3 = c.create_rectangle(230, 10, 320, 80,
                                   outline="#fb0", fill="#fff")
        rect4 = c.create_rectangle(330, 10, 420, 80,
                                   outline="#fb0", fill="#fff")
        rect5 = c.create_rectangle(430, 10, 520, 80,
                                   outline="#fb0", fill="#fff")
        rect6 = c.create_rectangle(530, 10, 620, 80,
                                   outline="#fb0", fill="#fff")
        rect7 = c.create_rectangle(630, 10, 720, 80,
                                   outline="#fb0", fill="#fff")

        def animate():
            # Coordinates of all the rectangles/bad guys
            rect1Coor = c.coords(rect1)
            rect2Coor = c.coords(rect2)
            rect3Coor = c.coords(rect3)
            rect4Coor = c.coords(rect4)
            rect5Coor = c.coords(rect5)
            rect6Coor = c.coords(rect6)
            rect7Coor = c.coords(rect7)

            # Moves and animates the rectangles.
            c.move(rect1, 0, 0.5)
            c.move(rect2, 0, 0.5)
            c.move(rect3, 0, 0.5)
            c.move(rect4, 0, 0.5)
            c.move(rect5, 0, 0.5)
            c.move(rect6, 0, 0.5)
            c.move(rect7, 0, 0.5)
            top.after(100, animate)

            # These if statements check if the rectangle still exists and if they are passed the bounds of screen then
            # delete characters and print you loose on screen.
            if rect1 in c.find_all() and rect1Coor[3] > 500:
                # Delete remainder of characters on screen.
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()

            if rect2 in c.find_all() and rect2Coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect3 in c.find_all() and rect3Coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect4 in c.find_all() and rect4Coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect5 in c.find_all() and rect5Coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect6 in c.find_all() and rect6Coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect7 in c.find_all() and rect7Coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()

        animate()
        top.bind("<Key>", move)

        top.mainloop()

    # This if statement is when the easy button is clicked.
    elif buttonClicked == 2:

        # Get rid of main screen.
        c.delete(textSpaceInvaders)
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        c.pack()

        # Create all the characters.
        spaceship = c.create_polygon((400, 400, 350, 500, 450, 500), fill="grey")
        rect1 = c.create_rectangle(30, 10, 120, 80,
                                   outline="#fb0", fill="#fff")
        rect2 = c.create_rectangle(130, 10, 220, 80,
                                   outline="#fb0", fill="#fff")
        rect3 = c.create_rectangle(230, 10, 320, 80,
                                   outline="#fb0", fill="#fff")
        rect4 = c.create_rectangle(330, 10, 420, 80,
                                   outline="#fb0", fill="#fff")
        rect5 = c.create_rectangle(430, 10, 520, 80,
                                   outline="#fb0", fill="#fff")
        rect6 = c.create_rectangle(530, 10, 620, 80,
                                   outline="#fb0", fill="#fff")
        rect7 = c.create_rectangle(630, 10, 720, 80,
                                   outline="#fb0", fill="#fff")

        def animate():
            # Coordinates of all the rectangles/bad guys
            rect1coor = c.coords(rect1)
            rect2coor = c.coords(rect2)
            rect3coor = c.coords(rect3)
            rect4coor = c.coords(rect4)
            rect5coor = c.coords(rect5)
            rect6coor = c.coords(rect6)
            rect7coor = c.coords(rect7)

            # Moves and animates the rectangles.
            c.move(rect1, 0, 0.5)
            c.move(rect2, 0, 0.5)
            c.move(rect3, 0, 0.5)
            c.move(rect4, 0, 0.5)
            c.move(rect5, 0, 0.5)
            c.move(rect6, 0, 0.5)
            c.move(rect7, 0, 0.5)
            top.after(50, animate)

            # These if statements check if the rectangle still exists and if they are passed the bounds of screen then
            # delete characters and print you loose on screen.
            if rect1 in c.find_all() and rect1coor[3] > 500:
                # Delete remainder of characters on screen.
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()

            if rect2 in c.find_all() and rect2coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect3 in c.find_all() and rect3coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect4 in c.find_all() and rect4coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect5 in c.find_all() and rect5coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect6 in c.find_all() and rect6coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect7 in c.find_all() and rect7coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()

        animate()
        top.bind("<Key>", move)

        top.mainloop()


    else:

        # Get rid of main screen.
        c.delete(textSpaceInvaders)
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        c.pack()

        # Create all the characters.
        spaceship = c.create_polygon((400, 400, 350, 500, 450, 500), fill="grey")
        rect1 = c.create_rectangle(30, 10, 120, 80,
                                   outline="#fb0", fill="#fff")
        rect2 = c.create_rectangle(130, 10, 220, 80,
                                   outline="#fb0", fill="#fff")
        rect3 = c.create_rectangle(230, 10, 320, 80,
                                   outline="#fb0", fill="#fff")
        rect4 = c.create_rectangle(330, 10, 420, 80,
                                   outline="#fb0", fill="#fff")
        rect5 = c.create_rectangle(430, 10, 520, 80,
                                   outline="#fb0", fill="#fff")
        rect6 = c.create_rectangle(530, 10, 620, 80,
                                   outline="#fb0", fill="#fff")
        rect7 = c.create_rectangle(630, 10, 720, 80,
                                   outline="#fb0", fill="#fff")

        def animate():
            # Coordinates of all the rectangles/bad guys
            rect1coor = c.coords(rect1)
            rect2coor = c.coords(rect2)
            rect3coor = c.coords(rect3)
            rect4coor = c.coords(rect4)
            rect5coor = c.coords(rect5)
            rect6coor = c.coords(rect6)
            rect7coor = c.coords(rect7)

            # Moves and animates the rectangles.
            c.move(rect1, 0, 0.5)
            c.move(rect2, 0, 0.5)
            c.move(rect3, 0, 0.5)
            c.move(rect4, 0, 0.5)
            c.move(rect5, 0, 0.5)
            c.move(rect6, 0, 0.5)
            c.move(rect7, 0, 0.5)
            top.after(20, animate)

            # These if statements check if the rectangle still exists and if they are passed the bounds of screen then
            # delete characters and print you loose on screen.
            if rect1 in c.find_all() and rect1coor[3] > 500:
                # Delete remainder of characters on screen.
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()

            if rect2 in c.find_all() and rect2coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect3 in c.find_all() and rect3coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect4 in c.find_all() and rect4coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect5 in c.find_all() and rect5coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect6 in c.find_all() and rect6coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()
            if rect7 in c.find_all() and rect7coor[3] > 500:
                c.delete(spaceship)
                c.delete(rect1)
                c.delete(rect2)
                c.delete(rect3)
                c.delete(rect4)
                c.delete(rect5)
                c.delete(rect6)
                c.delete(rect7)
                text = c.create_text(400, 50, text="YOU LOOSE", fill="white", font=('Helvetica 50 bold'))
                c.pack()

        animate()
        top.bind("<Key>", move)

        top.mainloop()


# Creates buttons for homescreen.
btn1 = Button(top, text='PRESS E - EASY', width=10,
              height=2, bg="white", command=lambda: action(1))

btn2 = Button(top, text='PRESS M - MEDIUM', width=10,
              height=2, bg="white", command=lambda: action(2))

btn3 = Button(top, text='PRESS H - HARD', width=10,
              height=2, bg="white", command=lambda: action(3))

# Place the buttons on the canvas.
btn1.place(x=350, y=100)
btn2.place(x=350, y=200)
btn3.place(x=350, y=300)

c.pack()

top.mainloop()
