"""Design a call center with 3 types of employees."""


class CallCenter(object):
    """Creates the call center object."""

    def __init__(self, name=None, address=None):
        """."""
        self.name = name
        self.address = address


class Employees(object):
    """."""

    def __init__(self, call_center):
        """."""
        if isinstance(call_center, CallCenter):
            self.call_center = call_center
        else:
            raise TypeError('Call center must be a call center object')
        self.employee_count = 0


class Director(Employees):
    """."""

    def __init__(self):
        # super(Employees, self).__init__()
        # how to best connect each director to employees of call center?
        # each director is an employee
        # reference cards in a deck, multiple instances
        pass


class Manager(Employees):
    """."""
    pass


class Respondent(Employees):
    """."""
    pass