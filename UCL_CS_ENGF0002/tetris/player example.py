from board import Direction, Rotation, Action
from random import Random


class Player:
    def choose_action(self, board):
        raise NotImplementedError


class RandomPlayer(Player):

    def __init__(self, seed=None):
        self.random = Random(seed)

    def choose_action(self, board):
        if self.random.random() > 0.97:
            # 3% chance we'll discard or drop a bomb
            move = self.random.choice([
                Action.Discard,
                Action.Bomb])
        else:
            # 97% chance we'll make a normal move
            move = self.random.choice([
                Direction.Left,
                Direction.Right,
                Direction.Down,
                Rotation.Anticlockwise,
                Rotation.Clockwise,
            ])
        return move


class MyPlayer(Player):
    def __init__(self, seed=None):
        self.random = Random(seed)

    shape_to_rotation = {"red": 2, "green": 2, "cyan": 2, "blue": 4, "orange": 4, "magenta": 4, "yellow": 1}

    def move_to_target(self, board, t_pos, t_rot):
        moves = []
        horizontal = 0
        r = 0
        landed = False

        while not landed and r < t_rot:
            moves.append(Rotation.Clockwise)
            landed = board.rotate(Rotation.Clockwise)
            r += 1
        if board.falling is not None:
            # then locate the bottom-left cell of the block
            bottom_left_cell = (10, 0)
            for cell in board.falling.cells:
                if cell[1] == board.falling.bottom and cell[0] < bottom_left_cell[0]:
                    bottom_left_cell = cell
            # calculate how many horizontal and vertical movements is required
            horizontal = t_pos[0] - bottom_left_cell[0]  # positive values = move right; negative = left

        # move the block horizontally
        while not landed and horizontal != 0 and board.falling.left >= 0 and board.falling.right <= 9:
            if horizontal < 0:
                horizontal += 1
                moves.append(Direction.Left)
                landed = board.move(Direction.Left)
            elif horizontal > 0:
                horizontal -= 1
                moves.append(Direction.Right)
                landed = board.move(Direction.Right)

        # move down
        if not landed:
            landed = board.move(Direction.Drop)
            moves.append(Direction.Drop)

        return moves

    def calculate_well_bonus(self, board, heights, starting_from= 0):
        # calculates the difference in blocks to the optimal 'I' well situation
        num_empty_column = 0
        empty = 0
        filled_cells = 0
        # check if there is only one empty column. If more than one or no empty column, skip the whole calculation
        for x in range(10):
            if heights[x] == starting_from:
                num_empty_column += 1
                if num_empty_column == 1:
                    empty = x
                else:
                    return 0
        if num_empty_column == 0:
            return 0
        # check if the bottom 4 lines of all other columns are filled, the more cells filled, the higher the bonus
        # check the columns on the left-hand-side of the well
        for x1 in range(empty):
            for y1 in range(20 + starting_from, 24 + starting_from):
                if (x1, y1) in board.cells:
                    filled_cells += 1
        # check the columns on the right-hand-side of the well
        for x2 in range(empty+1, 10):
            for y2 in range(20 + starting_from, 24 + starting_from):
                if (x2, y2) in board.cells:
                    filled_cells += 1
        # note that max #filled_cells = 4 * 9 = 36
        return filled_cells * 1

    def score_board(self, board, previous_board_count):
        # check for holes
        holes = 0
        all_holes = []
        for (x, y) in board.cells:
            for next_row in range(y + 1, board.height):
                if (x, next_row) not in board.cells and (x, next_row) not in all_holes:
                    holes += 1
                    all_holes.append((x, next_row))

        # check max and total in height of columns that is higher than a certain threshold
        max_height = 0
        sum_height = 0
        heights = []
        for x in range(board.width):
            this_column_height = 0
            for y in range(board.height):
                if (x, y) in board.cells:
                    height = board.height - y
                    if height > this_column_height:
                        this_column_height = height
            heights.append(this_column_height)
            if max_height < this_column_height:
                max_height = this_column_height
            if this_column_height > 10:
                sum_height += 1

        # bumpiness
        bumpiness = 0
        for x in range(len(heights) - 1):
            bumpiness += abs(heights[x] - heights[x + 1])

        # lines cleared
        rows_eliminated = (previous_board_count + 4 - len(board.cells)) / 10
        # line_bonus or penalty depending on how many rows are eliminated in different circumstances
        line_bonus = 0
        if rows_eliminated == 4:
            line_bonus = 20000
        elif rows_eliminated in [1, 2, 3]:
            if max_height <= 21:  # magic number
                line_bonus = -50
            else:
                line_bonus = 10

        # calculate a well_bonus for the 'I' well layout when the current situation is safe
        well_bonus = 0
        if max_height <= 12:
            well_bonus = self.calculate_well_bonus(board, heights)
            if not well_bonus:
                well_bonus = self.calculate_well_bonus(board, heights, 1)
        # calculate final score
        final_score = line_bonus * 1.25 + \
                      well_bonus - \
                      (
                              1.5 ** (max_height - 7) +
                              36 ** holes +
                              bumpiness * 4
                      )
        return final_score, holes

    def choose_landing_points(self, board):
        landing_points = []
        width = board.width
        height = board.height

        # checking for columns that have no cells on it, again we don't consider sliding the blocks horizontally.
        for x in range(width):
            empty_column = 1
            for y in range(height):
                if (x, y) in board.cells:
                    # the cell above the first filled cell we encounter is the landing position for this x.
                    (landing_points.append((x, y - 1)))
                    # indicate that this x is not empty.
                    empty_column = 0
                    # do not check further down.
                    break
            if empty_column:
                # no filled cells in this x, then additionally set the bottom cell as landing position.
                landing_points.append((x, height - 1))

        return landing_points

    def move_and_score(self, board, x, y, rotation, previous_board_count):
        moves = self.move_to_target(board, (x, y), rotation)
        score, holes = self.score_board(board, previous_board_count)
        return moves, score, holes

    def second_step_search(self, sandbox, last_is_discard, landing_points_provided):
        highest_score = -1000000
        if sandbox.falling is not None:
            max_rot = self.shape_to_rotation[sandbox.falling.color]
            if last_is_discard:
                landing_points = landing_points_provided
            else:
                landing_points = self.choose_landing_points(sandbox)
            for j in range(len(landing_points)):
                (x, y) = (landing_points[j][0], landing_points[j][1])
                for rotation in range(max_rot):
                    next_sandbox = sandbox.clone()
                    (moves, score, _) = self.move_and_score(next_sandbox, x, y,
                                                            rotation, len(sandbox.cells))
                    if (j == 0 and rotation == 0) or score > highest_score:
                        highest_score = score
        return highest_score

    def choose_action(self, board):
        highest_score = -1000000  # the higher, the better
        best_moves = [Direction.Drop]
        best_move_holes = 0

        max_rot = self.shape_to_rotation[board.falling.color]
        landing_points = self.choose_landing_points(board)

        for i in range(len(landing_points)):
            (x, y) = (landing_points[i][0], landing_points[i][1])
            for r in range(max_rot):
                sandbox = board.clone()
                (moves, score, holes) = self.move_and_score(sandbox, x, y, r, len(board.cells))

                next_highest_score = self.second_step_search(sandbox, 0, None)
                score += next_highest_score
                if (i == 0 and r == 0) or score > highest_score:
                    highest_score = score
                    best_moves = moves
                    best_move_holes = holes
        if best_move_holes >= 2 and board.discards_remaining > 0:
            best_moves = [Action.Discard]
        return best_moves


# SelectedPlayer = RandomPlayer
SelectedPlayer = MyPlayer
