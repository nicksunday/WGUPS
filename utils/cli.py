# Nicholas Sunday - Student ID 001068510
#!/usr/bin/env python3

import sys
from datetime import *
from utils.DestinationData import *
from utils.MasterDestinationDirectory import DESTINATIONS
from utils.Package import TIME_FORMAT

def print_help():
    print(f"""
Usage: {sys.argv[0]} [-h] [-L PACKAGE DATA] [-S 'HH:MM AM|PM'] [--all],

Optional arguments:,
  -h, --help      Show this message and exit

  -L, --lookup pkg_id=PACKAGE_ID address=ADDRESS deadline=DEADLINE city=CITY 
              zipcode=ZIPCODE weight=WEIGHT delivery_status=STATUS ('In Transit', 'On Truck', 'Delivered')
      Returns information for package searched for with all fields matching

  -A, --add pkg_id=PACKAGE_ID address=ADDRESS deadline=DEADLINE city=CITY 
              zipcode=ZIPCODE weight=WEIGHT delivery_status=STATUS ('In Transit', 'On Truck', 'Delivered')
      Adds a new package to the PackageData 

  -S, --status ['HH:MM AM|PM']    Returns status of all packages at specified time. 
                                  If no time is specified, time is EOD.

                      """)
    sys.exit()
def parse_args(args):
    """
    Parses command line arguments and returns data to be further parsed
    """
    if len(args) > 1:
        """
        Parses package to lookup.
        If the keys aren't presented properly, it prints an error and the help message
        """
        if args[1] in ["-L", "--lookup", "-A", "--add"]:
            search_dict = {attr:search_term for attr,search_term in (argument.split("=") for argument in args[2:])}
            if search_dict["deadline"] == "EOD":
                search_dict["deadline"] = "23:59 PM"
            deadline = search_dict["deadline"]
            search_dict["deadline"] = datetime.strptime(deadline, TIME_FORMAT)
            # O(N)
            for key in search_dict.keys():
                if key not in ["pkg_id", "address", "city", "zipcode", "deadline", "weight"]:
                    print(f"Improper argument used: {key}")
                    print_help()
            # O(N)
            for destination in DESTINATIONS.destinations.values():
                if destination.address == search_dict["address"] and destination.zipcode == search_dict["zipcode"]:
                    package_destination = destination
            search_dict["destination"] = package_destination
            if args[1] in ["-L", "--lookup"]:
                return ("lookup", search_dict)
            else:
                return ("add", search_dict)
        # Returns end time or EOD if none is supplied
        elif args[1] in ["-S", "--status"]:
            try:
                status_time = datetime.strptime(args[2], TIME_FORMAT)
            except IndexError:
                status_time = "EOD"
            return ("status", status_time)
        # Prints help menu if no valid arg is passed
        else:
            print_help()
    # Returns none if no arg is passed
    else:
        return None
