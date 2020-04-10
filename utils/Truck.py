# Nicholas Sunday - Student ID 001068510
#!/usr/bin/env python3

from datetime import *
from utils.Destination import *
from utils.DestinationData import *
from utils.MasterDestinationDirectory import DESTINATIONS
from utils.MasterPackageManifest import PACKAGE_DATA
from utils.Package import *

AVERAGE_SPEED = 18 #MPH
MAX_PACKAGES = 16

class Truck():
    """Truck class.

    name (string): The name of the truck object, set at creation time
    package_manifest (list): an empty list, that will later be populated by the load_truck function
    distance_traveled (double): cumulative distance the truck has driven to deliver packages
    current_time (datetime): the current time, starting at the time set with set_start_time function
    finished (bool): false if there are still packages in the manifest otherwise it is true
    """

    def __init__(self, name, current_location, start_time, end_time="EOD"):
        self.name = name
        self.package_manifest = []
        self.distance_traveled = 0.0
        self.current_location = current_location
        self.sub_manifest = []
        self.current_time = datetime.strptime(start_time, TIME_FORMAT)
        self.end_time = self.set_end_time(end_time)

    def load_truck(self, package_list):
        """Load packages into Truck

        Feed a list of packages to the truck and add it to the internal list.
        Prints a help message if you try to add more than the max (16),
        and does not continue adding packages.

        :arg package_list (list)
        """
        if self.current_time < self.end_time:
            distance_traveled = DESTINATIONS.destinations[0].dist_dict[self.current_location.name]
            self.distance_traveled += distance_traveled
            self.current_time += timedelta(minutes=((distance_traveled * 60) / AVERAGE_SPEED))
            self.current_location = DESTINATIONS.destinations[0]
            # O(N)
            for package in package_list:
                if len(self.package_manifest) < MAX_PACKAGES:
                    self.package_manifest.append(package)
                    package.delivery_status = f"On {self.name}"
                else:
                    print("Attempted to load too many packages")

    def set_start_time(self, start_time):
        """Set the time the Truck will begin delivering packages"""
        self.current_time =  datetime.strptime(start_time, TIME_FORMAT)

    def set_end_time(self, end_time):
        """Set the time to stop delivering and return status"""
        if end_time == "EOD":
            end_time = datetime.strptime("23:59 PM", TIME_FORMAT)
        return end_time

    def sort_by_deadline(self, package_list):
        """ Takes a list of packages and sorts it based on deadline """
        # O(nlogn)
        package_list = sorted(package_list, key=lambda package: package.deadline, reverse=True)
        return package_list

    def sort_by_distance(self, package_list):
        """ Takes a list of packages and sorts by distance """
        # O(nlogn)
        package_list = sorted(
            package_list,
            key=lambda package: package.destination.dist_dict[self.current_location.name],
            reverse=True
        )
        return package_list

    def deliver_packages(self):
        """ Delivers packages currently loaded into the truck

        Uses a greedy sorting of the manifest to get the soonest deadline.
        Checks the package against others to see if there are others with the same deadline,
        these are loaded into a smaller manifest and greedy sorted again, this time by distance.

        Each loop the main manifest and sub_manifest are checked for packages that need to be
        delivered to the same address as the current package.
        """
        # O(N^4
        # Continues loop until there are no packages left in the truck
        # First sorts by deadline and takes the earliest package off the stack
        # Checks for other packages with the same deadline and adds them to a smaller list
        while self.package_manifest:
            self.sort_by_deadline(self.package_manifest)
            package = self.package_manifest.pop()
            sub_list = [p for p in self.package_manifest if p.deadline == package.deadline]
            sub_list.append(package)
            # The second while loop continues until there are no more items in the smaller list
            # or until the end time is reached.
            # The smaller list is sorted by distance from the current location
            # After delivering the package it also updates the distance traveled and time elapsed
            while sub_list and self.current_time <= self.end_time:
                sub_list = self.sort_by_distance(sub_list)
                current_package = sub_list.pop()
                # Checks to see if package 9 is reach. If it is and it is before the update time it is
                # put back on the stack otherwise it updates the destination
                if current_package.pkg_id == "9":
                   if self.current_time >= datetime.strptime("10:20 AM", TIME_FORMAT):
                       current_package.update_address(DESTINATIONS.destinations[19], "Salt Lake City")
                   else:
                       self.package_manifest.append(package)
                       continue
                distance_traveled = current_package.destination.dist_dict[self.current_location.name]
                elapsed_time = timedelta(minutes=((distance_traveled * 60) / AVERAGE_SPEED))
                # This breaks out of the loop if end time is reached and does fractional time and distance calcs
                if (self.current_time + elapsed_time) > self.end_time:
                    time_diff = ((self.current_time + elapsed_time) - self.end_time).total_seconds() / 60
                    distance_diff = (18 * time_diff) / 60
                    adj_distance_traveled = distance_traveled - distance_diff
                    self.distance_traveled += adj_distance_traveled
                    self.current_time += elapsed_time - timedelta(minutes=time_diff)
                    break
                self.current_time += elapsed_time
                self.distance_traveled += distance_traveled
                current_package.update_status(self.current_time)
                self.current_location = current_package.destination
                if current_package in self.package_manifest:
                    self.package_manifest.remove(current_package)
                PACKAGE_DATA.packages[current_package.pkg_id] = current_package
                # Checks for any other packages in the truck that need to be delivered to the current package's address
                # and delivers them if so
                for p in self.package_manifest:
                    if p.destination.address == self.current_location.address:
                        p.update_status(self.current_time)
                        if p in sub_list: sub_list.remove(p)
                        self.package_manifest.remove(p)
                        PACKAGE_DATA.packages[p.pkg_id] = p
