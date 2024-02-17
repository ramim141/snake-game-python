import pygame
import time
import random

pygame.init()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (41, 240, 26)
red = (201, 18, 18)
yellow = (239, 250, 32)

# Set display dimensions
dis_width = 600
dis_height = 400

# Initialize display and set caption
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake game")

clock = pygame.time.Clock()

# Set snake block size and speed
snake_block = 10
snake_speed = 10

# Define font styles
font_style = pygame.font.SysFont("calibri", 25)
score_font = pygame.font.SysFont("comicsans", 34)

def my_score(score):
    """Display the player's score on the screen."""
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def message(msg, color):
    """Display a message on the screen."""
    mssg = font_style.render(msg, True, color)
    dis.blit(mssg, [0, dis_height / 2])

def my_snake(snake_block, snake_list):
    """Draw the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def main_game():
    """Main game loop."""
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_snake = 1

    # Initial position of the food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            # Display game over message
            dis.fill(white)
            message("You lost! Press P to play again or Q to quit", red)
            my_score(length_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        main_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        # Check if snake hits boundaries
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        # Draw food
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_snake:
            del snake_list[0]

        # Draw snake
        my_snake(snake_block, snake_list)
        my_score(length_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

main_game()
