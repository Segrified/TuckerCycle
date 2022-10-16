#Keeps a list of actor objects. Can add, check, and remove, what's in it 
class Cast:

    def __init__(self):
        self._actors = {}
        
    #Adds an actor
    def add_actor(self, group, actor):
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    #Checks specific actors
    def get_actors(self, group):
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    #Checks all actors
    def get_all_actors(self):
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    #Checks first actor
    def get_first_actor(self, group):
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result

    #Checks second actor
    def get_second_actor(self, group):
        result = None
        if group in self._actors.keys():
            result = self._actors[group][1]
        return result

    #Removes an actor
    def remove_actor(self, group, actor):
        if group in self._actors:
            self._actors[group].remove(actor)