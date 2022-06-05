class Calculator:
    """ A simple calculator App"""
<<<<<<< HEAD


    def add(self, x, y):
=======
    @staticmethod
    def add(x, y):
>>>>>>> 88d8a11d1b0ae54d56b8f7a93704cba30b45d104
        """Add Function"""
        return x+y

<<<<<<< HEAD
    def subtract(self, x, y):
        """Subtract Function"""
        return x - y

    def multiply(self, x, y):
        """Multiply Function"""
        return x * y

    def divide(self, x, y):
=======
    @staticmethod
    def subtract(x, y):
        """Subtract Function"""
        return x - y

    @staticmethod
    def multiply(x, y):
        """Multiply Function"""
        return x * y

    @staticmethod
    def divide(x, y):
>>>>>>> 88d8a11d1b0ae54d56b8f7a93704cba30b45d104
        """Divide Function"""
        if y == 0:
            raise ValueError('Can not divide by zero!')

        return x / y
