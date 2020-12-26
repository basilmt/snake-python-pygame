import random

HEIGHT = 20
WIDTH = 20

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

def initialState():
    snake = [
        [6,6],[6,5],[6,4]
    ]
    return snake

def makeMove(move, snake, food):
    # Switch cases to find where to
    head = snake[0].copy()
    if move == UP:
        head[0] -= 1
    elif move == DOWN:
        head[0] += 1
    elif move == RIGHT:
        head[1] +=1
    elif move == LEFT:
        head[1] -=1

    #case where it ran out of ground
    for i,item in enumerate(head):
        if item == WIDTH and i == 0 :
            head[i] = 0
        if item == -1 and i == 0:
            head[i] = WIDTH
        if item == HEIGHT and i == 1:
            head[i] = 0
        if item == -1 and i == 1:
            head[i] = HEIGHT

    lost = True if head in snake else False
    if not lost:
        snake.insert(0,head)
    if food == head :
        food = getFood(snake)
    elif not lost:
        snake.pop()

    return snake, food, lost

def getFood(snake):
    food = None
    while food is None:
        nf = [
            random.randint(0,HEIGHT-1),
            random.randint(0, WIDTH-1)
        ]
        food = nf if nf not in snake else None

    return food

def getScore(snake):
    score = (len(snake) - len(initialState()))*5
    return str(score)