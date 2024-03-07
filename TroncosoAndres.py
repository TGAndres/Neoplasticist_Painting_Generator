import turtle
import random

t = turtle.Turtle()
t.speed(100) 

def dibujar_linea():
    ancho=random.randint(10,40)
    o=random.randint(0,1)
    angulo=random.randint(0,180)
    if o==0:
        inicio=random.randint(-480,480)
        t.penup()
        t.goto(inicio,-400)
        t.pendown()
        t.forward(ancho)
        t.left(angulo)
        t.forward(1800)
        t.left(180-angulo)
        t.forward(ancho)
        t.left(angulo)
        t.forward(1800)
        t.left(180-angulo)
    else:
        inicio=random.randint(-400,400)
        t.penup()
        t.goto(-480,inicio)
        t.pendown() 
        t.right(90)
        t.forward(ancho)
        t.left(angulo)
        t.forward(1800)
        t.left(180-angulo)
        t.forward(ancho)
        t.left(angulo)
        t.forward(1800)
        t.left(180-angulo)
        t.left(90)


def dibujar_rectangulo():
    ancho=random.randint(10,700)
    alto=random.randint(10,750-ancho)
    for _ in range(2):
        t.forward(ancho)
        t.left(90)
        t.forward(alto)
        t.left(90)

def dibujar_circulo():
    t.circle(random.randint(10,150))

def dibujar_triangulo():
    angulo=random.randint(0,180)
    t.left(angulo)
    lado=random.randint(10,300)
    for _ in range(3):
        t.forward(lado)
        t.left(120)
    t.right(angulo)

colores_neo = ["yellow", "blue", "red", "black","white"]
colores_cmyk = ["yellow", "cyan", "magenta", "black","white"]
colores_rgb = ["red","green","blue","black","white"]
for i in range(80):
    t.penup()
    t.goto(random.randint(-600,480), random.randint(-500,400))
    t.pendown()
    t.begin_fill()
    o = random.randint(0,3)
    color= random.choice(colores_neo) #neo, cmyk o rgb
    t.color(color)
    t.fillcolor(color)  
    if o==0:
        #o = random.randint(1,3)
        dibujar_rectangulo()
    elif o==1:
        #o = random.randint(1,3)
        dibujar_circulo()
    elif o==2:
        #o = random.randint(1,3)
        dibujar_triangulo()
    else:
        #o = random.randint(1,3)
        dibujar_linea()
    t.end_fill()


turtle.done()