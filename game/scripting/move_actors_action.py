from game.scripting.action import Action
class MoveActorsAction(Action):

     #Handles cycle movement
     def execute(self, cast, script):
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()



