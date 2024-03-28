class TrafficLight:
    permissible_values = ['red', 'yellow', 'green']
    def __init__(self):
        self.current_signal = TrafficLight.permissible_values[2]

    def next_signal(self):
        if self.current_signal == TrafficLight.permissible_values[0]:
            self.current_signal = TrafficLight.permissible_values[1]




