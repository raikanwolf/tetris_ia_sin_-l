import pygame
import sys
from game import Game
from colors import Colors
from agente import Agente

def initialize():
    pygame.init()
    screen = pygame.display.set_mode((500, 620))
    pygame.display.set_caption("Python Tetris")
    clock = pygame.time.Clock()
    return screen, clock

def handle_key_events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            if not game.game_over:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_right()
                elif event.key == pygame.K_DOWN:
                    game.move_down()
                    game.update_score(0, 1)
                elif event.key == pygame.K_UP:
                    game.rotate()

def main():
    screen, clock = initialize()

    title_font = pygame.font.Font(None, 40)
    score_surface = title_font.render("Score", True, Colors.white)
    next_surface = title_font.render("Next", True, Colors.white)
    game_over_surface = title_font.render("GAME OVER", True, Colors.white)

    score_rect = pygame.Rect(320, 55, 170, 60)
    next_rect = pygame.Rect(320, 215, 170, 180)

    game = Game()
    agente=Agente()

    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 200)

    while True:
        handle_key_events(game)
        agente.logica()

        if not game.game_over:
            game.move_down()

        score_value_surface = title_font.render(str(game.score), True, Colors.white)

        screen.fill(Colors.dark_blue)
        screen.blit(score_surface, (365, 20, 50, 50))
        screen.blit(next_surface, (375, 180, 50, 50))

        if game.game_over:
            screen.blit(game_over_surface, (320, 450, 50, 50))

        pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                       centery=score_rect.centery))
        pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
        game.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
