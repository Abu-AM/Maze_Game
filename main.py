class Maze:
    def __init__(self, width, height):

        self.maze = []
        self.starting_h = 0
        self.starting_w = 0

        self.create_maze(width, height)

    def create_maze(self, width, height):
        for i in range(height):
            self.maze.append([])
            for j in range(width):
                self.maze[i] += ["u"]

    def starting_spot(self):
        pass

    def __repr__(self) -> str:

        str = ""

        for line in self.maze:
            for block in line:
                str += block + " "
            str = str[:-1] + "\n"

        return str

    # def __str__(self) -> str:
    #     for line in self.maze:
    #         print(line)


if __name__ == "__main__":
    maze = Maze(50, 50)
    print(maze)
