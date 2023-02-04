from config import *

class Parent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class plant(Parent):
    def __init__(self):
        super().__init__()
        self.imgRight = pygame.image.load(peashooterRight)
        