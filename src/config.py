import pygame
from pygame import Vector2 as v2
import time
import copy

pygame.init()

"""
* Screen
"""
screen_w = 900             # default=1200
screen_h = 900              # default=700
program_speed = 60          # default=30
screen = pygame.display.set_mode((screen_w, screen_h))
klokke = pygame.time.Clock()

pygame.display.set_caption("Plants against Zombies")
bg = (0, 255, 255)
font = pygame.font.Font("freesansbold.ttf", 30)


shopitemsize = 60
shopOffset = 3
shopitemY = 40

peashooterCost = 10
farmCost = 50
dualshotCost = 25

# Peashooter
peashooterRight = "src/media/singleRight.png"
peashooterRightIMG = pygame.transform.scale(pygame.image.load(peashooterRight),(90,90))

peashooterLeftIMG = pygame.transform.flip(peashooterRightIMG, True, False)

peashooterUp = "src/media/singleUp.png"
peashooterUpIMG = pygame.transform.scale(pygame.image.load(peashooterUp),(90,90))

peashooterDown = "src/media/singleDown.png"
peashooterDownIMG = pygame.transform.scale(pygame.image.load(peashooterDown),(90,90))

peashooterShopIMG = pygame.transform.scale(pygame.image.load(peashooterRight),(shopitemsize,shopitemsize))

# Dualshot
dualshotRight = "src/media/doubleshooterSides.png"
dualshotRightIMG = pygame.transform.scale(pygame.image.load(dualshotRight),(90,90))

dualshotUp = "src/media/doubleshooterUp.png"
dualshotUpIMG = pygame.transform.scale(pygame.image.load(dualshotUp),(90,90))

dualshotShopIMG = pygame.transform.scale(pygame.image.load(dualshotRight),(shopitemsize,shopitemsize))



# Farm
farmImage = "src/media/farm.png"
farmImageIMG = pygame.transform.scale(pygame.image.load(farmImage),(90,90))
farmShopIMG = pygame.transform.scale(pygame.image.load(farmImage),(shopitemsize,shopitemsize))

# Sell
sellImage = "src/media/sell.png"
sellImageIMG = pygame.transform.scale(pygame.image.load(sellImage),(shopitemsize,shopitemsize))

# Projectile
projectile = "src/media/bullet.png"
projectileIMG = pygame.transform.scale(pygame.image.load(projectile),(25,25))

# Fly
fly = "src/media/fly.png"
flyIMG = pygame.transform.scale(pygame.image.load(fly),(25,25))




# Zombie
zombieSourceImage1 = "src/media/zombie1.png"
zombieSourceImage1IMG = pygame.transform.scale(pygame.image.load(zombieSourceImage1),(90,90))
zombieSourceImage2 = "src/media/zombie2.png"
zombieSourceImage2IMG = pygame.transform.scale(pygame.image.load(zombieSourceImage2),(90,90))
zombieSourceImage3 = "src/media/zombie3.png"
zombieSourceImage3IMG = pygame.transform.scale(pygame.image.load(zombieSourceImage3),(90,90))
zombieSourceImage4 = "src/media/zombie4.png"
zombieSourceImage4IMG = pygame.transform.scale(pygame.image.load(zombieSourceImage4),(90,90))

zombieRightIMG1 = pygame.transform.flip(zombieSourceImage1IMG, True, False)
zombieRightIMG2 = pygame.transform.flip(zombieSourceImage2IMG, True, False)
zombieRightIMG3 = pygame.transform.flip(zombieSourceImage3IMG, True, False)
zombieRightIMG4 = pygame.transform.flip(zombieSourceImage4IMG, True, False)

zombieLeftWalkLoop = [zombieSourceImage1IMG, zombieSourceImage2IMG, zombieSourceImage3IMG, zombieSourceImage4IMG]
zombieRightWalkLoop = [zombieRightIMG1, zombieRightIMG2, zombieRightIMG3, zombieRightIMG4]

# Title screen
title_screen1 = "src/media/plant_shooter_GTA_Titlescreen.png"
title_screen = pygame.transform.scale(pygame.image.load(title_screen1),(screen_w,screen_h))

# Background
backgroundImage1 = "src/media/board.png"
backgroundImage = pygame.transform.scale(pygame.image.load(backgroundImage1),(screen_w,screen_h))


# Groups
enemies = pygame.sprite.Group()
plants = pygame.sprite.Group()
shots = pygame.sprite.Group()
cursorGroup = pygame.sprite.Group()
shopGroup = pygame.sprite.Group()
flyGroup = pygame.sprite.Group()


shopitemsize = 60
shopOffset = 3
shopitemY = 40

peashooterCost = 10
farmCost = 50
dualshotCost = 25

font = pygame.font.Font("freesansbold.ttf", 30)
game_over_font = pygame.font.Font("freesansbold.ttf", 90)
moneyPlacement = (850, 50)

startHealth = 1
health  = startHealth

startmoney = 250
money = startmoney


possibleSpawn = {
    0: [copy.copy(v2(0,270+45)), copy.copy(v2(0,360+45)), copy.copy(v2(0,450+45)), copy.copy(v2(0,540+45))], 
    1: [copy.copy(v2(270+45, 0)), copy.copy(v2(360+45, 0)), copy.copy(v2(450+45, 0)), copy.copy(v2(540+45, 0))],
    2: [copy.copy(v2(900,270+45)), copy.copy(v2(900,360+45)), copy.copy(v2(900,450+45)), copy.copy(v2(900,540+45))],
    3: [copy.copy(v2(360+45, 900)), copy.copy(v2(270+45, 900)), copy.copy(v2(450+45, 900)), copy.copy(v2(540+45, 900))]
}

