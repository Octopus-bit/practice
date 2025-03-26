# Observer interface
class Observer:
    def update(self, state):
        pass

# Subject class
class Device:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def change_state(self, state):
        self._state = state
        self.notify()

# Concrete Observer
class ScreenDisplay(Observer):
    def update(self, state):
        print(f"Screen displaying the new state: {state}")

class Logger(Observer):
    def update(self, state):
        print(f"Logging: Device state changed to {state}")

# Example Usage
if __name__ == "__main__":
    device = Device()

    screen_display = ScreenDisplay()
    logger = Logger()

    device.attach(screen_display)
    device.attach(logger)

    # Changing device states
    device.change_state("Active")
    device.change_state("Inactive")
    device.change_state("Resting")