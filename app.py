import pygame
import random
fruitx = 500
fruity = 500
WIDTH = 800
HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake 2.0")
background_surface = pygame.Surface((WIDTH, HEIGHT))
background_surface.fill((0, 0, 0))
game_over = False


def spawn_fruit():
    global fruity, fruitx
    fruitx = random.randrange(0, WIDTH, 20)
    fruity = random.randrange(0, HEIGHT, 20)


class snake:
    body = []
    direction = 0 # 0 is not moving 1 is left 2 is right 3 is up 4 is down

    def __init__(self, start_x, start_y):
        self.body.append([start_x, start_y])

    def draw(self):
        WIN.blit(background_surface, (0, 0))
        for square_coords in self.body:
            pygame.draw.rect(WIN, (0, 255, 0), pygame.Rect(square_coords[0], square_coords[1], 20, 20))
        pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(fruitx, fruity, 20, 20))

    def left(self):
        self.direction = 1

    def right(self):
        self.direction = 2

    def up(self):
        self.direction = 3

    def down(self):
        self.direction = 4

    def hit(self, head_coords):
        head = pygame.Rect(head_coords[0], head_coords[1], 20, 20)
        for square in self.body:
            if square is not self.body[0]:
                part = pygame.Rect(square[0], square[1], 20, 20)
                if head.colliderect(part):
                    global game_over
                    game_over = True

    def update(self):
        global game_over
        count = len(self.body) - 1
        for square in self.body:
            if count == 0:
                if self.direction == 1:
                    self.body[count][0] += -20
                    if self.body[count][0] < 0:
                        game_over = True
                if self.direction == 2:
                    self.body[count][0] += 20
                    if self.body[count][0] > WIDTH:
                        game_over = True
                if self.direction == 3:
                    self.body[count][1] += -20
                    if self.body[count][1] < 0:
                        game_over = True
                if self.direction == 4:
                    self.body[count][1] += 20
                    if self.body[count][1] > HEIGHT:
                        game_over = True
            else:
                x = self.body[count - 1][0]
                y = self.body[count - 1][1]
                self.body[count] = [x, y]
            count -= 1
        if pygame.Rect(self.body[0][0], self.body[0][1], 20, 20).colliderect(pygame.Rect(fruitx, fruity, 20, 20)):
            if self.direction == 1:
                self.body.insert(0, [self.body[0][0] - 20, self.body[0][1]])
            elif self.direction == 2:
                self.body.insert(0, [self.body[0][0] + 20, self.body[0][1]])
            elif self.direction == 3:
                self.body.insert(0, [self.body[0][0], self.body[0][1] + 20])
            elif self.direction == 4:
                self.body.insert(0, [self.body[0][0], self.body[0][1] - 20])
            spawn_fruit()
        self.hit(self.body[0])


player1 = snake(0, 0)
while not game_over:
    clock = pygame.time.Clock()
    clock.tick(30)
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
    player1.update()
    player1.draw()
    pygame.display.update()
