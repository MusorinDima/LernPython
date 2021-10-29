import pygame
from snake_control import Control
from snake import Snake
from gui import Gui
pygame.init()
window = pygame.display.set_mode((441,441))
pygame.display.set_caption('Змейка')
control = Control()
snake = Snake()
gui = Gui()
var_speed = 0

while control.flag_game:
    control.control()
    window.fill(pygame.Color('Black'))
    snake.draw_snake(window)
    if var_speed % 100 == 0 and control.flag_pause:
        snake.move(control)
        snake.animation()
    var_speed += 1
    pygame.display.flip()


