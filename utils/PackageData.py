# Nicholas Sunday - Student ID 001068510
#!/usr/bin/env python3

from utils.Destination import *
from utils.DestinationData import *
from utils.MasterDestinationDirectory import DESTINATIONS
from utils.Package import *

class PackageData():
    """ PackageData class
    Used to store package data in one place.
    """
    def __init__(self):
        self.packages = {}
        self.build_package_dictionary()

    def add_package(self, pkg_id, address, deadline, city, zipcode, weight, delivery_status=False):
        """
        FROM SECTION E
        Adds a package to the master package list

        :param pkg_id: Unique package ID
        :param address: Street name and number of delivery address
        :param deadline: Time package must be delivered by
        :param city: City of delivery address
        :param zipcode: Zipcode of delivery address
        :param weight: Weight of package
        :param delivery_status: Whether package has already been delivered or not
        """
        for package in self.packages.values():
            if pkg_id == package.pkg_id:
                print(f"Package ID '{pkg_id}' already in use")
                break
        for destination in DESTINATIONS.destinations.values():
            if destination.zipcode == zipcode and destination.address == address:
                self.packages[pkg_id] = Package(pkg_id, address, deadline, city, zipcode, weight, destination)
        if delivery_status:
            self.packages[package_id].update_status(deadline, "In Transit")

    def lookup_package(self, **kwargs):
        """
        FROM SECTION F
        Takes keyword arguments and turns them into a Package object,
        then searches the master manifest
        """
        package_to_match = Package(**kwargs)
        matches = []
        for package in self.packages.values():
            if package == package_to_match:
                matches.append(package)
        return matches

    def build_package_dictionary(self):
        """
        Function that takes the raw package data from the excel document and turns it into a master list of
        Package objects
        """

        # Raw package data from Excel document
        raw_packages = [
            ("1", "195 W Oakland Ave", "Salt Lake City", "84115", "10:30 AM", "21"),
            ("2", "2530 S 500 E", "Salt Lake City", "84106", "EOD", "44"),
            ("3", "233 Canyon Rd", "Salt Lake City", "84103", "EOD", "2"),
            ("4", "380 W 2880 S", "Salt Lake City", "84115", "EOD", "4"),
            ("5", "410 S State St", "Salt Lake City", "84111", "EOD", "5"),
            ("6", "3060 Lester St", "West Valley City", "84119", "10:30 AM", "88"),
            ("7", "1330 2100 S", "Salt Lake City", "84106", "EOD", "8"),
            ("8", "300 State St", "Salt Lake City", "84103", "EOD", "9"),
            ("9", "300 State St", "Salt Lake City", "84103", "EOD", "2"),
            ("10", "600 E 900 South", "Salt Lake City", "84105", "EOD", "1"),
            ("11", "2600 Taylorsville Blvd", "Salt Lake City", "84118", "EOD", "1"),
            ("12", "3575 W Valley Central Station bus Loop", "West Valley City", "84119", "EOD", "1"),
            ("13", "2010 W 500 S", "Salt Lake City", "84104", "10:30 AM", "2"),
            ("14", "4300 S 1300 E", "Millcreek", "84117", "10:30 AM", "88"),
            ("15", "4580 S 2300 E", "Holladay", "84117", "9:00 AM", "4"),
            ("16", "4580 S 2300 E", "Holladay", "84117", "10:30 AM", "88"),
            ("17", "3148 S 1100 W", "Salt Lake City", "84119", "EOD", "2"),
            ("18", "1488 4800 S", "Salt Lake City", "84123", "EOD", "6"),
            ("19", "177 W Price Ave", "Salt Lake City", "84115", "EOD", "37"),
            ("20", "3595 Main St", "Salt Lake City", "84115", "10:30 AM", "37"),
            ("21", "3595 Main St", "Salt Lake City", "84115", "EOD", "3"),
            ("22", "6351 South 900 East", "Murray", "84121", "EOD", "2"),
            ("23", "5100 South 2700 West", "Salt Lake City", "84118", "EOD", "5"),
            ("24", "5025 State St", "Murray", "84107", "EOD", "7"),
            ("25", "5383 South 900 East #104", "Salt Lake City", "84117", "10:30 AM", "7"),
            ("26", "5383 South 900 East #104", "Salt Lake City", "84117", "EOD", "25"),
            ("27", "1060 Dalton Ave S", "Salt Lake City", "84104", "EOD", "5"),
            ("28", "2835 Main St", "Salt Lake City", "84115", "EOD", "7"),
            ("29", "1330 2100 S", "Salt Lake City", "84106", "10:30 AM", "2"),
            ("30", "300 State St", "Salt Lake City", "84103", "10:30 AM", "1"),
            ("31", "3365 S 900 W", "Salt Lake City", "84119", "10:30 AM", "1"),
            ("32", "3365 S 900 W", "Salt Lake City", "84119", "EOD", "1"),
            ("33", "2530 S 500 E", "Salt Lake City", "84106", "EOD", "1"),
            ("34", "4580 S 2300 E", "Holladay", "84117", "10:30 AM", "2"),
            ("35", "1060 Dalton Ave S", "Salt Lake City", "84104", "EOD", "88"),
            ("36", "2300 Parkway Blvd", "West Valley City", "84119", "EOD", "88"),
            ("37", "410 S State St", "Salt Lake City", "84111", "10:30 AM", "2"),
            ("38", "410 S State St", "Salt Lake City", "84111", "EOD", "9"),
            ("39", "2010 W 500 S", "Salt Lake City", "84104", "EOD", "9"),
            ("40", "380 W 2880 S", "Salt Lake City", "84115", "10:30 AM", "45")
        ]

        """
        Ingest raw data and turn each tuple into a Package object.
        Package objects are stored in a dictionary with their ID as the key. 
        """
        for package in raw_packages:
            pkg_id, address, city, zipcode, deadline, weight = package
            if deadline == "EOD":
                deadline = datetime.strptime("23:59 PM", TIME_FORMAT)
            else:
                deadline = datetime.strptime(deadline, TIME_FORMAT)
            deadline = deadline.strftime(TIME_FORMAT)
            for destination in DESTINATIONS.destinations.values():
                if destination.address == address and destination.zipcode == zipcode:
                    package_destination = destination
            p = Package(pkg_id, address, deadline, city, zipcode, weight, package_destination)
            self.packages[pkg_id] = p
