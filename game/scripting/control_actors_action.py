import constants
from game.scripting.action import Action
from game.shared.point import Point

#Class for controlling the cycles
class ControlActorsAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._direction2 = Point(constants.CELL_SIZE, 0)

    #Controls the cycles based on input
    def execute(self, cast, script):

        #Cycle 1 left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        #Cycle 1 right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        #Cycle 1 up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        #Cycle 1 down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        #Switches Cycles
        cycle = cast.get_first_actor("cycles")
        cycle.turn_head(self._direction)

        #Cycle 2 left
        if self._keyboard_service.is_key_down('j'):
            self._direction2 = Point(-constants.CELL_SIZE, 0)
        
        #Cycle 2 right
        if self._keyboard_service.is_key_down('l'):
            self._direction2 = Point(constants.CELL_SIZE, 0)
        
        #Cycle 2 up
        if self._keyboard_service.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE)
        
        #Cycle 2 down
        if self._keyboard_service.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE)

        #Switches Cycles
        cycle2 = cast.get_second_actor("cycles")
        cycle2.turn_head(self._direction2)