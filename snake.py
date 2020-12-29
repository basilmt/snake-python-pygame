import random
class snake:
    def __init__(self):
        self.HEIGHT = 20
        self.WIDTH = 20

        self.UP = "UP"
        self.DOWN = "DOWN"
        self.LEFT = "LEFT"
        self.RIGHT = "RIGHT"

    def initialState(self):
        snake = [
            [6,6],[6,5],[6,4]
        ]
        return snake

    def makeMove(self, move, snake, food):
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
        for i,item in enumerate(head):
            if item == self.WIDTH and i == 0 :
                head[i] = 0
            if item == -1 and i == 0:
                head[i] = self.WIDTH
            if item == self.HEIGHT and i == 1:
                head[i] = 0
            if item == -1 and i == 1:
                head[i] = self.HEIGHT

        lost = True if head in snake else False
        if not lost:
            snake.insert(0,head)
        if food == head :
            food = self.getFood(snake)
        elif not lost:
            snake.pop()

        return snake, food, lost

    def getFood(self, snake):
        food = None
        while food is None:
            nf = [
                random.randint(0,self.HEIGHT-1),
                random.randint(0, self.WIDTH-1)
            ]
            food = nf if nf not in snake else None

        return food

    def getScore(self, snake):
        score = (len(snake) - len(self.initialState()))*5
        return str(score)