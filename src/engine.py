from classes import *

def engine():

    board = GameBoard()
    board.placePlant("d2")

    """ 
    enemies.add(Enemy(v2(0,270+45), 0))
    enemies.add(Enemy(v2(0,360+45), 0))
    enemies.add(Enemy(v2(0,450+45), 0))
    enemies.add(Enemy(v2(0,540+45), 0))
    enemies.add(Enemy(v2((270+45, 0)),1))
    enemies.add(Enemy(v2((360+45, 0)),1))
    enemies.add(Enemy(v2((450+45, 0)),1))
    enemies.add(Enemy(v2((540+45, 0)),1))
    enemies.add(Enemy(v2(900,270+45), 2))
    enemies.add(Enemy(v2(900,360+45), 2))
    enemies.add(Enemy(v2(900,450+45), 2))
    enemies.add(Enemy(v2(900,540+45), 2))
    enemies.add(Enemy(v2((360+45, 900)),3))
    enemies.add(Enemy(v2((270+45, 900)),3))
    enemies.add(Enemy(v2((450+45, 900)),3))
    enemies.add(Enemy(v2((540+45, 900)),3))
    """


    """
    * Main loop
    """
    game_loop = True
    running = True
    shootTiming = 0

    while running:
        # takes keypress input
        for event in pygame.event.get():
            # window X is pressed
            if event.type == pygame.QUIT:
                running = False

            
            if event.type == pygame.MOUSEBUTTONUP: #MOUSE POSITION
                mousePos = pygame.mouse.get_pos()
                board.click_tile(mousePos)

        keys = pygame.key.get_pressed()

        if game_loop:
            # Fills screen with bg color

            bg = pygame.image.load("src/media/gridPlaceholderNumerated.png")
            screen.fill((0,0,0))
            #INSIDE OF THE GAME LOOP
            screen.blit(bg, (0, 0))

            """
            Updates and draws the sprites from the sprite groups. 
            """
        
            for DaPlants in plants:
                if DaPlants.updatesSinceShot == 60:
                    DaPlants.shoot()
            if shootTiming % 30 == 0:
                board.newLevel()
                board.enemySpawns()
                

            for sprites in [plants, shots, enemies]:
                sprites.update()
                sprites.draw(screen)

            pygame.display.flip()

        shootTiming += 1
        # Limits program speed
        klokke.tick(program_speed)