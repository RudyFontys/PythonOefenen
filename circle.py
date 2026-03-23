import math

class Circle:
        # Construct a circle object
        def __init__(self, radius): # initializer
                self.radius = radius    # property or attribute

        def setRadius(self, radius):
                self.radius = radius

        def getArea(self):
                return self.radius * self.radius * math.pi

        def getPerimeter(self):
                return 2 * self.radius * math.pi