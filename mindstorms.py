import turtle

def draw_square(some_turtle):


    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():


    
    window = turtle.Screen()
    window.bgcolor("blue")

    #brad draws a bunch of squares
    brad = turtle.Turtle()
    brad.shape("square")
    brad.color("black")
    brad.speed(350)

    for i in range(0,36):
        draw_square(brad)
        brad.right(10)

    # angie draws a circle

    #angie = turtle.Turtle()
    #angie.hideturtle()
    #angie.color("green")
    #angie.circle(50)
    #angie.speed(10)

    # steve draws a triangle
    
    #steve = turtle.Turtle()
    #steve.speed(10)
    #steve.up()
    #steve.setpos(150, 150)
    #steve.down()   
    #for x in range(0,3):
        #steve.forward(100)
        #steve.right(120)
    
    #ken draws a bunch of circles that do cool things
    ken = turtle.Turtle()
    ken.color("green")
    ken.speed(100)
    ken.up()
    ken.setpos(200,200)
    ken.down()
    for i in range (0,19):
        ken.circle(50)
        ken.right(20)

    window.exitonclick()

draw_art()
