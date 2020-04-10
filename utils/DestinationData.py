# Nicholas Sunday - Student ID 001068510
#!/usr/bin/env python3

from utils.Destination import Destination

class DestinationData:
    def __init__(self):
        self.destinations = {}
        self.build_destination_dictionary()

    def build_destination_dictionary(self):
        """Create a dictionary of delivery destinations

        Takes the raw destination data and converts it into Destination items and stores
        them in a dictionary

        :return: destinations (dict): A dictionary of Destination objects
        """

        destinations = {}

        raw_destinations = [
            ("Western Governors University", "4001 South 700 East", "87104",
             (0.0, 7.2, 3.8, 11.0, 2.2, 3.5, 10.9, 8.6, 7.6, 2.8, 6.4, 3.2, 7.6,
              5.2, 4.4, 3.7, 7.6, 2.0, 3.6, 6.5, 1.9, 3.4, 2.4, 6.4, 2.4, 5.0, 3.6)
             ),
            ("International Peace Gardens", "1060 Dalton Ave S", "84106",
             (7.2, 0.0, 7.1, 6.4, 6.0, 4.8, 1.6, 2.8, 4.8, 1.6, 2.8, 4.8, 6.3, 7.3, 5.3,
              4.8, 3.0, 4.6, 4.5, 7.4, 6.0, 5.0, 4.8, 9.5, 10.9, 8.3, 6.9, 10.0, 4.4, 13.0)
             ),
            ("Sugar House Park", "1330 2100 S", "84123",
             (3.8, 7.1, 0.0, 9.2, 4.4, 2.8, 8.6, 6.3, 5.3, 1.6, 10.4, 3.0, 5.3, 6.5,
              5.6, 5.8, 5.7, 4.1, 3.6, 4.3, 3.3, 5.0, 6.1, 9.7, 6.1, 2.8, 7.4)
             ),
            ("Taylorsville-Bennion Heritage City Gov Off", "1488 4800 S", "84123",
             (11.0, 6.4, 9.2, 0.0, 5.6, 6.9, 8.6, 4.0, 11.1, 7.3, 1.0, 6.4, 11.1, 3.9,
              4.3, 4.4, 7.2, 5.3, 6.0, 10.6, 5.9, 7.4, 4.7, 0.6, 6.4, 10.1, 10.1)
             ),
            ("Salt Lake City Division of Health", "177 W Price Ave", "84115",
             (2.2, 6.0, 4.4, 5.6, 0.0, 1.9, 7.9, 5.1, 7.5, 2.6, 6.5, 1.5, 7.5, 3.2,
              2.4, 2.7, 1.4, 0.5, 1.7, 6.5, 3.2, 5.2, 2.5, 6.0, 4.2, 5.4, 5.5)
             ),
            ("South Salt Lake Public Works", "195 W Oakland Ave", "84115",
             (3.5, 4.8, 2.8, 6.9, 1.9, 0.0, 6.3, 4.3, 4.5, 1.5, 8.7, 0.8, 4.5, 3.9,
              3.0, 3.8, 5.7, 1.9, 1.1, 3.5, 4.9, 6.9, 4.2, 9.0, 5.9, 3.5, 7.2)
             ),
            ("Salt Lake City Streets and Sanitation", "2010 W 500 S", "84104",
             (10.9, 1.6, 8.6, 8.6, 7.9, 6.3, 0.0, 4.0, 4.2, 8.0, 8.6, 6.9, 4.2, 4.2,
              8.0, 5.8, 7.2, 7.7, 6.6, 3.2, 11.2, 12.7, 10.0, 8.2, 11.7, 5.1, 14.2)
             ),
            ("Deker Lake", "2300 Parkway Blvd", "84119",
             (8.6, 2.8, 6.3, 4.0, 5.1, 4.3, 4.0, 0.0, 7.7, 9.3, 4.6, 4.8, 7.7, 1.6,
              3.3, 3.4, 3.1, 5.1, 4.6, 6.7, 8.1, 10.4, 7.8, 4.2, 9.5, 6.2, 10.7)
             ),
            ("Salt Lake City Ottinger Hall", "233 Canyon Rd", "84103",
             (7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.0, 4.8, 11.9, 4.7, 0.6, 7.6,
              7.8, 6.6, 7.2, 5.9, 5.4, 1.0, 8.5, 10.3, 7.8, 11.5, 9.5, 2.8, 14.1)
             ),
            ("Columbus Library", "2530 S 500 E", "84106",
             (2.8, 6.3, 1.6, 7.3, 2.6, 1.5, 8.0, 9.3, 4.8, 0.0, 9.4, 1.1, 5.1, 4.6,
              3.7, 4.0, 6.7, 2.3, 1.8, 4.1, 3.8, 5.8, 4.3, 7.8, 4.8, 3.2, 6.0)
             ),
            ("Taylorsville City Hall", "2600 Taylorsville Blvd", "84118",
             (6.4, 7.3, 10.4, 1.0, 6.5, 8.7, 8.6, 4.6, 11.9, 9.4, 0.0, 7.3, 12.0, 4.9,
              5.2, 5.4, 8.1, 6.2, 6.9, 11.5, 6.9, 8.3, 4.1, 0.4, 4.9, 11.0, 6.8)
             ),
            ("South Salt Lake Police", "2835 Main St", "84115",
             (3.2, 5.3, 3.0, 6.4, 1.5, 0.8, 6.9, 4.8, 4.7, 1.1, 7.3, 0.0, 4.7, 3.5,
              2.6, 2.9, 6.3, 1.2, 1.0, 3.7, 4.1, 6.2, 3.4, 6.9, 5.2, 3.7, 6.4)
             ),
            ("Council Hall", "300 State St", "84103",
             (7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.6, 5.1, 12.0, 4.7, 0.0, 7.3,
              7.8, 6.6, 7.2, 5.9, 5.4, 1.0, 8.5, 10.3, 7.8, 11.5, 9.5, 2.8, 14.1)
             ),
            ("Redwood Park", "3060 Lester St", "84119",
             (5.2, 3.0, 6.5, 3.9, 3.2, 3.9, 4.2, 1.6, 7.6, 4.6, 4.9, 3.5, 7.3, 0.0,
              1.3, 1.5, 4.0, 3.2, 3.0, 6.9, 6.2, 8.2, 5.5, 4.4, 7.2, 6.4, 10.5)
             ),
            ("Salt Lake County Mental Health", "3148 S 1100 W", "84119",
             (4.4, 4.6, 5.6, 4.3, 2.4, 3.0, 8.0, 3.3, 7.8, 3.7, 5.2, 2.6, 7.8, 1.3,
              0.0, 0.6, 6.4, 2.4, 2.2, 6.8, 5.3, 7.4, 4.6, 4.8, 6.3, 6.5, 8.8)
             ),
            ("Salt Lake County/United Police Dept", "3365 S 900 W", "84119",
             (3.7, 4.5, 5.8, 4.4, 2.7, 3.8, 5.8, 3.4, 6.6, 4.0, 5.4, 2.9, 6.6, 1.5,
              0.6, 0.0, 5.6, 1.6, 1.7, 6.4, 4.9, 6.9, 4.2, 5.6, 5.9, 5.7, 8.4)
             ),
            ("West Valley Prosecutor", "3575 W Valley Central Station bus Loop", "84119",
             (7.6, 7.4, 5.7, 7.2, 1.4, 5.7, 7.2, 3.1, 7.2, 6.7, 8.1, 6.3, 7.2, 4.0,
              6.4, 5.6, 0.0, 7.1, 6.1, 7.2, 10.6, 12.0, 9.4, 7.5, 11.1, 6.2, 13.6)
             ),
            ("Housing Auth. of Salt Lake County", "3595 Main St", "84115",
             (2.0, 6.0, 4.1, 5.3, 0.5, 1.9, 7.7, 5.1, 5.9, 2.3, 6.2, 1.2, 5.9, 3.2,
              2.4, 1.6, 7.1, 0.0, 1.6, 4.9, 3.0, 5.0, 2.3, 5.5, 4.0, 5.1, 5.2)
             ),
            ("Utah DMV Administrative Office", "380 W 2880 S", "84115",
             (3.6, 5.0, 3.6, 6.0, 1.7, 1.1, 6.6, 4.6, 5.4, 1.8, 6.9, 1.0, 5.4, 3.0,
              2.2, 1.7, 6.1, 1.6, 0.0, 4.4, 4.6, 6.6, 3.9, 6.5, 5.6, 4.3, 6.9)
             ),
            ("Third District Juvenile Court", "410 S State St", "84111",
             (6.5, 4.8, 4.3, 10.6, 6.5, 3.5, 3.2, 6.7, 1.0, 4.1, 11.5, 3.7, 1.0, 6.9,
              6.8, 6.4, 7.2, 4.9, 4.4, 0.0, 7.5, 9.3, 6.8, 11.4, 8.5, 1.8, 13.1)
             ),
            ("Cottonwood Regional Softball Complex", "4300 S 1300 E", "84117",
             (1.9, 9.5, 3.3, 5.9, 3.2, 4.9, 11.2, 8.1, 8.5, 3.8, 6.9, 4.1, 8.5, 6.2,
              5.3, 4.9, 10.6, 3.0, 4.6, 7.5, 0.0, 2.0, 2.9, 6.4, 2.8, 6.0, 4.1)
             ),
            ("Holiday City Office", "4580 S 2300 E", "84117",
             (3.4, 10.9, 5.0, 7.4, 5.2, 6.9, 12.7, 10.4, 10.3, 5.8, 8.3, 6.2, 10.3,
              8.2, 7.4, 6.9, 12.0, 5.0, 6.6, 9.3, 2.0, 0.0, 4.4, 7.9, 3.4, 7.9, 4.7)
             ),
            ("Murray City Museum", "5025 State St", "84107",
             (2.4, 8.3, 6.1, 4.7, 2.5, 4.2, 10.0, 7.8, 7.8, 4.3, 4.1, 3.4, 7.8, 5.5,
              4.6, 4.2, 9.4, 2.3, 3.9, 6.8, 2.9, 4.4, 0.0, 4.5, 1.7, 6.8, 3.1)
             ),
            ("Valley Regional Softball Complex", "5100 South 2700 West", "84118",
             (6.4, 6.9, 9.7, 0.6, 6.0, 9.0, 8.2, 4.2, 11.5, 7.8, 0.4, 6.9, 11.5, 4.4,
              4.8, 5.6, 7.5, 5.5, 6.5, 11.4, 6.4, 7.9, 4.5, 0.0, 5.4, 10.6, 7.8)
             ),
            ("City Center of Rock Springs", "5383 South 900 East #104", "84117",
             (2.4, 10.0, 6.1, 6.4, 4.2, 5.9, 11.7, 9.5, 9.5, 4.8, 4.9, 5.2, 9.5, 7.2,
              6.3, 5.9, 11.1, 4.0, 5.6, 8.5, 2.8, 3.4, 1.7, 5.4, 0.0, 7.0, 1.3)
             ),
            ("Rice Terrace Pavilion Park", "600 E 900 South", "84105",
             (5.0, 4.4, 2.8, 10.1, 5.4, 3.5, 5.1, 6.2, 2.8, 3.2, 11.0, 3.7, 2.8, 6.4,
              6.5, 5.7, 6.2, 5.1, 4.3, 1.8, 6.0, 7.9, 6.8, 10.6, 7.0, 0.0, 8.3)
             ),
            ("Wheeler Historic Farm", "6351 South 900 East", "84121",
             (3.6, 13.0, 7.4, 10.1, 5.5, 7.2, 14.2, 10.7, 14.1, 6.0, 6.8, 6.4, 14.1,
              10.5, 8.8, 8.4, 13.6, 5.2, 6.9, 13.1, 4.1, 4.7, 3.1, 7.8, 1.3, 8.3, 0.0)
             )
        ]


        """
        Take the list of tuples and turn them into a dictionary. 
        The 'id_num' variable is the key for easier searching and sorting.
        """
        id_num = 0
        for destination in raw_destinations:
            name, address, zipcode, dist_tup = destination
            d = Destination(name, address, zipcode, dist_tup)
            destinations[id_num] = d
            id_num += 1


        """
        Add distance between current and each other destination.
        The integer 'i' corresponds to the position of the distance in each tuple 
        and the "ID" number of each destination.   
        """
        for d in destinations.values():
            i = 0
            for k,v in destinations.items():
                d.add_distance(v.name, d.dist_tup[i])
                i += 1

        """
        Sort the dictionary of distances. The name of the destination is the key for easier searching later
        """
        for k,v in destinations.items():
            v.sorted_distances = {k: v for k, v in sorted(v.dist_dict.items(), key=lambda item: item[1])}

        self.destinations = destinations
