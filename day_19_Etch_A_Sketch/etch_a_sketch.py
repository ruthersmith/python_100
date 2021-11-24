"""
    Interactive program that stimulate the Etch A Sketch toy
    which was a mechanical drawing toy invented by André Cassagnes of France, read more at: https://en.wikipedia.org/wiki/Etch_A_Sketch
    
    This is a fully interactive program where the user can
    -> use the arrow keys to move the drawing pen arround the screen
    -> use the 'c' key to clear the screen
    -> use the 'u' and 'd' keys representing 'pen up' and 'pen down' respectively to determine wether movement arround the screen
       will draw (when in pen down mode) or will just move the pens location (when in pen down mode)
       starting position is pen down
     
"""

from turtle import Turtle, Screen


class EtchASketch:

    MOVE_FORWARD_KEY = "Up"
    MOVE_BACKWARD_KEY = "Down"
    ROTATE_CLOCKWISE_KEY = "Right"
    ROTATE_COUNTER_CLOCKWISE_KEY = "Left"

    CLEAR_SCREEN_KEY = "c"

    PEN_UP_KEY = "u"
    PEN_DOWN_KEY = "d"

    MOVEMENT_SPEED = 10
    ROTATION_SPEED = 10

    def __init__(self):
        self.tim = Turtle()
        # Screen object controls the window when we run our code
        self.screen = Screen()

    def move_forwards(self):
        self.tim.forward(EtchASketch.MOVEMENT_SPEED)

    def move_backwards(self):
        self.tim.backward(EtchASketch.MOVEMENT_SPEED)

    def rotate_clockwise(self):
        self.tim.right(EtchASketch.ROTATION_SPEED)

    def rotate_counter_clockwise(self):
        self.tim.left(EtchASketch.ROTATION_SPEED)

    def pen_up(self):
        self.tim.penup()

    def pen_down(self):
        self.tim.pendown()

    def clear_screen(self):
        self.tim.clear()
        self.tim.reset()

    def run(self):
        # exist to allow us to start listening for events
        self.screen.listen()
        # movement/drawing listeners
        self.screen.onkeypress(fun=self.move_forwards, key=EtchASketch.MOVE_FORWARD_KEY)
        self.screen.onkeypress(fun=self.move_backwards, key=EtchASketch.MOVE_BACKWARD_KEY)
        self.screen.onkeypress(fun=self.rotate_clockwise, key=EtchASketch.ROTATE_CLOCKWISE_KEY)
        self.screen.onkeypress(fun=self.rotate_counter_clockwise, key=EtchASketch.ROTATE_COUNTER_CLOCKWISE_KEY)
        # clear the screen listener
        self.screen.onkey(fun=self.clear_screen, key=EtchASketch.CLEAR_SCREEN_KEY)
        # pen control listeners
        self.screen.onkey(fun=self.pen_up,key=EtchASketch.PEN_UP_KEY)
        self.screen.onkey(fun=self.pen_down,key=EtchASketch.PEN_DOWN_KEY)
        # Shut the turtle graphics window when mouse clicks on the Screen
        self.screen.exitonclick()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sketch_pad = EtchASketch()
    sketch_pad.run()
