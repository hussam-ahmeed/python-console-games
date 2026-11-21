"""A duck that moves around a simple coordinate grid."""

# Direction name -> (change in x, change in y)
MOVES = {
    "forward": (0, 1),
    "backward": (0, -1),
    "left": (-1, 0),
    "right": (1, 0),
}


class Duck:
    """A named duck that keeps track of its position."""

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0

    @property
    def position(self):
        return (self.x, self.y)

    def move(self, direction):
        """Move one step in the given direction and return the new position.

        Raises ValueError if the direction is not one of MOVES.
        """
        if direction not in MOVES:
            raise ValueError(f"Unknown direction: {direction!r}")
        dx, dy = MOVES[direction]
        self.x += dx
        self.y += dy
        return self.position


def main():
    name = input("Enter duck name: ").strip() or "Duck"
    duck = Duck(name)
    options = ", ".join(MOVES)

    while True:
        command = input(f"Move duck ({options}) or type 'exit' to stop: ").strip().lower()
        if command == "exit":
            print("Exiting the game!")
            break
        try:
            x, y = duck.move(command)
        except ValueError:
            print("Unknown command, try again.")
        else:
            print(f"{duck.name} moved {command}. Now at ({x}, {y})")


if __name__ == "__main__":
    main()
