class MapBuiltEvent():

  def __init__(self, game_map):
    self.name = 'MapBuiltEvent'
    self.game_map = game_map

class EventManager():

  def __init__(self):
    self.listeners = []

  def register_listener(self, listener):
    self.listeners.append(listener)

  def post(self, event):
    for listener in self.listeners:
      listener.notify(event)

