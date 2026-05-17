from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, widht, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (widht, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 155:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 155:
            self.rect.y += self.speed

back = (200, 255, 255)
win_height = 500
win_width = 600
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', randint(175, 225), randint(175, 225), 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180,0,0))

rand_speed = [-1,1]

speed_x = 3 * rand_speed[randint(0,1)]
speed_y = 3 * rand_speed[randint(0,1)]

score1 = 0
score2 = 0

score = font.render(f'Счёт: {str(score1)}/{score2}', True, (0,0,0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.y < 0 or ball.rect.y > win_height-50:
            speed_y *= -1
# Условия проигрыша 
        if ball.rect.x < 0:
            score2 += 1
            score = font.render(f'Счёт: {str(score1)}/{score2}', True, (0,0,0))
            ball.rect.x = randint(175, 255)
            ball.rect.y = randint(175, 255)
            speed_x *= rand_speed[randint(0,1)]
            speed_y *= rand_speed[randint(0,1)]
        
        if ball.rect.x > win_width-50:
            score1 += 1
            score = font.render(f'Счёт: {str(score1)}/{score2}', True, (0,0,0))
            ball.rect.x = randint(175, 255)
            ball.rect.y = randint(175, 255)
            speed_x *= rand_speed[randint(0,1)]
            speed_y *= rand_speed[randint(0,1)]

        if score1 > 5 or score2 > 5:
            finish = True
            ball.rect.x = 400
            ball.rect.y = 400
            if score1 > score2:
                window.blit(lose2, (200, 200))
            else:
                window.blit(lose1, (200, 200))
        
        window.blit(score, (250, 0))
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)