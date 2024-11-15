import pygame

class Player:


    def __init__(self, x, y, color, playerID, StartDirection, screen, gridSize, ai):
        """
        Initialize the player.
        :param x: Initial x-coordinate
        :param y: Initial y-coordinate
        :param color: Color of the player's trail
        """
        # TODO: Set initial position, color, direction (e.g., [1, 0] for right)
        # Initialize an empty list for the player's trail
        self.GRID_SIZE = gridSize
        self.screen = screen

        self.position = [x,y]
        self.color = color
        self.direction = StartDirection

        self.playerID = playerID

        self.ai = ai

    def move(self):
        """
        Move the player based on their current direction.
        """
        # TODO: Update the player's position based on their direction
        # Add the new position to the trail

        new_direction = self.ai.get_direction()

        #self.change_direction(new_direction)

        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]

    def change_direction(self, direction):
        """
        Change the player's direction.
        :param direction: New direction as a list [dx, dy]
        """
        # TODO: Update the player's direction
        # Ensure the new direction is not opposite to the current direction

        if(self.direction[0] * direction[0] + self.direction[1] * direction[1] == 0):
            self.direction = direction
        

    def draw(self):
        """
        Draw the player and their trail on the screen.
        :param screen: Pygame screen object to draw on
        """
        # TODO: Draw the player's current position and their entire trail

        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.position[0] * self.GRID_SIZE,
                                                        self.position[1] * self.GRID_SIZE,
                                                        self.GRID_SIZE,
                                                        self.GRID_SIZE))