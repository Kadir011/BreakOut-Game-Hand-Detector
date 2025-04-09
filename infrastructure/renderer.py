import pygame 
import numpy as np 
from domain.game_logic import GameLogic

# Clase para el renderizador
class Renderer:
    def __init__(self, width: int, height: int):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Breakout Game")
        self.font = pygame.font.SysFont(None, 36)
        self.width = width
        self.height = height
        self.paddle_image = pygame.image.load('img/paddle.png')
        self.paddle_image = pygame.transform.scale(self.paddle_image, (150, 40))
        self.ball_image = pygame.image.load('img/ball.png')
        self.ball_image = pygame.transform.scale(self.ball_image, (40, 40))
        self.block_image = pygame.image.load('img/brick.png')
        self.block_image = pygame.transform.scale(self.block_image, (width // 8, 50))

    def _render_text_with_border(self, text: str, x: int, y: int) -> None:
        text_surface = self.font.render(text, True, (0, 0, 0))
        border_surface = self.font.render(text, True, (255, 255, 255))
        text_surface_rect = text_surface.get_rect(topleft=(x, y))
        background_surface = pygame.Surface((text_surface.get_width() + 20, text_surface.get_height() + 20), pygame.SRCALPHA)
        background_surface.fill((255, 255, 255, 128))
        self.screen.blit(background_surface, (x - 10, y - 10))
        self.screen.blit(border_surface, (x - 1, y - 1))
        self.screen.blit(border_surface, (x + 1, y + 1))
        self.screen.blit(border_surface, (x - 1, y + 1))
        self.screen.blit(border_surface, (x + 1, y - 1))
        self.screen.blit(text_surface, (x, y))
        return text_surface_rect

    def render(self, game_logic: GameLogic, camera_frame: np.ndarray | None, landmarks: list | None):
        if camera_frame is not None:
            camera_surface = pygame.surfarray.make_surface(camera_frame)
            self.screen.blit(camera_surface, (0, 0))

        if landmarks:
            for landmark in landmarks:
                x = int(landmark.x * self.width)
                y = int(landmark.y * self.height)
                pygame.draw.circle(self.screen, (255, 0, 0), (x, y), 5)

            connections = [
                (0, 1), (1, 2), (2, 3), (3, 4),
                (0, 5), (5, 6), (6, 7), (7, 8),
                (0, 9), (9, 10), (10, 11), (11, 12),
                (0, 13), (13, 14), (14, 15), (15, 16),
                (0, 17), (17, 18), (18, 19), (19, 20),
                (5, 9), (9, 13), (13, 17)
            ]
            for start, end in connections:
                start_x = int(landmarks[start].x * self.width)
                start_y = int(landmarks[start].y * self.height)
                end_x = int(landmarks[end].x * self.width)
                end_y = int(landmarks[end].y * self.height)
                pygame.draw.line(self.screen, (0, 255, 0), (start_x, start_y), (end_x, end_y), 2)

        if not game_logic.game_over and not game_logic.game_won:
            self.screen.blit(self.paddle_image, (game_logic.paddle.x, game_logic.paddle.y))
            self.screen.blit(self.ball_image, (game_logic.ball.x - game_logic.ball.radius, game_logic.ball.y - game_logic.ball.radius))
            for block in game_logic.blocks:
                self.screen.blit(self.block_image, (block.x, block.y))

            # Dibujar puntaje y vidas
            self._render_text_with_border(f"Score: {game_logic.score}", 10, 10)
            self._render_text_with_border(f"Lives: {game_logic.lives}", self.width - 100, 10)

            if game_logic.paused:
                pause_rect = self._render_text_with_border("PAUSED", self.width // 2 - 50, self.height // 2)
        elif game_logic.game_over:
            self._render_text_with_border("GAME OVER", self.width // 2 - 70, self.height // 2)
        elif game_logic.game_won:
            self._render_text_with_border("HAS GANADO", self.width // 2 - 70, self.height // 2)

        pygame.display.flip()

    def quit(self):
        pygame.quit() 








