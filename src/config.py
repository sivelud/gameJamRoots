import pygame
from pygame import Vector2 as v2
import time
pygame.init()

"""
* Screen
"""
screen_w = 950             # default=1200
screen_h = 900              # default=700
program_speed = 60          # default=30
screen = pygame.display.set_mode((screen_w, screen_h))
klokke = pygame.time.Clock()

pygame.display.set_caption("Mayham game boyz")
bg = (0, 255, 255)
font = pygame.font.Font("freesansbold.ttf", 30)

peashooterRight = "src/media/peashooterR.png"
peashooterLeft = "src/media/peashooterL.png"
peashooterUp = "src/media/peashooterU.png"
peashooterDown = "src/media/peashooterD.png"
projectile_img = "src/media/shot_grey_small.png"



shots = pygame.sprite.Group()

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
