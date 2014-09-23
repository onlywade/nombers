from events import MapBuiltEvent

SECTOR_SIZE = 20

class GameMap():

  def __init__(self, event_manager=None):
    self.event_manager = event_manager

    self.sectors = []
    self.sectors_by_coord = []
    self.populate_sectors()

    if self.event_manager:
      self.event_manager.post(MapBuiltEvent(self))

  def populate_sectors(self):

    for x in range(10):
      self.sectors_by_coord.append([])
      for y in range(10):
        sector = Sector((x, y))
        self.sectors.append(sector)
        self.sectors_by_coord[x].append(sector)


class Sector():

  def __init__(self, coords=(0,0)):
    self.x = coords[0]
    self.y = coords[1]

  def __str__(self):
    return '<Sector - {0}, {1}>'.format(self.x, self.y)

