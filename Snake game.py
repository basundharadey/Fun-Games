#design snake game

from random import randrange
class SnakeGame(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snakeHead = [0,0]
        self.snakeBody = []
        self.score = 0
        self.isEnd = False
        
        self.food = [randrange(self.width),randrange(self.height)]
        if self.food == [0,0]:
            self.food[1] = self.food[1] + 1
        
    def moveHead(self, direction):
        x,y = 0,0
        if direction == 1:
            x,y = 1,0
        elif direction == 2:
            x,y = -1,0
        elif direction == 3:
            x,y = 0,-1
        elif direction == 4:
            x,y = 0,1
        else:
            print("Invalid Option. Try again")
            return
        
        self.snakeHead[0] = self.snakeHead[0]+x    
        self.snakeHead[1] = self.snakeHead[1]+y
        
        return [x, y]
        
    def move(self, direction):
        """
        The snake is initially positioned at the top left corner (0, 0) with a length         of 1 unit.
        Move the snake. return The game's score after the move. 
        """
        prevHead = [elem for elem in self.snakeHead]
        
        dir = self.moveHead(direction)
        if len(dir) == 0:
            return
        
        if self.isGameEnd() == -1:        
            print("Game End, Start Over!")
            return self.score
        
        self.snakeBody.append(prevHead)
        
        if not self.isFoodFound(direction, prevHead):
            self.snakeBody.pop(0)
        
        
    def isFoodFound(self, direction, prevHead):
        """
        If food found, snake body grows 1 unit ahead of food
        """
        if self.snakeHead == self.food:
            print("Found Food!!!")

            self.score += 1

            self.food = [randrange(self.width),randrange(self.height)]
            
            return True
            
        return False

      
    def isGameEnd(self):
        """
        Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        # print(self.snakeHead)
        # print(self.snakeBody)
        if self.snakeHead[0] < 0 or self.snakeHead[1] < 0 or self.snakeHead[0] >= self.width or self.snakeHead[1] >= self.height or self.snakeHead in self.snakeBody:
            self.isEnd = True
            return -1
            
        
width = int(input("Enter board width: "))
height = int(input("Enter board height: "))
obj = SnakeGame(width, height)


while(not obj.isEnd):
    print("Snake Head at : " + str(obj.snakeHead))
    print("Snake Body is : " + str(obj.snakeBody))
    print("Food at : " + str(obj.food))
    direction = input("Enter your choice: 1(R) / 2(L) / 3(U) / 4(D)     ")
    param1 = obj.move(int(direction))
    print("Score : " + str(obj.score))
    print("   ")