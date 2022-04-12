import svgwrite
from base import RectangularBoard


def render(filename, board: RectangularBoard, cell_size: int, lineWidth: int, color: list[int, int, int]):
    cell_size = 30
    lineWidth = 2
    color = svgwrite.rgb(*color)

    dwg = svgwrite.Drawing(filename, profile='tiny')
    pointer_x = 0
    pointer_y = 0
    for row in board.cells:
        for cell in row:
            if cell.top:
                dwg.add(dwg.line((pointer_x, pointer_y), (pointer_x+cell_size,
                        pointer_y), stroke=color, stroke_width=lineWidth))
            if cell.right:
                dwg.add(dwg.line((pointer_x+cell_size, pointer_y), (pointer_x+cell_size,
                                                                    pointer_y+cell_size), stroke=color, stroke_width=lineWidth))
            if cell.bottom:
                dwg.add(dwg.line((pointer_x, pointer_y+cell_size), (pointer_x+cell_size,
                        pointer_y+cell_size), stroke=color, stroke_width=lineWidth))
            if cell.left:
                dwg.add(dwg.line((pointer_x, pointer_y), (pointer_x,
                        pointer_y+cell_size), stroke=color, stroke_width=lineWidth))
            pointer_x += cell_size
        pointer_x = 0
        pointer_y += cell_size

    dwg.save()


if __name__ == "__main__":
    board = RectangularBoard(2, 2)
    board.cells[0][0].right.open()
    board.cells[0][1].bottom.open()
    render(filename="test.svg", board=board,
           cell_size=30, lineWidth=2, color=[10, 10, 16])
