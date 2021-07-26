import pygame
import time

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization
pygame.init()
# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT-BTN_HEIGHT))
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"), (HP_WIDTH, HP_HEIGHT))
buttons_continue = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_HEIGHT))
buttons_pause = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_HEIGHT))
buttons_sound = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_HEIGHT))
buttons_muse = pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH, BTN_HEIGHT))
hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"), (BTN_WIDTH//2, BTN_HEIGHT//2))
hp_gray_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (BTN_WIDTH//2, BTN_HEIGHT//2))


# set the title
pygame.display.set_caption("My first game")


class Game:
    def __init__(self):
        # window setting
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        # hp setting
        self.hp = 7
        self.max_hp = 10

        # font setting
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        pass

    def game_run(self):
        # game loop
        run = True
        t0 = time.time()  # start time
        while run:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # draw background
            self.win.blit(background_image, (0, BTN_HEIGHT))

            # draw enemy and health bar
            self.win.blit(enemy_image, (0, 300))
            pygame.draw.rect(self.win, RED, (10, 300, HP_WIDTH//2, HP_HEIGHT//20))

            # draw menu (and buttons)
            pygame.draw.rect(self.win, BLACK, (0, 0, WIN_WIDTH, BTN_HEIGHT))
            self.win.blit(buttons_muse, ((WIN_WIDTH-BTN_WIDTH*4), 0))
            self.win.blit(buttons_sound, ((WIN_WIDTH - BTN_WIDTH * 3), 0))
            self.win.blit(buttons_continue, ((WIN_WIDTH-BTN_WIDTH*2), 0))
            self.win.blit(buttons_pause, ((WIN_WIDTH - BTN_WIDTH), 0))

            # draw hp 2 row (5 col in a row)
            count = 0
            for i in range(2):
                for j in range(-2, 3, 1):
                    if count < self.hp:
                        # remaining hp
                        self.win.blit(hp_image, ((WIN_WIDTH-BTN_WIDTH//2)/2+j*(BTN_WIDTH//2), i*(BTN_HEIGHT//2)))
                    else:
                        # lost hp
                        self.win.blit(hp_gray_image, ((WIN_WIDTH-BTN_WIDTH//2)/2+j*(BTN_WIDTH//2), i*(BTN_HEIGHT//2)))
                    count += 1

            # draw time
            time_rect_size = 60
            pygame.draw.rect(self.win, BLACK, (0, WIN_HEIGHT-self.font.get_height(), time_rect_size, BTN_HEIGHT))
            # execution time calculation
            t1 = time.time()  # now time
            clock = t1 - t0
            minute = int(clock//60)
            second = clock % 60
            second = '%02d' % second
            text_time = self.font.render(str(minute)+':'+str(second), True, WHITE)
            self.win.blit(text_time, ((time_rect_size-self.font.get_linesize()*1.38)/2, WIN_HEIGHT-self.font.get_height()))
            pygame.display.update()

        # uninitialize all the pygame module
        pygame.quit()


if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()



