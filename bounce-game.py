import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball Game")

# Define colors
background_color = (255, 255, 255)
ball_color = (0, 0, 255)

# Set up the ball
ball_size = 20
ball_x = random.randrange(ball_size, screen_width - ball_size)
ball_y = random.randrange(ball_size, screen_height - ball_size)
ball_x_speed = random.randrange(-5, 5)
ball_y_speed = random.randrange(-5, 5)

# Define functions
def draw_ball(ball_x, ball_y, ball_size):
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_size)

# Set up the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the ball
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Bounce the ball off the walls
    if ball_x >= screen_width - ball_size or ball_x < ball_size:
        ball_x_speed = -ball_x_speed
    if ball_y >= screen_height - ball_size or ball_y < ball_size:
        ball_y_speed = -ball_y_speed

    # Draw the screen
    screen.fill(background_color)
    draw_ball(ball_x, ball_y, ball_size)
    pygame.display.update()

# Quit Pygame
pygame.quit()
