class User:
    def __init__(self, username, password, role, email, salary):
        # Function forms object, which have information about new user

        self.username = username
        self.password = password
        self.role = role  # 'manager' or 'leader'
        self.email = email
        self.salary = salary

    def register(self):
        # Function control every point in objects and shows how user should correct problem (Ksenia)

        pass

    def set_role(self, new_role):
        # Function could change role of users (Ksenia)

        self.role = new_role
