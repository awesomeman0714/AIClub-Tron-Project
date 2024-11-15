import pygame

class GameBoard:

    def __init__(self, width, height, gridSize, screen):
        """
        Initialize the game board.
        :param width: Width of the game board in grid cells
        :param height: Height of the game board in grid cells
        """
        # TODO: Initialize a 2D list to represent the game board
        # 0 can represent empty cells, 1 for trail of player 1, 2 for trail of player 2

        self.board = [[0 for i in range(width)] for j in range(height)]
        self.GRID_SIZE = gridSize

        self.screen = screen


    def draw(self):
        """
        Draw the game board on the screen.
        :param screen: Pygame screen object to draw on
        """
        # TODO: Iterate through the 2D list and draw rectangles for each cell
        # Empty cells can be one color, trails another

        for i in range(len(self.board)): # rows
            for j in range(len(self.board[i])): # columns
                
                pygame.draw.rect(self.screen,
                                 (128,128,128), 
                                 pygame.Rect(j * self.GRID_SIZE, i * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE))
    
                pygame.draw.rect(self.screen,
                                 (50,50,50), 
                                 pygame.Rect(j * self.GRID_SIZE, i * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE),
                                 1)

    def is_collision(self, x, y):
        """
        Check if the given coordinates collide with the board boundaries or a trail.
        :param x: X-coordinate to check
        :param y: Y-coordinate to check
        :return: True if collision, False otherwise
        """
        # TODO: Check if x and y are within board boundaries
        # Also check if the cell at (x, y) is not empty (i.e., has a trail)

        if((x < len(self.board[0]) and x >= 0) and (y < len(self.board) and y >= 0)):
            if(self.board[y][x] != 0):
                return True
        
            return False
        
        else:
            return True
        
    def updateBoard(self, x, y, playerID):
        self.board[y][x] = playerID

        pygame.draw.rect(self.screen,
                                 (254 / self.board[y][x], 127, 127 * self.board[y][x]), 
                                 pygame.Rect(x * self.GRID_SIZE, y * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE))
        
        pygame.draw.rect(self.screen,
                                 (50,50,50), 
                                 pygame.Rect(x * self.GRID_SIZE, y * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE),
                                 1)
