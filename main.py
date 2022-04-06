import random
import pygame as pg
import numpy as np

pg.init()

WIDTH, HEIGHT = 1300, 900
WIN = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 75
pg.display.set_caption('Circles collision')


class Circle:
    DELTA_TIME = 1 / FPS
    ACCELERATION = 9.81 * FPS

    def __init__(self, x, y, velocity, radius, color, circle_id):
        self.x = x
        self.y = y
        self.velocityX = velocity[0]
        self.velocityY = velocity[1]
        self.radius = radius
        self.color = color
        self.circle_id = circle_id

    def drawCircle(self):
        pg.draw.circle(WIN, self.color, (self.x, self.y), self.radius)

        # Circle movement calculations
        self.velocityY += self.ACCELERATION * self.DELTA_TIME
        self.x += self.velocityX * self.DELTA_TIME
        self.y += self.velocityY * self.DELTA_TIME

        # Bodrder collision handler
        isBorderLeft = self.x - self.radius <= 0 
        isBorderRight = self.x + self.radius >= WIDTH 
        isBorderTop = self.y - self.radius <= 0
        isBorderBot = self.y + self.radius >= HEIGHT

        if isBorderLeft: 
            self.x = self.radius
            self.velocityX *= -1
        if isBorderRight:
            self.x = WIDTH - self.radius
            self.velocityX *= -1
        if isBorderTop:
            self.y = self.radius
            self.velocityY *= -1
        if isBorderBot:
            self.y = HEIGHT - self.radius
            self.velocityY *= -1

        # Collision responce
        for other in circles:
            if not other.circle_id == self.circle_id:
                dx = other.x - self.x
                dy = other.y - self.y
                distance = np.sqrt(dx ** 2 + dy ** 2)
                isOverlap = distance <= other.radius + self.radius

                if isOverlap:
                    tangentDistance = distance - other.radius
                    overlapDistance = self.radius - tangentDistance

                    self.x -= overlapDistance
                    self.y -= overlapDistance

                    self.velocityX, self.velocityY = -self.velocityY, self.velocityX
                    other.velocityX, other.velocityY = -other.velocityY, other.velocityX

        self.velocityX *= 0.9994
        self.velocityY *= 0.9994


circles = []
circle_id = 0


def createCircle(mouse=False):
    global circles, circle_id

    radius = random.randint(10, 100)
    if mouse:
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]
    else:
        x = random.randint(radius, WIDTH - radius)
        y = random.randint(radius, HEIGHT - radius)

    x_vel = y_vel = random.randint(100, 800) / radius
    velocity = (x_vel, y_vel)

    r = lambda: random.randint(0, 255)
    color = (r(), r(), r(), 1)

    circle = Circle(x, y, velocity, radius, color, circle_id)
    circles.append(circle)
    circle_id += 1


def main():
    global circles, circle_id
    run = True
    clock = pg.time.Clock()

    for _ in range(5):
        createCircle()
    
    while run:
        clock.tick(FPS)
        WIN.fill('#161a1d')

        # event handler
        for event in pg.event.get():
            # quit pygame
            if event.type == pg.QUIT:
                run = False
            # mouse button pressed
            elif event.type == pg.MOUSEBUTTONDOWN: 
                # spawn new circle
                if pg.mouse.get_pressed()[0]:
                    createCircle(True)
            # keyboard key pressed
            elif event.type == pg.KEYDOWN:
                # restert screen
                if pg.key.get_pressed()[pg.K_r]:
                    WIN.fill('#161a1d')
                    circles.clear()
                    circle_id = 0
                    for _ in range(5):
                        createCircle()

        # drawing created circles
        for circle in circles:
            circle.drawCircle()
        
        pg.display.update()
        
    pg.quit()
    

if __name__ == '__main__':
    main()

