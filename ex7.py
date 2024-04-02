class TrafficLight:
    """
    Class of traffic light.

    Attributes:
        ind_current_signal (int): index current signal in list
        current_signal (str): color of current signal
    """
    permissible_values = ['red', 'yellow', 'green', 'yellow']

    def __init__(self):
        """
        The function sets attributes for an instance of a class.
        :param
        """
        self.ind_current_signal = 2
        self.current_signal = TrafficLight.permissible_values[2]

    def next_signal(self):
        """
        The function allows you to switch traffic lights.
        :return: new traffic light signal
        """
        ind_next_signal = (self.ind_current_signal + 1) % len(TrafficLight.permissible_values)
        self.ind_current_signal = ind_next_signal
        new_signal = TrafficLight.permissible_values[ind_next_signal]
        print(new_signal)

    def __str__(self):
        """
        Outputs a string in a readable format.
        """
        return f'Текущий цвет сигнала: {self.current_signal}'

    def __repr__(self):
        """
        Creates a string representation of an object.
        """
        return self.__str__()
