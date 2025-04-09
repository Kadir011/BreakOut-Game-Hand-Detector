from dataclasses import dataclass 

# Clase para el paddle
@dataclass
class Paddle:
    x: int
    y: int
    width: int
    heigth: int 

    # Método para el movimiento del paddle (en el juego) 
    def move(self, new_x:int, screen_width:int):
        self.x = max(0, min(new_x - self.width // 2, 
                            screen_width - self.width)) 
    
# Clase para la bola
@dataclass
class Ball:
    x: int
    y: int
    radius: int 
    speed_x: int
    speed_y: int 

# Clase para los bloques
@dataclass
class Block:
    x: int
    y: int
    width: int
    height: int 








