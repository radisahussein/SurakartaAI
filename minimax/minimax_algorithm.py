from copy import deepcopy
import pygame
from surakarta.board import Board
import random


RED = (255,0,0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game):

    
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        # print(best_move)
        return minEval, best_move

def minimax1(position,depth,max_player,game):
    
    
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        # print(best_move)
        return minEval, best_move

def randomMove(position, game):

    if position.winner() != None:
        return position.evaluate(),position

    else:
        randomMove = None
        possibleMoves = get_all_moves(position,RED,game)
        arrLen = len(possibleMoves)

        randomIndex = random.randint(0,arrLen-1)
        randomMove = possibleMoves[randomIndex]
            
        return randomMove


# def simulate_move(temp_piece, move, temp_board, game, valid):
#     eaten = temp_board.get_piece(move[0],move[1])
#     if valid == 0:
#         temp_board.move(piece, piece.row, piece.col)
#     elif eaten != 0:
#         temp_board.move(piece, move[0], move[1])
#         temp_board.remove(valid)
#
#     return temp_board

def simulate_move(temp_piece, move, temp_board, game, valid):
    if valid == [0]:
        temp_board.move(temp_piece, move[0], move[1])
    elif valid != [0]:
        # print(valid)
        temp_board.remove(valid)
        temp_board.move(temp_piece, move[0], move[1])
        # temp_board.move(temp_piece, move[0], move[1])

    return temp_board

def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, valid in valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, valid)
            moves.append(new_board)

    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(100)