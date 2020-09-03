import turtle as jerry
from random import randint

class jerryDraw:
  """ A object that jerry will draw"""
  def __init__(self,x,y,width):
    self._x = x
    self._y = y
    self._width = width
  def jerrySize(self):
    """Change pen size"""
    jerry.pensize(self._width)
  def jerryPickColor(self):
    """ Randomly pick a color for jerry"""
    jerry.colormode(255)
    jerry.pencolor((randint(0,256),randint(0,256),randint(0,256)))
  def jerryMove(self):
    """ Lift the jerry and change position then put jerry back down """
    jerry.up()
    jerry.setpos(self._x,self._y)
    jerry.down()
  def jerryGoHome(self):
    """ Lift the jerry and Reset position then put jerry back down """
    jerry.up()
    jerry.home()
    jerry.down()

class Rainbow(jerryDraw):
  """A Rainbow class that can draw rainbow"""
  def __init__(self,x,y,width):
    super().__init__(x,y,width)
  def jerryMove(self,x):
    """ Lift the jerry and change position then put jerry back down """
    jerry.up()
    jerry.setpos(x,self._y)
    jerry.down()
  def semi_circle(self,r,x):
    """ A method that draws one semi circle at a time"""
    self.jerryPickColor()
    jerry.circle(r,-180)
    self.jerryMove(x)
    jerry.right(180)
  def draw(self):
    """ A method draws rainbow (7 semi-circles)"""
    jerry.right(90)
    #jerry.speed(10)
    self.jerrySize()
    self.jerryMove(self._x)
    for i in range(7):
      self.semi_circle(self._width*(i+8),-self._width*(i+1)+self._x)
    self.jerryGoHome()

class Flower(jerryDraw):
  """ A flower class that can draw flower"""
  def __init__(self,num_petals,petal_length,width,x,y):
    """ Initialize the setting to draw a flower """
    super().__init__(x,y,width)
    self._num_petals = num_petals
    self._petal_length = petal_length

  def _get_turn_degrees(self,num_petals):
    """return how many degrees the turtle will need to turn to draw the next petal"""
    degree = 360/num_petals
    assert degree > 0, "Degree Shouldn't be negative"
    return degree
  def draw(self):
    """This function draws a flower using turtle graphics"""
    turn_degrees = self._get_turn_degrees(self._num_petals)
    self.jerryMove()
    self.jerryPickColor()
    self.jerrySize()
    for _ in range(self._num_petals):
      jerry.forward(self._petal_length)
      jerry.backward(self._petal_length)
      jerry.right(turn_degrees)
    #draw center
    jerry.pencolor("orange")
    jerry.dot(50)
    jerry.pensize(1)
                    

r2 = Rainbow(-245,-100,30)
r2.draw()
f2 = Flower(8,100,40,-230,-200)
f2.draw()
r1 = Rainbow(-125,-100,15)
r1.draw()
r3 = Rainbow(-44,-100,5)
r3.draw()
f3 = Flower(10,100,40,-0,-200)
f3.draw()
f1 = Flower(-15,100,40,230,-200)
f1.draw()
jerry.done() 
     