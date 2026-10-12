class Life:
    def __init__(self,lifes: int) -> None:
        self.lifes = lifes
    
    def removelife(self):
        self.lifes -= 1
    
    def addlife(self):
        self.lifes += 1