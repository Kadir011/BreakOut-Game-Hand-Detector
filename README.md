**Breakout Game with Hand Tracking**

**Overview**

This project is a modern implementation of the classic Breakout game, where players use a paddle to bounce a ball and break blocks. The game introduces a unique twist by using hand tracking via a webcam to control the paddle, leveraging computer vision with MediaPipe. The project is built with Python and follows SOLID principles, Clean Code, and Clean Architecture to ensure maintainability and scalability.

-----------------------------------------------------------------------------------------------------------------------------

**Features**

* **Hand Tracking Control:** Move the paddle using hand gestures detected via webcam.

* **Game Mechanics:**
- Break blocks to score points (10 points per block).
- 5 lives to start; lose a life if the ball falls below the paddle.
- Win by breaking all blocks ("HAS GANADO") or lose if all lives are depleted ("GAME OVER"). 

* **Pause/Resume:** Press Enter to pause or resume the game.

* **Visual Feedback:**
- Score and lives displayed in black with a white border.
- "PAUSED", "GAME OVER", and "HAS GANADO" messages in black with a white border and semi-transparent background. 

* **Performance:** Runs at 60 FPS for smooth gameplay. 

-----------------------------------------------------------------------------------------------------------------------------

**Prerequisites**

Before running the project, ensure you have the following installed:

* Python 3.9+ 
* pip (Python package manager)
* A webcam for hand tracking (e.g., USB webcam or built-in camera on laptop) 

-----------------------------------------------------------------------------------------------------------------------------

**Dependencies**

The project requires the following Python libraries:

* **pygame** (for rendering and game mechanics)
* **opencv-python** (for webcam capture)
* **mediapipe** (for hand tracking)
* **numpy** (for array operations) 

Install the dependencies using the provided **requi.txt**:

pip install -r requi.txt

-----------------------------------------------------------------------------------------------------------------------------

**Installation**

1. **Clone the repository:**

git clone https://github.com/your-username/breakout-game.git
cd breakout-game 

2. **Set Up a Virtual Environment** (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies:**

pip install -r requi.txt 

4. Ensure Images Are Available: The game uses three image assets located in the **img/** directory:

- paddle.png (the paddle image)
- ball.png (the ball image)
- brick.png (the block image)

Ensure these files are present in the **img/** directory. If you don't have these images, you can replace them with your own or modify the Renderer class to draw shapes instead.

-----------------------------------------------------------------------------------------------------------------------------

**Usage**

1. **Run the game:**

python main.py 

2. **Game Controls:**

- **Hand Tracking:** Move your hand in front of the webcam to control the paddle. The paddle follows the position of your index finger.
- **Pause/Resume:** Press Enter to pause or resume the game.
- **Exit:** Press Esc to exit the game at any time, or close the window. 

3. **Gameplay:**

- Use your hand to move the paddle and bounce the ball to break all the blocks.
- You start with 5 lives. If the ball falls below the paddle, you lose a life.
- Break all blocks to win ("HAS GANADO") or lose all lives to end the game ("GAME OVER").
- The game automatically closes after 3 seconds when "GAME OVER" or "HAS GANADO" is displayed. 

-----------------------------------------------------------------------------------------------------------------------------

**Project Structure**

The project follows **Clean Architecture** to separate concerns into layers: **Domain**, **Application**, and **Infrastructure**.

game/
├── domain/
│   ├── entities.py         # Defines game entities (Paddle, Ball, Block)
│   ├── game_logic.py       # Core game logic (collisions, scoring, lives, states)
├── application/
│   ├── game_service.py     # Coordinates interactions between domain and infrastructure
├── infrastructure/
│   ├── hand_detector.py    # Handles hand tracking with MediaPipe
│   ├── renderer.py         # Manages rendering with Pygame
├── img/
│   ├── paddle.png          # Paddle image
│   ├── ball.png            # Ball image
│   ├── brick.png           # Block image
├── main.py                 # Entry point of the application (Execute)
├── requi.txt               # Project dependencies
├── .gitignore              # Git ignore file
└── README.md               # Project documentation

**Architecture Overview**

* **Domain Layer:** Contains the core business logic and entities **(Paddle, Ball, Block)**. The **GameLogic** class manages game state, collisions, scoring, and lives.

* **Application Layer:** The **GameService** class orchestrates the game flow, connecting the domain logic with infrastructure components.

* **Infrastructure Layer:**

- **HandDetector:** Uses MediaPipe to detect hand movements and control the paddle.

- **Renderer:** Renders the game using Pygame, including the camera feed, game elements, and text.

-----------------------------------------------------------------------------------------------------------------------------

**Code Quality**

The project adheres to the following principles:

* **SOLID Principles:**

- **Single Responsibility:** Each class has a single responsibility (e.g., GameLogic for game rules, Renderer for drawing).

- **Open/Closed:** The code is extensible (e.g., new game states can be added without modifying existing classes).

- **Liskov Substitution:** Not directly applicable but ensured through proper class design.

- **Interface Segregation:** Classes only expose necessary methods.

- **Dependency Inversion:** High-level modules depend on abstractions (e.g., GameService depends on GameLogic, not concrete implementations). 

* **Clean Code:**

- Descriptive names (e.g., toggle_pause, render_text_with_border).

- Small, focused functions (e.g., move in Paddle only handles paddle movement).

- Minimal duplication (e.g., text rendering logic is centralized in Renderer).

- Clear and concise code with minimal comments where the code is self-explanatory. 

* **Clean Architecture:**

- Separation of concerns into layers (Domain, Application, Infrastructure).

- Dependency flow from infrastructure to domain, ensuring the core logic is independent of external frameworks.

-----------------------------------------------------------------------------------------------------------------------------

**Future Improvements**

* **Add Levels:** Introduce multiple levels with increasing difficulty (e.g., faster ball speed, more blocks).

* **Sound Effects:** Add sound effects for ball bounces, block breaks, and game events.

* **Customizable Controls:** Allow players to customize the hand gesture for paddle control.

* **Score Persistence:** Save high scores to a file or database.

* **UI Enhancements:** Add a start menu, settings screen, and better visual feedback.

-----------------------------------------------------------------------------------------------------------------------------

**License**

This project is licensed under the MIT License. See the  file for details.

**Acknowledgments**

* **MediaPipe:** For providing an excellent hand-tracking solution.

* **Pygame:** For providing a powerful and easy-to-use game development library.

* **OpenCV:** For webcam integration. 

-----------------------------------------------------------------------------------------------------------------------------
Last updated: April 9, 2025
-----------------------------------------------------------------------------------------------------------------------------

Developed by:

* Kadir Barquet (Python Developer) 