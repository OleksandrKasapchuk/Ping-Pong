from pygame import *

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_speed, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x , size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y +=self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
back = (200,255,255)
win_width = 600
win_height = 500
game = True
finish = False
window = display.set_mode((win_width, win_height))
window.fill(back)
clock = time.Clock()
FPS = 60

speed_x = 4
speed_y = 4

racket1 = Player("platform.png", 6, 30, 200, 39, 93)
racket2 = Player("platform.png", 6, 520, 200, 39, 93)
ball = GameSprite("ball.png", 4, 300, 200,  45, 45)

font.init()
font = font.Font(None, 35)
lose1 = font.render("Player 2 WIN", True, (0,180,0))
lose2 = font.render("Player 1 WIN", True, (0,180,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish: 
        window.fill(back)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.y > win_height-45 or ball.rect.y < 0:
            speed_y *= 1
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))
        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()
        ball.reset()
        display.update()
        clock.tick(FPS)
