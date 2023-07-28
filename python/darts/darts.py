"""darts"""
INNER_RADIUS = 1
INNER_POINTS = 10
MIDDLE_RADIUS = 5
MIDDLE_POINTS = 5
OUTER_RADIUS = 10
OUTER_POINTS = 1
OUTSIDE_POINTS = 0

def score(x, y):
    h = (x**2 + y**2)**(1/2)
    if h > OUTER_RADIUS:
        return OUTSIDE_POINTS
    if h > MIDDLE_RADIUS:
        return OUTER_POINTS
    if h > INNER_RADIUS:
        return MIDDLE_POINTS
    return INNER_POINTS

