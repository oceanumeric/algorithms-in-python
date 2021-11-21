"""
based on graham scan to find the covex hull:
    first, find the point with smallest y-coordinate
    second, sort the points based on the polar angle
    third, it searches for the collinear points and keep the farthest one
    next, pushe the first three points from the sorted list
    next, it checkes if the next point in the list turns right or left
    if it turns left, we drop the top point, and check the next one
Reference:
https://algorithmtutor.com/Computational-Geometry/Convex-Hull-Algorithms-Graham-Scan/
"""
from functools import reduce


def graham_convex_hull(points):
    '''
    Returns points on convex hull in CCW order according to Graham's scan
    The following code is by Tom Switzer <thomas.switzer@gmail.com>.
    '''
    # define the constant values
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        # compare point a and b
        # True - False = 1, it turns right
        # False - True = -1, it turns left
        # true - true or false - false = 0, no move
        # 1 when both true or false, 0 when one is falue
        return (a > b) - (a < b)

    def turn(p, q, r):
        # it moves with anticlockwise, which alwasy gives the larger y
        # if q_x is less than p_x, then it is negative, it should mean turn left
        # otherwise it should mean turn_right
        return cmp((q[0] - p[0]) * (r[1] - p[1]) -
                   (r[0] - p[0]) * (q[1] - p[1]), 0)

    def keep_left(hull, r):
        # push first three points from the sorted list to the stack
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()  # pop out the last value as it
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points = sorted(points)
    l = reduce(keep_left, points, [])
    u = reduce(keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l


if __name__ == "__main__":
    points = [(0, 0), (1, 4), (3, 1), (3, 3), (5, 2), (5, 5), (7, 0), (9, 6)]
    print(graham_convex_hull(points))
    points = [[181, 864], [182, 859], [182, 860], [182, 861],
              [182, 862], [182, 863], [182, 864]]
    print(graham_convex_hull(points))
