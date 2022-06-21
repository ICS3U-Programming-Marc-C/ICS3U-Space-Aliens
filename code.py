#!/usr/bin/env python3
# Created by Marc Coffi
# Created in June 2022
# Space Aliens Game on PyBadge

# import constant file
import constants
import stage
import ugame
import time
import random

# Defining the splash scene
def splash_scene():
    
    # Get sound ready 
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    
     
    # Defining the image banks
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
  
    # Setting the image background and pixel size
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    
    
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white


    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white


    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white


    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white
    
    # create stage for the background
    game = stage.Stage(ugame.display, constants.FPS)

    # Setting the layers of all sprites
    game.layers = [background]
    
    # Rendering the background
    game.render_block()
    
    # Infinite loop
    while True:
        # Wait 2 seconds
        time.sleep(2.0)
        menu_scene()
        
# Defining game main function
def menu_scene():
    
    # Defining the image banks
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
  
  # Setting the image background and pixel size
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    
    # Add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
    
    
    # create stage for the background
    game = stage.Stage(ugame.display, constants.FPS)

    # Setting the layers of all sprites
    game.layers = text + [background]
    
    # Rendering the background
    game.render_block()
    
    # looping the scene
    while True:
        # get user response from pressing buttons and change the x and y axis
        keys = ugame.buttons.get_pressed()
        
        # Start Button
        if keys & ugame.K_START != 0:
            game_scene()
        
        # render game
        game.tick()

def game_scene():
    
    # Defining the image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprite = stage.Bank.from_bmp16("space_aliens.bmp")

    # Buttons to keep the state information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    
    # importing sound file 
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # set background image
    background = stage.Grid(image_bank_background, constants.SCREEN_X, constants.SCREEN_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)
            
    # Setting sprites images
    ship = stage.Sprite(image_bank_sprite, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    alien = stage.Sprite(image_bank_sprite, 9, int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2), 16)
    
    # create stage for the background
    game = stage.Stage(ugame.display, constants.FPS)
    
    # set layers for all sprites
    game.layers = [ship] + [alien] + [background]
    game.render_block()

    # looping the scene
    while True:
        # get user response from pressing buttons and change the x and y axis
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_O != 0:
            # check the state of button a
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
                
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
                
            else:
                a_button = constants.button_state["button_up"]   
        # B Button
        if keys & ugame.K_X != 0:
            pass

        # Start Button
        if keys & ugame.K_START != 0:
            pass

        # Select Button
        if keys & ugame.K_SELECT != 0:
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


        # if button a is pressed play the sound
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # render game
        game.render_sprites([alien] + [ship])
        game.tick()

if __name__ == "__main__":
    splash_scene()
