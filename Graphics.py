import turtle

# Set up the turtle
square_size = 50
SIZE = 200

# Function to draw a single square
def draw_square(size,grid_turtle):
    for _ in range(4):
        grid_turtle.forward(size)
        grid_turtle.right(90)

def on_square_click(x,y):
    print("Square clicked!")

# Function to draw the entire grid
def draw_grid(size, rows, columns,grid_turtle):
    counter = 0
    for _ in range(rows):
        counter += 1
        for _ in range(columns):
            if counter % 2 == 0:
                paint_square_black(square_size,"#7b3c00",grid_turtle)  #Color cafe
            else: paint_square_black(square_size,"#Ecc640",grid_turtle) #Color beige
            counter += 1
            grid_turtle.forward(size)

        grid_turtle.backward(size * columns)
        grid_turtle.right(90)
        grid_turtle.forward(size)
        grid_turtle.left(90)

def draw_circle_in_square(row, column, size,color,grid_turtle):
    x = -SIZE + (size * column) + (size / 2)  # Calculate the center of the square
    y = SIZE - (size * row) - (size / 2)
    radius = 23
    grid_turtle.begin_fill()
    grid_turtle.fillcolor(color)
    grid_turtle.penup()
    grid_turtle.goto(x, y - radius)
    grid_turtle.circle(radius)
    grid_turtle.end_fill()

def paint_square_black(size,color,grid_turtle):
    grid_turtle.begin_fill()
    grid_turtle.fillcolor(color)
    draw_square(size,grid_turtle)
    turtle.onscreenclick(on_square_click)
    grid_turtle.end_fill()

def drawBoard(Pieces:list):
    # Set the initial position of the turtle
    grid_turtle = turtle.Turtle()
    grid_turtle.speed(0)  # Set the drawing speed to the fastest
    turtle.tracer(False)
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title("Checkers")

    grid_turtle.penup()
    grid_turtle.goto(-SIZE, SIZE)
    grid_turtle.pendown()
    # Draw the grid

    draw_grid(square_size, 8, 8, grid_turtle)
    drawPieces(Pieces,grid_turtle)
    # Hide the turtle and display the result
    grid_turtle.hideturtle()
    screen.mainloop()
    
def calc(Pieces: list):
    for i in range(64,1):
        NewPiece = True
        for piece in Pieces:
            if i == piece[0]: 
                NewPiece =False
                break
        if NewPiece:  Pieces.append([i,0,False])

    # for sublist in Pieces:
    #     sublist[0] *= 2
    Pieces.sort(key=lambda x: x[0])

def drawPieces(Pieces: list,grid_turtle):
    calc(Pieces)
    counter = 0
    for Piece in Pieces:
        if Piece[0] > 1: Piece[0] = Piece[0] * 2 -1
        row = Piece[0] // 8  # Calculate row index
        column = Piece[0] % 8 # Calculate column index
        if row % 2 !=0 : column-=1
        if Piece[1] ==1 : 
            if Piece[2] : color = "Red"  # King
            else: color = "Black"
        else : 
            if Piece[2] : color = "Blue"  # King
            else: color = "White"
        draw_circle_in_square(row, column, square_size, color,grid_turtle)

