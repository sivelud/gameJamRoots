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
        self.imgList = [peashooterRightIMG, peashooterDownIMG,peashooterLeftIMG,peashooterUpIMG]
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
        cn.playShootSound()
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
        self.cost = cn.peashooterCost
        self.name = "peashooter"

class DualShot(Plant):
    def __init__(self, pos):
        super().__init__(pos)
        self.pos = pos
        self.imgList = [dualshotRightIMG, dualshotUpIMG ,dualshotRightIMG ,dualshotUpIMG]
        self.listDirectionVectors = [v2(1,0),v2(0,1),v2(-1,0),v2(0,-1)]
        self.image = self.imgList[0]
        self.numberOfTimesClicked = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos.x, self.pos.y]
        self.updatesSinceShot = 0
        self.cost = cn.dualshotCost
        self.name = "dualshot"

    def shoot(self):
        shots.add(Projectile(copy.copy(self.pos + v2(45,45)), copy.copy(self.listDirectionVectors[self.numberOfTimesClicked%4])))
        shots.add(Projectile(copy.copy(self.pos + v2(45,45)), copy.copy(self.listDirectionVectors[(2+self.numberOfTimesClicked)%4])))
        self.updatesSinceShot = 0

class Farm(Plant):
    def __init__(self, pos):
        super().__init__(pos)
        self.imgList = [farmImageIMG, farmImageIMG, farmImageIMG, farmImageIMG]
        self.listDirectionVectors = [v2(1,0),v2(0,1),v2(-1,0),v2(0,-1)]
        self.image = self.imgList[0]
        self.numberOfTimesClicked = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos.x, self.pos.y]
        self.shotsCounter = 0
        self.cost = cn.farmCost
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
        self.image = projectileIMG
        self.rect = self.image.get_rect()
        self.rect.center = [pos.x, pos.y]
        self.pos = pos
        self.dire = dir
        self.life = 0

    def move(self):
        self.pos += self.dire * 10
        self.rect.center = [self.pos.x, self.pos.y]
        self.life += 1

    def update(self):
        self.move()
        self.execute()

    def execute(self):
        self.life +=1
        if self.life > 115:
            self.kill()

