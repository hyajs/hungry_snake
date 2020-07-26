import pygame
import sys
import random

# 全局设置
width = 600
height = 480


class Snake(object):
#   snake
#   属性: 1.初始化蛇的长度
#   2.蛇的头，方向
    def __init__(self):
        self.body = []
        self.direction = pygame.K_RIGHT

        for x in range(3):
            self.eat()

    def eat(self):
        x,y = (0,0)
        if self.body:
            x, y = (self.body[0].x,self.body[0].y)
        node = pygame.Rect(x,y,12,12)
        if self.direction == pygame.K_LEFT:
            node.x -= 12
        if self.direction == pygame.K_RIGHT:
            node.x += 12
        if self.direction == pygame.K_UP:
            node.y -= 12
        if self.direction == pygame.K_DOWN:
            node.y += 12
        self.body.insert(0,node)


    def delnode(self):
        self.body.pop()

    def dead(self):
#       检查是否死亡
        if self.body[0].x not in range(width):
            return True
        if self.body[0].y not in range(height):
            return True
        if self.body[0] in self.body[1:]:
            return True
        return False

    def move(self):
        self.eat()
        self.delnode()

    def change_direction(self, key_enter):
        LR = [pygame.K_LEFT,pygame.K_RIGHT]
        UD = [pygame.K_UP,pygame.K_DOWN]
        if key_enter in LR + UD:
            if (key_enter in LR) and (self.direction in LR):
                return
            if (key_enter in UD) and (self.direction in UD):
                return
            self.direction = key_enter


class Food(object):
    def __init__(self):
        self.rect = pygame.Rect(-12,0,12,12)

    def remove(self):
        self.rect.x = -12

    def put_food(self):
        if self.rect.x == -12:
            self.rect.x = random.randint(0,50)*12
            self.rect.y = random.randint(0,40)*12


def main():
    pygame.init()
    screen_size = (width,height)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('hungry_snake')
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                snake.change_direction(event.key)
                if snake.dead():
                    print('u dead!')
                    return main()

        screen.fill((255,255,255))

        if not snake.dead():
            snake.move()
        for rect in snake.body:
            pygame.draw.rect(screen,(20,220,39), rect, 0)

        if food.rect == snake.body[0]:
            food.remove()
            snake.eat()

        food.put_food()
        pygame.draw.rect(screen,(136,0,24), food.rect)
        pygame.display.update()
        clock.tick(10)



main()