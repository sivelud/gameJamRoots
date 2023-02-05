from config import *
import config as cn
import random as r

class Parent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Plant(Parent):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.imgList = [pygame.transform.scale(pygame.image.load(peashooterRight),(90,90)),pygame.transform.scale(pygame.image.load(peashooterDown),(90,90)),pygame.transform.scale(pygame.image.load(peashooterLeft),(90,90)),pygame.transform.scale(pygame.image.load(peashooterUp),(90,90))]
        self.listDirectionVectors = [v2(1,0),v2(0,1),v2(-1,0),v2(0,-1)]
        self.image = self.imgList[0]
        self.numberOfTimesClicked = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos.x, self.pos.y]
        self.updatesSinceShot = 0


    def rotateImage(self):
        #should run once per click 
        self.numberOfTimesClicked +=1
        self.image = self.imgList[self.numberOfTimesClicked%4]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos.x, self.pos.y]
        
    def shoot(self):
        shots.add(Projectile(copy.copy(self.pos + v2(45,45)), copy.copy(self.listDirectionVectors[self.numberOfTimesClicked%4])))
        self.updatesSinceShot = 0

    def clicked(self):
        self.rotateImage()
        #upgrade()?

    def update(self):
        self.updatesSinceShot +=1
        
class Peashooter(Plant):
    def __init__(self, pos):
        super().__init__(pos)
        self.cost = 10
        self.name = "peashooter"

class DualShot(Plant):
    def __init__(self, pos):
        super().__init__(pos)
        self.pos = pos
        self.imgList = [pygame.transform.scale(pygame.image.load(dualshotRight),(90,90)),pygame.transform.scale(pygame.image.load(dualshotDown),(90,90)),pygame.transform.scale(pygame.image.load(dualshotLeft),(90,90)),pygame.transform.scale(pygame.image.load(dualshotUp),(90,90))]
        self.listDirectionVectors = [v2(1,0),v2(0,1),v2(-1,0),v2(0,-1)]
        self.image = self.imgList[0]
        self.numberOfTimesClicked = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos.x, self.pos.y]
        self.updatesSinceShot = 0
        self.cost = 25
        self.name = "dualshot"

    def shoot(self):
        shots.add(Projectile(copy.copy(self.pos + v2(45,45)), copy.copy(self.listDirectionVectors[self.numberOfTimesClicked%4])))
        shots.add(Projectile(copy.copy(self.pos + v2(45,45)), copy.copy(self.listDirectionVectors[(2+self.numberOfTimesClicked)%4])))
        self.updatesSinceShot = 0

class Farm(Plant):
    def __init__(self, pos):
        super().__init__(pos)
        self.imgList = [pygame.transform.scale(pygame.image.load(farmImage),(90,90)),pygame.transform.scale(pygame.image.load(farmImage),(90,90)),pygame.transform.scale(pygame.image.load(farmImage),(90,90)),pygame.transform.scale(pygame.image.load(farmImage),(90,90))]
        self.listDirectionVectors = [v2(1,0),v2(0,1),v2(-1,0),v2(0,-1)]
        self.image = self.imgList[0]
        self.numberOfTimesClicked = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos.x, self.pos.y]
        self.shotsCounter = 0
        self.name = "farm"


    def shoot(self):
        self.shotsCounter += 1
        if self.shotsCounter >= 15:
            cn.money += 5
            self.shotsCounter = 0
        self.updatesSinceShot = 0

class ShopItem(Parent):
    def __init__(self, pos, image):
        super().__init__()
        self.pos = pos
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos.x, self.pos.y]
        self.updatesSinceShot = 0

    def clicked(self):
        return 1

    def shoot(self):
        pass

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
        self.execute()

    def execute(self):
        self.life +=1
        if self.life > 65:
            self.kill()


