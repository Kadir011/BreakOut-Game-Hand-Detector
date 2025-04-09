from typing import List 
from .entities import Paddle, Ball, Block 
import time

# Clase para el juego
class GameLogic:
    def __init__(self, screen_width:int, screen_height:int, lives:int=5):
        self.screen_width = screen_width 
        self.screen_height = screen_height 
        self.paddle = Paddle(screen_width // 2 - 75, screen_height - 100, 150, 40)
        self.ball = Ball(screen_width // 2, screen_height // 2, 20, 12, 12) 
        self.blocks = self._create_blocks()
        self.score = 0
        self.lives = lives
        self.game_over = False
        self.game_won = False
        self.paused = False
        self.game_over_time = 0
        self.game_over_duration = 3  # Duración en segundos para "Game Over" o "Has Ganado" 
    
    def _create_blocks(self) -> List[Block]:
        block_rows, block_columns = 4, 8 # Matriz 4x8 de bloques 
        block_width, block_height = self.screen_width // block_columns, 50
        blocks = [] 
        for row in range(block_rows):
            for column in range(block_columns):
                blocks.append(Block(column * block_width, 
                                    row * block_height, 
                                    block_width, 
                                    block_height))
        return blocks 
    
    def toogle_pause(self):
        self.paused = not self.paused
    
    def update(self):
        if self.game_over or self.game_won or self.paused:
            return 
        
        # Movimiento de la bola 
        self.ball.x += self.ball.speed_x
        self.ball.y += self.ball.speed_y 

        # Colisiones con bordes
        if self.ball.x - self.ball.radius < 0 or self.ball.x + self.ball.radius > self.screen_width:
            self.ball.speed_x *= -1
        if self.ball.y - self.ball.radius < 0:
            self.ball.speed_y *= -1
        if self.ball.y + self.ball.radius > self.screen_height:
            self.lives -= 1
            if self.lives <= 0:
                self.game_over = True
                self.game_over_time = time.time()
            else:
                self.reset_ball() 

        # Colisión con el paddle
        if (self.paddle.x < self.ball.x < self.paddle.x + self.paddle.width and
            self.ball.y + self.ball.radius >= self.paddle.y):
            self.ball.speed_y *= -1 
        
        # Colisión con bloques
        for block in self.blocks[:]:
            if block.x <= self.ball.x <= block.x + block.width and block.y <= self.ball.y <= block.y + block.height:
                self.blocks.remove(block)
                self.ball.speed_y *= -1
                self.score += 10
                break 
        
        # Verificar si se ganaron todos los bloques
        if not self.blocks:
            self.game_won = True
            self.game_over_time = time.time()
    
    def reset_ball(self):
        self.ball.x = self.screen_width // 2
        self.ball.y = self.screen_height // 2
        self.ball.speed_x, self.ball.speed_y = 12, 12 

