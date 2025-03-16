from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, x,y, w,h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, img, x,y, w,h, speed):
        super().__init__(self)
        self.start_x = x
        self.start_y = y 

    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP]and self.rect.y > 15:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN]and self.rect.y < 400:
            self.rect.y += self.speed
        if key_pressed[K_LEFT]and self.rect.x > 15:
            self.rect.x -= self.speed  
        if key_pressed[K_RIGHT]and self.rect.x < 600:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self,cl_1, cl_2, cl_3, x, y, w, h):
        super().__init__()
        self.cl_1 = cl_1
        self.cl_2 = cl_2
        self.cl_3 = cl_3
        self.image = Surface((w,h))
        self.image.fill((cl_1, cl_2, cl_3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def start(self):
        def.rect.x = self.start_x
        def.rect.y = self.start_y


class Enemy(GameSprite):
    def update(self):
        x1 = 500
        x2 = 620
        y = 300
        self.rect.y = y
        if self.rect.x <= x1:
            self.direction = 'right'
        elif self.rect.x >= x2:
            self.direction = 'left'
        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed


hero = Player("hero.png", 100,100, 65,65, 5)
enem = Enemy("cyborg.png", 100,100, 65,65, 5)
walls = [wall_1, wall_2, wall_3, wall_4]
wall_1 = Wall(255, 255,0, 200,200, 5,400)
wall_2 = Wall(255, 255,0, 100,400, 100,5)
walls.append(wall_1)
wall_3 = Wall(255, 255,0, 300,100, 5,400)
wall_4 = Wall(255, 255,0, 200,300, 5,100)
treasure = GameSprite('treasure.png', 600, 300,65, 65, 0)

window = display.set_mode((700,500))
display.set_caption("лаберинт")
background = transform.scale(image.load("background.jpg"),(700,500))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')


game = True 
finish = False
clock = time.Clock()
FPS = 60
while game:

    for i in range(player.hp):
    heart = GameSprite('g546.png'
    h_x, 5, 20, 20, 0)
    hearts.append(heart)
    h_x+=25

    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0, 0)) 
        hero.update()
        hero.reset()  
        enem.update()
        enem.reset()
        for w in walls:
            w.reset()
        wall_2.reset() 
        wall_1.reset() 
        wall_3.reset() 
        wall_4.reset() 
        treasure.reset()
        if sprite.collide_rect(hero,treasure):
            finish = True
            money.play()
        if sprite.collide_rect(hero,enem):
            finish = True
            licl.play()
        for w in walls:
        if sprite.collide_rect(hero,w):
            player.start()   
        for h in hearts:
            h.reset   
    display.update() 
    clock.tick(FPS) 

