from classes import *
import config as cn


def engine():

    board = GameBoard()


    """
    * Main loop
    """
    game_loop = 0
    running = True
    shootTiming = 0
    game_over_timer = 0

    while running:
        # takes keypress input
        for event in pygame.event.get():
            # window X is pressed
            if event.type == pygame.QUIT:
                running = False

            
            if event.type == pygame.MOUSEBUTTONUP: #MOUSE POSITION
                mousePos = pygame.mouse.get_pos()
                board.click_tile(mousePos)
                if game_loop == 0:
                    game_loop = 1

        if game_loop == 0:
            screen.fill((0,0,0))
            #INSIDE OF THE GAME LOOP
            screen.blit(title_screen, (0, 0))
            pygame.display.flip()

    
       
        if cn.health < 1:
            game_loop = 2

        if game_loop == 1:
            # Fills screen with bg color

            #bg = pygame.image.load(backgroundImage1)
            
            screen.fill((0,0,0))
            #INSIDE OF THE GAME LOOP
            screen.blit(backgroundImage, (0, 0))

            """
            Updates and draws the sprites from the sprite groups. 
            """
        
            for DaPlants in plants:
                if DaPlants.updatesSinceShot == 60:
                    DaPlants.shoot()
            if shootTiming % 30 == 0:
                board.newLevel()
                board.enemySpawns()
                
            board.mouseImage()

            for sprites in [plants, shots, enemies,cursorGroup]:
                sprites.update()
                sprites.draw(screen)
            

            board.writeMoney()

            # Writes score and score nr
            # Draws all the above on to the screen
            pygame.display.flip()

        if game_loop == 2:
            txt = "GAME OVER"

            cn.health = cn.startHealth

            game_over_txt = game_over_font.render(txt, True, (255, 50, 50))

            textRect1 = game_over_txt.get_rect()
            textRect1.center = (screen_w/2,screen_h/2)
            screen.blit(game_over_txt, textRect1)

            pygame.display.flip()
            game_over_timer += 1
            if game_over_timer > 200:
                game_over_timer = 0
                game_loop = 0

        shootTiming += 1
        # Limits program speed
        klokke.tick(program_speed)
        