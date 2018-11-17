# -*- coding: utf-8 -*-


"""planets.py:
__author__="wengpeiyi"
__pkuid__="1800011749"
__email__="594592395@qq.com"
"""

import math     
import turtle
Ear=turtle.Turtle()
Mer=turtle.Turtle()
Ven=turtle.Turtle()
Mar=turtle.Turtle()
Jup=turtle.Turtle()
Sat=turtle.Turtle()
turtle.delay(0.8)
Ear.pensize(3)
Mer.pensize(3)
Ven.pensize(3)
Mar.pensize(3)
Jup.pensize(3)
Sat.pensize(3)
wn=turtle.Screen()
wn.bgcolor("black")
Ear.shape("circle")
Ear.shapesize(0.5,0.5)

Mer.pencolor("blue")
Mer.shape("circle")
Mer.shapesize(0.2,0.2)
Mer.up()
Mer.goto(16,0)
Mer.down()

Ven.pencolor("gold")
Ven.shape("circle")
Ven.up()
Ven.goto(50,0)
Ven.shapesize(0.3,0.3)
Ven.down()

Mar.pencolor("#FF5000")
Mar.shape("circle")
Mar.up()
Mar.goto(162,0)
Mar.shapesize(0.6,0.6)
Mar.down()

Jup.pencolor("goldenrod3")
Jup.shape("circle")
Jup.shapesize(0.8,0.8)
Jup.up()
Jup.goto(200,0)
Jup.down()

Sat.pencolor("SaddleBrown")
Sat.shape("circle")
Sat.shapesize(0.9,0.9)
Sat.up()
Sat.goto(360,0)
Sat.down()

Ear.goto(0,0)
Ear.ht()
Ear.dot(20,"#FF5A00")
Ear.up()
Ear.goto(70,0)
Ear.down()
Ear.st()
Ear.pencolor("snow4")


for i in range(14400):
    sint=math.sin(math.radians(2*i))
    cost=math.cos(math.radians(2*i))
    sinm=math.sin(math.radians(8.8*i))
    cosm=math.cos(math.radians(8.8*i))
    sinM=math.sin(math.radians(i))
    cosM=math.cos(math.radians(i))
    sinv=math.sin(math.radians(3.5*i))
    cosv=math.cos(math.radians(3.5*i))
    sinj=math.sin(math.radians(0.7*i))
    cosj=math.cos(math.radians(0.7*i))
    sins=math.sin(math.radians(0.3*i))
    coss=math.cos(math.radians(0.3*i))
    Ear.goto(100*cost-30,95*sint)
    Mer.goto(26*cosm-10,24*sinm)
    Ven.goto(61*cosv-11,60*sinv)
    Mar.goto(181*cosM-19,180*sinM)
    Jup.goto(250*cosj-50,245*sinj)
    Sat.goto(400*coss-40,398*sins)

def f(par1, par2):
    pass

def main():
    f(1, 2)

if __name__ == '__main__':
    main()    