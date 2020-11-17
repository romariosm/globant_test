

class TemperatureKelvin:
    """
    Kelvin Temperature convention class
    """

    def __init__(self, value):
        self.__value = value

    def convert_to_celsius(self):
        """
        Convert kelvin unit to celsius
        """
        return round(self.__value - 273.15, 2)
