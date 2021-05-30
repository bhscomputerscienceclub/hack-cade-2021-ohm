import pygame
import random
import pygame.freetype
import irctest as irc

fruitx = 500
fruity = 500
WIDTH = 800
HEIGHT = 800
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake 2.0")
STAT_FONT = pygame.freetype.SysFont("Sans", 50)
background_surface = pygame.Surface((WIDTH, HEIGHT))
background_surface.fill((0, 0, 0))
game_over = False
hit = False
player1won = False
player2won = False
player = 1


def start_pos():
    x1 = random.randrange(0, WIDTH, 20)
    y1 = random.randrange(0, HEIGHT, 20)
    x2 = random.randrange(0, WIDTH, 20)
    y2 = random.randrange(0, HEIGHT, 20)
    if x1 is not x2 and y1 is not y2:
        return x1, y1, x2, y2
    while x1 == x2 or y1 == y2:
        x1 = random.randrange(0, WIDTH, 20)
        y1 = random.randrange(0, HEIGHT, 20)
        x2 = random.randrange(0, WIDTH, 20)
        y2 = random.randrange(0, HEIGHT, 20)
    return x1, y1, x2, y2


def spawn_fruit():
    global fruity, fruitx
    fruitx = random.randrange(0, WIDTH, 20)
    fruity = random.randrange(0, HEIGHT, 20)


class snake:
    def __init__(self, start_x, start_y, player):
        self.direction = 0 # 0 is not moving 1 is left 2 is right 3 is up 4 is down
        self.body = []
        self.player = player
        self.body.append([start_x, start_y])

    def draw(self):
        for square_coords in self.body:
            if self.player == 1:
                pygame.draw.rect(WIN, (0, 255, 0), pygame.Rect(square_coords[0], square_coords[1], 20, 20))
            else:
                pygame.draw.rect(WIN, (0, 255, 255), pygame.Rect(square_coords[0], square_coords[1], 20, 20))
        else:
            pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(fruitx, fruity, 20, 20))

    def left(self):
        self.direction = 1

    def right(self):
        self.direction = 2

    def up(self):
        self.direction = 3

    def down(self):
        self.direction = 4

    def hit(self):
        global game_over, hit, player2won, player1won
        head = pygame.Rect(self.body[0][0], self.body[0][1], 20, 20)
        for square in self.body:
            if square is not self.body[0]:
                part = pygame.Rect(square[0], square[1], 20, 20)
                if head.colliderect(part):
                    if self.player == 1:
                        player2won = True
                    else:
                        player1won = True
                    game_over = True
        for square in player2.body:
            part = pygame.Rect(square[0], square[1], 20, 20)
            if square is not player2.body[0]:
                if head.colliderect(part):
                    if self.player == 1:
                        player2won = True
                    else:
                        player1won = True
                    game_over = True
            elif square is not self.body[0]:
                if head.colliderect(part):
                    if self.player == 1:
                        player2won = False
                    else:
                        player1won = False
                    game_over = True

    def update(self):
        global game_over, hit, player2won, player1won
        count = len(self.body) - 1
        for square in self.body:
            if count == 0:
                if self.direction == 1:
                    self.body[count][0] += -20
                    if self.body[count][0] < 0:
                        if self.player == 1:
                            player2won = True
                        else:
                            player1won = True
                        game_over = True
                if self.direction == 2:
                    self.body[count][0] += 20
                    if self.body[count][0] > WIDTH:
                        if self.player == 1:
                            player2won = True
                        else:
                            player1won = True
                        game_over = True
                if self.direction == 3:
                    self.body[count][1] += -20
                    if self.body[count][1] < 0:
                        if self.player == 1:
                            player2won = True
                        else:
                            player1won = True
                        game_over = True
                if self.direction == 4:
                    self.body[count][1] += 20
                    if self.body[count][1] > HEIGHT:
                        if self.player == 1:
                            player2won = True
                        else:
                            player1won = True
                        game_over = True
            else:
                x = self.body[count - 1][0]
                y = self.body[count - 1][1]
                self.body[count] = [x, y]
            count -= 1
        if pygame.Rect(self.body[0][0], self.body[0][1], 20, 20).colliderect(
            pygame.Rect(fruitx, fruity, 20, 20)
        ):
            if self.direction == 1:
                self.body.insert(0, [self.body[0][0] - 20, self.body[0][1]])
            elif self.direction == 2:
                self.body.insert(0, [self.body[0][0] + 20, self.body[0][1]])
            elif self.direction == 3:
                self.body.insert(0, [self.body[0][0], self.body[0][1] + 20])
            elif self.direction == 4:
                self.body.insert(0, [self.body[0][0], self.body[0][1] - 20])
            spawn_fruit()
        self.hit()


if __name__ == "__main__":
    irc.init(123) 
    x1, y1, x2, y2 = start_pos()
    player1 = snake(x1, y1, 1)
    player2 = snake(x2, y2, 2)
    while not game_over:
        clock = pygame.time.Clock()
        clock.tick(9)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1.left()
                elif event.key == pygame.K_RIGHT:
                    player1.right()
                elif event.key == pygame.K_UP:
                    player1.up()
                elif event.key == pygame.K_DOWN:
                    player1.down()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        print(player1.direction)
        irc.send(player1.direction)
        player2.direction = irc.actions[-1]
        player1.update()
        player2.update()
        WIN.blit(background_surface, (0, 0))
        player1.draw()
        player2.draw()
        pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    text_str = ""
    if player == 1 and player1won is True:
        text_str = "You Win!"
    elif player == 1 and player1won is False:
        text_str = "Game Over!"
    elif player == 2 and player2won is True:
        text_str = "You Win!"
    elif player == 2 and player2won is False:
        text_str = "Game Over!"
    text_rect = STAT_FONT.get_rect(text_str)
    text_rect.center = WIN.get_rect().center
    STAT_FONT.render_to(WIN, text_rect.topleft, text_str, (100, 200, 255))
    pygame.display.update()
