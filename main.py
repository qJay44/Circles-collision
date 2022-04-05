import pygame
import numpy as np

pygame.init()

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Circle collision')


class Circle:
    ACCELERATION_X = 0
    ACCELERATION_Y = 400
    DELTA_TIME = 1 / 75

    def __init__(self, x, y, velocity, radius, color, circle_id):
        self.x = x
        self.y = y
        self.velocityX = velocity[0]
        self.velocityY = velocity[1]
        self.velocity = self.velocityX ** 2 + self.velocityY ** 2
        self.radius = radius
        self.color = color
        self.circle_id = circle_id

    def drawCircle(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius)

        # Circle movement calculations
        self.velocityX += self.ACCELERATION_X * self.DELTA_TIME
        self.velocityY += self.ACCELERATION_Y * self.DELTA_TIME

        self.x += self.velocityX * self.DELTA_TIME
        self.y += self.velocityY * self.DELTA_TIME

        # Collision handler
        isBorderX = self.x + self.radius >= WIDTH or self.x - self.radius <= 0 
        isBorderY = self.y + self.radius >= HEIGHT or self.y - self.radius <= 0

        if isBorderX: self.velocityX *= -1
        if isBorderY: self.velocityY *= -1
    
    def collisionHandler(self):
        for c in circles:
            if not c.circle_id == self.circle_id:
                dx = c.x - self.x
                dy = c.y - self.y
                distance = np.sqrt(dx ** 2 + dy ** 2)


        
velocity1 = (200, 300)
velocity2 = (400, 100)

circle1 = Circle(WIDTH / 2, HEIGHT / 2, velocity1, 40, 'orange', 1)
circle2 = Circle(WIDTH / 2, HEIGHT / 2, velocity2, 20, 'cyan', 2)

circles = [circle1, circle2]


def main():
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(75)
        WIN.fill('black')

        # quit pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        circle1.drawCircle()
        circle2.drawCircle()
        
        pygame.display.update()
        
    pygame.quit()
    

if __name__ == '__main__':
    main()

