#!/usr/bin/env python3
# Created by Marc Coffi
# Created in June 2022
# Space Aliens Game on PyBadge

import ugame
import stage

# The game_scene function is main function of the game 
def game_scene():
    # Defining the image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Setting the image background and pixel size
    background = stage.Grid(image_bank_background, 10, 8)
    # Defining the space ship sprite that will be displayed every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)
    # Stage for the background and setting frame to 60fps
    game = stage.Stage(ugame.display, 60)
    
    # Setting the layers of all sprites
    game.layers = [ship] + [background]

    # Render all sprites, only the background for now
    game.render_block()

    # Repeat forever game loop
    while True:
        # Get user input

        # Update game logic

        # Redraw Sprites
        game.render_sprites([ship])
        game.tick()
if __name__ == "__main__":
    game_scene()
