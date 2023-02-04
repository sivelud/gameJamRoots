from config import *

class Parent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Peashooter(Parent):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.imgRight = pygame.image.load(peashooterRight)
        self.imgLeft = pygame.image.load(peashooterLeft)
        self.imgUp = pygame.image.load(peashooterUp)
        self.imgDown = pygame.image.load(peashooterDown)
        self.imgList = [pygame.image.load(peashooterRight),pygame.image.load(peashooterDown),pygame.image.load(peashooterLeft),pygame.image.load(peashooterUp)]
        self.image = self.imgList[0]
        self.numberOfTimesClicked = 0
        self.rect = self.image.get_rect()

    def rotateImage(self):
        #should run once per click 
        self.numberOfTimesClicked +=1
        self.image = self.imgList[self.numberOfTimesClicked%4]
        self.rect = self.image.get_rect()