def shopitemplacement(nr):
            return (shopitemsize*nr + shopOffset*nr)-30

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

    if shopitemY <= y < shopitemY+shopitemsize:
        if shopitemplacement(1) <= x < shopitemplacement(1)+shopitemsize:
            key = "peashooter"
        if shopitemplacement(2) <= x < shopitemplacement(2)+shopitemsize:
            key = "dualshot"
        if shopitemplacement(3) <= x < shopitemplacement(3)+shopitemsize:
            key = "farm"



    if len(key) > 1:
        return key

    return None


"""
* GameBoard for 900 * 900 board
"""
class GameBoard():
    def __init__(self):
        self.mouseHolding = None

        self.cursorImage = cursorImageClass()

        """
        [0] = Tower tile
        [1] = Position. Topleft Corner tuple (x,y)
        """
        self.mapTiles = {
            # Centre:
            "a4":[None, (270,270)], "b4":[None, (360,270)], "c4":[None, (450, 270)], "d4": [None, (540, 270)],
            "a3":[None, (270, 360)], "b3":[None, (360, 360)], "c3":[None, (450, 360)], "d3":[None, (540, 360)],
            "a2":[None, (270, 450)], "b2":[None, (360, 450)], "c2":[None, (450, 450)], "d2":[None, (540, 450)],
            "a1":[None, (270, 540)], "b1":[None, (360, 540)], "c1":[None, (450, 540)], "d1":[None,(540, 540)],

            # Shop:
            "peashooter":[ShopItem(v2(shopitemplacement(1), shopitemY), pygame.transform.scale(pygame.image.load(peashooterShop),(shopitemsize,shopitemsize)))],
            "dualshot":[ShopItem(v2(shopitemplacement(2), shopitemY), pygame.transform.scale(pygame.image.load(dualshotShop),(shopitemsize,shopitemsize)))],
            "farm":[ShopItem(v2(shopitemplacement(3), shopitemY), pygame.transform.scale(pygame.image.load(farmImage),(shopitemsize,shopitemsize)))],
        }
        self.level = 0
        self.numOfEnemies = 0
        self.enemiesToBeSpawned = 0
        plants.add(self.mapTiles["peashooter"][0])
        plants.add(self.mapTiles["dualshot"][0])
        plants.add(self.mapTiles["farm"][0])

    def click_tile(self, mousePosClick):
        tile = coordinates_to_key(mousePosClick)
        if tile == None:
            self.mouseHolding = None
            return
        # If the mouse is holding something: If clicked in one of the tiles, place that something. If clicked outside of clickable tile, clear mouse holding.
        if self.mouseHolding != None:
            if tile != None:
                if len(tile) <= 2:
                    self.placePlant(tile)
                    self.mouseHolding = None
                    return
            if tile == None:
                self.mouseHolding = None
                return


        if self.mapTiles[tile] != None:
            print(tile)
            if self.mapTiles[tile][0] != None:
                checker = self.mapTiles[tile][0].clicked() # Shop tiles return 1, grid items return None
                if checker != None:
                    if tile == "peashooter":
                        if cn.money >= cn.peashooterCost: # Highlights peashooter only if you can afford it
                            self.mouseHolding = tile
                    elif tile == "dualshot":
                        if cn.money >= cn.dualshotCost:
                            self.mouseHolding = tile
                    elif tile == "farm":
                        if cn.money >= cn.farmCost:
                            self.mouseHolding = tile
        
    def placePlant(self, key):
        pos = self.mapTiles[key][1]
        posV2 = v2(pos[0], pos[1])
        global money

        if self.mapTiles[key][0] != None: # If the plant placed is the same as is there before, no money is lost.
            if self.mapTiles[key][0].name == self.mouseHolding:
                self.mouseHolding = None
                return


        if self.mouseHolding == "peashooter":
            if cn.money < peashooterCost:
                self.mouseHolding = None
                return
            plant = Peashooter(posV2)
            if self.mapTiles[key][0] != None:
                self.mapTiles[key][0].kill()
            self.mapTiles[key][0] = plant
            plants.add(plant)
            cn.money = cn.money - peashooterCost
        if self.mouseHolding == "dualshot":
            if cn.money < dualshotCost:
                self.mouseHolding = None
                return
            plant = DualShot(posV2)
            if self.mapTiles[key][0] != None:
                self.mapTiles[key][0].kill()
            self.mapTiles[key][0] = plant
            plants.add(plant)
            cn.money = cn.money - dualshotCost
        
        if self.mouseHolding == "farm":
            if cn.money < farmCost:
                self.mouseHolding = None
                return
            plant = Farm(posV2)
            if self.mapTiles[key][0] != None:
                self.mapTiles[key][0].kill()
            self.mapTiles[key][0] = plant
            plants.add(plant)
            cn.money = cn.money - farmCost

    def mouseImage(self):
        if self.mouseHolding != None:
            if self.mouseHolding == "peashooter":
                self.cursorImage.updateImage(peashooterRight)
            if self.mouseHolding == "dualshot":
                self.cursorImage.updateImage(dualshotRight)
            if self.mouseHolding == "farm":
                self.cursorImage.updateImage(farmImage)
            x,y = pygame.mouse.get_pos()
            #cursorImage = cursorImageClass()
            self.cursorImage.rect = self.cursorImage.image.get_rect()
            self.cursorImage.rect.center = [x, y]
            cursorGroup.add(self.cursorImage)
        else:
            self.cursorImage.kill()

    def writeMoney(self):
        txt = "$"
        txt += str(cn.money)

        money_txt = font.render(txt, True, (100, 100, 100))

        textRect1 = money_txt.get_rect()
        textRect1.center = (moneyPlacement)
        screen.blit(money_txt, textRect1)

    def enemySpawns(self):
        if self.numOfEnemies < self.enemiesToBeSpawned:
            if r.uniform(0,1) > 0.8:
                if r.uniform(0,10) - self.level*0.1 > 0.5:   
                    print("best enemy")
                    rint = r.randint(0,3)
                    enemies.add(EnemyBest(copy.copy(possibleSpawn[rint][r.randint(0,3)]), rint))
                    self.numOfEnemies += 1

                else:
                    rint = r.randint(0,3)
                    enemies.add(Enemy(copy.copy(possibleSpawn[rint][r.randint(0,3)]), rint))
                    self.numOfEnemies += 1

    def newLevel(self):
        if self.numOfEnemies == self.enemiesToBeSpawned and len(enemies) == 0:
            self.level +=1
            self.enemiesToBeSpawned = round(self.level**(1.5))
            self.numOfEnemies = 0
            print(self.level)


