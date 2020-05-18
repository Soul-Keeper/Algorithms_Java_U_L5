import turtle
import random
import time

def create_system(iterations, axiom, rules):
    start = axiom
    if iterations == 0:
        return axiom
    end = ""
    for _ in range(iterations):
        end = "".join(rules[i] if i in rules else i for i in start)
        start = end
    return end

def pick_color():
    colors = ["blue","brown","red","yellow","green","orange","beige","turquoise","pink"]
    random.shuffle(colors)
    return colors[0]

def draw(turtle, rules, angle, step):
    count = 0;
    for command in rules:
        if command == 'F':
            turtle.forward(step)
            count += 1
        elif command == '+':
            turtle.right(angle)
        elif command == '-':
            turtle.left(angle)
        if count % 100 == 0:
            random_color = pick_color()
            turtle.color(random_color)

def generate(n, axiom, rules, angle, step):
    t = turtle.Turtle()
    t.shape("turtle")
    t.shapesize(1, 1)
    t.width(2)
    t.speed(0)
    random_color = pick_color()
    t.color(random_color)

    screen = turtle.Screen()
    screen.setup(700, 700)
    screen.bgcolor("gray")

    start_time = time.time()
    system = create_system(n, axiom, rules)
    draw(t, system, angle, step)
    end_time = time.time() - start_time

    print(end_time)

    t.hideturtle()
    turtle.done()

#Входные данные для ковра Серпинского
A1 = "YF"
R1 = {"X":"YF+XF+Y", "Y":"XF-YF-X"}
AN1 = 60

#Входные данные для кривой Серпинского
A2 = "F+XF+F+XF"
R2 = {"X":"XF-F+F-XF+F+XF-F+F-X"}
AN2 = 90

#Входные данные для кривой дракона
A3 = "FX"
R3 = {"X":"X+YF+", "Y":"-FX-Y"}
AN3 = 90

#Входные данные для двойной кривой дракона
A4 = "FX+FX"
R4 = {"X":"X+YF+", "Y":"-FX-Y"}
AN4 = 90

#Входные данные для тройной кривой дракона
A5 = "FX+FX+FX"
R5 = {"X":"X+YF+", "Y":"-FX-Y"}
AN5 = 90

N = 10

generate(N, A5, R5, AN5, 10)




