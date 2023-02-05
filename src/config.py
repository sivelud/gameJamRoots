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

peashooterRight = "src/media/peashooterR.png"
peashooterLeft = "src/media/peashooterL.png"
peashooterUp = "src/media/peashooterU.png"
peashooterDown = "src/media/peashooterD.png"
peashooterShop = "src/media/peashooterShop.png"

dualshotRight = "src/media/dualshotR.png"
dualshotLeft = "src/media/dualshotL.png"
dualshotUp = "src/media/dualshotU.png"
dualshotDown = "src/media/dualshotD.png"
dualshotShop = "src/media/dualshotShop.png"

enemyRight = "src/media/zombieR.png"
enemyLeft = "src/media/zombieL.png"
enemyUp = "src/media/zombieU.png"
enemyDown = "src/media/zombieD.png"

farmImage = "src/media/farm.png"

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
