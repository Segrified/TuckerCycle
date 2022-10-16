from game.scripting.action import Action

#Draws everything on the screen
class DrawActorsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    #Gets what it needs, then draws them
    def execute(self, cast, script):
        cycle = cast.get_first_actor("cycles")
        cycle2 = cast.get_second_actor("cycles")
        segments = cycle.get_segments()
        segments2 = cycle2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()