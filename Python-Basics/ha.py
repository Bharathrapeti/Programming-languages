import turtle

def draw_cake_layer(radius, height):
    turtle.begin_fill()
    turtle.circle(radius, 180)  # top ellipse
    turtle.forward(height)
    turtle.circle(radius, -180)  # bottom ellipse
    turtle.forward(height)
    turtle.end_fill()

def draw_cake():
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.up()
    turtle.goto(0, -150)
    turtle.down()

    layers = [
        {"radius": 100, "height": 40, "color": "#D2691E"},  # Bottom chocolate
        {"radius": 70, "height": 40, "color": "#FFA07A"},   # Middle strawberry
        {"radius": 40, "height": 40, "color": "#FFD700"}    # Top vanilla
    ]

    for layer in layers:
        turtle.color("black", layer["color"])
        draw_cake_layer(layer["radius"], layer["height"])
        turtle.up()
        turtle.forward(layer["height"])
        turtle.down()

    # Candle
    turtle.up()
    turtle.forward(10)
    turtle.down()
    turtle.color("blue")
    turtle.begin_fill()
    turtle.goto(0, 80)
    turtle.goto(0, 120)
    turtle.goto(5, 120)
    turtle.goto(5, 80)
    turtle.end_fill()

    # Flame
    turtle.color("orange")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

    turtle.hideturtle()
    turtle.done()

draw_cake()
