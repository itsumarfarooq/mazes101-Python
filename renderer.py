import svgwrite
from base import Cell, RectangularBoard

board = RectangularBoard(2,2)
board.cells[0][0].right = True
board.cells[0][0].right
board.cells[0][1].left
board.cells[1][1].top = True


dwg = svgwrite.Drawing('test.svg', profile='tiny')
for row in board.cells:
    for cell in row:
        dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))