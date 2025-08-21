"""Solution to Ellen's Alien Game exercise."""

HEALTH = 3
class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = HEALTH
        Alien.total_aliens_created += 1

    def hit(self):
        if self.is_alive():
            self.health -= 1

    def is_alive(self):
        return self.health > 0
    
    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate  

    def get_position(self):
        return self.x_coordinate, self.y_coordinate
    
    def collision_detection(self, another):
        # this method must be undefined...
        #another_x, another_y = another.get_position()
        #return self.x_coordinate == another_x and self.y_coordinate == another_y
        pass
    
def new_aliens_collection(coordinates_list):
    return [
        Alien(coordinates[0], coordinates[1])
        for coordinates in coordinates_list
    ]

