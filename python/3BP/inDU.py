#! /usr/bin/python3

# input functions

def inputDeck():

    # initial values

    rx = [1, -3, 2]
    ry = [-1, 0, 1.7]

    vx = [2.1, 0.3, -0.5]
    vy = [2.5, 0.3, -3.5]

    m = [1, 2, 3]    
 
    return  rx, ry, vx, vy, m

def inputUser():

    # user input

    rx = []
    ry = []

    rx.append(float(input("Enter initial x1: ")))
    ry.append(float(input("Enter initial y1: ")))
    rx.append(float(input("Enter initial x2: ")))
    ry.append(float(input("Enter initial y2: ")))
    rx.append(float(input("Enter initial x3: ")))
    ry.append(float(input("Enter initial y3: ")))

    vx = []
    vy = []

    vx.append(float(input("Enter initial v_x1: ")))
    vy.append(float(input("Enter initial v_y1: ")))
    vx.append(float(input("Enter initial v_x2: ")))
    vy.append(float(input("Enter initial v_y2: ")))
    vx.append(float(input("Enter initial v_x3: ")))
    vy.append(float(input("Enter initial v_y3: ")))
 
    m = []
   
    m.append(abs(float(input("Enter mass 1: "))))
    m.append(abs(float(input("Enter mass 2: "))))
    m.append(abs(float(input("Enter mass 3: "))))

    return  rx, ry, vx, vy, m





