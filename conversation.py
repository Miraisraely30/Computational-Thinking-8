# Section 1 - Your code
from utils import *
player_name = input("What is your name?    ")

set_background("DISCO ")

s1 = create_sprite("Kat", -100, 0)
s2 = create_sprite("DOGGY", 100, 0)
s3 = create_sprite("bunnyy", 250, -50)
s4 = create_sprite("BIRDY", -250, -50)

s1.color("white")
s2.color("white")
time.sleep(5)

s1.write("Where are we?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s2.write("a partyyyyy!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s2.clear()
window.update()
time.sleep(1)

s2.write ("its super funnnnn", font = ("Arial", 20, "normal")")

s2.clear()
window.update()
time.sleep(1)

s1.write(f"I'm looking for {player_name}",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s1.write("Have you seen them?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()