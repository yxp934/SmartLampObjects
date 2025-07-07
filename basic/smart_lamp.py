from dataclasses import dataclass, field

@dataclass
class SmartLamp:
    name: str
    color: str = "white"
    brightness: int = 100
    is_on: bool = field(default=False, init=False)

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_brightness(self, percent):
        self.brightness = percent

    def set_color(self, new_color):
        self.color = new_color

    def status(self):
        state = "ON" if self.is_on else "OFF"
        return f"{self.name} [{state}]: {self.brightness}% brightness, {self.color}"

if __name__ == "__main__":
    lamp1 = SmartLamp(name="Desk Lamp", color="warm white", brightness=80)
    lamp2 = SmartLamp(name="Night-Stand", color="red", brightness=30)

    lamp1.turn_on()
    lamp2.turn_on()

    print(lamp1.status())
    print(lamp2.status()) 