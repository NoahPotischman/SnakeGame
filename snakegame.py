import pygame
import random

# initialize Pygame
pygame.init()

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# set up the screen
size = (900, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

# set up the snake
snake_block_size = 30
snake_speed = 10
x1 = 450
y1 = 450
x1_change = 0
y1_change = 0
snake_List = []
Length_of_snake = 1

# set up the food
foodx = round(random.randrange(0, 870, 30))
foody = round(random.randrange(0, 870, 30))

# define functions
def snake(snake_block_size, snake_List):
    for i in range(1, len(snake_List)):
        pygame.draw.rect(screen, GREEN, [snake_List[i][0], snake_List[i][1], snake_block_size, snake_block_size])
    pygame.draw.rect(screen, WHITE, [snake_List[-1][0], snake_List[-1][1], snake_block_size, snake_block_size])

def message(msg, color):
    font_style = pygame.font.SysFont(None, 50)
    rendered_message = font_style.render(msg, True, color)
    screen.blit(rendered_message, [size[0]/3, size[1]/3])

# game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block_size
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block_size
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block_size
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block_size
                x1_change = 0

    # check for collision with walls or snake's body
    if x1 >= size[0] or x1 < 0 or y1 >= size[1] or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [foodx, foody, snake_block_size, snake_block_size])

    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)

    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for x in snake_List[:-1]:
        if x == snake_Head:
            game_over = True

    snake(snake_block_size, snake_List)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, 870, 30))
        foody = round(random.randrange(0, 870, 30))
        Length_of_snake += 1
        snake_Head = [x1, y1]
        snake_List.insert(0, snake_Head)

    clock.tick(snake_speed)

# quit Pygame
pygame.quit()