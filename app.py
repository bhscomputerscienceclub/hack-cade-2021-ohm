import pygame
import random
import pygame.freetype
import irctest as irc
import time

fruitx = 500
fruity = 500
WIDTH = 800
HEIGHT = 600
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake 2.0")
STAT_FONT = pygame.font.Font(None, 32)
background_surface = pygame.Surface((WIDTH, HEIGHT))
background_surface.fill((30, 30, 30))
game_over = False
hit = False
player1won = False
player2won = False
player = 1


def quit_func():
    pygame.quit()
    if irc.irc is not None:
        irc.irc.disconnect()
    exit()


def start_pos():
    if player == 2:
        return irc.start_pos()
    x1 = 40
    y1 = 140
    x2 = WIDTH - 40
    y2 = HEIGHT - 140
    print(f"Width: {WIN.get_width()} Height {WIN.get_height()}")

    irc.set_start_pos(x1,y1,x2,y2)
    return x1, y1, x2, y2


def spawn_fruit():
    global fruity, fruitx
    if player == 2:
        fruitx, fruity = irc.spawn_fruit()
        return
    fruitx = random.randrange(0, WIDTH, 20)
    fruity = random.randrange(0, HEIGHT, 20)
    irc.set_fruit(fruitx, fruity)


class snake:
    def __init__(self, start_x, start_y, player):
        self.direction = 0  # 0 is not moving 1 is left 2 is right 3 is up 4 is down
        self.body = []
        self.player = player
        self.body.append([start_x, start_y])

    def draw(self):
        for square_coords in self.body:
            if self.player == 1:
                pygame.draw.rect(
                    WIN,
                    (0, 255, 0),
                    pygame.Rect(square_coords[0], square_coords[1], 20, 20),
                )
            else:
                pygame.draw.rect(
                    WIN,
                    (0, 255, 255),
                    pygame.Rect(square_coords[0], square_coords[1], 20, 20),
                )
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
        global game_over, player2won, player1won
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
        global game_over, player2won, player1won
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
            last = self.body[-1]
            if len(self.body) < 2:
                if self.direction == 1:
                    self.body.append([last[0] + 20, last[1]])
                elif self.direction == 2:
                    self.body.append([self.body[0][0] - 20, self.body[0][1]])
                elif self.direction == 3:
                    self.body.append([self.body[0][0], self.body[0][1] - 20])
                elif self.direction == 4:
                    self.body.append([self.body[0][0], self.body[0][1] + 20])
            else:
                x_dif = self.body[-2][0] - last[0]
                y_dif = self.body[-2][1] - last[1]
                self.body.append([last[0] - x_dif, last[1] - y_dif])
            spawn_fruit()
        self.hit()


def main():
    global code, done, input_code, join
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color("lightskyblue3")
    color_active = pygame.Color("dodgerblue2")
    button = pygame.Rect(100, 350, 150, 50)
    color = color_inactive
    active = False
    input_code = ""
    done = False
    join = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit_func()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                    if button.collidepoint(event.pos):
                        WIN.fill((30, 30, 30))
                        code = random.randint(0, 999999)
                        text = STAT_FONT.render(f"Join code: {code}", True, color)
                        clicked = False
                        while True:
                            WIN.blit(text, (input_box.x + 5, input_box.y - 25))
                            pygame.display.update()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    done = True
                                    clicked = True
                                    break
                            if clicked:
                                break
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        join = True
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        input_code = input_code[:-1]
                    else:
                        input_code += event.unicode
        WIN.fill((30, 30, 30))
        pygame.draw.rect(WIN, [255, 255, 255], button)
        txt_surface = STAT_FONT.render(input_code, True, color)
        txt_surface2 = STAT_FONT.render("Enter Code:", True, color)
        txt_surface3 = STAT_FONT.render("Create Game", True, (0, 0, 0))
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        WIN.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        WIN.blit(txt_surface2, (input_box.x + 5, input_box.y - 25))
        WIN.blit(txt_surface3, (button.x + 5, button.y + 10))
        pygame.draw.rect(WIN, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    clock = pygame.time.Clock()
    global code, join, input_code
    main()
    finalcode = 1
    if join is True and input_code is not None:
        finalcode = input_code
    elif code is not None:
        finalcode = code
    else:
        print("something very wrong")
        quit()

    irc.init(finalcode)
    time.sleep(1)
    if irc.twoppl():
        player = 2
    while not irc.twoppl():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_func()
        WIN.fill((30, 30, 30))
        txt_surface = STAT_FONT.render("Waiting...", True, (255, 255, 255))
        WIN.blit(txt_surface, (250, 200))
        pygame.display.update()
        clock.tick(5)
    print(0)
    spawn_fruit()
    print("A")
    x1, y1, x2, y2 = start_pos()
    print(x1, y1, x2, y2)
    print(fruitx, fruity)
    player1 = snake(x1, y1, 1)
    player2 = snake(x2, y2, 2)
    while not game_over:
        clock = pygame.time.Clock()
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
                    quit()

        irc.senddir(player1.direction)
        player2.direction = irc.actions[-1]
        player1.update()
        player2.update()
        WIN.blit(background_surface, (0, 0))
        player1.draw()
        player2.draw()
        pygame.display.update()


text_str = ""
if player1won is True:
    text_str = "You Win!"
elif player1won is False:
    text_str = "Game Over!"

while True:
    button = pygame.Rect(300, 350, 150, 50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_func()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit_func()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                quit_func()
    txt_surface = STAT_FONT.render(text_str, True, (255, 255, 255))
    txt_surface1 = STAT_FONT.render("Quit", True, (255, 255, 255))
    WIN.blit(txt_surface, (300, 250))
    pygame.draw.rect(WIN, [0, 0, 0], button)
    WIN.blit(txt_surface1, (button.x + 5, button.y + 5))
    pygame.display.update()
