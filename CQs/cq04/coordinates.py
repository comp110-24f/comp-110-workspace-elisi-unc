"""coordinates file for import in cq04"""

__author__ = "730577493"


def get_coords(xs: str, ys: str) -> None:
    idx_x: int = 0
    idx_y: int = 0
    while idx_x < len(xs):
        while idx_y < len(ys):
            print("(" + xs[idx_x] + ", " + ys[idx_y] + ")")
            idx_y += 1
        idx_y = 0
        idx_x += 1
