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

     def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, piece):
        # for piece in pieces:
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

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        col = piece.col

        # moving up
        moves.update(self._check_moves(row, left))
        # moving down
        moves.update(self._check_moves(row, right))
        # moving left
        moves.update(self._check_moves(row - 1, col))
        # moving right
        moves.update(self._check_moves(row + 1, col))
        # moving up left
        moves.update(self._check_moves(row - 1, left))
        # moving up right
        moves.update(self._check_moves(row - 1, right))
        # moving down left
        moves.update(self._check_moves(row + 1, left))
        # moving down right
        moves.update(self._check_moves(row + 1, right))

        if piece.row <= 2: #check down
            moves.update(self._check_eatable_vertical(row -1, max(piece.row-6, -1), -1, piece.col, piece.color, 0))
            moves.update(self._check_eatable_vertical(row +1, min(piece.row+6, ROWS), 1, piece.col, piece.color, 0))
        else: #check up
            moves.update(self._check_eatable_vertical(row -1, max(piece.row-6, -1), -1, piece.col, piece.color, 0))
            moves.update(self._check_eatable_vertical(row +1, min(piece.row+6, ROWS), 1, piece.col, piece.color, 0))
        if piece.col <= 2: #check right
            moves.update(self._check_eatable_horizontal(col + 1, min(piece.col+6, COLS), 1, piece.row, piece.color, 0))
            moves.update(self._check_eatable_horizontal(col -1, max(piece.col-6, -1), -1, piece.row, piece.color, 0))
        else: #check left
            moves.update(self._check_eatable_horizontal(col -1, max(piece.col-6, -1), -1, piece.row, piece.color, 0))
            moves.update(self._check_eatable_horizontal(col + 1, min(piece.col+6, COLS), 1, piece.row, piece.color, 0))

        return moves

    def _check_eatable_vertical(self, start, stop, step, col, color, count):
        moves = {}
        last = []

        for r in range(start, stop, step):
            if count > 5:
                break
            if start == - 1:
                if col <= 2:
                    moves.update(self._check_eatable_horizontal(0, min(col + 6, COLS), 1, col, color, count + 1))
                else:
                    moves.update(self._check_eatable_horizontal(COLS, max(col-6,-1), -1, ROWS-col, color, count + 1))
            elif start == 6:
                if col <= 2:
                    moves.update(self._check_eatable_horizontal(0, min(col + 6, COLS), 1, ROWS-col, color, count + 1))
                else:
                    moves.update(self._check_eatable_horizontal(COLS, max(col-6,-1), -1, col, color, count + 1))
            else:
                current = self.board[r][col]
                if current != 0 and current.color != color:
                    if count > 0 and not moves:
                        moves[(r, col)] = current
                    else:
                        break
                elif current == 0:
                    last = [(r, col)]
                    print(last)
                    print(current)
                    print(moves)

                    if last:
                        if last[0][0] == ROWS - 1 and last[0][1] > 2:
                            moves.update(self._check_eatable_horizontal(COLS, max(last[0][1]-6,-1), -1, col, color, count + 1))
                        elif last[0][0] == ROWS - 1 and last[0][1] <= 2:
                            moves.update(self._check_eatable_horizontal(0, min(last[0][1]+6, COLS), 1, last[0][0] - col, color, count + 1))
                        elif last[0][0] == 0 and last[0][1] > 2:
                            moves.update(self._check_eatable_horizontal(COLS, max(last[0][1]-6,-1), -1, ROWS - col, color, count + 1))
                        elif last[0][0] == 0 and last[0][1] <= 2:
                            moves.update(self._check_eatable_horizontal(0, min(last[0][1]+6, COLS), 1, col, color, count + 1))
                elif current.color == color:
                    break

        return moves

    def _check_eatable_horizontal(self, start, stop, step, row, color, count):
        moves = {}
        last = []

        for c in range(start, stop, step):
            if count > 5:
                break
            if start == - 1:
                if row <= 2:
                    moves.update(self._check_eatable_vertical(0, min(row + 6, ROWS), 1, row, color, count + 1))
                else:
                    moves.update(self._check_eatable_vertical(ROWS, max(row - 6, -1), -1, COLS - row, color, count + 1))
            elif start == 6:
                if row <= 2:
                    moves.update(self._check_eatable_vertical(0, min(row + 6, ROWS), 1, COLS - row, color, count + 1))
                else:
                    moves.update(self._check_eatable_vertical(ROWS, max(row - 6, -1), -1, row, color, count + 1))
            else:
                current = self.board[row][c]
                if current != 0 and current.color != color:
                    if count > 0 and not moves:
                        moves[(row, c)] = current
                    else:
                        break
                elif current == 0:
                    last = [(row, c)]

                    if last:
                        if last[0][1] == COLS - 1 and last[0][0] > 2:
                            moves.update(self._check_eatable_vertical(ROWS, max(last[0][0]-6,-1), -1, row, color, count + 1))
                        elif last[0][1] == COLS - 1 and last[0][0] <= 2:
                            moves.update(self._check_eatable_vertical(0, min(last[0][0]+6,ROWS), 1, last[0][1]-row, color, count + 1))
                        elif last[0][1] == 0 and last[0][0] > 2:
                            moves.update(self._check_eatable_vertical(ROWS, max(last[0][0]-6,-1), -1, COLS - row, color, count + 1))
                        elif last[0][1] == 0 and last[0][0] <= 2:
                            moves.update(self._check_eatable_vertical(0, min(last[0][0]+6,ROWS), 1, row, color, count + 1))
        return moves

    def _check_moves(self, go_row, go_col):
        moves = {}
        valid = []

        for i in range(1):
            if go_col < 0 or go_col > 5:
                break
            if go_row < 0 or go_row > 5:
                break
            else:
                current = self.board[go_row][go_col]
                if current == 0:
                    valid = [current]
                    moves[(go_row, go_col)] = valid

        return moves


    #RULES:
    " - Can move to an unoccupied space horizontally / vertically / diagonally"
    " - Capture by moving around any of the loops on the board until an opponent's piece is reached which is captured"
    " - All spaces between the start of the move and the piece being captured must be empty"
    " - No limit on the number of empty spaces or loops that a piece can travel across during the capture move"
    " - If more than 1 opponent piece is in a row during capture move, a player can capture all the pieces until there is a break in the row"

    
