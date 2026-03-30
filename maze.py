import turtle
pen=turtle.Turtle()
screen=turtle.Screen()
list=["xxxxxxxxxxxxxxx",
      "xxx xxx      xx",
      "xxx     xxxx xx",
      "xxx    xxxxxxxx",
      "xxxx xxxxxxxxxx",
      "xxxx  xxxxxxxxx",
      "xxxxx xxxxxxxxx",
      "xxxxx xxxxxxxxx",
      "xxx     xxxxxxx",
      "xxx   x  xxxxxx"]
for y in range(len(list)):
    for x in range(len(list[y])):
        tileX=-288+(x*24)
        tileY=288-(y*24)
        charecter=list[y][x]
        if charecter=="x":
            tile=turtle.Turtle()
            tile.shape("square")
            tile.up()
            tile.speed(0)
            tile.goto(tileX,tileY)
def right():
    x=pen.xcor()
    x+=24
    y=pen.ycor()
    pen.goto(x,y)
screen.listen()
screen.onkey(right,"Right")
turtle.done()