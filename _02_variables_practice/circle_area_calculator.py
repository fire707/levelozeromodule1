import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    simpledialog.askstring(title='Greeter',prompt="What is your name")
    # simpledialog.askinteger()
    
    # Make a new turtle
    rom=turtle.turtle()
    # Have your turtle draw a circle with the correct radius
    rom.circle(15)
    # my_turtle.circle()

    # Call the turtle .penup() method
turtle.penup('green')

    # Move your turtle to a new x,y position using .goto()
turtle.goto(x,y)

    # Calculate the area of your circle and store it in a variable
area =math.pi*15^2

    # Hint, you can use math.pi
    
    # Write the area of your circle using the turtle .write() method
turtle.write(area)
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle
turtle.hide()

    # Call turtle.done()
turtle.done()
