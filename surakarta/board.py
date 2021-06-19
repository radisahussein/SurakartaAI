import pygame
from .constants import BLACK,ROWS,RED,SQUARE_SIZE,COLS,WHITE, GREY
from .piece import Piece

class Board:

    def __init__(self):
        self.board=[]
        self.red_left = self.white_left = 12
        self.create_board()

    def draw_squares(self,win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win,GREY,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))

    def move(self,piece,row,col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col],self.board[piece.row][piece.col]
        piece.move(row,col)

    def get_piece(self,row,col):
        return self.board[row][col]
    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row < 2:
                    self.board[row].append(Piece(row,col,WHITE))
                elif row > 3:
                    self.board[row].append(Piece(row,col,RED))
                
                else:
                    self.board[row].append(0)


    def draw(self,win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
    
    def remove(self,pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1
    
    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        
        return None
    
    # def get_valid_moves(self,piece):

    def _horizontal_left(self, start, stop, step, color, left):
        moves = {}
        return moves

    


    #RULES:
    " - Can move to an unoccupied space horizontally / vertically / diagonally"
    " - Capture by moving around any of the loops on the board until an opponent's piece is reached which is captured"
    " - All spaces between the start of the move and the piece being captured must be empty"
    " - No limit on the number of empty spaces or loops that a piece can travel across during the capture move"
    " - If more than 1 opponent piece is in a row during capture move, a player can capture all the pieces until there is a break in the row"

    
