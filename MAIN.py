import turtle

screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('lightsteelblue')

t_ground = turtle.Turtle()
t_ground.penup()
t_ground.speed(0)
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.fillcolor('white')
t_ground.pencolor('white')
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)

def draw_circle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(radius)
    t.end_fill()

def draw_rectangle(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_snowman():
    t = turtle.Turtle()
    t.speed(0)
    t.pencolor("white")
    draw_circle(t, -200, -250, 100, "white")
    draw_circle(t, -200, -100, 75, "white")
    draw_circle(t, -200, 25, 50, "white")
    t.pencolor("black")
    draw_circle(t, -215, 45, 5, "black")
    draw_circle(t, -185, 45, 5, "black")
    draw_rectangle(t, -230, 75, 60, 10, "black")
    draw_rectangle(t, -215, 85, 30, 40, "black")
    t.hideturtle()
    t.penup()
    t.goto(-170, 15)
    t.pendown()
    t.pencolor("orange")
    t.setheading(0)
    t.begin_fill()
    t.fillcolor("orange")
    t.forward(30)
    t.left(150)
    t.forward(25)
    t.left(120)
    t.forward(15)
    t.left(120)
    t.end_fill()
    t.pencolor("black")
    draw_circle(t, -200, -50, 5, "black")
    draw_circle(t, -200, -75, 5, "black")
    draw_circle(t, -200, -100, 5, "black")
    t.hideturtle()

def draw_tree():
    t = turtle.Turtle()
    t.speed(0)
    t.pencolor("brown")
    draw_rectangle(t, 125, -250, 50, 100, "brown")
    t.pencolor("green")
    y_start = -150
    width = 200
    for i in range(3):
        draw_triangle(t, 150, y_start, width, "green")
        y_start += 50
        width -= 40
    t.pencolor("yellow")
    draw_star(t, 150, y_start + 60, 30, "yellow")
    t.hideturtle()


def draw_triangle(t, x, y, base, color):
    t.penup()
    t.goto(x - base // 2, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(3):
        t.forward(base)
        t.left(120)
    t.end_fill()
    t.hideturtle()
def draw_star(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.setheading(-72)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
def draw_presents():
    t = turtle.Turtle()
    t.speed(0)
    t.pencolor("red")
    draw_rectangle(t, -50, -250, 50, 50, "red")
    t.pencolor("gold")
    draw_rectangle(t, -30, -250, 10, 50, "gold")
    draw_rectangle(t, -50, -230, 50, 10, "gold")
    t.pencolor("blue")
    draw_rectangle(t, 250, -250, 70, 50, "blue")
    t.pencolor("silver")
    draw_rectangle(t, 280, -250, 10, 50, "silver")
    draw_rectangle(t, 250, -230, 70, 10, "silver")
    t.hideturtle()
def add_text():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 300)
    t.pencolor("red")
    t.write("Merry Christmas!", align="center", font=("Verdana", 24, "bold"))

def main():
    setup_screen()
    draw_snowman()
    draw_tree()
    draw_presents()
    add_text()
    turtle.done()

if __name__ == "__main__":
    main()
