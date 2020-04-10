# Nicholas Sunday - Student ID 001068510
#!/usr/bin/env python3

class Destination():
    """Destination class

    name (string): Name of the destination
    address (string): Street name and number of destination
    zipcode (string): zipcode of the address
    dist_tup (tuple): An ordered tuple of Destination objects and how far the parent is from each
    dist_dict (dict): Dictionary where Destination name is the key and distance from self is the value
    sorted_distances (dict): dist_dict, but sorted by distance from self
    """
    def __init__(self, name, address, zipcode, dist_tup):
        self.name = name
        self.address = address
        self.zipcode = zipcode
        self.dist_tup = dist_tup
        self.dist_dict = {}
        self.sorted_distances = {}

    def __eq__(self, other):
        return all([
            self.name == other.name,
            self.address == other.address,
            self.zipcode == other.zipcode,
            self.dist_tup == other.dist_tup,
            self.dist_dict == other.dist_dict,
            self.sorted_distances == other.sorted_distances
        ])

    def add_distance(self, dest_name, distance):
        """Fills the dist_dict with destinations (key = name) and their distance (value) from this Destination object"""
        self.dist_dict[dest_name] = distance