class Fly(Parent):
    def __init__(self, pos, endpos):
        super().__init__()
        self.image = flyIMG
        self.rect = self.image.get_rect()
        self.rect.center = [pos.x, pos.y]
        self.pos = pos
        self.endpos = endpos
        self.acc = endpos - pos
        self.acc.normalize_ip()
        self.timeStationary = 0
        self.dir = v2(-0.5,0)
    
    def move(self):
        if ((self.pos.x > self.endpos.x +20 and self.pos.x < self.endpos.x + 50)) and ((self.pos.y > self.endpos.y +20 and self.pos.y < self.endpos.y + 50)):
            self.timeStationary +=1
            
        else:
            self.acc = self.endpos + v2(45,45) - self.pos
            self.acc.normalize_ip()
            self.pos = + self.pos + + self.acc +self.dir
            self.rect.center = [self.pos.x, self.pos.y]

    def update(self):
        self.move()
        if self.timeStationary >=75:
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
        if shopitemplacement(4) <= x < shopitemplacement(4)+shopitemsize:
            key = "sell"



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
        self.mapTiles = { # ONLY plant tiles in the middle should have a 2 letter long name
            # Centre:
            "a4":[None, (270,270)], "b4":[None, (360,270)], "c4":[None, (450, 270)], "d4": [None, (540, 270)],
            "a3":[None, (270, 360)], "b3":[None, (360, 360)], "c3":[None, (450, 360)], "d3":[None, (540, 360)],
            "a2":[None, (270, 450)], "b2":[None, (360, 450)], "c2":[None, (450, 450)], "d2":[None, (540, 450)],
            "a1":[None, (270, 540)], "b1":[None, (360, 540)], "c1":[None, (450, 540)], "d1":[None,(540, 540)],

            # Shop:
            "peashooter":[ShopItem(v2(shopitemplacement(1), shopitemY), peashooterShopIMG)],
            "dualshot":[ShopItem(v2(shopitemplacement(2), shopitemY), dualshotShopIMG)],
            "farm":[ShopItem(v2(shopitemplacement(3), shopitemY), farmShopIMG)],
            "sell":[ShopItem(v2(shopitemplacement(4), shopitemY), sellImageIMG)]
        }
        self.level = 0
        self.numOfEnemies = 0
        self.enemiesToBeSpawned = 0
        shopGroup.add(self.mapTiles["peashooter"][0])
        shopGroup.add(self.mapTiles["dualshot"][0])
        shopGroup.add(self.mapTiles["farm"][0])
        self.lastSpawn = 0
        shopGroup.add(self.mapTiles["sell"][0])
        self.flyPlant = False
        self.flySpawned = False

    def killPlant(self, key):
        if self.mapTiles[key][0] != None:
            self.mapTiles[key][0].kill()
            self.mapTiles[key][0] = None

    def killAllPlants(self):
        for elem in self.mapTiles:
            if len(elem) == 2:
                self.killPlant(elem)
            


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
                    elif tile == "sell":
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

        if self.mouseHolding == "sell":
            if self.mapTiles[key][0] != None:
                sellprice = int(self.mapTiles[key][0].cost/2)
                cn.money += sellprice
                
                self.mapTiles[key][0].kill()
                self.mapTiles[key][0] = None
                           

        
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
            if self.mouseHolding == "sell":
                self.cursorImage.updateImage(sellImage)
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

        money_txt = font.render(txt, True, (250, 180, 0))

        textRect1 = money_txt.get_rect()
        textRect1.center = (moneyPlacement)
        screen.blit(money_txt, textRect1)

    def writeShopPrice(self):
        yPlace = shopitemY + 80
        pea_price = str(cn.peashooterCost)
        dual_price = str(cn.dualshotCost)
        farm_price = str(cn.farmCost)
        


        pea_txt = font.render(pea_price, True, (250, 180, 0))
        textRect1 = pea_txt.get_rect()
        textRect1.center = (shopitemplacement(1) + 30, yPlace)
        screen.blit(pea_txt, textRect1)

        dual_txt = font.render(dual_price, True, (250, 180, 0))
        textRect1 = dual_txt.get_rect()
        textRect1.center = (shopitemplacement(2) + 30, yPlace)
        screen.blit(dual_txt, textRect1)

        farm_txt = font.render(farm_price, True, (250, 180, 0))
        textRect1 = farm_txt.get_rect()
        textRect1.center = (shopitemplacement(3) + 30, yPlace)
        screen.blit(farm_txt, textRect1)

        

    def writeLevel(self):
        txt = "LEVEL: "
        txt += str(self.level)

        level_txt = font.render(txt, True, (0, 0, 0))

        textRect1 = level_txt.get_rect()
        textRect1.center = (levelPlacement)
        screen.blit(level_txt, textRect1)

    def enemySpawns(self):
        if self.numOfEnemies < self.enemiesToBeSpawned:
            if r.uniform(0,1) > 0.4:
                spawn = r.uniform(0,10)
                rint = self.lastSpawn
                if r.uniform(0,10) > self.level*1.2:
                    rint = r.randint(0,3)
                    self.lastSpawn = rint

                if (r.uniform(0,10) - self.level*0.1 < 1) and len(plants) != 0 and len(flyGroup) == 0 and self.level > 4:
                    self.flyPlant = self.chooseFlySpawn()
                    flyGroup.add(Fly(v2(910,910), self.flyPlant))
                    if self.level > 10:
                        flyGroup.add(Fly(v2(910,910), self.flyPlant))
                    self.flySpawned = True
                elif len(flyGroup) == 0:
                    self.flySpawned = False
                if spawn - self.level*0.1 < 0.5:   
                    if self.level > 10:
                        if r.uniform(0,1) > 0.5 - self.level*0.1 :
                            print("super enemy")
                            enemies.add(SuperEnemy(copy.copy(possibleSpawn[rint][r.randint(0,3)]), rint))
                            self.numOfEnemies += 1           
                    else:
                        print("best enemy")
                        enemies.add(EnemyBest(copy.copy(possibleSpawn[rint][r.randint(0,3)]), rint))
                        self.numOfEnemies += 1


                elif spawn - self.level*0.1 < 1:
                    print("better enemy")
                    enemies.add(EnemyBetter(copy.copy(possibleSpawn[rint][r.randint(0,3)]), rint))
                    self.numOfEnemies += 1
                else:
                    enemies.add(Enemy(copy.copy(possibleSpawn[rint][r.randint(0,3)]), rint))
                    self.numOfEnemies += 1

    def newLevel(self):
        if self.numOfEnemies == self.enemiesToBeSpawned and len(enemies) == 0:
            self.level +=1
            self.enemiesToBeSpawned = round(self.level**(1.5))
            self.numOfEnemies = 0
            self.lastSpawn = r.randint(0,3)
        if self.flySpawned and len(flyGroup) == 0:
            self.removePlantFly()
            self.flySpawned = False
            print(self.level)

    def removePlantFly(self):
        (x,y) = self.flyPlant.x, self.flyPlant.y
        try:
            self.mapTiles[coordinates_to_key((x,y))][0].kill()
            self.mapTiles[coordinates_to_key((x,y))][0] = None
        except AttributeError:
            pass

    def chooseFlySpawn(self):
        keyList = ['a4','a3','a2','a1','b4','b3','b2','b1','c4','c3','c2','c1','d4','d3','d2','d1']
        r.shuffle(keyList)
        for key in keyList:
            if self.mapTiles[key][0] != None:
                return v2(self.mapTiles[key][1])
        


