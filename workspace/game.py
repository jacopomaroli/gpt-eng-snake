from dataclasses import dataclass
import random

@dataclass
class Position:
    x: int
    y: int

class Snake:
    def __init__(self, position):
        self.body = [position]
        self.direction = "right"

    @property
    def head_position(self):
        return self.body[-1]

    def move(self):
        if self.direction == "up":
            new_head = Position(self.head_position.x, self.head_position.y - 1)
        elif self.direction == "down":
            new_head = Position(self.head_position.x, self.head_position.y + 1)
        elif self.direction == "left":
            new_head = Position(self.head_position.x - 1, self.head_position.y)
        elif self.direction == "right":
            new_head = Position(self.head_position.x + 1, self.head_position.y)
        self.body.append(new_head)

    def grow(self):
        self.body.insert(0, Position(-1, -1))

class Food:
    def __init__(self):
        self.position = None

    def place(self):
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        self.position = Position(x, y)

class Player:
    def __init__(self):
        self.score = 0
        self.snake = Snake(Position(10, 10))

    def move(self, direction):
        if direction == "up" and self.snake.direction != "down":
            self.snake.direction = "up"
        elif direction == "down" and self.snake.direction != "up":
            self.snake.direction = "down"
        elif direction == "left" and self.snake.direction != "right":
            self.snake.direction = "left"
        elif direction == "right" and self.snake.direction != "left":
            self.snake.direction = "right"

class Game:
    def __init__(self):
        self.players = []
        self.snakes = []
        self.food = []
        self.winner = None

    def start(self):
        self.players = [Player(), Player()]
        self.snakes = [player.snake for player in self.players]
        self.food = [Food()]

    def update(self):
        for snake in self.snakes:
            snake.move()
            if snake.head_position.x < 0 or snake.head_position.x > 19 or snake.head_position.y < 0 or snake.head_position.y > 19:
                self.snakes.remove(snake)
            elif len(snake.body) > 1 and snake.head_position in snake.body[:-1]:
                self.snakes.remove(snake)
            else:
                for food in self.food:
                    if snake.head_position == food.position:
                        snake.grow()
                        self.players[self.snakes.index(snake)].score += 1
                        self.food.remove(food)
                        self.food.append(Food())

        if len(self.snakes) == 1:
            self.winner = self.players[self.snakes.index(self.snakes[0])]

    def end(self):
        pass
