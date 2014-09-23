import events
import game_map
import view

event_manager = events.EventManager()
the_view = view.View(event_manager)
the_map = game_map.GameMap(event_manager)
