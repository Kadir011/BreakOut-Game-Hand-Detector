from application.game_service import GameService

def main():
    WIDTH, HEIGTH = 800, 600
    game_service = GameService(WIDTH, HEIGTH)
    game_service.run()

if __name__ == "__main__":
    main() 

