
from project import brick
from project import variables

# My Blocks
from lower_pen import lower_pen
from lift_pen import lift_pen


def print_w(size):
    seg2 = variables['Seg2']
    seg4 = variables['Seg4']
    lower_pen()
    brick['motor']['B'].on_for_degrees(-20, seg4)
    brick['motor']['A+B'].on_for_degrees(10,10, seg2)
    brick['motor']['A+B'].on_for_degrees(10,-10, seg2)
    brick['motor']['B'].on_for_degrees(20, seg4)
    lift_pen()
