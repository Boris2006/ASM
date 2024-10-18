class UserManager:
    def __init__(self):
        self.users = []

    def register_user(self, username, password, role):
        user_id = len(self.users) + 1
        user = User(user_id, username, password, role)
        self.users.append(user)
        return user

    def manage_roles(self, user_id, new_role):
        user = self.find_user_by_id(user_id)
        if user:
            user.set_role(new_role)

    def find_user_by_id(self, user_id):
        return next((user for user in self.users if user.user_id == user_id), None)
