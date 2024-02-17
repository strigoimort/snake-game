import pygame
import time
import random

pygame.init()

# Set the display width and height
display_width = 800
display_height = 600

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the block size and speed
block_size = 20
snake_speed = 15

# Set the font
font = pygame.font.SysFont(None, 25)

# Initialize the display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Define the snake
def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, black, [x[0], x[1], block_size, block_size])

# Display the message
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [display_width / 6, display_height / 2])

# The main game loop
def game_loop():
    game_exit = False
    game_over = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    rand_apple_x = round(random.randrange(0, display_width - block_size) / float(block_size)) * block_size
    rand_apple_y = round(random.randrange(0, display_height - block_size) / float(block_size)) * block_size

    while not game_exit:
        while game_over:
            game_display.fill(white)
            message_to_screen("Game Over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_over = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(white)
        pygame.draw.rect(game_display, red, [rand_apple_x, rand_apple_y, block_size, block_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        snake(block_size, snake_list)

        pygame.display.update()

        if lead_x == rand_apple_x and lead_y == rand_apple_y:
            rand_apple_x = round(random.randrange(0, display_width - block_size) / float(block_size)) * block_size
            rand_apple_y = round(random.randrange(0, display_height - block_size) / float(block_size)) * block_size
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
