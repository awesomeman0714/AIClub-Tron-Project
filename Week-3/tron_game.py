import pygame

from player import Player
from game_board import GameBoard

def initialize_game(WIDTH, HEIGHT):
    """
    Initialize Pygame and create the game window.
    :return: Pygame screen object
    """
    # TODO: Initialize Pygame
    # Create and return a Pygame screen object

    pygame.init()

    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tron")

    screen.fill((255,255,255))

    return screen

def pauseTillClose():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
    return True


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

            match event.key:
                case pygame.K_w:
                    directionChange_1 = [0,-1]

                case pygame.K_s:
                    directionChange_1 = [0,1]

                case pygame.K_a:
                    directionChange_1 = [-1,0]

                case pygame.K_d:
                    directionChange_1 = [1,0]

                case pygame.K_UP:
                    directionChange_2 = [0,-1]

                case pygame.K_DOWN:
                    directionChange_2 = [0,1]

                case pygame.K_LEFT:
                    directionChange_2 = [-1,0]

                case pygame.K_RIGHT:
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

def displayWinner(screen, GameOverP1, GameOverP2, width, height):

    font = pygame.font.Font('freesansbold.ttf', 48)
 
    text = 0
    if(GameOverP1):
        text = font.render('Blue Player Wins!', True, (0,0,255), (255,255,255))
    elif(GameOverP2):
        text = font.render('Red Player Wins', True, (255,0,0), (255,255,255))
    
    
    textRect = text.get_rect()
    
    textRect.center = (width // 2, height // 2)

    return text, textRect

def updateWinnerWindow(window, text, textRect):
    
    window.blit(text, textRect)

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

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

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

    screen = initialize_game(WINDOW_WIDTH, WINDOW_HEIGHT)

    running = True
    GameOverP1 = False
    GameOverP2 = False

    while running and not (GameOverP1 or GameOverP2):
        running = handle_events(player1, player2)

        GameOverP1 = update_game_state(player1, gameboard)

        GameOverP2 = update_game_state(player2, gameboard)

        if(not (GameOverP1 or GameOverP2)):
            draw_game(screen, gameboard, player1, player2)

        pygame.time.delay(100)

    text, textRect = displayWinner(screen, GameOverP1, GameOverP2, WINDOW_WIDTH, WINDOW_HEIGHT)

    while running:
        running = pauseTillClose()

        updateWinnerWindow(screen, text, textRect)

main()
