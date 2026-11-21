# Python Console Games

Two small console games written in plain Python to practice classes, loops, input validation, and writing testable code. No third-party packages are needed.

## Programs

### `Game.py` — Number guessing game

The computer picks a number from 1 to 100. You guess, and the game tells you whether your guess is too low or too high until you find it, then shows how many attempts it took. Invalid input and numbers outside 1–100 are rejected without counting as an attempt.

```bash
python3 Game.py
```

### `Duck.py` — Duck on a grid

Name a duck and move it around a coordinate grid starting at (0, 0).

```bash
python3 Duck.py
```

Commands: `forward`, `backward`, `left`, `right`, `exit`.

## Tests

The game logic is separated from the input/output code, so it can be tested without typing anything:

```bash
python3 -m unittest -v
```

## Requirements

- Python 3.8 or newer

## What I practiced

- Classes and object state
- Separating logic from user interface
- Input validation with `try`/`except`
- Unit tests with `unittest`

## Ideas for next steps

- Add a difficulty setting (different number ranges) to the guessing game.
- Add obstacles or a goal square to the duck game.
- Run the tests automatically with GitHub Actions.

## License

No license has been declared yet. Add one (for example MIT) if you want others to reuse the code.
