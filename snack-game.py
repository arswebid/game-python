import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define colors
background_color = (255, 255, 255)
snake_color = (0, 255, 0)
food_color = (255, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Set up the snake
snake_block_size = 10
snake_speed = 15
snake_list = []
snake_length = 1
snake_x = screen_width // 2
snake_y = screen_height // 2
snake_x_change = 0
snake_y_change = 0

# Set up the food
food_block_size = 10
food_x = round(random.randrange(0, screen_width - food_block_size) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - food_block_size) / 10.0) * 10.0

# Define functions
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, snake_color, [x[0], x[1], snake_block_size, snake_block_size])

def draw_food(food_x, food_y, food_block_size):
    pygame.draw.rect(screen, food_color, [food_x, food_y, food_block_size, food_block_size])

# Set up the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block_size
                snake_x_change = 0

    # Move the snake
    snake_x += snake_x_change
    snake_y += snake_y_change
    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check if the snake has collided with the food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, screen_width - food_block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - food_block_size) / 10.0) * 10.0
        snake_length += 1

    # Check if the snake has collided with the walls
    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        game_over = True

    # Check if the snake has collided with itself
    for block in snake_list[:-1]:
        if block == snake_head:
            game_over = True

    # Draw the screen
    screen.fill(background_color)
    draw_snake(snake_block_size, snake_list)
    draw_food(food_x, food_y, food_block_size)
    pygame
    
# Update the display
pygame.display.update()

# Set the frame rate
clock.tick(snake_speed)

pygame.quit()
