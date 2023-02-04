from config import *
import copy

class Parent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Plant(Parent):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.imgList = [pygame.transform.scale(pygame.image.load(peashooterRight),(90,90)),pygame.transform.scale(pygame.image.load(peashooterDown),(90,90)),pygame.transform.scale(pygame.image.load(peashooterLeft),(90,90)),pygame.transform.scale(pygame.image.load(peashooterUp),(90,90))]
        self.listDirectionVectors = [v2(1,0),v2(0,-1),v2(-1,0),v2(0,1)]
        self.image = self.imgList[0]
        self.numberOfTimesClicked = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos.x, self.pos.y]


    def rotateImage(self):
        #should run once per click 
        self.numberOfTimesClicked +=1
        self.image = self.imgList[self.numberOfTimesClicked%4]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos.x, self.pos.y]
        
    def shoot(self):
        shots.add(Projectile(copy.copy(self.pos + v2(45,45)), copy.copy(self.listDirectionVectors[self.numberOfTimesClicked%4])))


    def clicked(self):
        pass

class Peashooter(Plant):
    def __init__(self, pos):
        super().__init__(pos)

class Projectile(Parent):

    def __init__(self, pos, dir):
        super().__init__()
        self.image = pygame.image.load(projectile_img)
        self.rect = self.image.get_rect()
        self.rect.center = [pos.x, pos.y]
        self.pos = pos
        self.dire = dir

    def update(self):
        """
            Updates the projectiles position. 

            Parameters:
            -----------
            Key, sprites_platform, level_blocks are needed for the polymorphism to work. 
        """
        self.pos += self.dire * 25
        self.rect.center = [self.pos.x, self.pos.y]