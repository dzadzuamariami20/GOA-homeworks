from turtle import *


#we want to paint a house

#step 1: draw a square
shape() #turtle or arrow or  square or triangle or circle
speed(30)
width(7) # კალამს მისცემს სისქეს 7 პიქსელით
color("purple") # ფერი შევარჩიეთ
forward(200) # რამდენი პიქსელით წავიდეს წინ, ჩვენ შემთხვევაში უნდა წავიდეს 200 პიქსელით - პარამეტრის მნიშვნელობა.
left(90) # რამდენი გრადუსით მოუხვიოს 
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
# end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) # height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of the door

#drawing a roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of the roof

#drawing the left window

penup()

color("brown")
begin_fill()
left(75)
forward(35)
left(45)
pendown()
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
end_fill()

# end of the left window

#drawing the right window
penup()
goto(200, 200)
color("blue")
begin_fill()
left(135)
forward(35)
right(45)
pendown()
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
end_fill()

#end of the right window



exitonclick()

# დავალება: ფანჯრები დავუხატოთ ან ყავისფერი ან ლურჯი, ფანჯრები უნდა ამოვავსოთ და კარიც