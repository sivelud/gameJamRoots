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

# Peashooter
peashooterRight = "src/media/peashooterR.png"
peashooterRightIMG = pygame.transform.scale(pygame.image.load(peashooterRight),(90,90))

peashooterLeft = "src/media/peashooterL.png"
peashooterLeftIMG = pygame.transform.scale(pygame.image.load(peashooterLeft),(90,90))

peashooterUp = "src/media/peashooterU.png"
peashooterUpIMG = pygame.transform.scale(pygame.image.load(peashooterUp),(90,90))

peashooterDown = "src/media/peashooterD.png"
peashooterDownIMG = pygame.transform.scale(pygame.image.load(peashooterDown),(90,90))

peashooterShop = "src/media/peashooterShop.png"
peashooterShopIMG = pygame.transform.scale(pygame.image.load(peashooterShop),(90,90))

# Dualshot
dualshotRight = "src/media/dualshotR.png"
dualshotRightIMG = pygame.transform.scale(pygame.image.load(dualshotRight),(90,90))

dualshotLeft = "src/media/dualshotL.png"
dualshotLeftIMG = pygame.transform.scale(pygame.image.load(dualshotLeft),(90,90))

dualshotUp = "src/media/dualshotU.png"
dualshotUpIMG = pygame.transform.scale(pygame.image.load(dualshotUp),(90,90))

dualshotDown = "src/media/dualshotD.png"
dualshotDownIMG = pygame.transform.scale(pygame.image.load(dualshotDown),(90,90))

dualshotShop = "src/media/dualshotShop.png"
dualshotShopIMG = pygame.transform.scale(pygame.image.load(dualshotShop),(90,90))

# Farm
farmImage = "src/media/farm.png"
farmImageIMG = pygame.transform.scale(pygame.image.load(farmImage),(90,90))

# Enemy
enemyRight = "src/media/zombieR.png"
enemyLeft = "src/media/zombieL.png"
enemyUp = "src/media/zombieU.png"
enemyDown = "src/media/zombieD.png"

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





sellImage = "src/media/sell.png"

projectile_img = "src/media/shot_grey_small.png"

title_screen1 = "src/media/plant_shooter_GTA_Titlescreen.png"
title_screen = pygame.transform.scale(pygame.image.load(title_screen1),(screen_w,screen_h))

backgroundImage1 = "src/media/board.png"
backgroundImage = pygame.transform.scale(pygame.image.load(backgroundImage1),(screen_w,screen_h))



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

money = 250


possibleSpawn = {
    0: [copy.copy(v2(0,270+45)), copy.copy(v2(0,360+45)), copy.copy(v2(0,450+45)), copy.copy(v2(0,540+45))], 
    1: [copy.copy(v2(270+45, 0)), copy.copy(v2(360+45, 0)), copy.copy(v2(450+45, 0)), copy.copy(v2(540+45, 0))],
    2: [copy.copy(v2(900,270+45)), copy.copy(v2(900,360+45)), copy.copy(v2(900,450+45)), copy.copy(v2(900,540+45))],
    3: [copy.copy(v2(360+45, 900)), copy.copy(v2(270+45, 900)), copy.copy(v2(450+45, 900)), copy.copy(v2(540+45, 900))]
}

"""
* Controls
"""
# Player 1
boost_key_p1 = pygame.K_w
left_key_p1 = pygame.K_a
right_key_p1 = pygame.K_d
shoot_key_p1 = pygame.K_SPACE
# Player 2
boost_key_p2 = pygame.K_UP
left_key_p2 = pygame.K_LEFT
right_key_p2 = pygame.K_RIGHT
shoot_key_p2 = pygame.K_p
# Both players
reset_key = pygame.K_r
