# Nicholas Sunday - Student ID 001068510
#!/usr/bin/env python3

import sys
from utils.cli import *
from utils.Destination import *
from utils.DestinationData import *
from utils.MasterDestinationDirectory import DESTINATIONS
from utils.MasterPackageManifest import PACKAGE_DATA
from utils.Package import *
from utils.PackageData import *
from utils.Truck import *

def pkg_id_to_package(pkg_id_list):
    """
    Takes a list of strings corresponding to package IDs,
    searches the `packages` list for those IDs and returns
    a list filled with Package objects.
    """
    package_list = []
    for pkg_id, package in PACKAGE_DATA.packages.items():
        if pkg_id in pkg_id_list:
            package_list.append(package)
    return package_list


def main():
    # Take command line args and parse them
    cli_args = parse_args(sys.argv)

    # O(N)
    # Creates 3 Truck Objects and optionally sets an early end time
    trucks = {}
    for i in range(1,4):
        if cli_args and cli_args[0] == "status":
            trucks[f"truck{i}"] = Truck(f"Truck {i}", DESTINATIONS.destinations[0], "8:00 AM", end_time=cli_args[1])
        else:
            trucks[f"truck{i}"] = Truck(f"Truck {i}", DESTINATIONS.destinations[0], "8:00 AM")

    if cli_args and cli_args[0] == "add":
        """ Add command line args as package """
        d = cli_args[1]
        PACKAGE_DATA.add_package(
            pkg_id=d["pkg_id"],
            address=d["address"],
            city=d["city"],
            zipcode=d["zipcode"],
            deadline=d["deadline"].strftime(TIME_FORMAT),
            weight=d["weight"],
        )

    # Easier to call names for each truck
    truck1, truck2, truck3 = trucks.values()
    # Easier to call name for late package time
    late_arrival_time = datetime.strptime("9:05 AM", TIME_FORMAT)

    """ Load Truck 1
    Then sets the start time for Truck 1 to 8 AM """
    truck1_pkgs = pkg_id_to_package(["1", "13", "14", "15", "16", "19", "20", "4", "27", "35", "39"])
    truck1.load_truck(truck1_pkgs)
    truck1.deliver_packages()

    """ Load Truck 1 with two late packages """
    if truck1.current_time < late_arrival_time and truck1.end_time > late_arrival_time:
        truck1.set_start_time("9:05 AM")
    truck1_pkgs = pkg_id_to_package(["25", "26"])
    truck1.load_truck(truck1_pkgs)
    truck1.deliver_packages()

    """ Load Truck 2
    Then sets the start time for Truck 2 to 8 AM """
    truck2_pkgs = pkg_id_to_package(
        ["2", "3", "5", "9", "10", "11", "12", "18", "23", "30", "33", "36", "37", "38", "40"]
    )
    truck2.load_truck(truck2_pkgs)
    truck2.deliver_packages()

    """ Load Truck 3
    Only loading packages that are on time and due before 10:30 """
    truck3_pkgs = pkg_id_to_package(["29", "34"])
    truck3.load_truck(truck3_pkgs)
    truck3.deliver_packages()

    """ Load Truck 3 with delayed packages and rest of EOD packages """
    if truck3.current_time <  late_arrival_time and truck3.end_time > late_arrival_time:
        truck3.set_start_time("9:05 AM")
    truck3_pkgs = pkg_id_to_package(["6", "7", "8", "17", "21", "22", "24", "28", "31", "32"])
    truck3.load_truck(truck3_pkgs)
    truck3.deliver_packages()

    if cli_args and cli_args[0] == "lookup":
        """ Search for parsed search terms and return info about found package """
        d = cli_args[1]
        package_matches = PACKAGE_DATA.\
            lookup_package(
            pkg_id=d["pkg_id"],
            address=d["address"],
            city=d["city"],
            zipcode=d["zipcode"],
            deadline=d["deadline"].strftime(TIME_FORMAT),
            weight=d["weight"],
            destination=d["destination"]
        )
        # O(N)
        for package in package_matches:
            package.print_all_info()


    """ Prints truck distances and end times if Status is requested """
    truck_times = {}
    # O(N)
    for truck in trucks.values():
        if truck.end_time > truck.current_time:
            truck_times[truck] = truck.end_time
        else:
            truck_times[truck] = truck.current_time
    print(f"{'-' * 63}")
    print(f"| {'Truck #':^7} | {'Distance (Mi)':^20} | {'Status Time':^11} | {'End of Day':^12} |")
    print(f"{'-' * 63}")
    print(f"| {truck1.name:^7} | {truck1.distance_traveled:^20.2f} |\
{truck_times[truck1].strftime(TIME_FORMAT):^12} | {truck1.current_time.strftime(TIME_FORMAT):^12} |")
    print(f"| {truck2.name:^7} | {truck2.distance_traveled:^20.2f} |\
{truck_times[truck2].strftime(TIME_FORMAT):^12} | {truck2.current_time.strftime(TIME_FORMAT):^12} |")
    print(f"| {truck3.name:^7} | {truck3.distance_traveled:^20.2f} |\
{truck_times[truck3].strftime(TIME_FORMAT):^12} | {truck3.current_time.strftime(TIME_FORMAT):^12} |")
    print(f"{'-' * 63}")
    print()
    print(f"Total Distance: {truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled:.2f} Miles")
    print()

    """ Prints info about all packages at the end time specified """
    print(f"{'-' * 147}")
    print(
        f"| {'ID':^4} | {'Address':^40} | {'City':^20} | {'State':^5} | {'Zip Code':^10}\
| {'Deadline':^12} | {'Delivery Status':^20} | {'Weight (KG)':^12} |")
    print(f"{'-' * 147}")
    for package in PACKAGE_DATA.packages.values():
        #package.print_all_info()
        package.print_just_info()
    print(f"{'-' * 147}")

if __name__ == '__main__':
    main()
