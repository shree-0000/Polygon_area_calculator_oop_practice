class Rectangle:
    def __init__(self, width = 0, height = 0):
        #run check for inputed values
        assert width&height >= 0, f"width {width} or height {height} is less than zero, invalid lenght"

        #initalisation
        self.width = width
        self.height = height
        if width == height:
            self.type = "Square"
        else:
            self.type = "Rectangle"

    def set_width(self, width) -> None:
        self.width = width

    def set_height(self, height) -> None:
        self.height = height

    def get_area(self) -> float:
        return self.width*self.height

    def get_perimeter(self) -> float:
        return 2*(self.width + self.height)

    def get_diagonal(self) -> float:
        return ((self.width**2 + self.height**2)**0.5)

    def get_picture(self) -> str:
        if self.width>50:
            return "Too big for picture"
        else:
            return ("*"*self.width + "\n")*self.height

    def get_amount_inside(self, shape: object) -> int:
        if ((self.width//shape.width)>=0)&((self.height//shape.height)>=0):
            return (self.width//shape.width)*(self.height//shape.height)
        else:
            print(f"The {shape.type} cannot fit inside the other shape")
            return 0

    def __str__(self) -> str:
        return f"Rectangle(width = {self.width}, height = {self.height})"

class Square(Rectangle):
 
    def __init__(self, side=0) -> None:
        super().__init__(side, side)

    def set_side(self, side) -> None:
        self.__init__(side)

    def __str__(self) -> str:
        return f"Square(side = {self.width})"
    