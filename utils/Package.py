# Nicholas Sunday - Student ID 001068510
#!/usr/bin/env python3

from datetime import *

TIME_FORMAT = '%H:%M %p'

class Package():
    """Package class.

    pkg_id (int): Unique integer to identify packages
    address (string): Street address package needs to be delivered to
    deadline (datetime): Time package must be delivered by, EOD is set to 11:59 PM
    city (string): the city the address is in
    zipcode (string): the zipcode the package is being delivered to
    weight (int): the weight of the item in KG
    delivery_status (bool): whether or not the package has been delivered
    delivery_time (datetime): the time the package is delivered
    """
    def __init__(self, pkg_id, address, deadline, city, zipcode, weight, destination):
        self.pkg_id = pkg_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.destination = destination
        self.delivery_status = "In Transit"
        self.delivery_time = None

    def __eq__(self, other):
        return all([
            self.pkg_id == other.pkg_id,
            self.address == other.address,
            self.deadline == other.deadline,
            self.city == other.city,
            self.zipcode == other.zipcode,
            self.weight == other.weight,
            self.delivery_status == other.delivery_status
        ])

    def update_status(self, delivery_time, delivery_status="Delivered"):
        """Update the delivery_status and delivery_time of a package

        delivery_time (datetime): the time at which the package was delivered
        """
        self.delivery_status = delivery_status
        self.delivery_time = delivery_time.strftime(TIME_FORMAT)

    def update_address(self, destination, city):
        """Update the delivery address of a package

        :arg address (string): Street number and name
        :arg city (string): City the address is in
        :arg zipcode (string): zipcode the package needs to be delivered to
        """
        self.destination = destination
        self.address = destination.address
        self.city = city
        self.zipcode = destination.zipcode

    def print_all_info(self):
        """ Returns info in a pretty format, intended for easier viewing with less packages """
        print(f"""Package ID: {self.pkg_id}
    Destination: {self.destination.name}
    Address: {self.address}, {self.city}, UT {self.zipcode}
    Deadline: {self.deadline}
    Delivery Time: {self.delivery_time}
    Delivery Status: {self.delivery_status}
    Weight: {self.weight} KG    
    """)

    def print_just_info(self):
        """ Returns info in a table format, intended for viewing all packages """
        print(f"| {self.pkg_id:^4} | {self.address:^40} | {self.city:^20} | {'UT':5} | {self.zipcode:^10}\
| {self.deadline:^12} | {self.delivery_status:^20} | {self.weight:^12} |")
