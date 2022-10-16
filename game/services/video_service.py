import pyray
import constants

#Creates a window and displays the game
class VideoService:

    def __init__(self, debug = False):
        self._debug = debug

    #Closes the window
    def close_window(self):
        pyray.close_window()

    #Clears the buffer
    def clear_buffer(self):
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    #Draws one actor on the screen
    def draw_actor(self, actor, centered=False):
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset
            
        pyray.draw_text(text, x, y, font_size, color)
        
    #Draws all actors from a list on the screen
    def draw_actors(self, actors, centered=False):
        for actor in actors:
            self.draw_actor(actor, centered)
    
    #Copies the buffer to the screen
    def flush_buffer(self):
        pyray.end_drawing()

    #Checks if window is open
    def is_window_open(self):
        return not pyray.window_should_close()

    #Opens a window
    def open_window(self):
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)

    #Draws a grid
    def _draw_grid(self):
        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.GRAY)
            
        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GRAY)
    
    #Gets the X offset
    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)