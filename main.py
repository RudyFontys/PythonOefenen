def main():
    # Create a circle with radius
    circle1 = Circle(1)
    area1 = circle1.getArea()
    print("The area of the circle of radius",
    circle1.radius , "is", area1)

    # Create a circle with radius 5
    circle2 = Circle(5)
    area2 = circle2.getArea()
    print("The area of the circle of radius",
    circle2.radius, "is", area2)

    # Create a circle with radius 100
    circle3 = Circle(100)
    area3 = circle3.getArea()
    print("The area of the circle of radius",
    circle3.radius, "is", area3)

    # Modify circle radius
    circle2.setRadius(10)

    new_radius2 = circle2.getArea()
    print("The area of the circle of radius",
    circle2.radius, "is", new_radius2)

main()