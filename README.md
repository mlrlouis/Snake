# 🐍 Classic Snake - MVC Architecture

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Architecture](https://img.shields.io/badge/Architecture-MVC%20Pattern-green?style=for-the-badge)
![Library](https://img.shields.io/badge/Library-Turtle-orange?style=for-the-badge)

## 📖 About The Project

This is a modern implementation of the classic **Snake** arcade game, built with Python.

While Snake is a common beginner project, this repository focuses on **Clean Code principles** and **Software Architecture**. Instead of a monolithic script, the application is structured using the **Model-View-Controller (MVC)** pattern to ensure strict separation of concerns between game logic, rendering, and input handling.

### ✨ Key Features
* **Dynamic Difficulty:** The game speed automatically increases as the player's score grows.
* **Clean UI:** Custom-built grid and rendering engine using Python's `turtle` library.
* **State Management:** robust game loop handling start, pause, and game-over states.
* **Scalable Codebase:** Modular design allows for easy addition of new features (e.g., obstacles or power-ups) without breaking existing logic.

---

## 🏗️ Architecture

The project is structured to demonstrate modular software design:

```text
Snake-Game/
├── model.py      # The "Brain" (Model) - Handles coordinates, collision logic, and growth.
├── drawer.py     # The "Painter" (View) - Handles all Turtle graphics drawing commands.
├── main.py       # The "Manager" (Controller) - Ties logic and view together, handles inputs.
└── README.md
```

---

## Technical Breakdown:

* `model.py` (Model): Contains the Snake and Apple classes. This file handles pure data and logic (e.g., coordinate calculation, tail growth, collision checks). It has zero dependencies on the graphics engine.

* `drawer.py` (View): A wrapper around the turtle library. It receives data objects from the model and renders them to the screen. It knows how to draw, but not game rules.

* `main.py` (Controller): Contains the Launcher class. It manages the Game Loop, listens for user inputs (keyboard/mouse), and orchestrates the communication between the Model and the View.

---

## 🚀 How to Run

Since this project uses Python's standard library, no external installation (`pip install`) is required.

  1. Clone the repository
     ```text
     git clone [https://github.com/mlrlouis/Snake.git](https://github.com/mlrlouis/Snake.git)
     ```
  2. Navigate to the directory
     ```text
     cd snake-mvc
     ```
  3. Run the game
     ```text
     python main.py
     ```

---

## 🕹️ Controls

* Arrow Keys: Change direction (Up, Down, Left, Right).
* Mouse Click: Start the game or Restart after Game Over.

---

## 👨‍💻 Author

Louis Müller

<p align="right">(<a href="#top">back to top</a>)</p>
