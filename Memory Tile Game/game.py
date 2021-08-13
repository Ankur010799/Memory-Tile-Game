class MemoryGame:

    def __init__(self, size, winning_action):
        if size <= 0 or size % 2 != 0:
            raise ValueError("size should be even and greater than 0")
        self.size = size
        self.tiles = []
        self.winning_action = winning_action
        self.previous = None
        self.current = None

    def add_tiles(self, tiles):
        self.tiles.clear()
        self.tiles.extend(tiles)

    def deselect_move(self):
        self.previous = None
        self.current = None

    def select(self, row, column):
        self.previous = self.current
        self.current = self.tiles[row][column]
        self.current.show()

        if self.previous is None:
            return

        if self.previous == self.current:
            self.current.hide()
        elif self.previous.is_content_same(self.current):
            self.previous.matched()
            self.current.matched()
        else:
            self.previous.hide()
            self.current.hide()
        self.deselect_move()

        if self.is_game_over():
            self.winning_action()

    def is_game_over(self):
        for row in self.tiles:
            for tile in row:
                if not tile.is_matched:
                    return False
        return True
