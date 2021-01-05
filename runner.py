import pygame
import sys
import time

import snake

snake = snake.snake()
HEIGHT = snake.FRAME_HEIGHT
WIDTH = snake.FRAME_WIDTH

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (180, 180, 180)
WHITE = (255, 255, 255)

# Create game
pygame.init()
size = width, height = 900, 600
screen = pygame.display.set_mode(size)

# Fonts
OPEN_SANS = "assets/fonts/OpenSans-Regular.ttf"
smallFont = pygame.font.Font(OPEN_SANS, 20)
mediumFont = pygame.font.Font(OPEN_SANS, 28)
largeFont = pygame.font.Font(OPEN_SANS, 40)

# Compute board size
BOARD_PADDING = 20
board_width = ((2 / 3) *width) - (BOARD_PADDING * 2)
board_height = height - (BOARD_PADDING * 2)
cell_size = int(min(board_width / WIDTH, board_height / HEIGHT))
board_origin = (BOARD_PADDING, BOARD_PADDING)

#move the snake to right initially
move = snake.RIGHT
# Show instructions initially
instructions = True

while True:

    # Check if game quit and keystrokes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and move != snake.LEFT:
                move = snake.RIGHT

            elif event.key == pygame.K_LEFT and move != snake.RIGHT:
                move = snake.LEFT

            elif event.key == pygame.K_UP and move != snake.DOWN:
                move = snake.UP

            elif event.key == pygame.K_DOWN and move != snake.UP:
                move = snake.DOWN
            
            break


    screen.fill(BLACK)

    # Show game instructions
    if instructions:
        # Title
        title = largeFont.render("Play Snake Game", True, WHITE)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Rules
        rules = [
            "I think you know how to play snakes",
            "In case you don't, learn it and come back"
        ]
        for i, rule in enumerate(rules):
            line = smallFont.render(rule, True, WHITE)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2), 150 + 30 * i)
            screen.blit(line, lineRect)

        # Play game button
        buttonRect = pygame.Rect((width / 4), (3 / 4) * height, width / 2, 50)
        buttonText = mediumFont.render("Play Game", True, BLACK)
        buttonTextRect = buttonText.get_rect()
        buttonTextRect.center = buttonRect.center
        pygame.draw.rect(screen, WHITE, buttonRect)
        screen.blit(buttonText, buttonTextRect)

        # Check if play button clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if buttonRect.collidepoint(mouse):
                instructions = False
                time.sleep(0.3)

        time.sleep(0.3)
        pygame.display.flip()
        continue

    
        # Reset button
    
    resetButton = pygame.Rect(
        (2 / 3) * width + BOARD_PADDING, (1 / 3) * height + 20,
        (width / 3) - BOARD_PADDING * 2, 50
    )
    buttonText = mediumFont.render("Reset", True, BLACK)
    buttonRect = buttonText.get_rect()
    buttonRect.center = resetButton.center
    pygame.draw.rect(screen, WHITE, resetButton)
    screen.blit(buttonText, buttonRect)

    left, _, _ = pygame.mouse.get_pressed()
    if left == 1:
        mouse = pygame.mouse.get_pos()
        # Reset game state
        if resetButton.collidepoint(mouse):
            time.sleep(0.3)
            move = snake.RIGHT
            snake.reset()

    if not snake.isGameOver():
        snake.makeMove(move)

    snakeList = snake.getSnake()
    snakeFood = snake.getFood()

    # Draw board
    cells = []
    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):

            # Draw rectangle for cell
            rect = pygame.Rect(
                board_origin[0] + j * cell_size,
                board_origin[1] + i * cell_size,
                cell_size, cell_size
            )
            pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, WHITE, rect, 1)

            # Add snake

            if [i, j] in snakeList:
                pygame.draw.rect(screen, BLACK, rect)
                # screen.blit(mine, rect)
            elif [i,j] == snakeFood:
                pygame.draw.rect(screen, RED, rect)
            row.append(rect)
        cells.append(row)

    # Display Score
    text = "SCORE"
    text = mediumFont.render(text, True, WHITE)
    textRect = text.get_rect()
    textRect.center = ((5 / 6) * width, (2 / 3) * height)
    screen.blit(text, textRect)

    text = snake.getScore()
    text = mediumFont.render(text, True, WHITE)
    textRect = text.get_rect()
    textRect.center = ((5 / 6) * width, (2 / 3) * height *1.1)
    screen.blit(text, textRect)

    time.sleep(0.05)
    pygame.display.flip()