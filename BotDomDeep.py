from Bot import *

class BotDomDeep(Bot):
    def __init__(self, settings):
        super().__init__(settings)
        self.setName('DomDeep')
        self.cleaning_mode = False
        self.skip_next = False
        self.double_skip = False
        self.need_to_move_up = False
        self.need_to_move_down = False
        self.wall_mode = False
        self.move_counter = 0

    def detect_stains(self, vision):
        """Check vision to detect stains and set cleaning mode."""
        self.cleaning_mode = any(vision[i][j] == "@" for i in range(3) for j in range(3))

    def detect_walls(self, vision, currentCell):
        """Set wall_mode if walls are detected in certain positions."""
        if (vision[2][1] == "x" or vision[1][0] == "x") and 1 < currentCell[1] < self.nrCols - 2:
            self.wall_mode = True
        elif vision[1][2] == "x" and currentCell[1] != self.nrCols - 2:
            self.wall_mode = True

    def handle_backtracking(self):
        """Handle movement back up or down when in cleaning mode."""
        if self.need_to_move_up:
            self.need_to_move_up = False
            return UP
        if self.need_to_move_down:
            self.need_to_move_down = False
            return DOWN
        return None

    def handle_cleaning(self, vision):
        """Handle movement when in cleaning mode to clean stains."""
        if self.cleaning_mode:
            if vision[0][1] == "@":
                self.need_to_move_down = True
                return UP
            if vision[2][1] == "@":
                self.need_to_move_up = True
                return DOWN
        return None

    def handle_skip_logic(self):
        """Handle skipping logic to avoid redundant moves."""
        if self.skip_next:
            self.skip_next = False
            self.double_skip = True
            return DOWN
        if self.double_skip:
            self.double_skip = False
            return DOWN
        return None

    def standard_movement(self, currentCell):
        """Define the default movement pattern based on position."""
        if currentCell[0] % 2 == 1 and currentCell[1] != self.nrCols - 2:
            return RIGHT
        elif currentCell[0] % 2 == 1 and currentCell[1] == self.nrCols - 2:
            self.skip_next = True
            return DOWN
        elif currentCell[0] % 2 == 0 and currentCell[1] != 1:
            return LEFT
        elif currentCell[0] % 2 == 0 and currentCell[1] == 1:
            self.skip_next = True
            self.move_counter += 1
            return DOWN
        return None

    def nextMove(self, currentCell, currentEnergy, vision, remainingStainCells):
        self.detect_stains(vision)
        self.detect_walls(vision, currentCell)

        # Handle backtracking if necessary
        move = self.handle_backtracking()
        if move:
            return move

        # Handle cleaning if necessary
        move = self.handle_cleaning(vision)
        if move:
            return move

        # Handle skipping logic
        move = self.handle_skip_logic()
        if move:
            return move

        # Default movement logic based on position
        if self.move_counter == 8:
            if currentCell[0] % 2 == 1 and currentCell[1] != self.nrCols - 2:
                return RIGHT
            elif currentCell[0] % 2 == 1 and currentCell[1] == self.nrCols - 2:
                return DOWN
            elif currentCell[0] % 2 == 0 and currentCell[1] != 1:
                return LEFT
            elif currentCell[0] % 2 == 0 and currentCell[1] == 1:
                return DOWN

        # Standard movement when not in wall mode
        return self.standard_movement(currentCell)
