class User:
    def __init__(self, username, password, role, email, salary):
        # Function forms object, which have information about new user

        self.username = username
        self.password = password
        self.role = role  # 'manager' or 'leader'
        self.email = email
        self.salary = salary

    def register(self):
        # Function control every point in objects and shows how user should correct problem 
        errors = []
        if not self.username:
            errors.append("Имя пользователя не заполнено.")

        if self.role not in ['менеджер', 'руководитель', 'стажер']:
            errors.append("Такой должности нет.")

        if '@' not in self.email or '.' not in self.email.split('@')[-1]:
            errors.append("Адрес эл. почты недействителен.")

        if self.salary <= 0:
            errors.append("Зарплата должна быть больше 0.")

        if errors:
            return "\n Возникла ошибка инициализации:\n" + "\n".join(errors)
        else:
            return "Инициализация успешна!"
        

        if user_manager.find_user_by_username(self.username):
            return "\n Ошибка: имя пользователя уже существует."
        
        user_manager.users.append(self)
        return "\n Пользователь успешно зарегистрирован."


    def set_role(self, new_role):
        # Function could change role of users 
        if new_role in ['менеджер', 'руководитель', 'стажер']:
            self.role = new_role
            return f"Должность изменена на {new_role}."
        else:
            return "Смена должности невозможна."
