#Handles the actions
class Script:

    def __init__(self):
        self._actions = {}

    #Adds an action to a group 
    def add_action(self, group, action):
        if not group in self._actions.keys():
            self._actions[group] = []
            
        if not action in self._actions[group]:
            self._actions[group].append(action)

    #Gets all actions in a group
    def get_actions(self, group):
        results = []
        if group in self._actions.keys():
            results = self._actions[group].copy()
        return results
    
    #Removes an action from a group
    def remove_action(self, group, action):
        if group in self._actions:
            self._actions[group].remove(action)