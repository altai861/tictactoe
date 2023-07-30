# Example file showing a circle moving on screen
import pygame
from helper import draw_border, check_pos, update_board, draw_values, terminal, winner, clear_board
pygame.font.init()

FONT = pygame.font.SysFont(None, 80)


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

BOARD = pygame.Rect(300, 100, 300, 300)


WHITE = (255, 255,255)
FPS = 60


def draw_window():
    WIN.fill((0, 0, 0))
    pygame.draw.rect(WIN, WHITE, BOARD)
    draw_border(WIN) 
    draw_values(WIN, board)
    pygame.display.update()

def draw_winner(text):
    draw_text = FONT.render(f"{text} wins!", True, WHITE)
    WIN.blit(draw_text, (350, 25))

    pygame.display.update()
    pygame.time.delay(5000)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if check_pos(event.pos, board):
                    update_board(event.pos, board)
        draw_window()
        if terminal(board):
            won = winner(board)
            if won == None:
                print("Tie")
            else:
                print(f"Winner is {won}")
                draw_winner(won)
                clear_board(board)
                break
    main()

if __name__ == "__main__":
    main()