class Enemy(Parent):
    def __init__(self, pos, dire):
        super().__init__()
        self.pos = pos
        self.dire = dire
        self.imgList = [pygame.transform.scale(pygame.image.load(enemyRight),(90,90)),pygame.transform.scale(pygame.image.load(enemyDown),(90,90)),pygame.transform.scale(pygame.image.load(enemyLeft),(90,90)),pygame.transform.scale(pygame.image.load(enemyUp),(90,90))]
        self.listDirectionVectors = [v2(0.5,0),v2(0,0.5),v2(-0.5,0),v2(0,-0.5)]
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
        self.enemyCrossedLanes()

    def collision(self):
        for _ in shots:
            if pygame.sprite.spritecollide(self, shots, True):
                self.health -= 1
        if self.health <= 0:
            cn.money += cn.money_per_kill
            self.kill()
        
    def enemyCrossedLanes(self):
        
        if self.pos.x > 975 or self.pos.x < -25 or self.pos.y > 950 or self.pos.y < -25:

            cn.health -= 1

            #print("in func:", health)

            self.kill()

class EnemyBetter(Enemy):
    def __init__(self, pos, dire):
        super().__init__(pos, dire)
        self.health = 5

class EnemyBest(Enemy):
    def __init__(self, pos, dire):
        super().__init__(pos, dire)
        self.health = 10
    
class cursorImageClass(Parent):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(peashooterRight),(60,60))

    def updateImage(self, image):
        self.image = pygame.transform.scale(pygame.image.load(image),(60,60))