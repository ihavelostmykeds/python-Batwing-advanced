class ListMixin:
    def __str__(self):
        lst = []
        for value in self.__dict__.values():
            lst.append(value)
        return lst.__repr__()


class Profile(ListMixin):
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex


anton = Profile('Anton', 'Gera', '0730333333', 'Lviv', 'test@test.com', '29.07.1995', '26', 'male')
print(anton)
