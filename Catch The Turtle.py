import random
import turtle

ekran = turtle.Screen()
ekran.title("Catch Me İf You Can")
ekran.bgcolor("light blue")


puan = 0
kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("green")
kaplumbaga.shapesize(3,3)


def go_to():
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
    ekran.ontimer(go_to, 500)

def yazdir():
    turtle.clear()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 260)
    turtle.write("Puan: {}".format(puan), align="center", font=("Arial", 16, "normal"))
def game_over():
    turtle.clear()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 0)
    turtle.write("Game Over", align="center", font=("Arial", 24, "normal"))
    turtle.ontimer(lambda:kapat(),3000)
    turtle.goto(0, 50)
    turtle.write("Puan: {}".format(puan), align="center", font=("Arial", 16, "normal"))

def kapat():
    turtle.bye()
go_to()

oyun_suresi = 20
baslangic_zamani = ekran.ontimer(lambda: game_over(), oyun_suresi * 1000)


turtle.mainloop()
