import pygame

from player import Player
from game_board import GameBoard
from mock_ai import MockAI

def initialize_game(WIDTH, HEIGHT):
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
    directionChange_1 = player1.direction
    directionChange_2 = player2.direction

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

def update_game(player: Player, game_board: GameBoard):
    game_board.updateBoard(player.position[0], player.position[1], player.playerID)

    player.move()

    pygame.display.flip()

def checkWinner(player1: Player, player2: Player, game_board: GameBoard):
    player1Next = [player1.position[0] + player1.direction[0], player1.position[1] + player1.direction[1]]
    player2Next = [player2.position[0] + player2.direction[0], player2.position[1] + player2.direction[1]]

    headOnCollision = player1Next == player2.position or player2Next == player1.position

    isCollision1 = game_board.is_collision(player1.position[0], player1.position[1])

    isCollision2 = game_board.is_collision(player2.position[0], player2.position[1])

    if(headOnCollision):
        return 4
    elif(isCollision1 and isCollision2):
        return 3
    elif(isCollision1):
        return 1
    elif(isCollision2):
        return 2
    
    return 0

def draw_game(game_board):
    game_board.draw()

    pygame.display.flip()

def drawPlayer(player: Player):
    player.draw()

    pygame.display.flip()

def displayWinner(screen, GameOver, width, height):

    font = pygame.font.Font('freesansbold.ttf', 48)
 
    text = 0
    if(GameOver == 1):
        text = font.render('Blue Player Wins!', True, (0,0,255), (255,255,255))
    elif(GameOver == 2):
        text = font.render('Red Player Wins', True, (255,0,0), (255,255,255))
    else:
        text = font.render("It's a Draw", True, (0,255,0), (255,255,255))
    
    
    textRect = text.get_rect()
    
    textRect.center = (width // 2, height // 2)

    return text, textRect

def updateWinnerWindow(window, text, textRect):
    
    window.blit(text, textRect)

    pygame.display.flip()



def main():

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    GAMEBOARD_WIDTH = 80
    GAMEBOARD_HEIGHT = 40

    GRID_SIZE = 10

    PLAYER_1_X_POS = int(GAMEBOARD_WIDTH/3) + 1
    PLAYER_1_COLOR = (255,0,0)
    PLAYER_1_DEFAULT_DIRECTION = [1,0]

    PLAYER_2_X_POS = int(2 * GAMEBOARD_WIDTH/3)
    PLAYER_2_COLOR = (0,0,255)
    PLAYER_2_DEFAULT_DIRECTION = [-1,0]

    PLAYER_Y_POS = int(GAMEBOARD_HEIGHT / 2)

    screen = initialize_game(WINDOW_WIDTH, WINDOW_HEIGHT)

    ai1 = MockAI()
    ai2 = MockAI()

    player1 = Player(PLAYER_1_X_POS, PLAYER_Y_POS, PLAYER_1_COLOR, 1, PLAYER_1_DEFAULT_DIRECTION, screen, GRID_SIZE, ai1)
    player2 = Player(PLAYER_2_X_POS, PLAYER_Y_POS, PLAYER_2_COLOR, 2, PLAYER_2_DEFAULT_DIRECTION, screen, GRID_SIZE, ai2)

    gameboard = GameBoard(GAMEBOARD_WIDTH, GAMEBOARD_HEIGHT, GRID_SIZE, screen)

    clock = pygame.time.Clock()

    running = True
    Gameover = 0

    draw_game(gameboard)

    while running and not Gameover:
        running = handle_events(player1, player2)
        
        update_game(player1, gameboard)
        update_game(player2, gameboard)

        Gameover = checkWinner(player1, player2, gameboard)

        if(Gameover != 4):
            drawPlayer(player1)
            drawPlayer(player2)


        clock.tick(2)

    text, textRect = displayWinner(screen, Gameover, WINDOW_WIDTH, WINDOW_HEIGHT)

    while running:
        running = pauseTillClose()

        updateWinnerWindow(screen, text, textRect)

    

if __name__ == "__main__":
    main()
