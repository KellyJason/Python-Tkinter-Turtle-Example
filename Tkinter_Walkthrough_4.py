import os
import tkinter as tk
import turtle

#begining of the window
root= tk.Tk()

#this creates an area for the labes and button to go in
canvas1 = tk.Canvas(root, width = 350, height = 250, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

# this is the label
label1 = tk.Label(root, text='Want to see something ''\n''cool? Click the button!', bg = 'lightsteelblue2',font=('helvetica', 20))

#This adds the label to the canvas
canvas1.create_window(175, 80, window=label1)


#now to try and configure the button to go somewhere
def button ():
  
    t = turtle.Pen() 
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] #clolors
    t.speed(0)
    turtle.bgcolor('black') 
    for x in range(1000): #how mant times
      t.pencolor(colors[x%6]) #cycle through all colors
      t.width(x/100 + 1) #width between lines
      t.forward(x) 
      t.left(59) 

    turtle.done() #turtle done to keep window open after completion

# here is the button   
but1 = tk.Button(text='      Click the Button    ', command = button, bg='green', fg='white', font=('helvetica', 12, 'bold' ))
but1.pack()

#this adds the button to the canvas
canvas1.create_window(175, 180, window=but1)

#end of window
root.mainloop()


