class Submarine(object):
    my_attrs = ['color', 'year', 'name']

    def __init__(self, color, year, name):
        self.color = color
        self.year = year
        self.name = name


class Tank(object):
    my_attrs = ['weight', 'year', 'identifier']

    def __init__(self, weight, year, identifier):
        self.weight = weight
        self.year = year
        self.identifier = identifier


sub = Submarine(name="Narwal", year=2000, color="Black")
tank = Tank(weight=5000, year=1956, identifier="AXXXXXXXX123")

print(tank.identifier)
