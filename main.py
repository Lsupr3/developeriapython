import os
os.system('cls')


class Square:
    def __init__(self, ancho, alto):
        self.__height = alto
        self.__width = ancho

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

try:
    square = Square(2,2)
    square.height = 3
    print(square.isSquare())
    print(square.height)
except Exception as err:
    print(err)