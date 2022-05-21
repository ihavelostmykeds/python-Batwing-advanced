class Person:
    def __init__(self, name):
        left_arm = Arm('I will always love my mother')
        right_arm = Arm('標準漢字表')
        self.name = name
        self.message = f'my name is {self.name} and I have two tats: {left_arm.tatoo} and {right_arm.tatoo}'


class Arm:
    def __init__(self, tatoo):
        self.tatoo = tatoo


mike = Person('Mike')
print(mike.message)


class CellPhone:
    def __init__(self, screen):
        self.screen = screen
        self.message = f'I have a great {screen.screen_type} screen on my phone'


class Screen:
    def __init__(self, screen_type):
        self.screen_type = screen_type


screen = Screen('ultra-wide')
phone = CellPhone(screen)
print(phone.message)
