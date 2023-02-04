from config import *

class Parent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Plant(Parent):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.imgList = [pygame.image.load(peashooterRight),pygame.image.load(peashooterDown),pygame.image.load(peashooterLeft),pygame.image.load(peashooterUp)]
        self.image = self.imgList[0]
        self.numberOfTimesClicked = 0
        self.rect = self.image.get_rect()

    def rotateImage(self):
        #should run once per click 
        self.numberOfTimesClicked +=1
        self.image = self.imgList[self.numberOfTimesClicked%4]
        self.rect = self.image.get_rect()

class Peashooter(Plant):
    def __init__(self, pos):
        super().__init__(pos)