class Enemy(Parent):
    def __init__(self, pos, dire):
        super().__init__()
        self.pos = pos
        self.dire = dire
        self.imgList = [zombieRightWalkLoop, zombieLeftWalkLoop, zombieLeftWalkLoop, zombieLeftWalkLoop]
        self.listDirectionVectors = [v2(0.5,0),v2(0,0.5),v2(-0.5,0),v2(0,-0.5)]
        self.animationLoop = self.imgList[dire]
        self.walkloopN = 0
        self.walkloopTimer = 0
        self.image = self.animationLoop[self.walkloopN]
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos.x, self.pos.y]
        self.health = 3
        self.moneyPerKill = 2

    
    def move(self):
        self.pos += self.listDirectionVectors[self.dire] 
        self.rect.center = [self.pos.x, self.pos.y]

    def update(self):
        self.move()
        self.collision()
        self.enemyCrossedLanes()
        self.walkloopTimer += 1
        if self.walkloopTimer > 10:
            self.walkloopN += 1
            self.walkloopTimer = 0
        if self.walkloopN >= len(self.animationLoop):
            self.walkloopN = 0
        self.image = self.animationLoop[self.walkloopN]
        

    def collision(self):
        for _ in shots:
            if pygame.sprite.spritecollide(self, shots, True):
                self.health -= 1
        if self.health <= 0:
            cn.money += self.moneyPerKill
            cn.playDeathSound()
            self.kill()
        
    def enemyCrossedLanes(self):
        
        if self.pos.x > 975 or self.pos.x < -25 or self.pos.y > 950 or self.pos.y < -25:
            cn.health -= 1
            self.kill()

class EnemyBetter(Enemy):
    def __init__(self, pos, dire):
        super().__init__(pos, dire)
        self.health = 5
        self.moneyPerKill = 5

    def collision(self):
        for _ in shots:
            if pygame.sprite.spritecollide(self, shots, True):
                self.health -= 1
        if self.health <= 0:
            cn.money += self.moneyPerKill
            self.kill()

class EnemyBest(Enemy):
    def __init__(self, pos, dire):
        super().__init__(pos, dire)
        self.health = 10
        self.moneyPerKill = 7

    def collision(self):
        for _ in shots:
            if pygame.sprite.spritecollide(self, shots, True):
                self.health -= 1
        if self.health <= 0:
            cn.money += self.moneyPerKill
            self.kill()

class SuperEnemy(Enemy):
    def __init__(self, pos, dire):
        super().__init__(pos, dire)
        self.listDirectionVectors = [v2(1,0),v2(0,1),v2(-1,0),v2(0,-1)]
        self.health = 10
        self.imgList = [pinkzombieRightWalkLoop, pinkzombieLeftWalkLoop, pinkzombieLeftWalkLoop, pinkzombieLeftWalkLoop]
        self.animationLoop = self.imgList[dire]




class cursorImageClass(Parent):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(peashooterRight),(60,60))

    def updateImage(self, image):
        self.image = pygame.transform.scale(pygame.image.load(image),(60,60))