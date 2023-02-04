from classes import *

def engine():

    plant = Peashooter(v2(500,500))
    plants = pygame.sprite.Group()
    plants.add(plant)


    """
    * Main loop
    """
    game_loop = True
    running = True

    while running:
        # takes keypress input
        for event in pygame.event.get():
            # window X is pressed
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if game_loop:
            # Fills screen with bg color
            screen.fill(bg)
            # Gets keypressed array
            # Updates the players
            

            """
            Updates and draws the sprites from the sprite groups. 
            """
            plants.update()
            plants.draw(screen)
            plant.rotateImage()
            plant.shoot()
            shots.update()
            shots.draw(screen)

            # Writes score and score nr
            # Draws all the above on to the screen
            pygame.display.flip()

        # Limits program speed
        klokke.tick(program_speed)