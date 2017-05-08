import turtle
import copy

# -----------------------------------------------------------------------------------------------
        # - GLOBAL VARIABLES
# -----------------------------------------------------------------------------------------------
window = turtle.Screen()
window.bgcolor("#000000")
nemo = turtle.Turtle()
nemo.shape("classic")
nemo.color("green")
nemo.speed(2)
vertex = [nemo.pos(), nemo.pos(), nemo.pos()] #Stores the vertex for the last triangle drawn
# -----------------------------------------------------------------------------------------------
        # - FUNCTION DECLARATIONS
# -----------------------------------------------------------------------------------------------
def draw_triangle(): #This function just draw a triangle
    nemo.fill(True)
    for i in range(0, 3):
        vertex[i] = nemo.pos() #Store the vertex
        nemo.forward(40)
        nemo.right(120)
    nemo.setheading(0) #Reset the position
    nemo.fill(False)

def draw_figure(): #This function has 3 loops, one for each edge
    for i in range(0, 10):
        nemo.left(60)
        if i == 3 or i == 6:
            nemo.setheading(0)
            nemo.goto(vertex[2])
            nemo.left(60)
            temp = copy.deepcopy(vertex)
            draw_triangle()
            nemo.left(120)
            nemo.goto(temp[1])
            nemo.setheading(0)
            vertex[1] = nemo.pos()
        else:
            nemo.goto(vertex[1])
            draw_triangle()
    nemo.goto(vertex[2])
    for i in range(0, 9):
        nemo.right(60)
        if i == 2 or i == 5:
            nemo.right(120)
            nemo.goto(vertex[2])
            temp = copy.deepcopy(vertex)
            nemo.left(120)
            draw_triangle()
            nemo.goto(temp[1])
            vertex[1] = nemo.pos()
        else:
            draw_triangle()
            nemo.right(60)
            nemo.goto(vertex[1])
            nemo.setheading(0)
    nemo.setheading(180)
    nemo.goto(vertex[2])
    nemo.forward(40)
    for i in range(0, 8):
        nemo.right(120)
        if i == 3 or i == 6:
            nemo.goto(vertex[1])
            temp = copy.deepcopy(vertex)
            draw_triangle()
            nemo.right(120)
            nemo.goto(temp[0])
            nemo.right(60)
            nemo.forward(40)
        else:
            draw_triangle()
            nemo.right(180)
            if i != 2 and i != 5:
                nemo.forward(40)


#-------------------------------------------------------------------------------------------------
draw_figure()
window.exitonclick()
