class TrafficLight:
    """
    Class of traffic light.
    """
    permissible_values = ['red', 'yellow', 'green', 'yellow']

    def __init__(self):
        """
        The function sets attributes for an instance of a class.
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
