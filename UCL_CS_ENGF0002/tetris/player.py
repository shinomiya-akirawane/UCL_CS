from board import Direction, Rotation, Action, Board
from random import Random


class Player:
    def choose_action(self, board):
        raise NotImplementedError


class RandomPlayer(Player):
    def __init__(self, seed=None):
        self.random = Random(seed)


class shinomiyaPlayer(Player):
    def __init__(self, seed=None):
        self.random = Random(seed)
        self.holeNum=0
    def landingHeight(self, board, landed_y):
        ans = board.height-landed_y-1
        return ans

    def erodedPieceCellsMetric(self, board, landedcells):
        removedLines = 0
        removedBlocks = 0
        for y in range(0, board.height):
            if(board.line_full(y) == 1):
                removedLines += 1
                for x in range(0, board.width):
                    if((x, y) in landedcells):
                        removedBlocks += 1
        res =removedLines
        return res

    def boardRowTransitions(self, board):
        sum = 0
        lastX = 0
        for y in range(0, board.height):
            for x in range(0, board.width):
                if(x < 9):
                    if((lastX ^ ((x, y) in board)) == 1):
                        sum += 1
                        lastX = (x, y) in board
            lastX=0
        return sum

    def boardColTransitions(self, board):
        sum = 0
        lastY = 0
        for x in range(0, board.width):
            for y in range(0, board.height):
                if((lastY ^ ((x, y) in board)) == 1):
                    sum += 1
                    lastY = (x, y) in board
            lastY = 0
        return sum

    def boardBuriesHoles(self, board):
        sum = 0
        for x in range(0, board.width):
            colHoles = None
            for y in range(0, board.height):
                if(colHoles == None and ((x, y) in board) == 1):
                    colHoles = 0
                if(colHoles != None and ((x, y) in board) == 0):
                    colHoles += 1
            if(colHoles != None):
                sum += colHoles
        return sum

    def boardWells(self, board):
        sum_n = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55,
                 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
        sum = 0
        wellDepth = 0
        for x in range(0, board.width):
            for y in range(0, board.height):
                if(((x, y) in board) == 0):
                    if((x-1 < 0 or ((x-1, y) in board) == 1) and ((x+1 >= 10 or ((x+1, y) in board) == 1))):
                        wellDepth += 1
                else:
                    sum += sum_n[wellDepth]
                    wellDepth = 0
        return sum

    def evaluate_function_1(self, board, landed_cells,landed_y):

        erodedPieceCellsMetric = self.erodedPieceCellsMetric(
            board, landed_cells)
        grade = 2*erodedPieceCellsMetric
        if(landed_y<13):
            grade*=1000
            return grade
        return grade

    def evaluate_function_2(self, board, landed_y):
        landingHeight = self.landingHeight(board, landed_y)
        boardRowTransitions = self.boardRowTransitions(board)
        boardColTransitions = self.boardColTransitions(board)
        boardBuriesHoles = self.boardBuriesHoles(board)
        boardWells = self.boardWells(board)
        grade = -6*landingHeight - 4*boardRowTransitions - 9 * \
            boardColTransitions - 81*boardBuriesHoles - 2*boardWells
        return grade

    def priority(self, currentX, moveNum, rotateNum):
        if(currentX <= 5):
            priority = 100*moveNum+10+rotateNum
        else:
            priority = 100*moveNum+rotateNum
        return priority

    def choose_action(self, board):
        self.holeNum=0
        currentMove_action = []
        currentRotate_action = []
        best_action = []
        current_score = 0
        best_score = -99999999
        best_x = 0
        best_i = 0
        for i in range(0, 4):
            currentMove_action = []
            currentRotate_action = []
            cloneBoard = board.clone()
            j = 0
            while(j < i):
                cloneBoard.rotate(Rotation.Clockwise)
                currentRotate_action.append(Rotation.Clockwise)
                j += 1
            for x in range(0, board.width):
                cloneBoard2 = cloneBoard.clone()
                if(x < 5):
                    while(x != cloneBoard2.falling.left):
                        if(cloneBoard2.move(Direction.Left) == False):
                            currentMove_action.append(Direction.Left)
                        else:
                            break
                elif(x > 5):
                    while(x != cloneBoard2.falling.right):
                        if(cloneBoard2.move(Direction.Right) == False):
                            currentMove_action.append(Direction.Right)
                        else:
                            break
                if(cloneBoard2.falling != None):
                    landed_cells = cloneBoard2.falling.cells
                    for landed_y in range(cloneBoard2.falling.bottom, board.height):
                        for (fallingX, y) in landed_cells:
                            if((fallingX, y+1) in cloneBoard2.cells or y+1 == cloneBoard2.height):
                                break
                        else:
                            landed_cells = {(cellsX, cellsY+1)
                                            for (cellsX, cellsY) in landed_cells}
                            continue
                        break
                else:
                    landed_y = 2
                    landed_cells = {(cellsX, cellsY) for (
                        cellsX, cellsY) in cloneBoard.falling.cells}
                    return
                cloneBoard3 = cloneBoard2.clone()
                for (x, y) in landed_cells:
                    cloneBoard3.cells.add((x, y))
                cloneBoard2.move(Direction.Drop)
                currentMove_action.append(Direction.Drop)
                current_score = self.evaluate_function_1(
                    cloneBoard3, landed_cells,landed_y)+self.evaluate_function_2(cloneBoard2, landed_y)
                if(current_score > best_score):
                    best_score = current_score
                    best_action = currentRotate_action+currentMove_action
                    best_x = x
                    best_i = j
                    self.holeNum=self.boardBuriesHoles(board)
                    currentMove_action = []
                elif(current_score == best_score):
                    if(self.priority(best_x, len(best_action)-best_i-1, best_i) < self.priority(x, len(currentMove_action), j)):
                        best_score = current_score
                        best_x = x
                        best_i = j
                        best_action = currentRotate_action+currentMove_action
                        currentMove_action = []
                    else:
                        currentMove_action = []
                else:
                    currentMove_action = []
        if(self.holeNum >2 and board.discards_remaining >0):
            return [Action.Discard]
        return best_action


SelectedPlayer = shinomiyaPlayer
