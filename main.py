import os
os.system('cls')


class Square:
    def __init__(self, ancho, alto):
        self.__height = ancho
        self.__width = alto

    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side

    def isSquare(self):
        if self.__height == self.__width:
            return True
        else:
            return False
    
    @property    
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_value):
        if new_value >= 0:
            self.__height = new_value
        else:
            raise Exception("value needs to be 0 or larger")

square = Square(2, 2)
square.height = 2
square.set_side(3)
print(square.isSquare())
print(square.height)