class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.name = "Rectangle"

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * (self.width + self.height)

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      metin = ""

      for i in range(self.height):
        metin += "*" * self.width + "\n"
      return metin

  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width, self.height)

  def get_amount_inside(self, obj):
    a = self.width // obj.width
    b = self.height // obj.height
    return a * b


class Square(Rectangle):

  def __init__(self, side):
    self.width = side
    self.height = side
    self.name = "Square"

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return "Square(side={})".format(self.width)
