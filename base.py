from pprint import pprint


class Boundary:
    def __init__(self, is_wall: bool):
        self.is_wall = is_wall

    def open(self):
        self.is_wall = False

    def close(self):
        self.is_wall = True

    def __bool__(self):
        return self.is_wall


class Cell:
    def __init__(self, top: Boundary = Boundary(True), right: Boundary = Boundary(True), bottom: Boundary = Boundary(True), left: Boundary = Boundary(True)):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left


class RectangularBoard:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.cells = self._generate_board(height, width)

    def _generate_board(self, height: int, width: int):
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
