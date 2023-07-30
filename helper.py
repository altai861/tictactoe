import pygame
pygame.font.init()

BLACK = (0, 0, 0)
FONT = pygame.font.SysFont(None, 80)

position_map = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}

def draw_border(WIN):
    pygame.draw.rect(WIN, BLACK, pygame.Rect(400, 100, 5, 300))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(500, 100, 5, 300))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(300, 200, 300, 5))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(300, 300, 300, 5))

def whose_turn(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != None:
                count += 1
    if count % 2 == 0:
        return "X"
    else:
        return "O"
    

def check_pos(pos, board):
    x, y = pos
    if x < 300 or x > 600 or y < 100 or y > 400:
        return False
    x = (x-300) // 100
    y = (y-100) // 100
    if board[y][x] != None:
        return False
    else:
        return True
    
def update_board(pos, board):
    x, y = pos
    x = (x-300) // 100
    y = (y-100) // 100
    board[y][x] = whose_turn(board)

def draw_values(WIN, board):
    for i in range(3):
        for j in range(3):
            if board[i][j] != None:
                x = (j * 100) + 330
                y = (i * 100) + 125
                value = FONT.render(board[i][j], True, BLACK)
                WIN.blit(value, (x, y))
                
def winner(board):
    rows, cols = len(board), len(board[0])
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0 and board[i][j] != None:
                element = board[i][j]
                if board[i][j + 1] == element and board[i][j + 2] == element:
                    return element
                elif board[i + 1][j] == element and board[i + 2][j] == element:
                    return element
                elif board[i + 1][j + 1] == element and board[i + 2][j + 2] == element:
                    return element
            elif i == 0 and j == 1 and board[i][j] != None:
                element = board[i][j]
                if board[i][j - 1] == element and board[i][j + 1] == element:
                    return element
                elif board[i + 1][j] == element and board[i + 2][j] == element:
                    return element
                
            elif i == 0 and j == 2 and board[i][j] != None:
                element = board[i][j]
                if board[i][j - 1] == element and board[i][j - 2] == element:
                    return element
                elif board[i + 1][j] == element and board[i + 2][j] == element:
                    return element
                elif board[i + 1][j - 1] == element and board[i + 2][j - 2] == element:
                    return element
            elif i == 1 and j == 0 and board[i][j] != None:
                element = board[i][j]
                if board[i][j + 1] == element and board[i][j + 2] == element:
                    return element
                elif board[i - 1][j] == element and board[i + 1][j] == element:
                    return element
                
            elif i == 1 and j == 1 and board[i][j] != None:
                element = board[i][j]
                if board[i][j - 1] == element and board[i][j + 1] == element:
                    return element
                elif board[i - 1][j] == element and board[i + 1][j] == element:
                    return element
                elif board[i - 1][j - 1] == element and board[i + 1][j + 1] == element:
                    return element
                elif board[i - 1][j + 1] == element and board[i + 1][j - 1] == element:
                    return element
            elif i == 1 and j == 2 and board[i][j] != None:
                element = board[i][j]
                if board[i][j - 1] == element and board[i][j - 2] == element:
                    return element
                elif board[i - 1][j] == element and board[i + 1][j] == element:
                    return element
               
            elif i == 2 and j == 0 and board[i][j] != None:
                element = board[i][j]
                if board[i][j + 1] == element and board[i][j + 2] == element:
                    return element
                elif board[i - 1][j] == element and board[i - 2][j] == element:
                    return element
                elif board[i - 1][j + 1] == element and board[i - 2][j + 2] == element:
                    return element
            elif i == 2 and j == 1 and board[i][j] != None:
                element = board[i][j]
                if board[i][j - 1] == element and board[i][j + 1] == element:
                    return element
                elif board[i - 1][j] == element and board[i - 2][j] == element:
                    return element
                
            elif i == 2 and j == 2 and board[i][j] != None:
                element = board[i][j]
                if board[i][j - 1] == element and board[i][j - 2] == element:
                    return element
                elif board[i - 1][j] == element and board[i - 2][j] == element:
                    return element
                elif board[i - 1][j - 1] == element and board[i - 2][j - 2] == element:
                    return element

    return None


def terminal(board):
    if winner(board) is not None:
        return True
    
    rows, cols = len(board), len(board[0])
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == None:
                return False
    
    return True


def clear_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = None