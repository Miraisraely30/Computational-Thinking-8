from utils import *

x1 = -200
y1 = 150
x2 = -200
y2 = 0
x3 = -200
y3 = -125
x4 = -200
y4 = -200



set_background("Farm")
t1 = create_sprite("bunnyy (1)",x1,y1)
t2 = create_sprite("corgi",x2,y2)
t3 = create_sprite("kitten",x3,y3)
t4 = create_sprite("BIRDY (1)",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(40):
    x1 += random.randint(5,15)
    x2 += random.randint(5,15)
    x3 += random.randint(5,15)
    x4 += random.randint(5,15)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
s5 = create_sprite("farmer ",-200,-200)
s5.color("white")
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("Bunny wins!", font = ("Arial", 40, "normal"))
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write("Puppy wins!", font = ("Arial", 40, "normal"))
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    s5.write("Cat wins!", font = ("Arial", 40, "normal"))
elif x4 >= x1 and x4 >= x3 and x4 >= x2:
    s5.write("Bird wins!", font = ("Arial", 40, "normal"))
turtle.exitonclick()