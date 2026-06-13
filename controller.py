
###imports

import inspect
import model
from model import island
from model import islandslist
import view
from view import view

###implements the printview method from view to display info on a chosen island
class displaycontrol():
        @staticmethod

        def print_island_info(item):
          # Check if the item has a wrapped object (e.g., in a decorator)
          if hasattr(item, '__wrapped__'):
             item = item.__wrapped__
          elif hasattr(item, '_wrapped'):
             item = item._wrapped
          elif hasattr(item, 'original'):
             item = item.original
    # Fallback: Use inspect to get the original object
          elif inspect.isclass(item) or inspect.isfunction(item):
             item = getattr(item, '__wrapped__', item)
          for attribute, value in vars(item).items():
              if not attribute.startswith('__') and not callable(value):
                view.printline(f"{value}")

###control

class controller():
    while True: 
      displaycontrol.print_island_info(islandslist[1])
      break


    ####prints island information
   ### def printislandinfo(islandchoice):
   ##     view.printline(islandchoice.name)
    ##    view.printline(islandchoice.sea)
    ###    view.printline(islandchoice.storyarc)
    ###    view.printline(islandchoice.government)

    

###controller.print_island_info(islandslist[0])