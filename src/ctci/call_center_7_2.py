"""Module for call center."""


class CallCenter(object):
    """
    Call Center queues up the calls and has an overall record of
    the employees and which are on calls.

    Attributes:
        Dictionary with the amount of each employee type.

    Methods:
        add_employee
        Receive call, add to queue.
        Return initial voice message, maybe with spot in queue if not available
        Dispatch to first, lowest level employee.
    """

    def __init__(self, name, address):
        """."""
        self.name = name
        self.address = address
        self.employees = {
            'Directors': [],
            'Managers': [],
            'Respondents': []
        }

    def add_employee(self):
        """Here you would add an employee to the dictionary
        and create the new employee object."""
        pass

    def receive_call(self):
        """Handle the phone call, assign to queue if all 
        employees are busy, return greeting message."""
        pass

    def dispatch_call(self):
        """dispatch call to first available employee."""


class Call(object):
    """."""

    pass


class Employee(object):
    """."""

#  class for each type
