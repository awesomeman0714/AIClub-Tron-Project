import pygame
import time

from player import Player
from game_board import GameBoard

def initialize_game():
    """
    Initialize Pygame and create the game window.
    :return: Pygame screen object
    """
    # TODO: Initialize Pygame
    # Create and return a Pygame screen object

    pygame.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tron")

    screen.fill((255,255,255))

    return screen

def handle_events(player):
    """
    Handle Pygame events, including player input.
    :param player: Player object to update based on input
    :return: False if the game should quit, True otherwise
    """
    # TODO: Loop through Pygame events
    # Handle QUIT event
    # Handle KEYDOWN events to change player direction

    directionChange = [0,0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                directionChange = [0,-1]

            elif event.key ==pygame.K_s:
                directionChange = [0,1]

            elif event.key == pygame.K_a:
                directionChange = [-1,0]

            elif event.key == pygame.K_d:
                directionChange = [1,0]
    
    player.change_direction(directionChange)

    return True

def update_game_state(player, game_board):
    """
    Update the game state, including player movement and collision detection.
    :param player: Player object to update
    :param game_board: GameBoard object to check collisions against
    :return: False if the game is over (collision), True otherwise
    """
    # TODO: Move the player
    # Check for collisions with game_board
    # Update game_board with new player position

    player.move()

    isCollision = game_board.is_collision(player.position[0], player.position[1])

    return isCollision

def draw_game(screen, game_board, player):
    """
    Draw the current game state.
    :param screen: Pygame screen object to draw on
    :param game_board: GameBoard object to draw
    :param player: Player object to draw
    """
    # TODO: Clear the screen
    # Draw the game board
    # Draw the player
    # Update the display


    game_board.draw(screen)

    player.draw(screen)

    pygame.display.flip()

def main():
    """
    Main game loop.
    """
    # TODO: Initialize the game
    # Create game objects (game_board, player)
    # Run the game loop:
    #   - Handle events
    #   - Update game state
    #   - Draw game
    #   - Control game speed

    PLAYER_X_POS = 5
    PLAYER_Y_POS = 5
    PLAYER_COLOR = (255,0,0)

    player = Player(PLAYER_X_POS, PLAYER_Y_POS, PLAYER_COLOR)


    GAMEBOARD_WIDTH = 30
    GAMEBOARD_HEIGHT = 40

    gameboard = GameBoard(GAMEBOARD_WIDTH, GAMEBOARD_HEIGHT)

    screen = initialize_game()

    running = True
    GameOver = False
    while running and not GameOver:
        running = handle_events(player)

        GameOver = update_game_state(player, gameboard)

        if(not GameOver):
            draw_game(screen, gameboard, player)

        time.sleep(0.1)

main()
