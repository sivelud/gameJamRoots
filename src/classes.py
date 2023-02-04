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
        self.listDirectionVectors = [v2(1,0),v2(0,1),v2(-1,0),v2(0,-1)]
        self.image = self.imgList[1]
        self.numberOfTimesClicked = 1
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
        self.rotateImage()
        #upgrade()?

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
        self.life = 0

    def move(self):
        self.pos += self.dire * 10
        self.rect.center = [self.pos.x, self.pos.y]

    def update(self):
        self.move()
        self.life +=1
        self.execute()

    def execute(self):
        if self.life > 65:
            self.kill()

"""
* Input: touple (x, y)
* Returns: key for mapTiles in GameBoard. Returns None, if outside.
"""
def coordinates_to_key(pos):
    x = pos[0]
    y = pos[1]
    key = ""
    if 270 <= x < 360:
        key += "a"
        if 270 <= y < 360:
            key += "4"
        if 360 <= y < 450:
            key += "3"
        if 450 <= y < 540:
            key += "2"
        if 540 <= y < 630:
            key += "1"
    if 360 <= x < 450:
        key += "b"
        if 270 <= y < 360:
            key += "4"
        if 360 <= y < 450:
            key += "3"
        if 450 <= y < 540:
            key += "2"
        if 540 <= y < 630:
            key += "1"
        
    if 450 <= x < 540:
        key += "c"
        if 270 <= y < 360:
            key += "4"
        if 360 <= y < 450:
            key += "3"
        if 450 <= y < 540:
            key += "2"
        if 540 <= y < 630:
            key += "1"
        
    if 540 <= x < 630:
        key += "d"
        if 270 <= y < 360:
            key += "4"
        if 360 <= y < 450:
            key += "3"
        if 450 <= y < 540:
            key += "2"
        if 540 <= y < 630:
            key += "1"

    if len(key) == 2:
        return key
    return None


"""
* GameBoard for 900 * 900 board
"""
class GameBoard():
    def __init__(self):
        """
        [0] = Tower tile
        [1] = Position. Topleft Corner tuple (x,y)
        """
        self.mapTiles = {
            "a4":[None, (270,270)], "b4":[None, (360,270)], "c4":[None, (450, 270)], "d4": [None, (540, 270)],
            "a3":[None, (270, 360)], "b3":[None, (360, 360)], "c3":[None, (450, 360)], "d3":[None, (540, 360)],
            "a2":[None, (270, 450)], "b2":[None, (360, 450)], "c2":[None, (450, 450)], "d2":[None, (540, 450)],
            "a1":[None, (270, 540)], "b1":[None, (360, 540)], "c1":[None, (450, 540)], "d1":[None,(540, 540)]
        }

    def click_tile(self, mousePosClick):
        tile = coordinates_to_key(mousePosClick)
        print("tile clicked = ", tile)
        if self.mapTiles[tile][0] != None:
            self.mapTiles[tile][0].clicked()
            return
        print("Tile is empty")

    def placePlant(self, key):
        pos = self.mapTiles[key][1]
        posV2 = v2(pos[0], pos[1])
        plant = Peashooter(posV2)
        if self.mapTiles[key][0] != None:
            self.mapTiles[key][0].kill()
        self.mapTiles[key][0] = plant
        plants.add(plant)


class Enemy(Parent):
    def __init__(self, pos, dire):
        super().__init__()
        self.pos = pos
        self.dire = dire
        self.imgList = [pygame.transform.scale(pygame.image.load(peashooterRight),(90,90)),pygame.transform.scale(pygame.image.load(peashooterDown),(90,90)),pygame.transform.scale(pygame.image.load(peashooterLeft),(90,90)),pygame.transform.scale(pygame.image.load(peashooterUp),(90,90))]
        self.listDirectionVectors = [v2(1,0),v2(0,1),v2(-1,0),v2(0,-1)]
        self.image = self.imgList[dire]
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos.x, self.pos.y]
        self.health = 3
    
    def move(self):
        self.pos += self.listDirectionVectors[self.dire] 
        self.rect.center = [self.pos.x, self.pos.y]  

    def update(self):
        self.move()
        self.collision()

    def collision(self):
        for _ in shots:
            if pygame.sprite.spritecollide(self, shots, True):
                self.health -= 1
        if self.health <= 0:
            self.kill()
        
    
        
        



