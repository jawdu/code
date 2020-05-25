#! /usr/bin/python3



def inputDeck():

    # initial values

    x1 = 1
    y1 = -1
    x2 = -3
    y2 = 0
    x3 = 2
    y3 = 2

    vx1 = 2.1
    vy1 = 2.5
    vx2 = 0.3
    vy2 = 1.3
    vx3 = -0.5
    vy3 = -3.5

    m1 = 1
    m2 = 2
    m3 = 3

    return  x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3, m1, m2, m3

def inputUser():

    # user input

    x1 = float(input("Enter initial x1: "))
    y1 = float(input("Enter initial y1: "))
    x2 = float(input("Enter initial x2: "))
    y2 = float(input("Enter initial y2: "))
    x3 = float(input("Enter initial x3: "))
    y3 = float(input("Enter initial y3: "))

    vx1 = float(input("Enter initial v_x1: "))
    vy1 = float(input("Enter initial v_y1: "))
    vx2 = float(input("Enter initial v_x2: "))
    vy2 = float(input("Enter initial v_y2: "))
    vx3 = float(input("Enter initial v_x3: "))
    vy3 = float(input("Enter initial v_y3: "))
    
    m1 = abs(float(input("Enter mass 1: ")))
    m2 = abs(float(input("Enter mass 2: ")))
    m3 = abs(float(input("Enter mass 3: ")))

    return  x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3, m1, m2, m3





