import turtle

x=-200
y=-200
i=1
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
while i<6:
    j=1
    while j<6:
        k=1
        while k<5:
            turtle.forward(100)
            turtle.left(90)
            k+=1
        x+=100
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        j+=1
    x=-200
    y+=100
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    i+=1
        
turtle.exitonclick()
