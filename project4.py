from utils import *

# Section 1 - setup
# TODO - set a background using set_background()
set_background("Smoothie ")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
fruits = 0 
smoothies = 0
cost = 5
# spritelist makes it so i can get rid of the fruit after you make a smoothie 
spritelist = []


# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -270,175)
m1.hideturtle()

# the goal is 2 get 50 smoothies and you do that by clicking space to get fruit and s to make smoothies 

# Section 2 - controls
# TODO - define an action. ex: def my_control()
def make_smoothie(): 
    global smoothies,fruits,cost,x
    if fruits >= cost : 
        smoothies += 1
        fruits -= cost
        cost += 5 
        x = random.randint(-300,300)
        create_sprite("smoothie",x,-200 )
        for i in range(cost):
            fruit = spritelist.pop()
            fruit.hideturtle()
def newfruits(): 
    global fruits, fruit 
    fruits += 1
    x = random.randint(-25,200)
    y = random.randint(-100,200)
    fruit = create_sprite("fruits",x,y)
    # want to change so its different fruits everytime
    spritelist.append(fruit)
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(make_smoothie,"s")
window.onkeypress(newfruits,"space")
# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    m1.clear()
    m1.color("blue")
    m1.write(f"Fruit:{fruits}\nSmoothies:{smoothies}\n Fruit needed:{cost}", font = ("Arial", 20, "normal"))
    # change font 
    if smoothies >= 50:
        m1.clear()
        m1.write("You WIIINNNNN!!!!!!!!!!!!!", font = ("Arial", 20, "normal"))

    time.sleep(0.01)
    window.update()




