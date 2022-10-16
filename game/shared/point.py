#Holds the X and Y values of an object
class Point:
    
    def __init__(self, x, y):
        self._x = x
        self._y = y

    #Adds two points
    def add(self, other):
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    #Checks if two points are equal
    def equals(self, other):
        return self._x == other.get_x() and self._y == other.get_y()

    #Checks X value
    def get_x(self):
        return self._x

    #Checks Y value
    def get_y(self):
        return self._y

    #Inverts the X and Y values
    def reverse(self):
        new_x = self._x * -1
        new_y = self._y * -1
        return Point(new_x, new_y)

    #Multiplies point values by a factor
    def scale(self, factor):
        return Point(self._x * factor, self._y * factor)