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

def handle_events(player1, player2):
    """
    Handle Pygame events, including player input.
    :param player: Player object to update based on input
    :return: False if the game should quit, True otherwise
    """
    # TODO: Loop through Pygame events
    # Handle QUIT event
    # Handle KEYDOWN events to change player direction

    directionChange_1 = [0,0]
    directionChange_2 = [0,0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                directionChange_1 = [0,-1]

            elif event.key ==pygame.K_s:
                directionChange_1 = [0,1]

            elif event.key == pygame.K_a:
                directionChange_1 = [-1,0]

            elif event.key == pygame.K_d:
                directionChange_1 = [1,0]

            elif event.key == pygame.K_UP:
                directionChange_2 = [0,-1]

            elif event.key ==pygame.K_DOWN:
                directionChange_2 = [0,1]

            elif event.key == pygame.K_LEFT:
                directionChange_2 = [-1,0]

            elif event.key == pygame.K_RIGHT:
                directionChange_2 = [1,0]
    
    player1.change_direction(directionChange_1)
    player2.change_direction(directionChange_2)

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

    isCollision = game_board.is_collision(player.position[0], player.position[1], player.playerID)

    return isCollision

def draw_game(screen, game_board, player1, player2):
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


    game_board.draw(screen,)

    player1.draw(screen)

    player2.draw(screen)

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

    GAMEBOARD_WIDTH = 80
    GAMEBOARD_HEIGHT = 40

    PLAYER_1_X_POS = int(GAMEBOARD_WIDTH/3)
    PLAYER_1_COLOR = (255,0,0)
    PLAYER_1_DEFAULT_DIRECTION = [1,0]

    PLAYER_2_X_POS = int((2 * GAMEBOARD_WIDTH)/3)
    PLAYER_2_COLOR = (0,0,255)
    PLAYER_2_DEFAULT_DIRECTION = [-1,0]

    PLAYER_Y_POS = int(GAMEBOARD_HEIGHT / 2)

    player1 = Player(PLAYER_1_X_POS, PLAYER_Y_POS, PLAYER_1_COLOR, 1, PLAYER_1_DEFAULT_DIRECTION)
    player2 = Player(PLAYER_2_X_POS, PLAYER_Y_POS, PLAYER_2_COLOR, 2, PLAYER_2_DEFAULT_DIRECTION)

    gameboard = GameBoard(GAMEBOARD_WIDTH, GAMEBOARD_HEIGHT)

    screen = initialize_game()

    running = True
    GameOver = False
    GameOver2 = False
    while running and not (GameOver or GameOver2):
        running = handle_events(player1, player2)

        GameOver = update_game_state(player1, gameboard)

        GameOver2 = update_game_state(player2, gameboard)

        if(not (GameOver or GameOver2)):
            draw_game(screen, gameboard, player1, player2)

        time.sleep(0.1)

main()
