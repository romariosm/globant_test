class ParameterAPI:
    def __init__(self, name):
        self.__name = name

    @staticmethod
    def is_valid(value):
        pass

    @property
    def get_name(self):
        return self.__name


class IntegerParameter(ParameterAPI):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def is_valid(value):
        return isinstance(value, int)


class StringParameter(ParameterAPI):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def is_valid(value):
        return isinstance(value, str)
