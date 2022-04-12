from pprint import pprint

class Boundary:
    def __init__(self,is_open):
        self.is_open = True

class Cell:
    def __init__(self):
        self._top = False
        self._right = False
        self._bottom = False
        self._left = False

    @property
    def top(self):
        value = self._top
        if isinstance(value,Cell):
            return getattr(value,dir_mirror["top"])
        return value

    @top.setter
    def top(self,value):
        print("setter of x called")
        existing_value = self._top
        if isinstance(existing_value,Cell):
            setattr(existing_value, dir_mirror["top"], value)
        else:
            self._top = value

    @property
    def right(self):
        print("setter of right called")
        value = self._right
        if isinstance(value,Cell):
            return getattr(value,dir_mirror["right"])
        return value

    @right.setter
    def right(self,value):
        print("setter of right called")
        existing_value = self._right
        if isinstance(existing_value,Cell):
            setattr(existing_value, dir_mirror["right"], value)
        else:
            self._right = value

    @property
    def bottom(self):
        value = self._bottom
        if isinstance(value,Cell):
            return getattr(value,dir_mirror["bottom"])
        return value

    @bottom.setter
    def bottom(self,value):
        print("setter of x called")
        existing_value = self._bottom
        if isinstance(existing_value,Cell):
            setattr(existing_value, dir_mirror["bottom"], value)
        else:
            self._bottom = value

    @property
    def left(self):
        value = self._left
        if isinstance(value,Cell):
            return getattr(value,dir_mirror["left"])
        return value

    @left.setter
    def left(self,value):
        print("setter of x called")
        existing_value = self._left
        if isinstance(existing_value,Cell):
            setattr(existing_value, dir_mirror["left"], value)
        else:
            self._left = value

    def can_move(self, dir):
        dir_value = self.__getattribute__(dir)
        if isinstance(dir_value, Cell):
            opposite_dir = dir_mirror[dir]
            return dir_value.__getattribute__(opposite_dir)
        elif isinstance(dir_value, bool):
            return dir_value
        return False

class RectangularBoard:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cells = self._generate_board(height, width)

    def _generate_board(self, height, width):
        cells = []
        top = False
        for y in range(height):
            left = False
            row = []
            for x in range(width):
                cell = Cell()
                if cells:
                    top = cells[y-1][x]
                    cell.top = top
                    top.bottom = cell
                if left:
                    cell.left = left
                    left.right = cell
                left = cell
                row.append(cell)
            cells.append(row)
        return cells

board = RectangularBoard(2,2)
pprint(board.cells)