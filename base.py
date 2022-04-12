from pprint import pprint


class Boundary:
    def __init__(self, is_open):
        self.is_open = is_open

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def __bool__(self):
        return self.is_open


class Cell:
    def __init__(self, top=None, right=None, bottom=None, left=None):
        self.top = top if isinstance(top,Boundary) else Boundary(False)
        self.right = right if isinstance(right,Boundary) else Boundary(False)
        self.bottom = bottom if isinstance(bottom,Boundary) else Boundary(False)
        self.left = left if isinstance(left,Boundary) else Boundary(False)


class RectangularBoard:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cells = self._generate_board(height, width)

    def _generate_board(self, height, width):
        cells = []
        top_cell = False
        for y in range(height):
            left_cell = False
            row = []
            for x in range(width):
                if cells:
                    top_cell = cells[y-1][x]
                    top_boundary = top_cell.bottom
                else:
                    top_boundary = None
                if left_cell:
                    left_boundary = left_cell.right
                else:
                    left_boundary = None
                cell = Cell(left=left_boundary, top=top_boundary)
                left_cell = cell
                row.append(cell)
            cells.append(row)
        return cells


board = RectangularBoard(2, 2)
pprint(board.cells)
