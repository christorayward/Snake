# -*- coding: utf-8 -*-

import turtle
from turtle import Turtle, Screen
import time
import random

posponer = 0.1
bandera_direccion = "stop"
#Marcador
score = 0
high_score = 0


#Setup Ventana
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

#Cabeza Snake
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup() #Quitar Rastro
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("orange")
comida.penup() #Quitar Rastro
comida.goto(0,100)

#Segmentos / Cuerpo Serpiente
Segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: {}	High Score: {}".format(score, high_score),
			align = "center", font = ("Courier", 20, "normal"))


#Funciones
def arriba():
	cabeza.direction = "up"
def abajo():
	cabeza.direction = "down"
def izquierda():
	cabeza.direction = "left"
def derecha():
	cabeza.direction = "right"

def mov():

    if cabeza.direction == "up":
    	texto.clear()
    	texto.write("Score: {}	High Score: {}".format(score, high_score),
			align = "center", font = ("Courier", 20, "normal"))
    	global 	bandera_direccion
    	if bandera_direccion != "up":
	        y = cabeza.ycor()
	        cabeza.sety(y + 20)
	        texto.clear()
	        bandera_direccion = "down"
    	else:
	        y = cabeza.ycor()
	        cabeza.sety(y - 20)
	        bandera_direccion = "up"

    if cabeza.direction == "down":
    	texto.clear()
    	texto.write("Score: {}	High Score: {}".format(score, high_score),
			align = "center", font = ("Courier", 20, "normal"))
    	if bandera_direccion != "down":
	        y = cabeza.ycor()
	        cabeza.sety(y - 20)
	        bandera_direccion = "up"
    	else:
	        y = cabeza.ycor()
	        cabeza.sety(y + 20)
	        texto.clear()
	        bandera_direccion = "down"

    if cabeza.direction == "left":
    	texto.clear()
    	texto.write("Score: {}	High Score: {}".format(score, high_score),
			align = "center", font = ("Courier", 20, "normal"))
    	if bandera_direccion != "left":
	        x = cabeza.xcor()
	        cabeza.setx(x - 20)
	        texto.clear()
	        bandera_direccion = "right"
    	else:
	        x = cabeza.xcor()
	        cabeza.setx(x + 20)
	        texto.clear()
	        bandera_direccion = "left"

    if cabeza.direction == "right":
    	texto.clear()
    	texto.write("Score: {}	High Score: {}".format(score, high_score),
			align = "center", font = ("Courier", 20, "normal"))
    	if bandera_direccion != "right":
	        x = cabeza.xcor()
	        cabeza.setx(x + 20)
	        texto.clear()
	        bandera_direccion = "left"
    	else:
	        x = cabeza.xcor()
	        cabeza.setx(x - 20)
	        texto.clear()
	        bandera_direccion = "right"



#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")


while(True):
	wn.update()

	#Colisiones bordes
	if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
		time.sleep(1)
		cabeza.goto(0,0)
		cabeza.direction = "stop"
		bandera_direccion = "stop"
		
		#Esconder los segmentos
		for segmento in Segmentos:
			segmento.goto(1000,1000)
			
		#Limpiar lista de segmentos
		Segmentos.clear()

		#Resetear marcador
		score = 0
		texto.clear()
		texto.write("Score: {}	High Score: {}".format(score, high_score),
			align = "center", font = ("Courier", 20, "normal"))



	#Colisiones comida
	if cabeza.distance(comida) < 20:
		x = random.randint(-14,14)*20
		y = random.randint(-14,12)*20
		comida.goto(x,y)

		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("square")
		nuevo_segmento.color("grey")
		nuevo_segmento.penup() #Quitar Rastro
		nuevo_segmento.direction = "stop"
		Segmentos.append(nuevo_segmento)

		#Aumentar marcador
		score += 10

		if score > high_score:
			high_score = score
		texto.clear()
		texto.write("Score: {}	High Score: {}".format(score, high_score),
			align = "center", font = ("Courier", 20, "normal"))

	#Mover el cuerpo de la serpiente
	totalSeg = len(Segmentos)
	for index in range(totalSeg -1, 0, -1):
		x = Segmentos[index - 1].xcor()
		y = Segmentos[index - 1].ycor()
		Segmentos[index].goto(x,y)

	if totalSeg > 0:
		x = cabeza.xcor()
		y = cabeza.ycor()
		Segmentos[0].goto(x,y)

	mov()

	#Colisiones con el cuerpo
	for segmento in Segmentos:
		if segmento.distance(cabeza) < 20:
			time.sleep(1)
			cabeza.goto(0,0)
			cabeza.direction = "stop"
		
			#Esconder los segmentos
			for segmento in Segmentos:
				segmento.goto(1000,1000)
			
			#Limpiar lista de segmentos
			Segmentos.clear()

			#Resetear marcador
			score = 0
			texto.clear()
			texto.write("Score: {}	High Score: {}".format(score, high_score),
				align = "center", font = ("Courier", 20, "normal"))


	time.sleep(posponer)