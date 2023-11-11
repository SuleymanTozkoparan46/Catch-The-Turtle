import random
import turtle

ekran = turtle.Screen()
ekran.title("Catch Me İf You Can")
ekran.bgcolor("light blue")

gmover = False

puan = 0
kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("green")
kaplumbaga.shapesize(3,3)


def go_to():
    if not gmover:
        kaplumbaga.penup()
        kaplumbaga.speed(0)
        kaplumbaga.goto(random.randrange(-200, 201,200), random.randrange(-200, 201,200))
        kaplumbaga.showturtle()
        kaplumbaga.onclick(tıklama_olayı)
        ekran.ontimer(gizle)
def tıklama_olayı(x, y):
    global puan
    puan += 1
    yazdir()
    return puan

def gizle():
    ekran.ontimer(go_to, 600)

def yazdir():
    turtle.clear()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 260)
    turtle.write("Score: {}".format(puan), align="center", font=("Arial", 16, "normal"))
def game_over():
    global gmover
    gmover = True
    turtle.clear()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 0)
    turtle.write("Game Over", align="center", font=("Arial", 24, "normal"))
    turtle.ontimer(lambda:kapat(),5000)
    turtle.goto(0, 50)
    turtle.write("Puan: {}".format(puan), align="center", font=("Arial", 16, "normal"))
    kaplumbaga.hideturtle()


countdown_turtle = turtle.Turtle()
def timer(time):
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.goto(0,235)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write("Time: {}".format(time), align="center", font=("Arial", 16, "normal"))
        ekran.ontimer(lambda :timer(time - 1),1000)

timer(10)
def kapat():
    turtle.bye()
go_to()

Sure = 10
baslangic_zamani = ekran.ontimer(lambda: game_over(), Sure * 1000)


turtle.mainloop()
