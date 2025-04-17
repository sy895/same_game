# Same Game

A classic puzzle game implemented in Python, inspired by the original Same Game. This project features a clean graphical interface using Tkinter and a well-structured game logic.

## Concept

Click on groups of adjacent squares of the same color to remove them and score points. The bigger the group, the higher your score. When no moves are left, the game ends.

## Project Structure

same_game/ 
  ├── img/ # Contains image assets used in the GUI 
  ├── main.py # Launches the game 
  ├── modele.py # Contains game logic (model) 
  ├── vue.py # Manages the graphical interface (view) 
  ├── testercode.py # Optional test/debugging script


## Features

- Component-based architecture (Model–View separation)
- Tkinter graphical interface
- Real-time score display
- Automatic update of the board after each move
- Game-over detection

## How to Run

Make sure you have Python 3 installed.

Then run:

```bash
cd same_game
python main.py
