from class_figures import Rectangle, Square, Circle


rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.get_area_rectangle())
print((rect_2.get_area_rectangle()))

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square())
print(square_2.get_area_square())

circle_1 = Circle(5)
circle_2 = Circle(10)

print(circle_1.get_area_circle())
print(circle_2.get_area_circle())

print()

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for item in figures:
    if isinstance(item, Square):
        print(item.get_area_square())
    elif isinstance(item, Rectangle):
        print(item.get_area_rectangle())
    elif isinstance(item, Circle):
        print(item.get_area_circle())
