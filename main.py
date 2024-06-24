import time
import keyboard
from random import choice
from typing import List, Tuple

class board:
    def __init__(self, boardlen: int = 20, boardheight: int = 10, deafultstart: List[tuple[int, int]] = [(4, 5), (5, 5)],
                  deafultapple: Tuple[int, int] = (6, 6)) -> None:
        self.boardsize: List[int, int] = [boardlen, boardheight]

        self.snake_direction: int = 1
        self.apple_location: Tuple[int, int] = deafultapple
        self.snake_points: List[Tuple[int, int]] = deafultstart

    def generate_board(self) -> str:
        board: str = "\n"

        for column in range(self.boardsize[1]):
            for row in range(self.boardsize[0]):
                if (column, row) == self.apple_location:
                    board += "O"
                elif (column, row) in self.snake_points:
                    board += "X"
                else:
                    board += "_"
            board += "\n"
        
        return board
    
    def spawn_apple(self) -> None:
        randomlist: List[Tuple[int, int]] = []

        for x in range(self.boardsize[1]):
            for y in range(self.boardsize[0]):
                if (x, y) not in self.snake_points:
                    randomlist.append((x, y))
        
        self.apple_location = choice(randomlist)
    
    def move(self, direction: int) -> None:
        snake_head: Tuple[int, int] = self.snake_points[-1]

        if direction == 0:
            newpos: Tuple[int, int] = (snake_head[0], snake_head[1]+1)
        elif direction == 1:
            newpos: Tuple[int, int] = (snake_head[0]+1, snake_head[1])
        elif direction == 2:
            newpos: Tuple[int, int] = (snake_head[0], snake_head[1]-1)
        elif direction == 3:
            newpos: Tuple[int, int] = (snake_head[0]-1, snake_head[1])
        else:
            raise ValueError
        
        self.snake_direction = direction
        
        if newpos != self.apple_location:
            self.snake_points.pop(0)
        else:
            self.spawn_apple()
        
        if newpos in self.snake_points or newpos[0] > self.boardsize[1] or newpos[1] > self.boardsize[0] or newpos[0] < 0 or newpos[1] < 0:
            print("You SUCK")
            exit()

        self.snake_points.append(newpos)


snake: board = board()
imputbuffer: int = 4

timebetweenframes: int = 1

reset_time = time.time()
print(snake.generate_board())

def keycheck() -> None:
    global imputbuffer
    if keyboard.is_pressed('w'):
        imputbuffer = 3
    if keyboard.is_pressed('a'):
        imputbuffer = 2
    if keyboard.is_pressed('s'):
        imputbuffer = 1
    if keyboard.is_pressed('d'):
        imputbuffer = 0

while True:
    keycheck()

    if time.time() - reset_time >= timebetweenframes:
        if imputbuffer != 4:
            snake.move(imputbuffer)
            imputbuffer = 4
        else:
            snake.move(snake.snake_direction)

        print(snake.generate_board())
        reset_time = time.time()
