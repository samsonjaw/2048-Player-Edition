# 2048 Game
2048 Game Implementation in Python
This Python script implements the classic 2048 game using Pygame. Players can combine tiles by moving them up, down, left, or right, with the goal to reach the 2048 tile.

# Features
Smooth gameplay using Pygame for graphics and animations.
Real-time score tracking displayed during gameplay.
Game over detection with the ability to restart the game.

# Prerequisites
Ensure these prerequisites are installed on your system:

- Python 3.x: Python 3.6 or higher is recommended. I am developing with Python 3.9.5.
- pygame
- numPy
- 
Install the required libraries using pip:

```bash
pip install pygame numpy
```

# Running the Game
1. Clone or download the repository containing the game script.
2. Run the game using Python:
```bash
python 2048.py
```
3. Game Controls
  W: Move tiles up.
  S: Move tiles down.
  A: Move tiles left.
  D: Move tiles right.
  R: Restart the game after game over.

# Game Mechanics
The game starts with two numbers (2 or 4) placed in random positions on the grid.
Use the arrow keys to slide all tiles in the chosen direction.
Tiles with the same number merge into one when they touch, doubling the number.
Each move randomly introduces a new tile of 2 or 4 into an empty spot on the grid.
The game ends when there are no possible moves left (no empty spaces and no adjacent tiles with the same value).

## Contributing
Contributions are welcome!

You can help by:

- Reporting issues
- Suggesting improvements
- Adding new features through pull requests

## License
This project is licensed under the MIT License.
