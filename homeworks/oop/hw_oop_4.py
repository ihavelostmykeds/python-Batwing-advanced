from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def get_screen(self):
        pass

    @abstractmethod
    def get_keyboard(self):
        pass

    @abstractmethod
    def get_touchpad(self):
        pass

    @abstractmethod
    def get_webcam(self):
        pass

    @abstractmethod
    def get_ports(self):
        pass

    @abstractmethod
    def get_dynamics(self):
        pass

    @abstractmethod
    def get_laptop_info(self):
        pass


class HPLaptop(Laptop):

    def __init__(self, screen_size, keyboard_model, touchpad_exists, webcam_exists, number_of_ports, dynamics_type):
        self.screen_size = screen_size
        self.keyboard_model = keyboard_model
        self.touchpad_exist = touchpad_exists
        self.webcam_exist = webcam_exists
        self.number_of_ports = number_of_ports
        self.dynamics_type = dynamics_type

    def get_screen(self):
        return self.screen_size

    def get_keyboard(self):
        return self.keyboard_model

    def get_touchpad(self):
        return self.touchpad_exist

    def get_webcam(self):
        self.webcam_exist = True
        return self.webcam_exist

    def get_ports(self):
        return self.number_of_ports

    def get_dynamics(self):
        return self.dynamics_type

    def get_laptop_info(self):
        return f'''
        screen size = {self.get_screen()}
        keyboard manufacturer = {self.get_keyboard()}
        has touchpad = {self.get_touchpad()}
        has webcam = {self.get_webcam()}
        number of ports = {self.get_ports()}
        dynamics type = {self.get_dynamics()}
'''


new_laptop = HPLaptop(24, 'Razer', True, True, 4, 'Dolby')
print(new_laptop.get_laptop_info())
