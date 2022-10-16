import constants
from game.casting.actor import Actor
from game.shared.point import Point

#Child of Actor Class, makes an controls a cycle object
class Cycle(Actor):

    def __init__(self, color, x, y):
        super().__init__()
        self._segments = []
        self._color = color
        self._position_x = x
        self._position_y = y
        self._prepare_body()

    #Checks segments
    def get_segments(self):
        return self._segments

    #Moves the cycle forward
    def move_next(self):
        for segment in self._segments:
            segment.move_next()
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    #Checks the first segment
    def get_head(self):
        return self._segments[0]

    #Adds to the length
    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("*")
            segment.set_color(self._color)
            self._segments.append(segment)
            
    #Changes direction of movement
    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    #Specifies how the cycle should be drawn
    def _prepare_body(self):
        x = self._position_x
        y = self._position_y

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "*"
            color = self._color
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)