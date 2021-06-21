from .constants import RED,WHITE,SQUARE_SIZE, GREY, BOARD_POS
import pygame

class Piece:
    PADDING = 20
    OUTLINE = 2

    def __init__(self,row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + 150 + SQUARE_SIZE  // 2 
        self.y = SQUARE_SIZE * self.row + 150 + SQUARE_SIZE  // 2
    
    def draw(self,win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win,GREY,(self.x ,self.y), radius+self.OUTLINE)
        pygame.draw.circle(win,self.color,(self.x,self.y), radius)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
    
    def __repr__(self):
        return str(self.color)


# x = (100 * row) + 150 + (100 // 2)
# x - (100 // 2) = (100 * row) + 150
# x - (100//2) - 150 = 100 * row
# x - 200 = 100 * row
# x - 200 // 100 = row
# x = 100 * r + 200
#  r = (x - 200) / 100