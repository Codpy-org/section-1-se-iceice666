# Project

## Install Requirements

In the folder named "backend", run the following command:

```sh
pip install -r requirements.txt  
```

This testing section will need **pytest, pytest-asyncio and httpx**, the others are for running the backend.

## Game Over  (10 points)

1. Go to DarkMaze/backend/tests/test_game_over.py

> The function ```game_over()``` should return ```True``` if health is equal to 0 or 666.

2. **Write the needed tests to test game_over (there should at least be 3 to test all cases)**
3. Go to DarkMaze/backend/tests/ and run ```pytest test_game_over.py```, all tests should pass.

## Integration (12 points)

1. Go to DarkMaze/backend/ and run ```python -m src.main```, running the backend
2. Go to DarkMaze/backend/tests/ and run ```pytest test_solve_maze.py```  
   **You should see two failed, both KeyError's**

> Note that all of the request functions have asserts within them. They are like unit tests, and they've passed.  
> In theory:  
> reset_request() resets the game state to the starting position.  
> move_request() moves the player one block. Valid strings include "up", "down", "left", "right".

3. **Fix reset_request() and move_request() to make the integration test work**

> The answer can be as simple as adding 4 words, two for each function.  
> printing the game_state may help.

4. Go to DarkMaze/backend/tests/ and run ```pytest test_solve_maze.py```, **You should get a result
   saying ``` 1 failed, 1 passed in <time>s ```**

## Solve Maze (8 points)

Brace for pain. **Solve the maze.**

Running ```pytest test_solve_maze.py``` should get you ```2 passed in <time>s ```**

## Scoring specifics

- Game Over
    - All test should pass using the original code.
    - Two codes with mistakes will be tested. Both codes should fail.
    - If both tasks above are successfully done, you will receive 10 points.

- Integration + Solve Maze
    - Both tests should't pass with the backend not running. (6 points)
    - test_integration should pass using a mock backend, but test_solve_maze shouldn't (6 points)
    - Both tests should pass using the real backend (8 points)  
