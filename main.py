from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if (keys[K_UP] or keys[K_W])and self.rect.y > 5:
            self.rect.x -= self.speed
        if (keys[K_DOWN] or keys[K_S]) and self.rect.x < win_height - 80:
            self.rect.x += self.speed

back = (200,255,255)
win_height = 500
win_width = 600
window = display.set_mode((win_width,win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
    display.update()
    clock.tick(FPS)


    