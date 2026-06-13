
###the basic island class###
class island:
    def __init__(self, name, sea, storyarc, government):
        self.name = name
        self.sea = sea
        self.storyarc = storyarc
        self.government = government

###decorator pattern for islands that have a main villain

class villaindecorator(island):
    def __init__(self, island, villain):
        self.name = island.name
        self.sea = island.sea
        self.storyarc = island.storyarc
        self.gvernment = island.government
        self.villain = villain
    


islandslist = [ island("Dawn Island", 
                       "East Blue", 
                       "Romance Dawn Arc", 
                       "Goa Kingdom", ),

                island("Baratie Restaurant", 
                       "East Blue",
                       "Baratie Arc",
                       "Baratie Restaurant Ownership" ),

                island("Drum Island", 
                      "Grand Line", 
                      "Drum Island Arc", 
                      "Drum Kingdom"),
                      
                villaindecorator(island(
                            "Dressrosa Island", 
                            "Grand Line - New World",
                            "Dressrosa Arc", 
                            "Dressrosa Kingdom"),
                            "Don Quixote Doflamingo")

]


###decorator for creating islands that are important to the "One Piece" storyline

###class storyarcdecorator:
   ### def __init__(self, island_instance):
    ###    self.island_instance = island_instance
    
   ### def addinfo(self, entry):
   ###     self.storyarc = entry

   ### def printinfo(self):
  ###      self.island_instance.printinfo()
  ###      print(self.storyarc)




