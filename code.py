#!/usr/bin/env python3
# Created by Marc Coffi
# Created in June 2022
# Space Aliens Game on PyBadge

import ugame
import stage
import constants

# The game_scene function is main function of the game 
def game_scene():
    # Defining the image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Setting the image background and pixel size
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    # Defining the space ship sprite that will be displayed every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    # Stage for the background and setting frame to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    
    # Setting the layers of all sprites
    game.layers = [ship] + [background]

    # Render all sprites
    game.render_block()

    # Repeat forever game loop
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        # Moving right
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        # Moving left
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)

        # Moving up
        if keys & ugame.K_UP:
            pass
        # Moving down
        if keys & ugame.K_DOWN:
            pass

        # Update game logic

        # Redraw Sprites
        game.render_sprites([ship])
        game.tick()
        
if __name__ == "__main__":
    game_scene()
