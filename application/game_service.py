import time
import pygame 
from domain.game_logic import GameLogic 
from infrastructure.hand_detector import HandDetector
from infrastructure.renderer import Renderer

# Clase para el servicio del juego
class GameService:
    def __init__(self, screen_width:int, screen_height:int):
        self.game_logic = GameLogic(screen_width, screen_height)
        self.hand_detector = HandDetector(screen_width, screen_height)
        self.renderer = Renderer(screen_width, screen_height) 
    
    def run(self):
        clock = pygame.time.Clock()
        running = True 

        while running:
            running = self._handle_events()
            self._update_game_state()
            self.renderer.render(self.game_logic, self.camera_frame, self.landmarks)
            clock.tick(60)  # Aumentamos los FPS de 30 a 60

            if (self.game_logic.game_over or self.game_logic.game_won) and \
               time.time() - self.game_logic.game_over_time > self.game_logic.game_over_duration:
                running = False 
        
        self.hand_detector.release()
        self.renderer.quit() 
    
    def _handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Presionar Enter para pausar/reanudar
                    self.game_logic.toogle_pause()
                if event.key == pygame.K_ESCAPE:
                    return False 
        return True 
    
    def _update_game_state(self):
        hand_x, _, _, self.camera_frame, self.landmarks = self.hand_detector.detect_hand() 
        if hand_x is not None:
            self.game_logic.paddle.move(int(hand_x * self.game_logic.screen_width), self.game_logic.screen_width)
        self.game_logic.update() 



