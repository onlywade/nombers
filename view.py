import sys

from events import MapBuiltEvent

class View():

  def __init__(self, event_manager):
    self.event_manager = event_manager
    self.event_manager.register_listener(self)

  def notify(self, event):
    if isinstance(event, MapBuiltEvent):
      self.draw_map(event.game_map)

  def draw_map(self, game_map):
    sys.stdout.write('\n')
    for x in game_map.sectors_by_coord:
      for y in x:
        #print('{0}, {1}'.format(x, y))
        sys.stdout.write('#')
      sys.stdout.write('\n')
