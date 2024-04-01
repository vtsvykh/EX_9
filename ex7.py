class TrafficLight:
    """
    Class of traffic light.
    """
    permissible_values = ['red', 'yellow', 'green']
    def __init__(self):
        """
        The function sets attributes for an instance of a class.
        """
        self.current_signal = TrafficLight.permissible_values[2]

    def next_signal(self):
        """
        The function allows you to switch traffic lights.
        :return: new traffic light signal
        """
        if self.current_signal == TrafficLight.permissible_values[0]:
            self.current_signal = TrafficLight.permissible_values[1]




