import random

class snake:
    def __init__(self):
        self.FRAME_HEIGHT = 20
        self.FRAME_WIDTH = 20

        self.UP = "UP"
        self.DOWN = "DOWN"
        self.LEFT = "LEFT"
        self.RIGHT = "RIGHT"

        self.score = 0
        self.snake = self.initialState()
        self.food = self.setFood()
        self.gameOver = False

        self.scoreIncrement = 5



    def initialState(self):
        snake = [
            [6,6],[6,5],[6,4]
        ]
        return snake

    def makeMove(self, move):
        snake = self.getSnake()
        food = self.getFood()
        # Switch cases to find where to
        head = snake[0].copy()
        if move == self.UP:
            head[0] -= 1
        elif move == self.DOWN: 
            head[0] += 1
        elif move == self.RIGHT:
            head[1] +=1
        elif move == self.LEFT:
            head[1] -=1

        #case where it ran out of ground
        # this case come through the other way - classic i think
        for i,item in enumerate(head):
            if item == self.FRAME_WIDTH and i == 0 :
                head[i] = 0
            if item == -1 and i == 0:
                head[i] = self.FRAME_WIDTH
            if item == self.FRAME_HEIGHT and i == 1:
                head[i] = 0
            if item == -1 and i == 1:
                head[i] = self.FRAME_HEIGHT

        lost = True if head in snake else False
        if not lost:
            snake.insert(0,head)
        if food == head :
            food = self.setFood()
            self.setScore()
        elif not lost:
            snake.pop()

        self.snake = snake
        self.food = food
        self.gameOver = lost

        return snake, food, lost

    def setFood(self):
        snake = self.getSnake()
        food = None
        while food is None:
            nf = [
                random.randint(0,self.FRAME_HEIGHT-1),
                random.randint(0, self.FRAME_WIDTH-1)
            ]
            food = nf if nf not in snake else None

        return food

    def getScore(self):
        return str(self.score)

    def reset(self):
        self.score = 0
        self.gameOver = False
        self.snake = self.initialState()
        self.food = self.setFood()


    def isGameOver(self):
        return self.gameOver

    def getSnake(self):
        return self.snake

    def getFood(self):
        return self.food

    def setScore(self):
        self.score += self.scoreIncrement